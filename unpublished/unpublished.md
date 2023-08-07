# Preamble
**Prompt:**  
You are a physicist helping me to construct Hamiltonian and perform Hartree-Fock step by step based on my instructions. 
You should follow the instruction strictly.
Your reply should be succinct while complete. You should not expand any unwanted content.
You will be learning background knowledge by examples if necessary.
Confirm and repeat your duty if you understand it.

**Completion:**  
I understand my duty. I will be acting as a physicist, assisting you in constructing a Hamiltonian and performing the Hartree-Fock method step by step based on your instructions. My responses will be concise, accurate, and strictly following your instructions without adding any unnecessary content. I will explain any necessary background knowledge through examples.

# Hamiltonian construction
## Construct Kinetic Hamiltonian (lattice version)
**Prompt:**  
You will be instructed to describe the kinetic term of Hamiltonian in honeycomb lattice in the real space in the second-quantized form.   
The degrees of freedom of the system are: spin index (spin up and spin down), sublattice index (A and B)    
The kinetic term is a tight-binding model composed of the following hopping process: 
1. $c_{A,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i)$ with the hopping amplitude $-t_1$.  
2. $c_{A,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i+a_1)$ with the hopping amplitude $-t_1$.  
3. $c_{A,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i+a_2)$ with the hopping amplitude $-t_1$.  
4. $c_{A,s}^\dagger(R_i)$ and $c_{A,s}^\dagger(R_i+a_1)$ with the hopping amplitude $-t_2$.  
5. $c_{A,s}^\dagger(R_i)$ and $c_{A,s}^\dagger(R_i+a_2)$ with the hopping amplitude $-t_2$.  
6. $c_{A,s}^\dagger(R_i)$ and $c_{A,s}^\dagger(R_i-a_1)$ with the hopping amplitude $-t_2$.  
7. $c_{A,s}^\dagger(R_i)$ and $c_{A,s}^\dagger(R_i-a_2)$ with the hopping amplitude $-t_2$.  
8. $c_{A,s}^\dagger(R_i)$ and $c_{A,s}^\dagger(R_i+a_1-a_2)$ with the hopping amplitude $-t_2$.  
9. $c_{A,s}^\dagger(R_i)$ and $c_{A,s}^\dagger(R_i-a_1+a_2)$ with the hopping amplitude $-t_2$.  
10. $c_{B,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i+a_1)$ with the hopping amplitude $-t_2$.  
11. $c_{B,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i+a_2)$ with the hopping amplitude $-t_2$.  
12. $c_{B,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i-a_1)$ with the hopping amplitude $-t_2$.  
13. $c_{B,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i-a_2)$ with the hopping amplitude $-t_2$.  
14. $c_{B,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i+a_1-a_2)$ with the hopping amplitude $-t_2$.  
15. $c_{B,s}^\dagger(R_i)$ and $c_{B,s}^\dagger(R_i-a_1+a_2)$ with the hopping amplitude $-t_2$.  
15. $c_{A,\uparrow}^\dagger(R_i)$ and $c_{A,\uparrow}^\dagger(R_i)$ with the hopping amplitude $h_x$.  
16. $c_{A,\downarrow}^\dagger(R_i)$ and $c_{A,\downarrow}^\dagger(R_i)$ with the hopping amplitude $-h_x$.  
17. $c_{B,\uparrow}^\dagger(R_i)$ and $c_{B,\uparrow}^\dagger(R_i)$ with the hopping amplitude $h_x$.  
18. $c_{B,\downarrow}^\dagger(R_i)$ and $c_{B,\downarrow}^\dagger(R_i)$ with the hopping amplitude $-h_x$.  
You should ensure the hermiticity of the Hamiltonian.
The summation should be taken over all spin index and all real space positions.  
Return the Kinetic Hamiltonian $H_0$.

Use the following conventions for the symbols:  
$s$ : spin index  
$\uparrow$ : spin up  
$\downarrow$ : spin down
$\alpha$: sublattice index  
A: sublattice A  
B: sublattice B  
$a$: lattice constance  
$a_1$: unit vector, equals $a (cos 60^\circ , sin 60^\circ)$  
$a_2$: unit vector, equals $a (cos 120^\circ , sin 120^\circ)$  
$t_1$: hopping amplitude between nearest neighor sites
$t_2$: hopping amplitude between next nearest neighor sites
$h_x$: hopping amplitude between onsite sites, corresponding to the Zeeman field


**Prompt:**  
Given your instructions, the kinetic term of the Hamiltonian in the honeycomb lattice in real space in the second-quantized form can be written as:

$H_0 = -t_1\sum_{i,s} [c_{A,s}^\dagger(R_i) c_{B,s}(R_i) + c_{A,s}^\dagger(R_i) c_{B,s}(R_i + a_1) + c_{A,s}^\dagger(R_i) c_{B,s}(R_i + a_2) + h.c.] -t_2\sum_{i,s} [c_{A,s}^\dagger(R_i) c_{A,s}(R_i + a_1) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i + a_2) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i - a_1) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i - a_2) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i + a_1 - a_2) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i - a_1 + a_2) + h.c.]-t_2\sum_{i,s} [c_{B,s}^\dagger(R_i) c_{B,s}(R_i + a_1) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i + a_2) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i - a_1) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i - a_2) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i + a_1 - a_2) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i - a_1 + a_2) + h.c.]+ h_x\sum_{i} [c_{A,\uparrow}^\dagger(R_i) c_{A,\uparrow}(R_i) - c_{A,\downarrow}^\dagger(R_i) c_{A,\downarrow}(R_i) + c_{B,\uparrow}^\dagger(R_i) c_{B,\uparrow}(R_i) - c_{B,\downarrow}^\dagger(R_i) c_{B,\downarrow}(R_i)]$

In the above expression, "h.c." stands for the Hermitian conjugate, which ensures the hermiticity of the Hamiltonian. The sums over $i$ are taken over all positions in real space, and the sums over $s$ are taken over all spin indices. The dagger denotes the creation operator, and the absence of a dagger denotes the annihilation operator. The hopping amplitudes are denoted by $t_1$, $t_2$, and $h_x$ for the nearest neighbors, next-nearest neighbors, and on-site terms, respectively. The terms $a_1$ and $a_2$ represent the lattice vectors.


## Construct interaction Hamiltonian (real space, lattice version)
**Prompt:**  
You will be instructed to construct the interaction part of the Hamiltonian, $\hat{H}^{int}$ in the real space in the second-quantized form.   
The interacting Hamiltonian has the same degrees of freedom as the kinetic Hamiltonian $H_0$.  
The interaction is a density-density interaction composed of the following process:
1. onsite interaction between $n_{A,\uparrow}^\dagger(R_i)$ and $n_{A,\downarrow}^\dagger(R_i)$ with interaction strength $U_0$
2. onsite interaction between $n_{B,\uparrow}^\dagger(R_i)$ and $n_{B,\downarrow}^\dagger(R_i)$ with interaction strength $U_0$
3. Nearest neighbor interaction between $n_{A,s}^\dagger(R_i)$ and $n_{B,s^{\prime}}^\dagger(R_i)$ with interaction strength $U_1$
4. Nearest neighbor interaction between $n_{A,s}^\dagger(R_i)$ and $n_{B,s^{\prime}}^\dagger(R_i+a_1)$ with interaction strength $U_1$
5. Nearest neighbor interaction between $n_{A,s}^\dagger(R_i)$ and $n_{B,s^{\prime}}^\dagger(R_i+a_2)$ with interaction strength $U_1$
The summation should be taken over all spin index and all real space positions.  
Return the interaction term $H_{int}$ in terms of $n_{\alpha,s}(R_i)$.

Use the following conventions for the symbols (You should also remember the conventions in my previous prompts if there are no conflicts. If you have conflicts in the conventions, you should stop and let me know): 
$s^{\prime}$: spin index   
$n_{\alpha,s}(R_i)$: density of particle with sublattice $\alpha$ and spin $s$ at site $R_i$
$U_0$: onsite interaction strength
$U_1$: Nearest neighbor interaction strength

**Completion:**  
Given your instructions, the interaction term of the Hamiltonian in the honeycomb lattice in real space in the second-quantized form can be written as:

$H_{int} = U_0\sum_{i} [n_{A,\uparrow}(R_i) n_{A,\downarrow}(R_i) + n_{B,\uparrow}(R_i) n_{B,\downarrow}(R_i)]+ U_1\sum_{i,s,s'} [n_{A,s}(R_i) n_{B,s'}(R_i) + n_{A,s}(R_i) n_{B,s'}(R_i + a_1) + n_{A,s}(R_i) n_{B,s'}(R_i + a_2)]$

In the above expression, the sums over $i$ are taken over all positions in real space, and the sums over $s$ and $s'$ are taken over all spin indices. The interaction strengths are denoted by $U_0$ for the onsite interaction and $U_1$ for the nearest neighbor interaction. The terms $n_{\alpha,s}(R_i)$ represent the particle density at site $R_i$ in the $\alpha$ sublattice with spin $s$.

## Convert noninteracting Hamiltonian in real space to momentum space (lattice version)
**Prompt:**  
You will be instructed to convert the Kinetic Hamiltonian $H_0$ in the second quantized form from the basis in real space to the basis in momentum space.  
To do that, you should apply the Fourier transformation to $c_{\alpha,s}^\dagger(R_i)$ in the real space to the $c_{\alpha,s}^\dagger(k)$ in the momentum space, which is defined as $c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over all sites in the entire real space. You should follow the EXAMPLE below to apply the Fourier transformation. Note that $t_1$ and $t_2$ have no position dependence now.  
Recall that  
$$H_0 = -t_1\sum_{i,s} [c_{A,s}^\dagger(R_i) c_{B,s}(R_i) + c_{A,s}^\dagger(R_i) c_{B,s}(R_i + a_1) + c_{A,s}^\dagger(R_i) c_{B,s}(R_i + a_2) + h.c.] -t_2\sum_{i,s} [c_{A,s}^\dagger(R_i) c_{A,s}(R_i + a_1) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i + a_2) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i - a_1) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i - a_2) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i + a_1 - a_2) + c_{A,s}^\dagger(R_i) c_{A,s}(R_i - a_1 + a_2) + h.c.]-t_2\sum_{i,s} [c_{B,s}^\dagger(R_i) c_{B,s}(R_i + a_1) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i + a_2) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i - a_1) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i - a_2) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i + a_1 - a_2) + c_{B,s}^\dagger(R_i) c_{B,s}(R_i - a_1 + a_2) + h.c.]+ h_x\sum_{i} [c_{A,\uparrow}^\dagger(R_i) c_{A,\uparrow}(R_i) - c_{A,\downarrow}^\dagger(R_i) c_{A,\downarrow}(R_i) + c_{B,\uparrow}^\dagger(R_i) c_{B,\uparrow}(R_i) - c_{B,\downarrow}^\dagger(R_i) c_{B,\downarrow}(R_i)]$$
Express the Kinetic Hamiltonian $H_0$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$.   

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$c_{\alpha,s}(k)$ : electron annihilation operator at momentum $k$, spin $s$ and sublattice $\alpha$  
$c_{\alpha,s}^\dagger(k)$ : electron creation operator at momentum $k$, spin $s$ and sublattice $\alpha$
$N$ : number of the unit cells in the real space  

