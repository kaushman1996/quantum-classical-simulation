from quspin.basis import spinful_fermion_basis_general
from quspin.operators import hamiltonian
import numpy as np
Lx, Ly = 6, 3 # linear dimension of spin 1 2d lattice
N_2d = Lx*Ly # number of sites for spin 1
#
U=75.0 # onsite interaction
mu=0.0 # chemical potential

T_x=[4,5,7,6,8,9,10,11,13,12,14,15,16,17,1,0,2,3]
T_y=[2,3,5,4,7,6,8,9,11,10,13,12,14,15,17,16,1,0]
T_z=[3,2,4,5,6,7,9,8,10,11,12,13,15,14,16,17,0,1]
def cv(nup,ndown,kx1,ky1,J):
    V=10.5
    basis_2d=spinful_fermion_basis_general(N_2d,Nf=[(nup,ndown)],kxblock=(T_x,kx1),kyblock=(T_y,ky1),Ns_block_est=40000)

    print("Size of 1D H-space: {Ns:d}",basis_2d.Ns)
    hopping_left =[[-J,i,T_x[i]] for i in range(N_2d)] + [[-J,i,T_y[i]] for i in range(N_2d)] + [[-J,i,T_z[i]] for i in range(N_2d)]
    hopping_right=[[+J,i,T_x[i]] for i in range(N_2d)] + [[+J,i,T_y[i]] for i in range(N_2d)] + [[+J,i,T_z[i]] for i in range(N_2d)]
    potential=[[-mu,i] for i in range(N_2d)]
    interaction=[[U,i,i] for i in range(N_2d)]
    interaction1=[[V,i,T_x[i]] for i in range(N_2d)] + [[V,i,T_y[i]] for i in range(N_2d)] + [[V,i,T_z[i]] for i in range(N_2d)]
    interaction2=[[V,T_x[i],i] for i in range(N_2d)] + [[V,T_y[i],i] for i in range(N_2d)] + [[V,T_z[i],i] for i in range(N_2d)]
    static=[["+-|",hopping_left], # spin up hops to left
                    ["-+|",hopping_right], # spin up hops to right
                    ["|+-",hopping_left], # spin down hopes to left
                    ["|-+",hopping_right], # spin up hops to right
                    ["n|",potential], # onsite potenial, spin up
                    ["|n",potential], # onsite potential, spin down
                    ["n|n",interaction], # spin up-spin down interaction
                    ["n|n",interaction1], # spin up-spin down interaction
                    ["nn|",interaction1], # spin up-spin down interaction
                    ["|nn",interaction1], # spin up-spin down interaction
                    ["n|n",interaction2]] # spin up-spin down interaction
    H=hamiltonian(static,[],basis=basis_2d,dtype=np.complex128)
    w=H.eigvalsh()
    return w
def save_eigenvalues(nup, ndown, kx, ky, J, eigenvalues):
    filename = f"eigenvalues_nup{nup}_ndown{ndown}_kx{kx}_ky{ky}_J{J}.txt"
    np.savetxt(filename, eigenvalues)
    print(f"Eigenvalues saved to {filename}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python 15site_kx_ky.py <nup> <ndown> <kx> <ky> <J>")
        sys.exit(1)

    nup = int(sys.argv[1])
    ndown = int(sys.argv[2])
    kx = int(sys.argv[3])
    ky = int(sys.argv[4])
    J = int(sys.argv[5])

    if nup + ndown != 6:
        print("Error: nup and ndown must sum to 6.")
        sys.exit(1)

    kx_ky_values = [
        (-8, -2), (-5, 1), (-7, -4), (-4, -1),
        (-1, 2), (-3, -3), (0, 0), (3, 3), (1, -2),
        (4, 1), (7, 4), (5, -1), (8, 2), (-2, 4), (2, 5),(9,0),(12,3),(6,6)
    ]

    if (kx, ky) not in kx_ky_values:
        print(f"Error: (kx, ky) must be one of {kx_ky_values}.")
        sys.exit(1)

    eigenvalues = cv(nup, ndown, kx, ky, J)
    save_eigenvalues(nup, ndown, kx, ky, J, eigenvalues)

if __name__ == "__main__":
    main()
