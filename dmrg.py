import numpy as np
from tenpy.algorithms import dmrg
from tenpy.networks.mps import MPS
from tenpy.networks import site
from tenpy.models.model import CouplingMPOModel
from tenpy.networks.site import FermionSite
from tenpy.models import lattice
from tenpy.models import hubbard
from tenpy.networks.purification_mps import PurificationMPS
from tenpy.algorithms.purification import PurificationTEBD, PurificationApplyMPO
import pickle
import logging
logging.basicConfig(level=logging.INFO)
model_params = dict(cons_N='N',cons_Sz='Sz', t=1.81, U=75.0*1.81,mu=0.0,V= 39.92, lattice="Triangular", bc_MPS='finite',
                        order='default', Lx=6, Ly=6,bc_x='periodic',bc_y='periodic', verbose=0)

M = hubbard.FermiHubbardModel(model_params)
a=np.array([1,0,0,2,0,0,0,1,0,0,2,0,0,0,1,0,0,2,1,0,0,2,0,0,0,1,0,0,2,0,0,0,1,0,0,2])
product_state=[]
for i in range(36):
        product_state.append(a[i])
print(product_state)

psi1 = MPS.from_product_state(M.lat.mps_sites(), product_state, bc=M.lat.bc_MPS)
print("Sz",psi1.expectation_value('Sz'))
print(psi1.expectation_value('Sz'))
dmrg_params = {
        'mixer': True,
        'trunc_params': {
            'chi_max': 10000,
            'svd_min': 1.e-10
        },
        'max_E_err': 1.e-10,
        'verbose': 0,
        'N_sweeps_check': 10,
        'max_sweeps':200
    }
logging.basicConfig(level=logging.INFO)
info = dmrg.run(psi1, M, dmrg_params)
logging.basicConfig(level=logging.INFO)
E = info['E']
print("Ntot",psi1.expectation_value('Ntot'))
print("Nd",psi1.expectation_value('Nd'))
print("Nu",psi1.expectation_value('Nu'))
with open('my_psi_final.pkl', 'wb') as f1:
        pickle.dump(psi1, f1)
print("Sz",psi1.expectation_value('Sz'))