===
EXAMPLE:  
Write a Kinetic Hamiltonian $\hat{H}$ in the second quantized form in the real space, $\hat{H}=\sum_{i,j} t(R_i-R_j) c^\dagger(R_i) c(R_j)$, where $i,j$ are summed over the entire real space.  
Define the Fourier transformation $c^\dagger(k)=\frac{1}{\sqrt{N}} \sum_{i}c^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over the entire real space containing $N$ unit cells, $N$ is the number of unit cells.  
This leads to the inverse Fourier transformation $c^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c^\dagger(k) e^{-i k \cdot R_i}$, where $k$ is first Brillouin zone.  
Thus, substitute $c^\dagger(R_i)$ and $c(R_j)$ into $\hat{H}$, we get  
$$\hat{H} = \sum_{i,j} t(R_i-R_j) \frac{1}{\sqrt{N}} \sum_{k_1} c^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{\sqrt{N}} \sum_{k_2} c(k_2) e^{i k_2 \cdot R_j} =\frac{1}{N} \sum_{i,j}\sum_{k_1,k_2} c^\dagger(k_1)  c(k_2)  e^{-i k_1\cdot R_i} e^{i k_2 \cdot R_j} t(R_i-R_j) $$
Now make a replacement by defining $n= R_i-R_j$  
The Hamiltonian become  
$$\hat{H}=\frac{1}{N} \sum_{i,n} \sum_{k_1,k_2} c^\dagger(k_1)  c(k_2) t(n) e^{-i (k_1-k_2)\cdot R_i} e^{-i k_2 \cdot n}$$
Because $\frac{1}{N}\sum_{i} e^{-i (k_1-k_2)\cdot R_i} = \delta(k_1,k_2)$, where $\delta(k_1,k_2)$ is the Kronecker delta function.  
therefore   
$$\hat{H}=\sum_{k_1,k_2} \sum_{n} t(n) e^{-i k_2 \cdot n} c^\dagger(k_1)  c(k_2) \delta(k_1,k_2)$$
Using the property of Kronecker delta function and sum over $k_2$, we obtain  
$$\hat{H}=\sum_{k_1} \sum_{n} t(n) e^{-i k_1 \cdot n} c^\dagger(k_1)  c(k_1) $$
For simplicity, we replace $k_1$ with $k$, we obtain  
$$\hat{H}=\sum_{k} \sum_{n} t(n) e^{-i k \cdot n} c^\dagger(k)  c(k)$$
If we define energy dispersion $E(k)=\sum_{n} t(n) e^{-i k \cdot n}$, where $n$ is the summation of all hopping pairs, the Hamiltonian in the momentum space is 
$$\hat{H}=\sum_{k} E(k) c^\dagger(k)  c(k)$$

**Completion:**  
To write the kinetic Hamiltonian in the momentum space, we need to Fourier transform the operator from real space to momentum space using the transformation you have defined:

$c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$,

where $N$ is the total number of lattice sites (i.e., the number of unit cells). The inverse of this transformation is:

$c_{\alpha,s}^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}^\dagger(k) e^{-i k \cdot R_i}$.

Substituting this into the kinetic Hamiltonian, and using the property that $\frac{1}{N}\sum_{i} e^{-i (k_1-k_2)\cdot R_i} = \delta(k_1,k_2)$, we get the following expressions:

$H_0 = -t_1\sum_{k,s} (e^{-i k \cdot a_1} + e^{-i k \cdot a_2} + 1) c_{A,s}^\dagger(k) c_{B,s}(k) + h.c.-t_2\sum_{k,s} (e^{-i k \cdot a_1} + e^{-i k \cdot a_2} + e^{i k \cdot a_1} + e^{i k \cdot a_2} + e^{-i k \cdot (a_1 - a_2)} + e^{i k \cdot (a_1 - a_2)}) [c_{A,s}^\dagger(k) c_{A,s}(k) + c_{B,s}^\dagger(k) c_{B,s}(k)]+ h_x\sum_{k} [c_{A,\uparrow}^\dagger(k) c_{A,\uparrow}(k) - c_{A,\downarrow}^\dagger(k) c_{A,\downarrow}(k) + c_{B,\uparrow}^\dagger(k) c_{B,\uparrow}(k) - c_{B,\downarrow}^\dagger(k) c_{B,\downarrow}(k)]$,

where $k$ is summed over the first Brillouin zone and $s$ is summed over the spin. The terms with $h.c.$ denote the Hermitian conjugate of the preceding terms. The terms $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$ represent the annihilation and creation operators in momentum space, respectively. The $a_1$ and $a_2$ are vectors denoting the nearest-neighbor displacements in the lattice.

## Convert interacting Hamiltonian in real space to momentum space (lattice version) [first term] 
**Prompt:**  
You will be instructed to convert the interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form the basis in real space to the basis in momentum space. You will be instructed to perform the transformation to the first term with $U_0$.
To do that, you should apply the Fourier transformation to $c_{\alpha,s}^\dagger(R_i)$ in the real space to the $c_{\alpha,s}^\dagger(k)$ in the momentum space, which is defined as $c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over all sites in the entire real space, and $k$ is defined within the first Brillouin zone. You should follow the EXAMPLE below to apply the Fourier transformation. Note that the interaction $U_0$ is onsite.  
You should recall that the first term in $\hat{H}^{int}$ is
$U_0\sum_{i} n_{A,\uparrow}(R_i) n_{A,\downarrow}(R_i) $
Express the first term in interacting Hamiltonian $\hat{H}^{int}$ with $U_0$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$. Simplify any summation index if possible.  

===  
EXAMPLE:  
Write an interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form in the real space, $\hat{H}^{int}=\sum_{s,s'}\sum_{i,j} U(R_i-R_j) c_s^\dagger(R_i) c_{s'}^\dagger(R_j) c_{s'}(R_j) c_s(R_i)$, where $i,j$ are summed over the entire real space.  
Define the Fourier transformation $c_s^\dagger(k)=\frac{1}{\sqrt{N}} \sum_{i}c_s^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over the entire real space containing $N$ unit cells, $N$ is the number of unit cells.  
This leads to the inverse Fourier transformation $c_s^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_s^\dagger(k) e^{-i k \cdot R_i}$, where $k$ is summed over the first Brillouin zone.  
Thus, substitute $c^\dagger(R_i)$ and $c(R_j)$ into $\hat{H}^{int}$, we get  
$$\hat{H}^{int} = \sum_{s,s'}\sum_{i,j} U(R_i-R_j) \frac{1}{\sqrt{N}} \sum_{k_1} c_s^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{\sqrt{N}} \sum_{k_2} c_{s'}^\dagger(k_2) e^{-i k_2 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_3} c_{s'}(k_3) e^{i k_3 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_4} c_s(k_4) e^{i k_4 \cdot R_i}=\sum_{s,s'}\sum_{i,j}\frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4}U(R_i-R_j)c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot R_i} e^{-i(k_2-k_3)\cdot R_j}$$
Now make a replacement by defining $n= R_i-R_j$  
The Hamiltonian become  
$$\hat{H}^{int}=\frac{1}{N^2} \sum_{j,n} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} U(n) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot n} e^{-i(k_1-k_4+k_2-k_3)\cdot r_j }$$
Because $\frac{1}{N}\sum_{i} e^{-i (k_1-k_4+k_2-k_3)\cdot R_i} = \sum\delta(k_1-k_4+k_2-k_3,G)$, where $\delta(..,..)$ is the Kronecker delta function, and $G$ is the all reciprocal lattices in the momentum space.  
Therefore,  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{n} U(n) e^{-i (k_1-k_4) \cdot n} c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$
If we define interaction in the momentum space $U(k)=\sum_{n} U(n) e^{-i k \cdot n}$, where $n$ is the summation of all hopping pairs, the interacting Hamiltonian in the momentum space is  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4}  U(k_1-k_4) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$


**Completion:**  
Following the example, we first need to express the first term of the interacting Hamiltonian $\hat{H}^{int}$ in terms of the Fourier transformed creation and annihilation operators. 

The term in real space representation is given by

$$U_0\sum_{i} n_{A,\uparrow}(R_i) n_{A,\downarrow}(R_i),$$

where $n_{A,\uparrow}(R_i)$ and $n_{A,\downarrow}(R_i)$ are the number operators in the real space, which can be written in terms of the creation and annihilation operators as 

$$n_{A,\uparrow}(R_i) = c_{A,\uparrow}^\dagger(R_i) c_{A,\uparrow}(R_i) \quad \text{and} \quad n_{A,\downarrow}(R_i) = c_{A,\downarrow}^\dagger(R_i) c_{A,\downarrow}(R_i).$$

Now, following the example, we apply the Fourier transform to each operator. First, remember that the inverse Fourier transforms are defined as

$$c_{\alpha,s}^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}^\dagger(k) e^{-i k \cdot R_i} \quad \text{and} \quad c_{\alpha,s}(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}(k) e^{i k \cdot R_i}.$$

By substituting these into the first term, we get

$$U_0\sum_{i} n_{A,\uparrow}(R_i) n_{A,\downarrow}(R_i) = U_0\sum_{i} \left(\frac{1}{\sqrt{N}} \sum_{k_1} c_{A,\uparrow}^\dagger(k_1) e^{-i k_1 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_2} c_{A,\uparrow}(k_2) e^{i k_2 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_3} c_{A,\downarrow}^\dagger(k_3) e^{-i k_3 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_4} c_{A,\downarrow}(k_4) e^{i k_4 \cdot R_i}\right).$$

Simplifying, we get

$$U_0\sum_{i} \frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4} c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) e^{-i(k_1-k_2)\cdot R_i} e^{-i(k_3-k_4)\cdot R_i}.$$

This interaction is onsite, which means we have to enforce momentum conservation. As in the example, we can use the identity 

$$\frac{1}{N}\sum_{i} e^{-i (k_1-k_2+k_3-k_4)\cdot R_i} = \sum\delta(k_1-k_2+k_3-k_4,G),$$

where $\delta(..,..)$ is the Kronecker delta function and $G$ represents all reciprocal lattice vectors in momentum space. 

Applying the identity, we can rewrite the interaction term as

$$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G).$$

Here, the delta function enforces the momentum conservation. Therefore, the first term in the interacting Hamiltonian $\hat{H}^{int}$ with $U_0$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$ is given by the expression above. Please note that the expression simplifies considerably in the case of an infinite system (where $N$ tends to infinity), because in that case, the sum over $G$ reduces to a delta function that enforces momentum conservation.

