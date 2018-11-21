class FormatParams: 
    """
    doc
    """
    def __init__(self, params, data):
        self.per = params[data.par_order['per']*data.nvisit:(1 + data.par_order['per'])*data.nvisit]
        self.t0 = params[data.par_order['t0']*data.nvisit:(1 + data.par_order['t0'])*data.nvisit]
        self.t_secondary = params[data.par_order['t_secondary']*data.nvisit:(1 + data.par_order['t_secondary'])*data.nvisit]
        self.w = params[data.par_order['w']*data.nvisit:(1 + data.par_order['w'])*data.nvisit]
        self.a = params[data.par_order['a']*data.nvisit:(1 + data.par_order['a'])*data.nvisit]
        self.inc = params[data.par_order['inc']*data.nvisit:(1 + data.par_order['inc'])*data.nvisit]
        self.rp = params[data.par_order['rp']*data.nvisit:(1 + data.par_order['rp'])*data.nvisit]
        self.fp = params[data.par_order['fp']*data.nvisit:(1 + data.par_order['fp'])*data.nvisit]
        self.u1 = params[data.par_order['u1']*data.nvisit:(1 + data.par_order['u1'])*data.nvisit]
        self.u2 = params[data.par_order['u2']*data.nvisit:(1 + data.par_order['u2'])*data.nvisit]
        self.ecc = params[data.par_order['ecc']*data.nvisit:(1 + data.par_order['ecc'])*data.nvisit]
        self.c = params[data.par_order['c']*data.nvisit:(1 + data.par_order['c'])*data.nvisit]
        self.v = params[data.par_order['v']*data.nvisit:(1 + data.par_order['v'])*data.nvisit]
        self.v2 = params[data.par_order['v2']*data.nvisit:(1 + data.par_order['v2'])*data.nvisit]
        self.r1 = params[data.par_order['r1']*data.nvisit:(1 + data.par_order['r1'])*data.nvisit]
        self.r2 = params[data.par_order['r2']*data.nvisit:(1 + data.par_order['r2'])*data.nvisit]
        self.r3 = params[data.par_order['r3']*data.nvisit:(1 + data.par_order['r3'])*data.nvisit]
        self.scale = params[data.par_order['scale']*data.nvisit:(1 + data.par_order['scale'])*data.nvisit]
        self.a1 = params[data.par_order['a1']*data.nvisit:(1 + data.par_order['a1'])*data.nvisit]
        self.omega1 = params[data.par_order['omega1']*data.nvisit:(1 + data.par_order['omega1'])*data.nvisit]
        self.b1 = params[data.par_order['b1']*data.nvisit:(1 + data.par_order['b1'])*data.nvisit]
        self.a2 = params[data.par_order['a2']*data.nvisit:(1 + data.par_order['a2'])*data.nvisit]
        self.omega2 = params[data.par_order['omega2']*data.nvisit:(1 + data.par_order['omega2'])*data.nvisit]
        self.b2 = params[data.par_order['b2']*data.nvisit:(1 + data.par_order['b2'])*data.nvisit]
        self.a3 = params[data.par_order['a3']*data.nvisit:(1 + data.par_order['a3'])*data.nvisit]
        self.omega3 = params[data.par_order['omega3']*data.nvisit:(1 + data.par_order['omega3'])*data.nvisit]
        self.b3 = params[data.par_order['b3']*data.nvisit:(1 + data.par_order['b3'])*data.nvisit]
        self.a12 = params[data.par_order['a12']*data.nvisit:(1 + data.par_order['a12'])*data.nvisit]
        self.omega12 = params[data.par_order['omega12']*data.nvisit:(1 + data.par_order['omega12'])*data.nvisit]
        self.b12 = params[data.par_order['b12']*data.nvisit:(1 + data.par_order['b12'])*data.nvisit]
        self.a22 = params[data.par_order['a22']*data.nvisit:(1 + data.par_order['a22'])*data.nvisit]
        self.omega22 = params[data.par_order['omega22']*data.nvisit:(1 + data.par_order['omega22'])*data.nvisit]
        self.b22 = params[data.par_order['b22']*data.nvisit:(1 + data.par_order['b22'])*data.nvisit]
        self.a32 = params[data.par_order['a32']*data.nvisit:(1 + data.par_order['a32'])*data.nvisit]
        self.omega32 = params[data.par_order['omega32']*data.nvisit:(1 + data.par_order['omega32'])*data.nvisit]
        self.b32 = params[data.par_order['b32']*data.nvisit:(1 + data.par_order['b32'])*data.nvisit]
        self.trap_pop_s = params[data.par_order['trap_pop_s']*data.nvisit:(1 + data.par_order['trap_pop_s'])*data.nvisit]
        self.trap_pop_f = params[data.par_order['trap_pop_f']*data.nvisit:(1 + data.par_order['trap_pop_f'])*data.nvisit]
        self.cRate = params[data.par_order['cRate']*data.nvisit:(1 + data.par_order['cRate'])*data.nvisit]

def PrintParams(m, data): 
    for i, name in enumerate(data.parnames):
        for vis in range(data.nvisit):
            #if m.perror[data.par_order[name]*data.nvisit + vis] > 0.: 
            if data.fixedpar[i] == "False":
                print name+"_"+str(vis), \
                      "\t", "{0:0.2e}".format(m.params[data.par_order[name]*data.nvisit + vis]), \
                      "\t", "{0:0.1e}".format(m.perror[data.par_order[name]*data.nvisit + vis])
                


