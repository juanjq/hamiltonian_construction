# mplot
A script to plot a matrix.


For installing it you can do:

```
import httpimport
with httpimport.remote_repo(['matrix_plot'],'https://raw.githubusercontent.com/juanjq/matrix_plot/main'):
     import matrix_plot as mplot
```

You can use the function `plot(M,cmap)`

* `M` is the matrix to represent
* `cmap` is the colormap used, by default `bwr` is used


Some examples of plotted  matrixes


<p align="center">
    <img align="center" src="https://github.com/juanjq/matrix_plot/blob/main/data/matrix_1.png?raw=true">
</p>
<p align="center">
    <img align="center" src="https://github.com/juanjq/matrix_plot/blob/main/data/matrix_2.png?raw=true">
</p>
<p align="center">
    <img align="center" src="https://github.com/juanjq/matrix_plot/blob/main/data/matrix_3.png?raw=true">
</p>


# hamiltonian
A script to construct matrixes for different Hamiltonian definitions.

For installing it you can do:

```
import httpimport
with httpimport.remote_repo(['line_plot'], 'https://raw.githubusercontent.com/juanjq/hamiltonian_matrix/main'):
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