## Convert interacting Hamiltonian in real space to momentum space (lattice version) [second term] 
**Prompt:**  
You will be instructed to convert the interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form the basis in real space to the basis in momentum space. You will be instructed to perform the transformation to the second term with $U_0$.
To do that, you should apply the Fourier transformation to $c_{\alpha,s}^\dagger(R_i)$ in the real space to the $c_{\alpha,s}^\dagger(k)$ in the momentum space, which is defined as $c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over all sites in the entire real space, and $k$ is defined within the second Brillouin zone. You should follow the EXAMPLE below to apply the Fourier transformation. Note that the interaction $U_0$ is onsite.  
You should recall that the second term in $\hat{H}^{int}$ is
$U_0\sum_{i} n_{B,\uparrow}(R_i) n_{B,\downarrow}(R_i)$
Express the second term in interacting Hamiltonian $\hat{H}^{int}$ with $U_0$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$. Simplify any summation index if possible.  

===  
EXAMPLE:  
Write an interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form in the real space, $\hat{H}^{int}=\sum_{s,s'}\sum_{i,j} U(R_i-R_j) c_s^\dagger(R_i) c_{s'}^\dagger(R_j) c_{s'}(R_j) c_s(R_i)$, where $i,j$ are summed over the entire real space.  
Define the Fourier transformation $c_s^\dagger(k)=\frac{1}{\sqrt{N}} \sum_{i}c_s^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over the entire real space containing $N$ unit cells, $N$ is the number of unit cells.  
This leads to the inverse Fourier transformation $c_s^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_s^\dagger(k) e^{-i k \cdot R_i}$, where $k$ is summed over the first Brillouin zone.  
Thus, substitute $c^\dagger(R_i)$ and $c(R_j)$ into $\hat{H}^{int}$, we get  
$$\hat{H}^{int} = \sum_{s,s'}\sum_{i,j} U(R_i-R_j) \frac{1}{\sqrt{N}} \sum_{k_1} c_s^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{\sqrt{N}} \sum_{k_2} c_{s'}^\dagger(k_2) e^{-i k_2 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_3} c_{s'}(k_3) e^{i k_3 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_4} c_s(k_4) e^{i k_4 \cdot R_i}=\sum_{s,s'}\sum_{i,j}\frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4}U(R_i-R_j)c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot R_i} e^{-i(k_2-k_3)\cdot R_j}$$
Now make a replacement by defining $n= R_i-R_j$  
The Hamiltonian become  
$$\hat{H}^{int}=\frac{1}{N^2} \sum_{j,n} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} U(n) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot n} e^{-i(k_1-k_4+k_2-k_3)\cdot r_j }$$
Because $\frac{1}{N}\sum_{i} e^{-i (k_1-k_4+k_2-k_3)\cdot R_i} = \sum\delta(k_1-k_4+k_2-k_3,G)$, where $\delta(..,..)$ is the Kronecker delta function, and $G$ is the all reciprocal lattices in the momentum space.  
Therefore,  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{n} U(n) e^{-i (k_1-k_4) \cdot n} c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$
If we define interaction in the momentum space $U(k)=\sum_{n} U(n) e^{-i k \cdot n}$, where $n$ is the summation of all hopping pairs, the interacting Hamiltonian in the momentum space is  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4}  U(k_1-k_4) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$


**Completion:**  
The second term in the interacting Hamiltonian $\hat{H}^{int}$ in the real space is given by 

$$U_0\sum_{i} n_{B,\uparrow}(R_i) n_{B,\downarrow}(R_i),$$

where $n_{B,\uparrow}(R_i)$ and $n_{B,\downarrow}(R_i)$ are the number operators in the real space, which can be written in terms of the creation and annihilation operators as 

$$n_{B,\uparrow}(R_i) = c_{B,\uparrow}^\dagger(R_i) c_{B,\uparrow}(R_i) \quad \text{and} \quad n_{B,\downarrow}(R_i) = c_{B,\downarrow}^\dagger(R_i) c_{B,\downarrow}(R_i).$$

Now, following the example, we apply the Fourier transform to each operator. The inverse Fourier transforms are defined as

$$c_{\alpha,s}^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}^\dagger(k) e^{-i k \cdot R_i} \quad \text{and} \quad c_{\alpha,s}(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}(k) e^{i k \cdot R_i}.$$

By substituting these into the second term, we get

$$U_0\sum_{i} n_{B,\uparrow}(R_i) n_{B,\downarrow}(R_i) = U_0\sum_{i} \left(\frac{1}{\sqrt{N}} \sum_{k_1} c_{B,\uparrow}^\dagger(k_1) e^{-i k_1 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_2} c_{B,\uparrow}(k_2) e^{i k_2 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_3} c_{B,\downarrow}^\dagger(k_3) e^{-i k_3 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_4} c_{B,\downarrow}(k_4) e^{i k_4 \cdot R_i}\right).$$

Simplifying, we get

$$U_0\sum_{i} \frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4} c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) e^{-i(k_1-k_2)\cdot R_i} e^{-i(k_3-k_4)\cdot R_i}.$$

This interaction is also onsite, which means we have to enforce momentum conservation. We can use the identity 

$$\frac{1}{N}\sum_{i} e^{-i (k_1-k_2+k_3-k_4)\cdot R_i} = \sum\delta(k_1-k_2+k_3-k_4,G),$$

where $\delta(..,..)$ is the Kronecker delta function and $G$ is all the reciprocal lattice vectors in momentum space. 

Applying the identity, we can rewrite the interaction term as

$$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G).$$

Here, the delta function enforces the momentum conservation. Therefore, the second term in the interacting Hamiltonian $\hat{H}^{int}$ with $U_0$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$ is given by the expression above. Please note that the expression simplifies considerably in the case of an infinite system (where $N$ tends to infinity), because in that case, the sum over $G$ reduces to a delta function that enforces momentum conservation.

## Convert interacting Hamiltonian in real space to momentum space (lattice version) [third term] 
**Prompt:**  
You will be instructed to convert the interacting Hamiltonian $\hat{H}^{int}$ in the third quantized form the basis in real space to the basis in momentum space. You will be instructed to perform the transformation to the third term with $U_1$.
To do that, you should apply the Fourier transformation to $c_{\alpha,s}^\dagger(R_i)$ in the real space to the $c_{\alpha,s}^\dagger(k)$ in the momentum space, which is defined as $c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over all sites in the entire real space, and $k$ is defined within the third Brillouin zone. You should follow the EXAMPLE below to apply the Fourier transformation. 
You should recall that the third term in $\hat{H}^{int}$ is
$U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i)$   
Express the third term in interacting Hamiltonian $\hat{H}^{int}$ with $U_1$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$. Simplify any summation index if possible.  

===  
EXAMPLE:  
Write an interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form in the real space, $\hat{H}^{int}=\sum_{s,s'}\sum_{i,j} U(R_i-R_j) c_s^\dagger(R_i) c_{s'}^\dagger(R_j) c_{s'}(R_j) c_s(R_i)$, where $i,j$ are summed over the entire real space.  
Define the Fourier transformation $c_s^\dagger(k)=\frac{1}{\sqrt{N}} \sum_{i}c_s^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over the entire real space containing $N$ unit cells, $N$ is the number of unit cells.  
This leads to the inverse Fourier transformation $c_s^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_s^\dagger(k) e^{-i k \cdot R_i}$, where $k$ is summed over the first Brillouin zone.  
Thus, substitute $c^\dagger(R_i)$ and $c(R_j)$ into $\hat{H}^{int}$, we get  
$$\hat{H}^{int} = \sum_{s,s'}\sum_{i,j} U(R_i-R_j) \frac{1}{\sqrt{N}} \sum_{k_1} c_s^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{\sqrt{N}} \sum_{k_2} c_{s'}^\dagger(k_2) e^{-i k_2 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_3} c_{s'}(k_3) e^{i k_3 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_4} c_s(k_4) e^{i k_4 \cdot R_i}=\sum_{s,s'}\sum_{i,j}\frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4}U(R_i-R_j)c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot R_i} e^{-i(k_2-k_3)\cdot R_j}$$
Now make a replacement by defining $n= R_i-R_j$  
The Hamiltonian become  
$$\hat{H}^{int}=\frac{1}{N^2} \sum_{j,n} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} U(n) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot n} e^{-i(k_1-k_4+k_2-k_3)\cdot r_j }$$
Because $\frac{1}{N}\sum_{i} e^{-i (k_1-k_4+k_2-k_3)\cdot R_i} = \sum\delta(k_1-k_4+k_2-k_3,G)$, where $\delta(..,..)$ is the Kronecker delta function, and $G$ is the all reciprocal lattices in the momentum space.  
Therefore,  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{n} U(n) e^{-i (k_1-k_4) \cdot n} c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$
If we define interaction in the momentum space $U(k)=\sum_{n} U(n) e^{-i k \cdot n}$, where $n$ is the summation of all hopping pairs, the interacting Hamiltonian in the momentum space is  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4}  U(k_1-k_4) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$

**Completion:**  
The third term in the interacting Hamiltonian $\hat{H}^{int}$ in the real space is given by 

$$U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i),$$

