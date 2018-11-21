import sys
sys.path.insert(0, './models')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
import seaborn as sns
from formatter import FormatParams
from model import Model, calc_sys, calc_astro
from sine2_hires import sine2_hires

sns.set_context("talk")
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})
matplotlib.rcParams.update({'lines.markeredgewidth':0.3})
matplotlib.rcParams.update({'axes.formatter.useoffset':False})

def plot_raw(data):
    palette = sns.color_palette("husl", data.nvisit)
    for i in range(data.nvisit): 	
        ind = data.vis_num==i
        plt.subplot((data.nvisit)*100+10+i+1)
        plt.plot(data.t_vis[ind]*24., data.flux[ind], marker='o', \
                markersize=3.0, linestyle="none", \
                label = "Visit {0}".format(i), color= palette[i])
        plt.xlim(((data.t_vis.min()-0.02)*24., (data.t_vis.max()+0.05)*24.))
        plt.ylim((0.998*data.flux.min(), 1.002*data.flux.max()))
        plt.legend()
    plt.xlabel("Time after visit start (hours)")
    plt.ylabel("Flux (e-)")
    plt.tight_layout()
    plt.show()	


def plot_systematics(data, model):
    #sys_porder for sine2
    sys_porder =  [data.par_order['a1']*data.nvisit, data.par_order['omega1']*data.nvisit, data.par_order['b1']*data.nvisit, data.par_order['a2']*data.nvisit, data.par_order['omega2']*data.nvisit, data.par_order['b2']*data.nvisit, data.par_order['a3']*data.nvisit, data.par_order['omega3']*data.nvisit, data.par_order['b3']*data.nvisit, data.par_order['a12']*data.nvisit, data.par_order['omega12']*data.nvisit, data.par_order['b12']*data.nvisit, data.par_order['a22']*data.nvisit, data.par_order['omega22']*data.nvisit, data.par_order['b22']*data.nvisit, data.par_order['a32']*data.nvisit, data.par_order['omega32']*data.nvisit, data.par_order['b32']*data.nvisit] 

    params = [model.params[j:j + data.nvisit] for j in sys_porder]
    per  = model.params[data.par_order['per']*data.nvisit]
    t0  = model.params[data.par_order['t0']*data.nvisit]

    colors = ['blue', 'red']
    for i in range(2):
        plt.figure()
        visit = i
        t = data.time[data.vis_idx[visit]]
        t_hr = np.linspace(t[0], t[-1], 1000)
        sys = sine2_hires(t_hr, data, params, visit)
        phase_hr = (t_hr - t0)/per - np.floor((t_hr - t0)/per)
        phase = (t - t0)/per - np.floor((t - t0)/per)
        plt.plot(phase_hr, sys, color = colors[i])

        #mark gaps in orbit
        for j in range(1, len(t)):
            if t[j] - t[j - 1] > 20./60./24.: 
                plt.fill_betweenx(np.linspace(0.998, 1.002, 100), phase[j], phase[j-1], color = '0.7', alpha = 0.5) 
        
        plt.ylim(0.998, 1.002)
        plt.savefig("wiggles" + str(i) + ".png")


def plot_fit(data, model):
    p = FormatParams(model.params, data)    #FIXME 

    sns.set_palette("muted")
    palette = sns.color_palette("muted", data.nvisit)

    #ind = model.phase > 0.5
    #model.phase[ind] -= 1.

    #calculate a range of times at higher resolution to make model look nice
    phase_hr = np.linspace(model.phase.min()-0.05, model.phase.max()+0.05, 1000)
    t_hr = phase_hr*p.per[0]+p.t0[0]

    colors = ['blue', 'red']

    #plot data
    plt.subplot(211)
    #plot best fit model from first visit
    plt.plot(phase_hr, calc_astro(t_hr, model.params, data, model.myfuncs, 0))

    #plot systematics removed data
    for i in range(data.nvisit):
        ind = data.vis_num == i
        plt.plot(model.phase[ind], model.data_nosys[ind], color = colors[i], marker = 'o', markersize = 3, linestyle = "none") 

    #add labels/set axes
    #xlo, xhi = np.min(model.phase)*0.9, np.max(model.phase)*1.1
    xlo, xhi = 0.35, 0.6
    plt.xlim(xlo,xhi)
    plt.ylabel("Relative Flux")

    #annotate plot with fit diagnostics
    ax = plt.gca()
    ax.text( 0.85, 0.29, 
             '$\chi^2_\\nu$:    ' + '{0:0.2f}'.format(model.chi2red) + '\n'
            + 'obs. rms:  ' + '{0:0d}'.format(int(model.rms)) + '\n' 
            + 'exp. rms:  ' + '{0:0d}'.format(int(model.rms_predicted)), 
            verticalalignment='top',horizontalalignment='left', 
            transform=ax.transAxes, fontsize = 12
    )
    
    #plot fit residuals
    plt.subplot(212)
    plt.axhline(0, zorder=1, color='0.2', linestyle='dashed')

    for i in range(data.nvisit):
        ind = data.vis_num == i
        plt.plot(model.phase[ind], 1.0e6*model.norm_resid[ind], color = colors[i], marker = 'o', markersize = 3, linestyle = "none")

    #add labels/set axes
    plt.xlim(xlo,xhi)
    plt.ylabel("Residuals (ppm)")
    plt.xlabel("Orbital phase")
    
    plt.savefig("white_lc.pdf")

    plot_systematics(data, model)
    #plt.show()


