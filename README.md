# hamiltonian_matrix
A program to construct matrixes for different Hamiltonian definitions.

For installing it you can do:

```
import httpimport
with httpimport.remote_repo(['line_plot'], 'https://gist.githubusercontent.com/juanjq/ce998b35950c752f4177db2983c915dc/raw/b5328a785e3cb9def910539d441ea553028ee7ae'):
     import hamiltonian_matrix as hamiltonian_matrix
```

## Ising model Hamiltonian with thransverse field

<p align="center">
    <img align="center" src="https://github.com/juanjq/hamiltonian_matrix/blob/main/data/Ising_model.png?raw=true">
</p>

You can use the function as,
**`ising_h(N,J,h,g)`**,

* `N` Is the total number of particles of the chain
* `J` The first constant value
* `h` Second constant value
* `g` Transverse constant value

It returns the total matrix of the system

<p align="center">
    <img align="center" src="https://github.com/juanjq/hamiltonian_matrix/blob/main/data/ising_hamiltonian_img.png?raw=true">
</p>


## XX model Hamiltonian with thransverse field

<p align="center">
    <img align="center" src="https://github.com/juanjq/hamiltonian_matrix/blob/main/data/XX_model.png?raw=true">
</p>

You can use the function as,
**`XX_h(N,J,h,g)`**,

* `N` Is the total number of particles of the chain
* `t1` The first constant value
* `t2` Second constant value

It returns the total matrix of the system

<p align="center">
    <img align="center" src="https://github.com/juanjq/hamiltonian_matrix/blob/main/data/XX_hamiltonian_img.png?raw=true">
</p>