where $n_{A,s}(R_i)$ and $n_{B,s'}(R_i)$ are the number operators in the real space, which can be written in terms of the creation and annihilation operators as 

$$n_{A,s}(R_i) = c_{A,s}^\dagger(R_i) c_{A,s}(R_i) \quad \text{and} \quad n_{B,s'}(R_i) = c_{B,s'}^\dagger(R_i) c_{B,s'}(R_i).$$

Now, following the example, we apply the Fourier transform to each operator. The inverse Fourier transforms are defined as

$$c_{\alpha,s}^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}^\dagger(k) e^{-i k \cdot R_i} \quad \text{and} \quad c_{\alpha,s}(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}(k) e^{i k \cdot R_i}.$$

By substituting these into the third term, we get

$$U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i) = U_1\sum_{i,s,s'} \left(\frac{1}{\sqrt{N}} \sum_{k_1} c_{A,s}^\dagger(k_1) e^{-i k_1 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_2} c_{A,s}(k_2) e^{i k_2 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_3} c_{B,s'}^\dagger(k_3) e^{-i k_3 \cdot R_i}\right) \left(\frac{1}{\sqrt{N}} \sum_{k_4} c_{B,s'}(k_4) e^{i k_4 \cdot R_i}\right).$$

Simplifying, we get

$$U_1\sum_{i,s,s'} \frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) e^{-i(k_1-k_2)\cdot R_i} e^{-i(k_3-k_4)\cdot R_i}.$$

This interaction is also onsite, which means we have to enforce momentum conservation. We can use the identity 

$$\frac{1}{N}\sum_{i} e^{-i (k_1-k_2+k_3-k_4)\cdot R_i} = \sum\delta(k_1-k_2+k_3-k_4,G),$$

where $\delta(..,..)$ is the Kronecker delta function and $G$ is all the reciprocal lattice vectors in momentum space. 

Applying the identity, we can rewrite the interaction term as

$$U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G).$$

Here, the delta function enforces the momentum conservation. Therefore, the third term in the interacting Hamiltonian $\hat{H}^{int}$ with $U_1$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$ is given by the expression above. As noted before, the expression simplifies considerably in the case of an infinite system (where $N$ tends to infinity), because in that case, the sum over $G$ reduces to a delta function that enforces momentum conservation.

## Convert interacting Hamiltonian in real space to momentum space (lattice version) [fourth term] 
**Prompt:**  
You will be instructed to convert the interacting Hamiltonian $\hat{H}^{int}$ in the fourth quantized form the basis in real space to the basis in momentum space. You will be instructed to perform the transformation to the fourth term with $U_1$.
To do that, you should apply the Fourier transformation to $c_{\alpha,s}^\dagger(R_i)$ in the real space to the $c_{\alpha,s}^\dagger(k)$ in the momentum space, which is defined as $c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over all sites in the entire real space, and $k$ is defined within the fourth Brillouin zone. You should follow the EXAMPLE below to apply the Fourier transformation. 
You should recall that the fourth term in $\hat{H}^{int}$ is
$U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i + a_1)$   
Express the fourth term in interacting Hamiltonian $\hat{H}^{int}$ with $U_1$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$. Simplify any summation index if possible.  

===  
EXAMPLE:  
Write an interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form in the real space, $\hat{H}^{int}=\sum_{s,s'}\sum_{i,j} U(R_i-R_j) c_s^\dagger(R_i) c_{s'}^\dagger(R_j) c_{s'}(R_j) c_s(R_i)$, where $i,j$ are summed over the entire real space.  
Define the Fourier transformation $c_s^\dagger(k)=\frac{1}{\sqrt{N}} \sum_{i}c_s^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over the entire real space containing $N$ unit cells, $N$ is the number of unit cells.  
This leads to the inverse Fourier transformation $c_s^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_s^\dagger(k) e^{-i k \cdot R_i}$, where $k$ is summed over the first Brillouin zone.  
Thus, substitute $c^\dagger(R_i)$ and $c(R_j)$ into $\hat{H}^{int}$, we get  
$$\hat{H}^{int} = \sum_{s,s'}\sum_{i,j} U(R_i-R_j) \frac{1}{\sqrt{N}} \sum_{k_1} c_s^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{\sqrt{N}} \sum_{k_2} c_{s'}^\dagger(k_2) e^{-i k_2 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_3} c_{s'}(k_3) e^{i k_3 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_4} c_s(k_4) e^{i k_4 \cdot R_i}=\sum_{s,s'}\sum_{i,j}\frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4}U(R_i-R_j)c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot R_i} e^{-i(k_2-k_3)\cdot R_j}$$
Now make a replacement by defining $n= R_i-R_j$  
The Hamiltonian become  
$$\hat{H}^{int}=\frac{1}{N^2} \sum_{j,n} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} U(n) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot n} e^{-i(k_1-k_4+k_2-k_3)\cdot r_j }$$
Because $\frac{1}{N}\sum_{i} e^{-i (k_1-k_4+k_2-k_3)\cdot R_i} = \sum\delta(k_1-k_4+k_2-k_3,G)$, where $\delta(..,..)$ is the Kronecker delta function, and $G$ is the all reciprocal lattices in the momentum space.  
Therefore,  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{n} U(n) e^{-i (k_1-k_4) \cdot n} c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$
If we define interaction in the momentum space $U(k)=\sum_{n} U(n) e^{-i k \cdot n}$, where $n$ is the summation of all hopping pairs, the interacting Hamiltonian in the momentum space is  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4}  U(k_1-k_4) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$

**Completion:**  
The fourth term in the interacting Hamiltonian $\hat{H}^{int}$ in real space is given by 

$$U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i + a_1).$$ 

Here $n_{A,s}(R_i)$ and $n_{B,s'}(R_i + a_1)$ represent the number of electrons at site $R_i$ and $R_i + a_1$, respectively. In terms of the creation and annihilation operators, they are given by $c_{A,s}^\dagger(R_i)c_{A,s}(R_i)$ and $c_{B,s'}^\dagger(R_i+a_1)c_{B,s'}(R_i+a_1)$, respectively. 

Therefore, we can rewrite the fourth term as:

$$U_1\sum_{i,s,s'} c_{A,s}^\dagger(R_i)c_{A,s}(R_i) c_{B,s'}^\dagger(R_i+a_1)c_{B,s'}(R_i+a_1)$$

Now we will apply the Fourier transformation:

$c_{\alpha,s}^\dagger(k) = \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$

and its inverse:

$c_{\alpha,s}^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_{\alpha,s}^\dagger(k) e^{-i k \cdot R_i}$.

After substituting the Fourier transformations for the creation and annihilation operators, we obtain:

$$\hat{H}^{int} = \frac{U_1}{N^2} \sum_{i,s,s'} \sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1)e^{-i k_1 \cdot R_i} c_{A,s}(k_2)e^{i k_2 \cdot R_i} c_{B,s'}^\dagger(k_3)e^{-i k_3 \cdot (R_i + a_1)} c_{B,s'}(k_4)e^{i k_4 \cdot (R_i + a_1)}.$$

Now, we sum over $i$ and employ the orthonormality of the plane wave states:

$$\hat{H}^{int} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1},$$

where $G$ runs over the fourth Brillouin zone. Note that the phase factor $e^{-i (k_3 - k_4) \cdot a_1}$ appears because the operators for $c_{B,s'}^\dagger$ and $c_{B,s'}$ act on different sites ($R_i$ and $R_i + a_1$), and we have taken the translation invariance of the lattice into account. This transformation transforms the interaction from the real space to the momentum space.


## Convert interacting Hamiltonian in real space to momentum space (lattice version) [fifth term] 
**Prompt:**  
You will be instructed to convert the interacting Hamiltonian $\hat{H}^{int}$ in the fifth quantized form the basis in real space to the basis in momentum space. You will be instructed to perform the transformation to the fifth term with $U_1$.
To do that, you should apply the Fourier transformation to $c_{\alpha,s}^\dagger(R_i)$ in the real space to the $c_{\alpha,s}^\dagger(k)$ in the momentum space, which is defined as $c_{\alpha,s}^\dagger(k)= \frac{1}{\sqrt{N}} \sum_i c_{\alpha,s}^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over all sites in the entire real space, and $k$ is defined within the fifth Brillouin zone. You should follow the EXAMPLE below to apply the Fourier transformation. 
You should recall that the fifth term in $\hat{H}^{int}$ is
$U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i + a_2)$   
Express the fifth term in interacting Hamiltonian $\hat{H}^{int}$ with $U_1$ in terms of $c_{\alpha,s}(k)$ and $c_{\alpha,s}^\dagger(k)$. Simplify any summation index if possible.  

===  
EXAMPLE:  
Write an interacting Hamiltonian $\hat{H}^{int}$ in the second quantized form in the real space, $\hat{H}^{int}=\sum_{s,s'}\sum_{i,j} U(R_i-R_j) c_s^\dagger(R_i) c_{s'}^\dagger(R_j) c_{s'}(R_j) c_s(R_i)$, where $i,j$ are summed over the entire real space.  
Define the Fourier transformation $c_s^\dagger(k)=\frac{1}{\sqrt{N}} \sum_{i}c_s^\dagger(R_i) e^{i k \cdot R_i}$, where $i$ is integrated over the entire real space containing $N$ unit cells, $N$ is the number of unit cells.  
This leads to the inverse Fourier transformation $c_s^\dagger(R_i) = \frac{1}{\sqrt{N}} \sum_k c_s^\dagger(k) e^{-i k \cdot R_i}$, where $k$ is summed over the first Brillouin zone.  
Thus, substitute $c^\dagger(R_i)$ and $c(R_j)$ into $\hat{H}^{int}$, we get  
$$\hat{H}^{int} = \sum_{s,s'}\sum_{i,j} U(R_i-R_j) \frac{1}{\sqrt{N}} \sum_{k_1} c_s^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{\sqrt{N}} \sum_{k_2} c_{s'}^\dagger(k_2) e^{-i k_2 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_3} c_{s'}(k_3) e^{i k_3 \cdot R_j} \frac{1}{\sqrt{N}} \sum_{k_4} c_s(k_4) e^{i k_4 \cdot R_i}=\sum_{s,s'}\sum_{i,j}\frac{1}{N^2}\sum_{k_1,k_2,k_3,k_4}U(R_i-R_j)c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot R_i} e^{-i(k_2-k_3)\cdot R_j}$$
Now make a replacement by defining $n= R_i-R_j$  
The Hamiltonian become  
$$\hat{H}^{int}=\frac{1}{N^2} \sum_{j,n} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} U(n) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4)e^{-i(k_1-k_4)\cdot n} e^{-i(k_1-k_4+k_2-k_3)\cdot r_j }$$
Because $\frac{1}{N}\sum_{i} e^{-i (k_1-k_4+k_2-k_3)\cdot R_i} = \sum\delta(k_1-k_4+k_2-k_3,G)$, where $\delta(..,..)$ is the Kronecker delta function, and $G$ is the all reciprocal lattices in the momentum space.  
Therefore,  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{n} U(n) e^{-i (k_1-k_4) \cdot n} c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$
If we define interaction in the momentum space $U(k)=\sum_{n} U(n) e^{-i k \cdot n}$, where $n$ is the summation of all hopping pairs, the interacting Hamiltonian in the momentum space is  
$$\hat{H}^{int}=\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4}  U(k_1-k_4) c_s^\dagger(k_1)c_{s'}^\dagger(k_2)c_{s'}(k_3)c_s(k_4) \sum_{G} \delta(k_1-k_4+k_2-k_3,G)$$

**Completion:**  
Alright, the fifth term of the Hamiltonian $\hat{H}^{int}$ in real space is given by $U_1\sum_{i,s,s'} n_{A,s}(R_i) n_{B,s'}(R_i + a_2)$.

We express $n_{A,s}(R_i)$ and $n_{B,s'}(R_i + a_2)$ in terms of creation and annihilation operators. We have:

$$n_{A,s}(R_i) = c_{A,s}^\dagger(R_i) c_{A,s}(R_i)$$

and

$$n_{B,s'}(R_i + a_2) = c_{B,s'}^\dagger(R_i + a_2) c_{B,s'}(R_i + a_2)$$

Substituting these expressions and using the Fourier transformations for the creation and annihilation operators, we obtain

$$\hat{H}^{int} = U_1\sum_{i,s,s'} \left( \frac{1}{N} \sum_{k_1} c_{A,s}^\dagger(k_1) e^{-i k_1 \cdot R_i} \frac{1}{N} \sum_{k_2} c_{A,s}(k_2) e^{i k_2 \cdot R_i} \right) \left( \frac{1}{N} \sum_{k_3} c_{B,s'}^\dagger(k_3) e^{-i k_3 \cdot (R_i + a_2)} \frac{1}{N} \sum_{k_4} c_{B,s'}(k_4) e^{i k_4 \cdot (R_i + a_2)} \right)$$

Now, rearranging the terms:

$$\hat{H}^{int} = \frac{U_1}{N^2} \sum_{i,s,s'}\sum_{k_1,k_2,k_3,k_4} e^{-i (k_1 - k_2 + k_3 - k_4) \cdot R_i} e^{-i (k_3 - k_4) \cdot a_2} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4)$$

We can again use the property of the Fourier transformation for the periodic lattice system:

$$\frac{1}{N}\sum_{i} e^{-i (k_1 - k_2 + k_3 - k_4)\cdot R_i} = \sum_{G}\delta(k_1 - k_2 + k_3 - k_4, G)$$

And get:

$$\hat{H}^{int} = \frac{U_1}{N} \sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4)$$

With this result, we've converted the fifth term in the interacting Hamiltonian $\hat{H}^{int}$ from the real space basis to the momentum space basis. The Kronecker delta function enforces momentum conservation during the interaction.

# Mean-field theory
## Wick's theorem [first term]
You will be instructed to perform a Hartree-Fock approximation to expand the interaction term $\hat{H}^{int}$. You will be instructed to perform the transformation to the first term with $U_0$.
You should use Wick's theorem to expand the four-fermion term in $\hat{H}^{int}$ into quadratic terms. You should strictly follow the EXAMPLE below to expand using Wick's theorem, select the correct EXAMPLE by noticing the order of four term product with and without ${}^\dagger$, and be extremely cautious about the order of the index and sign before each term.  
You should only preserve the normal terms. Here, the normal terms mean the product of a creation operator and an annihilation operator.  
You should recall that the first term is $$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G).$$ 
Return the expanded interaction term after Hartree-Fock approximation $\hat{H}^{int,HF,U_0}$.

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\langle c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2) \rangle$ : expectation of $c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2)$ over the many-body ground states  
$\hat{H}^{int,HF,U_0}$ : first term in the interaction term after Hartree-Fock approximation  

===  
EXAMPLE 1:  
For a four-fermion term $a_1^\dagger a_2^\dagger a_3 a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2^\dagger a_3 a_4 = \langle a_1^\dagger a_4 \rangle a_2^\dagger a_3 + \langle a_2^\dagger a_3 \rangle a_1^\dagger a_4 - \langle a_1^\dagger a_4 \rangle \langle a_2^\dagger a_3\rangle - \langle a_1^\dagger a_3 \rangle a_2^\dagger a_4 - \langle a_2^\dagger a_4 \rangle a_1^\dagger a_3 + \langle a_1^\dagger a_3\rangle \langle a_2^\dagger a_4 \rangle$  
Be cautious about the order of the index and sign before each term here.

EXAMPLE 2:  
For a four-fermion term $a_1^\dagger a_2 a_3^\dagger a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2 a_3^\dagger a_4 = \langle a_1^\dagger a_2 \rangle a_3^\dagger a_4 + \langle a_3^\dagger a_4 \rangle a_1^\dagger a_2 - \langle a_1^\dagger a_2 \rangle \langle a_3^\dagger a_4\rangle - \langle a_1^\dagger a_4 \rangle a_3^\dagger a_2 - \langle a_3^\dagger a_2 \rangle a_1^\dagger a_4 + \langle a_1^\dagger a_4\rangle \langle a_3^\dagger a_2 \rangle$  
Be cautious about the order of the index and sign before each term here.

**Completion:**  
Following the provided examples, we can apply the Wick's theorem to the interaction term, to get normal terms. Given the interaction term:

$$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G)$$

Let's denote the above operators as: $a = c_{A,\uparrow}^\dagger(k_1)$, $b = c_{A,\uparrow}(k_2)$, $c = c_{A,\downarrow}^\dagger(k_3)$, and $d = c_{A,\downarrow}(k_4)$ for simplicity. 

We can expand it using Wick's theorem. As the first term has the form $a^\dagger b c^\dagger d$, we should use the expansion provided in EXAMPLE 2:

$$a^\dagger b c^\dagger d = \langle a^\dagger b \rangle c^\dagger d + \langle c^\dagger d \rangle a^\dagger b - \langle a^\dagger b \rangle \langle c^\dagger d\rangle - \langle a^\dagger d \rangle c^\dagger b - \langle c^\dagger b \rangle a^\dagger d + \langle a^\dagger d\rangle \langle c^\dagger b \rangle$$

After substituting back the actual operators we get:

$$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) + \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) - \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle - \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) - \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) + \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle]$$

So, we obtain the first term in the interaction term after Hartree-Fock approximation, $\hat{H}^{int,HF,U_0}$.


## Wick's theorem [second term]
You will be instructed to perform a Hartree-Fock approximation to expand the interaction term $\hat{H}^{int}$. You will be instructed to perform the transformation to the second term with $U_0$.
You should use Wick's theorem to expand the four-fermion term in $\hat{H}^{int}$ into quadratic terms. You should strictly follow the EXAMPLE below to expand using Wick's theorem, select the correct EXAMPLE by noticing the order of four term product with and without ${}^\dagger$, and be extremely cautious about the order of the index and sign before each term.  
You should only preserve the normal terms. Here, the normal terms mean the product of a creation operator and an annihilation operator.  
You should recall that the second term is $$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G).$$ 
Return the expanded interaction term after Hartree-Fock approximation $\hat{H}^{int,HF,U_0}$.

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\langle c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2) \rangle$ : expectation of $c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2)$ over the many-body ground states  
$\hat{H}^{int,HF,U_0}$ : second term in the interaction term after Hartree-Fock approximation  

===  
EXAMPLE 1:  
For a four-fermion term $a_1^\dagger a_2^\dagger a_3 a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2^\dagger a_3 a_4 = \langle a_1^\dagger a_4 \rangle a_2^\dagger a_3 + \langle a_2^\dagger a_3 \rangle a_1^\dagger a_4 - \langle a_1^\dagger a_4 \rangle \langle a_2^\dagger a_3\rangle - \langle a_1^\dagger a_3 \rangle a_2^\dagger a_4 - \langle a_2^\dagger a_4 \rangle a_1^\dagger a_3 + \langle a_1^\dagger a_3\rangle \langle a_2^\dagger a_4 \rangle$  
Be cautious about the order of the index and sign before each term here.

EXAMPLE 2:  
For a four-fermion term $a_1^\dagger a_2 a_3^\dagger a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2 a_3^\dagger a_4 = \langle a_1^\dagger a_2 \rangle a_3^\dagger a_4 + \langle a_3^\dagger a_4 \rangle a_1^\dagger a_2 - \langle a_1^\dagger a_2 \rangle \langle a_3^\dagger a_4\rangle - \langle a_1^\dagger a_4 \rangle a_3^\dagger a_2 - \langle a_3^\dagger a_2 \rangle a_1^\dagger a_4 + \langle a_1^\dagger a_4\rangle \langle a_3^\dagger a_2 \rangle$  
Be cautious about the order of the index and sign before each term here.

**Completion:**  
The interaction term you specified is:

$$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G)$$

This term can be rearranged to a form $a^\dagger b c^\dagger d$ as before. Specifically, we have: $a = c_{B,\uparrow}^\dagger(k_1)$, $b = c_{B,\uparrow}(k_2)$, $c = c_{B,\downarrow}^\dagger(k_3)$, and $d = c_{B,\downarrow}(k_4)$.

We can then expand this term using Wick's theorem as given in EXAMPLE 2:

$$a^\dagger b c^\dagger d = \langle a^\dagger b \rangle c^\dagger d + \langle c^\dagger d \rangle a^\dagger b - \langle a^\dagger b \rangle \langle c^\dagger d\rangle - \langle a^\dagger d \rangle c^\dagger b - \langle c^\dagger b \rangle a^\dagger d + \langle a^\dagger d\rangle \langle c^\dagger b \rangle$$

Substituting the original operators back into this expression gives:

$$U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) + \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) - \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle - \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) - \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) + \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle]$$

This is the second term in the interaction term after the Hartree-Fock approximation, $\hat{H}^{int,HF,U_0}$.   

## Wick's theorem [third term]
You will be instructed to perform a Hartree-Fock approximation to expand the interaction term $\hat{H}^{int}$. You will be instructed to perform the transformation to the third term with $U_1$.
You should use Wick's theorem to expand the four-fermion term in $\hat{H}^{int}$ into quadratic terms. You should strictly follow the EXAMPLE below to expand using Wick's theorem, select the correct EXAMPLE by noticing the order of four term product with and without ${}^\dagger$, and be extremely cautious about the order of the index and sign before each term.  
You should only preserve the normal terms. Here, the normal terms mean the product of a creation operator and an annihilation operator.  
You should recall that the third term is $$U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G).$$ 
Return the expanded interaction term after Hartree-Fock approximation $\hat{H}^{int,HF,U_1}$.

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\langle c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2) \rangle$ : expectation of $c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2)$ over the many-body ground states  
$\hat{H}^{int,HF,U_1}$ : third term in the interaction term after Hartree-Fock approximation  

===  
EXAMPLE 1:  
For a four-fermion term $a_1^\dagger a_2^\dagger a_3 a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2^\dagger a_3 a_4 = \langle a_1^\dagger a_4 \rangle a_2^\dagger a_3 + \langle a_2^\dagger a_3 \rangle a_1^\dagger a_4 - \langle a_1^\dagger a_4 \rangle \langle a_2^\dagger a_3\rangle - \langle a_1^\dagger a_3 \rangle a_2^\dagger a_4 - \langle a_2^\dagger a_4 \rangle a_1^\dagger a_3 + \langle a_1^\dagger a_3\rangle \langle a_2^\dagger a_4 \rangle$  
Be cautious about the order of the index and sign before each term here.

EXAMPLE 2:  
For a four-fermion term $a_1^\dagger a_2 a_3^\dagger a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2 a_3^\dagger a_4 = \langle a_1^\dagger a_2 \rangle a_3^\dagger a_4 + \langle a_3^\dagger a_4 \rangle a_1^\dagger a_2 - \langle a_1^\dagger a_2 \rangle \langle a_3^\dagger a_4\rangle - \langle a_1^\dagger a_4 \rangle a_3^\dagger a_2 - \langle a_3^\dagger a_2 \rangle a_1^\dagger a_4 + \langle a_1^\dagger a_4\rangle \langle a_3^\dagger a_2 \rangle$  
Be cautious about the order of the index and sign before each term here.

**Completion:**  
The interaction term you specified is:

$$U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \sum_{G} \delta(k_1-k_2+k_3-k_4,G)$$

This term can be rearranged to a form $a^\dagger b c^\dagger d$ as before. Specifically, we have: $a = c_{A,s}^\dagger(k_1)$, $b = c_{A,s}(k_2)$, $c = c_{B,s'}^\dagger(k_3)$, and $d = c_{B,s'}(k_4)$.

We can then expand this term using Wick's theorem as given in EXAMPLE 2:

$$a^\dagger b c^\dagger d = \langle a^\dagger b \rangle c^\dagger d + \langle c^\dagger d \rangle a^\dagger b - \langle a^\dagger b \rangle \langle c^\dagger d\rangle - \langle a^\dagger d \rangle c^\dagger b - \langle c^\dagger b \rangle a^\dagger d + \langle a^\dagger d\rangle \langle c^\dagger b \rangle$$

Substituting the original operators back into this expression gives:

$$U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) + \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle]$$

This is the third term in the interaction term after the Hartree-Fock approximation, $\hat{H}^{int,HF,U_1}$.

## Wick's theorem [fourth term]
You will be instructed to perform a Hartree-Fock approximation to expand the interaction term $\hat{H}^{int}$. You will be instructed to perform the transformation to the fourth term with $U_1$.
You should use Wick's theorem to expand the four-fermion term in $\hat{H}^{int}$ into quadratic terms. You should strictly follow the EXAMPLE below to expand using Wick's theorem, select the correct EXAMPLE by noticing the order of four term product with and without ${}^\dagger$, and be extremely cautious about the order of the index and sign before each term.  
You should only preserve the normal terms. Here, the normal terms mean the product of a creation operator and an annihilation operator.  
You should recall that the fourth term is $$\hat{H}^{int} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1}$$ 
Return the expanded interaction term after Hartree-Fock approximation $\hat{H}^{int,HF,U_1}$.

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\langle c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2) \rangle$ : expectation of $c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2)$ over the many-body ground states  
$\hat{H}^{int,HF,U_1}$ : fourth term in the interaction term after Hartree-Fock approximation  

===  
EXAMPLE 1:  
For a four-fermion term $a_1^\dagger a_2^\dagger a_3 a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2^\dagger a_3 a_4 = \langle a_1^\dagger a_4 \rangle a_2^\dagger a_3 + \langle a_2^\dagger a_3 \rangle a_1^\dagger a_4 - \langle a_1^\dagger a_4 \rangle \langle a_2^\dagger a_3\rangle - \langle a_1^\dagger a_3 \rangle a_2^\dagger a_4 - \langle a_2^\dagger a_4 \rangle a_1^\dagger a_3 + \langle a_1^\dagger a_3\rangle \langle a_2^\dagger a_4 \rangle$  
Be cautious about the order of the index and sign before each term here.

EXAMPLE 2:  
For a four-fermion term $a_1^\dagger a_2 a_3^\dagger a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2 a_3^\dagger a_4 = \langle a_1^\dagger a_2 \rangle a_3^\dagger a_4 + \langle a_3^\dagger a_4 \rangle a_1^\dagger a_2 - \langle a_1^\dagger a_2 \rangle \langle a_3^\dagger a_4\rangle - \langle a_1^\dagger a_4 \rangle a_3^\dagger a_2 - \langle a_3^\dagger a_2 \rangle a_1^\dagger a_4 + \langle a_1^\dagger a_4\rangle \langle a_3^\dagger a_2 \rangle$  
Be cautious about the order of the index and sign before each term here.

**Completion:**  
The interaction term you specified is:

$$\frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1}$$

As in the previous example, we can rearrange this term into a form $a^\dagger b c^\dagger d$ as: $a = c_{A,s}^\dagger(k_1)$, $b = c_{A,s}(k_2)$, $c = c_{B,s'}^\dagger(k_3)$, and $d = c_{B,s'}(k_4)$.

We can then apply Wick's theorem as given in EXAMPLE 2 to expand this term. Doing so, we get:

$$\hat{H}^{int,HF,U_1} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) + \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle]$$

This is the fourth term in the interaction term after the Hartree-Fock approximation, $\hat{H}^{int,HF,U_1}$. The expectation values in this expression represent averages over the many-body ground states.


## Wick's theorem [fifth term]
You will be instructed to perform a Hartree-Fock approximation to expand the interaction term $\hat{H}^{int}$. You will be instructed to perform the transformation to the fifth term with $U_1$.
You should use Wick's theorem to expand the four-fermion term in $\hat{H}^{int}$ into quadratic terms. You should strictly follow the EXAMPLE below to expand using Wick's theorem, select the correct EXAMPLE by noticing the order of four term product with and without ${}^\dagger$, and be extremely cautious about the order of the index and sign before each term.  
You should only preserve the normal terms. Here, the normal terms mean the product of a creation operator and an annihilation operator.  
You should recall that the fifth term is $$\hat{H}^{int} = \frac{U_1}{N} \sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4)$$
 
Return the expanded interaction term after Hartree-Fock approximation $\hat{H}^{int,HF,U_1}$.

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\langle c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2) \rangle$ : expectation of $c_{\alpha,s}^\dagger(k_1) c_{\alpha^{\prime},s^{\prime}}(k_2)$ over the many-body ground states  
$\hat{H}^{int,HF,U_1}$ : fifth term in the interaction term after Hartree-Fock approximation  

===  
EXAMPLE 1:  
For a four-fermion term $a_1^\dagger a_2^\dagger a_3 a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2^\dagger a_3 a_4 = \langle a_1^\dagger a_4 \rangle a_2^\dagger a_3 + \langle a_2^\dagger a_3 \rangle a_1^\dagger a_4 - \langle a_1^\dagger a_4 \rangle \langle a_2^\dagger a_3\rangle - \langle a_1^\dagger a_3 \rangle a_2^\dagger a_4 - \langle a_2^\dagger a_4 \rangle a_1^\dagger a_3 + \langle a_1^\dagger a_3\rangle \langle a_2^\dagger a_4 \rangle$  
Be cautious about the order of the index and sign before each term here.

EXAMPLE 2:  
For a four-fermion term $a_1^\dagger a_2 a_3^\dagger a_4$, using Wick's theorem and preserving only the normal terms. this is expanded as $a_1^\dagger a_2 a_3^\dagger a_4 = \langle a_1^\dagger a_2 \rangle a_3^\dagger a_4 + \langle a_3^\dagger a_4 \rangle a_1^\dagger a_2 - \langle a_1^\dagger a_2 \rangle \langle a_3^\dagger a_4\rangle - \langle a_1^\dagger a_4 \rangle a_3^\dagger a_2 - \langle a_3^\dagger a_2 \rangle a_1^\dagger a_4 + \langle a_1^\dagger a_4\rangle \langle a_3^\dagger a_2 \rangle$  
Be cautious about the order of the index and sign before each term here.

**Completion:**  
The interaction term you specified is:

$$\hat{H}^{int} = \frac{U_1}{N} \sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} c_{A,s}^\dagger(k_1) c_{A,s}(k_2) c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4)$$

In this term, $a = c_{A,s}^\dagger(k_1)$, $b = c_{A,s}(k_2)$, $c = c_{B,s'}^\dagger(k_3)$, and $d = c_{B,s'}(k_4)$. This is in the form $a^\dagger b c^\dagger d$ as in EXAMPLE 2. We can apply Wick's theorem to this term, getting:

$$\hat{H}^{int,HF,U_1} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) + \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle]$$

This is the fifth term in the interaction term after the Hartree-Fock approximation, $\hat{H}^{int,HF,U_1}$. The expectation values in this expression represent averages over the many-body ground states.

## Extract quadratic term [first term]
**Prompt:**  
You will be instructed to extract the quadratic terms in the $\hat{H}^{int,HF,U_0}$.  
The quadratic terms mean terms that are proportional to $c^\dagger c$, which excludes terms that are solely expectations or products of expectations.  
You should only preserve the quadratic terms in $\hat{H}^{int,HF,U_0}$, which is called $\hat{H}^{int,HF,U_0,2}$.
You should recall that 
$$\hat{H}^{int,HF,U_0}= U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) + \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) - \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle - \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) - \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) + \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle]$$
Return this Hamiltonian $\hat{H}^{int,HF,U_0,2}$.  

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\hat{H}^{int,HF,U_0,2}$ : the quadratic terms in $\hat{H}^{int,HF,U_0}$
**Completion:**  
Looking at the expression for $\hat{H}^{int,HF,U_0}$, the quadratic terms are those which involve operator products of the form $c^\dagger c$. 

This is so because terms involving only expectations and terms that are products of expectations are not quadratic in the fermionic operators. We do not need to include those terms.

So, we keep the terms that are proportional to $c^\dagger c$, which gives us:

$$\hat{H}^{int,HF,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) + \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) - \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) - \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4)]$$

This is $\hat{H}^{int,HF,U_0,2}$, which contains only the quadratic terms from the Hartree-Fock approximation of the interaction term $\hat{H}^{int,HF,U_0}$. The terms with only expectations or products of expectations have been excluded.

## Extract quadratic term [second term]
**Prompt:**  
You will be instructed to extract the quadratic terms in the $\hat{H}^{int,HF,U_0}$.  
The quadratic terms mean terms that are proportional to $c^\dagger c$, which excludes terms that are solely expectations or products of expectations.  
You should only preserve the quadratic terms in $\hat{H}^{int,HF,U_0}$, which is called $\hat{H}^{int,HF,U_0,2}$.
You should recall that 
$$\hat{H}^{int,HF,U_0}= U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) + \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) - \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle - \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) - \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) + \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle]$$
Return this Hamiltonian $\hat{H}^{int,HF,U_0,2}$.  

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\hat{H}^{int,HF,U_0,2}$ : the quadratic terms in $\hat{H}^{int,HF,U_0}$

**Completion:**  
Given the interaction Hamiltonian $\hat{H}^{int,HF,U_0}$, the quadratic terms are those which involve operator products of the form $c^\dagger c$. These terms are not the same as terms involving only expectations or terms that are products of expectations. We exclude those latter terms to get the quadratic term Hamiltonian.

In this case, the quadratic terms from $\hat{H}^{int,HF,U_0}$ are:

$$\hat{H}^{int,HF,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) + \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) - \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) - \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4)]$$

This $\hat{H}^{int,HF,U_0,2}$ contains only the quadratic terms from the Hartree-Fock approximation of the interaction term $\hat{H}^{int,HF,U_0}$. The terms with only expectations or products of expectations have been excluded.

## Extract quadratic term [third term]
**Prompt:**  
You will be instructed to extract the quadratic terms in the $\hat{H}^{int,HF,U_1}$.  
The quadratic terms mean terms that are proportional to $c^\dagger c$, which excludes terms that are solely expectations or products of expectations.  
You should only preserve the quadratic terms in $\hat{H}^{int,HF,U_1}$, which is called $\hat{H}^{int,HF,U_1,2}$.
You should recall that 
$$\hat{H}^{int,HF,U_1}= U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) + \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle]$$
Return this Hamiltonian $\hat{H}^{int,HF,U_1,2}$.  

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\hat{H}^{int,HF,U_1,2}$ : the quadratic terms in $\hat{H}^{int,HF,U_1}$

**Completion:**  
Given the interaction Hamiltonian $\hat{H}^{int,HF,U_1}$, the quadratic terms are those which involve operator products of the form $c^\dagger c$. We need to extract these terms while excluding those that are solely expectations or products of expectations.

In this case, the quadratic terms from $\hat{H}^{int,HF,U_1}$ are:

$$\hat{H}^{int,HF,U_1,2} = U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)]$$

This $\hat{H}^{int,HF,U_1,2}$ contains only the quadratic terms from the Hartree-Fock approximation of the interaction term $\hat{H}^{int,HF,U_1}$. The terms with only expectations or products of expectations have been excluded.


## Extract quadratic term [fourth term]
**Prompt:**  
You will be instructed to extract the quadratic terms in the $\hat{H}^{int,HF,U_1}$.  
The quadratic terms mean terms that are proportional to $c^\dagger c$, which excludes terms that are solely expectations or products of expectations.  
You should only preserve the quadratic terms in $\hat{H}^{int,HF,U_1}$, which is called $\hat{H}^{int,HF,U_1,2}$.
You should recall that 
$$\hat{H}^{int,HF,U_1}= \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) + \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle]$$
Return this Hamiltonian $\hat{H}^{int,HF,U_1,2}$.  

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\hat{H}^{int,HF,U_1,2}$ : the quadratic terms in $\hat{H}^{int,HF,U_1}$

**Completion:**  
Given the interaction Hamiltonian $\hat{H}^{int,HF,U_1}$, the quadratic terms are those which involve operator products of the form $c^\dagger c$. We need to extract these terms while excluding those that are solely expectations or products of expectations.

In this case, the quadratic terms from $\hat{H}^{int,HF,U_1}$ are:

$$\hat{H}^{int,HF,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)]$$

This $\hat{H}^{int,HF,U_1,2}$ contains only the quadratic terms from the Hartree-Fock approximation of the interaction term $\hat{H}^{int,HF,U_1}$. The terms with only expectations or products of expectations have been excluded.

## Extract quadratic term [fifth term]
**Prompt:**  
You will be instructed to extract the quadratic terms in the $\hat{H}^{int,HF,U_1}$.  
The quadratic terms mean terms that are proportional to $c^\dagger c$, which excludes terms that are solely expectations or products of expectations.  
You should only preserve the quadratic terms in $\hat{H}^{int,HF,U_1}$, which is called $\hat{H}^{int,HF,U_1,2}$.
You should recall that 
$$\hat{H}^{int,HF,U_1}= \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) + \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle]$$
Return this Hamiltonian $\hat{H}^{int,HF,U_1,2}$.  

Use the following conventions for the symbols (You should also obey the conventions in all my previous prompts if you encounter undefined symbols. If you find it is never defined or has conflicts in the conventions, you should stop and let me know):  
$\hat{H}^{int,HF,U_1,2}$ : the quadratic terms in $\hat{H}^{int,HF,U_1}$

**Completion:** 
Given the interaction Hamiltonian $\hat{H}^{int,HF,U_1}$, the quadratic terms are those which involve operator products of the form $c^\dagger c$. We need to extract these terms while excluding those that are solely expectations or products of expectations.

In this case, the quadratic terms from $\hat{H}^{int,HF,U_1}$ are:

$$\hat{H}^{int,HF,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)]$$

This $\hat{H}^{int,HF,U_1,2}$ contains only the quadratic terms from the Hartree-Fock approximation of the interaction term $\hat{H}^{int,HF,U_1}$. The terms with only expectations or products of expectations have been excluded.

# Simplify the MF quadratic term 
## Swap the index only [first Hartree term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Hartree,U_0,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Hartree term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Hartree term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ applied to ONLY the second Hartree term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Hartree term, you can make the second Hartree term look identical to the first Hartree term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Hartree,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) \langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) + \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2)$  
Return the simplied $\hat{H}^{int,Hartree,U_0,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
The objective is to simplify $\hat{H}^{int,Hartree,U_0,2}$ by relabeling the indices of the momenta in the second Hartree term, which is $\langle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2)$. Following the direction given, we perform a swapping operation $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ to this term. Note that we only perform the swap in the second term. The first term remains unchanged.

The relabeled second Hartree term becomes: $\langle c_{A,\downarrow}^\dagger(k_1) c_{A,\downarrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_3) c_{A,\uparrow}(k_4)$. 

With this modification, the Hamiltonian $\hat{H}^{int,Hartree,U_0,2}$ simplifies to:

$$\hat{H}^{int,Hartree,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,\uparrow}^\dagger(k_1) c_{A,\uparrow}(k_2) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\downarrow}(k_4) + \langle c_{A,\downarrow}^\dagger(k_1) c_{A,\downarrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_3) c_{A,\uparrow}(k_4)]$$

This is the simplified quadratic term $\hat{H}^{int,Hartree,U_0,2}$ in the Hartree approximation after index relabeling.

## Swap the index only [first Fock term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Fock,U_0,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Fock term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Fock term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ applied to ONLY the second Fock term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Fock term, you can make the second Fock term look identical to the first Fock term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Fock,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) ( -\langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) - \langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4))$  
Return the simplied $\hat{H}^{int,Fock,U_0,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
Following the instructions, we want to simplify the quadratic term $\hat{H}^{int,Fock,U_0,2}$ by relabeling the indices of the momenta in the second Fock term. We will perform the replacement operation $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ to the second term only, leaving the first term unchanged. 

In this case, the second Fock term is $-\langle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) \rangle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4)$. After the relabeling, it becomes $-\langle c_{A,\downarrow}^\dagger(k_1) c_{A,\uparrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_3) c_{A,\downarrow}(k_2)$.

This simplifies $\hat{H}^{int,Fock,U_0,2}$ to:

$$\hat{H}^{int,Fock,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) (-\langle c_{A,\uparrow}^\dagger(k_1) c_{A,\downarrow}(k_4) \rangle c_{A,\downarrow}^\dagger(k_3) c_{A,\uparrow}(k_2) - \langle c_{A,\downarrow}^\dagger(k_1) c_{A,\uparrow}(k_4) \rangle c_{A,\uparrow}^\dagger(k_3) c_{A,\downarrow}(k_2))$$

This is the simplified quadratic term $\hat{H}^{int,Fock,U_0,2}$ in the Fock approximation after index relabeling.


## Swap the index only [second Hartree term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Hartree,U_0,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Hartree term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Hartree term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ applied to ONLY the second Hartree term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Hartree term, you can make the second Hartree term look identical to the first Hartree term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Hartree,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) + \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) ]$  
Return the simplied $\hat{H}^{int,Hartree,U_0,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
The given Hamiltonian is $\hat{H}^{int,Hartree,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) + \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) ]$. We need to simplify this Hamiltonian by swapping the indices in the second Hartree term. 

The instruction is to make a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$, applied only to the second Hartree term.

Doing this, we have for the second term: $\langle c_{B,\downarrow}^\dagger(k_1) c_{B,\downarrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_3) c_{B,\uparrow}(k_4)$. 

Also note that the Kronecker delta $\delta(k_1-k_2+k_3-k_4,G)$ implies $k_1-k_2+k_3-k_4=G$, which means $k_3-k_4=k_1-k_2$. 

Therefore, after swapping the indices in the second term, the Hamiltonian becomes: 

$\hat{H}^{int,Hartree,U_0,2} = U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{B,\uparrow}^\dagger(k_1) c_{B,\uparrow}(k_2) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\downarrow}(k_4) + \langle c_{B,\downarrow}^\dagger(k_1) c_{B,\downarrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_3) c_{B,\uparrow}(k_4) ]$

which looks much simpler as both Hartree terms now look the same. Please keep in mind that this is based on the assumption that $V(q)=V(-q)$, which is satisfied in the case of Coulomb interaction.


## Swap the index only [second Fock term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Fock,U_0,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Fock term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Fock term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ applied to ONLY the second Fock term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Fock term, you can make the second Fock term look identical to the first Fock term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Fock,U_0,2} =U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [- \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) - \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4)]$  
Return the simplied $\hat{H}^{int,Fock,U_0,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
Given the Hamiltonian
$\hat{H}^{int,Fock,U_0,2} =U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [- \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) - \langle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) \rangle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4)]$

As instructed, in the second Fock term, we will relabel the indices as following: $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$. 

After the replacement, the second term becomes:

$- \langle c_{B,\downarrow}^\dagger(k_1) c_{B,\uparrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_3) c_{B,\downarrow}(k_2)$

By using the Kronecker delta function $\delta(k_1-k_2+k_3-k_4,G)$ which implies $k_1-k_2=k_3-k_4$, i.e., $k_3-k_2=k_1-k_4$, the second term further simplifies to 

$- \langle c_{B,\downarrow}^\dagger(k_1) c_{B,\uparrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_3) c_{B,\downarrow}(k_2)$.

As a result, the Hamiltonian is simplified as

$\hat{H}^{int,Fock,U_0,2} =U_0\frac{1}{N}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [- \langle c_{B,\uparrow}^\dagger(k_1) c_{B,\downarrow}(k_4) \rangle c_{B,\downarrow}^\dagger(k_3) c_{B,\uparrow}(k_2) - \langle c_{B,\downarrow}^\dagger(k_1) c_{B,\uparrow}(k_4) \rangle c_{B,\uparrow}^\dagger(k_3) c_{B,\downarrow}(k_2)]$

which is the desired form where both terms have the same structure.

## Swap the index only [third Hartree term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Hartree,U_1,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Hartree term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Hartree term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ applied to ONLY the second Hartree term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Hartree term, you can make the second Hartree term look identical to the first Hartree term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Hartree,U_1,2} = U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) ]$  
Return the simplied $\hat{H}^{int,Hartree,U_1,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
Following the example, we will perform a relabeling in the second Hartree term in $\hat{H}^{int,Hartree,U_1,2}$.

Namely, we will swap:
- $k_1 \leftrightarrow k_3$
- $k_2 \leftrightarrow k_4$
- $s \leftrightarrow s'$

This results in the second term being transformed into:

$\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) \langle c_{B,s}^\dagger(k_1) c_{B,s}(k_2) \rangle c_{A,s'}^\dagger(k_3) c_{A,s'}(k_4)$.

Now the Kronecker dirac function $\delta(k_1-k_2+k_3-k_4,G)$ implies $k_3-k_4=k_1-k_2$, and as per the condition $V(q)=V(-q)$, it simplifies to $V(k_1-k_2)$.

The complete simplified Hamiltonian $\hat{H}^{int,Hartree,U_1,2}$ becomes:

$U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s}^\dagger(k_1) c_{B,s}(k_2) \rangle c_{A,s'}^\dagger(k_3) c_{A,s'}(k_4) ]$.

This simplification is based on the idea of equivalence between the quantum states in terms of their momentum and spin, while ensuring that the order of operators remains unchanged.

## Swap the index only [third Fock term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Fock,U_1,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Fock term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Fock term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$ applied to ONLY the second Fock term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Fock term, you can make the second Fock term look identical to the first Fock term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Fock,U_1,2} = U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [ - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) ]$  
Return the simplied $\hat{H}^{int,Fock,U_1,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
Following the given example, we want to simplify the second Fock term of $\hat{H}^{int,Fock,U_1,2}$ by swapping the indices in the expectation value and the quadratic operators. This will involve the replacements: $s \leftrightarrow s'$, $k_1 \leftrightarrow k_3$, $k_2 \leftrightarrow k_4$. This replacement should not be applied to the indices A and B, as those are not in the summation and are not to be swapped. 

We start with the second term of $\hat{H}^{int,Fock,U_1,2}$, which is:

$- \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) $

After relabeling the indices, we have:

$- \langle c_{B,s}^\dagger(k_1) c_{A,s'}(k_4) \rangle c_{A,s'}^\dagger(k_3) c_{B,s}(k_2)$

The δ function $\delta(k_1-k_2+k_3-k_4,G)$ after relabeling becomes $\delta(k_3-k_4+k_1-k_2,G)$, which is equivalent to $\delta(k_1-k_2+k_3-k_4,G)$ because it requires momentum conservation, which remains the same after swapping.

So the simplified Hamiltonian is then given by:

$\hat{H}^{int,Fock,U_1,2} = U_1\frac{1}{N}\sum_{s,s'}\sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1-k_2+k_3-k_4,G) [ - \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s}^\dagger(k_1) c_{A,s'}(k_4) \rangle c_{A,s'}^\dagger(k_3) c_{B,s}(k_2) ]$

which is a simplified form of the Hamiltonian in which the terms appear more symmetrical.


## Swap the index only [fourth Hartree term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Hartree,U_1,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Hartree term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Hartree term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$, $s\leftrightarrow s^\prime$ applied to ONLY the second Hartree term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Hartree term, you can make the second Hartree term look identical to the first Hartree term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Hartree,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) ]$  
Return the simplied $\hat{H}^{int,Hartree,U_1,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
To simplify the second term of the $\hat{H}^{int,Hartree,U_1,2}$ Hamiltonian by relabeling the indices as per the instructions, we follow the EXAMPLE's methodology. Specifically, we need to swap $k_1 \leftrightarrow k_3$, $k_2 \leftrightarrow k_4$ and $s \leftrightarrow s'$. 

Doing this, the second term of the original Hamiltonian:

$\langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2)$

becomes:

$\langle c_{B,s}^\dagger(k_1) c_{B,s}(k_2) \rangle c_{A,s'}^\dagger(k_3) c_{A,s'}(k_4)$

The delta function also transforms as $\delta(k_1 - k_2 + k_3 - k_4, G) \rightarrow \delta(k_3 - k_4 + k_1 - k_2, G)$, but because the delta function is even, it does not affect the final result.

As such, $\hat{H}^{int,Hartree,U_1,2}$ can be simplified to:

$\hat{H}^{int,Hartree,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s}^\dagger(k_1) c_{B,s}(k_2) \rangle c_{A,s'}^\dagger(k_3) c_{A,s'}(k_4)]$

In this expression, the two terms are now identical except for the labels A and B, making it clearer to interpret and easier to use in subsequent analysis or computations.


## Swap the index only [fourth Fock term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Fock,U_1,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Fock term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Fock term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$, $s\leftrightarrow s^\prime$ applied to ONLY the second Fock term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Fock term, you can make the second Fock term look identical to the first Fock term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Fock,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_1}[- \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)]$  
Return the simplied $\hat{H}^{int,Fock,U_1,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
Following the procedure given in the example, let's simplify $\hat{H}^{int,Fock,U_1,2}$. We can apply the relabeling to the second Fock term:
$\langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)$

According to the instructions, we swap $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$, $s\leftrightarrow s'$, giving:

$\langle c_{B,s}^\dagger(k_1) c_{A,s'}(k_4) \rangle c_{A,s'}^\dagger(k_3) c_{B,s}(k_2)$

Next, we apply the symmetry of the delta function. Note that $\delta(k_1 - k_2 + k_3 - k_4, G) = \delta(k_3 - k_2 + k_1 - k_4, G)$ by the property of the Dirac delta function, so we will keep it as it is.

Finally, since $V(q)=V(-q)$ for Coulomb interaction, the term $e^{-i (k_3 - k_4) \cdot a_1}$ becomes $e^{-i (k_1 - k_2) \cdot a_1}$

Therefore, the simplified $\hat{H}^{int,Fock,U_1,2}$ is:

$\hat{H}^{int,Fock,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_1 - k_2) \cdot a_1}[- \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s}^\dagger(k_1) c_{A,s'}(k_4) \rangle c_{A,s'}^\dagger(k_3) c_{B,s}(k_2)]$

## Swap the index only [fifth Hartree term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Hartree,U_1,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Hartree term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Hartree term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$, $s\leftrightarrow s^\prime$ applied to ONLY the second Hartree term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Hartree term, you can make the second Hartree term look identical to the first Hartree term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Hartree,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2)]$  
Return the simplied $\hat{H}^{int,Hartree,U_1,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
To simplify the given Hamiltonian term $\hat{H}^{int,Hartree,U_1,2}$ by relabeling the indices as per the instructions, let's begin by looking at the second Hartree term:

$\langle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) \rangle c_{A,s}^\dagger(k_1) c_{A,s}(k_2)$

As suggested, we relabel the indices as follows:

$s \leftrightarrow s'$, $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$. After this relabeling, the term becomes:

$\langle c_{B,s}^\dagger(k_1) c_{B,s}(k_2) \rangle c_{A,s'}^\dagger(k_3) c_{A,s'}(k_4)$

Note that $A$ and $B$ are not swapped as they are not part of the indices under the summation.

Next, we have to handle the Kronecker delta function, $\delta(k_1 - k_2 + k_3 - k_4, G)$, which becomes $\delta(k_3 - k_4 + k_1 - k_2, G)$ after the relabeling. 

Since $\delta(x, y) = \delta(y, x)$ for any $x, y$, this is equivalent to $\delta(k_1 - k_2 + k_3 - k_4, G)$. 

Hence, the simplified Hamiltonian term $\hat{H}^{int,Hartree,U_1,2}$, after relabeling the indices becomes:

$\hat{H}^{int,Hartree,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2} [\langle c_{A,s}^\dagger(k_1) c_{A,s}(k_2) \rangle c_{B,s'}^\dagger(k_3) c_{B,s'}(k_4) + \langle c_{B,s}^\dagger(k_1) c_{B,s}(k_2) \rangle c_{A,s'}^\dagger(k_3) c_{A,s'}(k_4)]$

It can be seen that the two terms now look identical, except for the exchange of $A$ and $B$ labels. Note that the order of momenta $k_1, k_2, k_3, k_4$ remains unchanged due to the momentum conservation. This relabeling makes it easier to compare and combine terms in further analytical treatments.


## Swap the index only [fifth Fock term]
You will be instructed to simplify the quadratic term $\hat{H}^{int,Fock,U_1,2}$ through relabeling the index.  
The logic is that the expected value ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle$) in the first Fock term ($\langle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2) \rangle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)$) has the same momentum dependence as the quadratic operators ($c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$) in the second Fock term ($\langle c_{\alpha_2,s_2}^\dagger(k_3) c_{\alpha_2,s_2}(k_4)\rangle c_{\alpha_1,s_1}^\dagger(k_1) c_{\alpha_1,s_1}(k_2)$), and vice versa. Namely, this means a replacement of $k_1 \leftrightarrow k_3$ and $k_2 \leftrightarrow k_4$, $s\leftrightarrow s^\prime$ applied to ONLY the second Fock term. You should not swap any index that is not in the summation, which includes $\uparrow$ and $\downarrow$, A and B. 
This means, if you relabel the index by swapping the index in the "expected value" and "quadratic operators" in the second Fock term, you can make the second Fock term look identical to the first Fock term, as long as $V(q)=V(-q)$, which is naturally satisfied in Coulomb interaction. You should follow the EXAMPLE below to simplify it through relabeling the index.  
You should recall that $\hat{H}^{int,Fock,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_3 - k_4) \cdot a_2}[- \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)]$  
Return the simplied $\hat{H}^{int,Fock,U_1,2}$.

===  
EXAMPLE:  
Given a Hamiltonian $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \rangle c_{d,\sigma_1}^\dagger(k_1) c_{\sigma_4}(k_4) ) \delta_{k_1+k_2,k_3+k_4}$, where $V(q)=V(-q)$.  
In the second term, we relabel the index to swap the index in expected value and the index in quadratic operators, namely, $\sigma_1 \leftrightarrow \sigma_2$, $\sigma_3 \leftrightarrow \sigma_4$, $k_1 \leftrightarrow k_2$, $k_3 \leftrightarrow k_4$. Important: $d$ and $p$ cannot be swapped because they are not indices in the summation.  
After the replacement, the second term becomes $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_2-k_3) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.  
Note that the Kronecker dirac function $\delta_{k_4+k_3,k_2+k_1}$ implies $k_1+k_2=k_3+k_4$, i.e., $k_2-k_3=k_4-k_1$. Thus, the second term simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_4-k_1) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.
Because $V(q)=V(-q)$, meaning $V(k_4-k_1)=V(k_1-k_4)$, the second term further simplifies to $\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3) \delta_{k_4+k_3,k_2+k_1}$.   
Finally, we have the simplified Hamiltonian as  $\hat{H}=\sum_{k_1,k_2, k_3, k_4,\sigma_1,\sigma_2,\sigma_3,\sigma_4} V(k_1-k_4) (\langle c_{d,\sigma_1}^\dagger(k_1) c_{d,\sigma_4}(k_4) \rangle c_{p,\sigma_2}^\dagger(k_2) c_{p,\sigma_3}(k_3) + \langle c_{p,\sigma_1}^\dagger(k_1) c_{p,\sigma_4}(k_4) \rangle c_{d,\sigma_2}^\dagger(k_2) c_{d,\sigma_3}(k_3)) \delta_{k_4+k_3,k_2+k_1}$.

**Completion:**  
Following the example given, we can relabel the indices of the second Fock term in $\hat{H}^{int,Fock,U_1,2}$. We want to swap $s \leftrightarrow s'$, $k_1 \leftrightarrow k_3$, and $k_2 \leftrightarrow k_4$.

The second term of the Hamiltonian initially reads:

$\langle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) \rangle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4)$

After relabeling the indices, it becomes:

$\langle c_{B,s}^\dagger(k_1) c_{A,s'}(k_4) \rangle c_{A,s'}^\dagger(k_3) c_{B,s}(k_2)$

Noting that the Delta function $\delta(k_1 - k_2 + k_3 - k_4, G)$ implies $k_3 - k_2 = k_1 - k_4$, we can replace the argument of the exponential $e^{-i (k_3 - k_4) \cdot a_2}$ with $e^{-i (k_1 - k_2) \cdot a_2}$ since $k_1 - k_2 = k_3 - k_4$ under the constraint of the delta function.

Now, our simplified $\hat{H}^{int,Fock,U_1,2}$ becomes:

$\hat{H}^{int,Fock,U_1,2} = \frac{U_1}{N} \sum_{s,s'} \sum_{k_1,k_2,k_3,k_4} \sum_{G} \delta(k_1 - k_2 + k_3 - k_4, G) e^{-i (k_1 - k_2) \cdot a_2}[- \langle c_{A,s}^\dagger(k_1) c_{B,s'}(k_4) \rangle c_{B,s'}^\dagger(k_3) c_{A,s}(k_2) - \langle c_{B,s}^\dagger(k_1) c_{A,s'}(k_4) \rangle c_{A,s'}^\dagger(k_3) c_{B,s}(k_2)]$

In this form, it is clear that the two terms of the Hamiltonian are identical if the conditions for the Coulomb interaction, $V(q)=V(-q)$, are met, as stated in the problem.
