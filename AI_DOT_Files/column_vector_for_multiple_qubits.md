- For computation to be useful, we must use multiple bits rather than one.
- The size and contents of a qubit's (or group of qubits') column vector corresponds with binary:
$2^{(\text{number of qubits})}$

> - You need an entry in the column vector for every possible state that the number of qubits can make.

**1 Qubit** : column vector size = $2^1$

$$
0 = 
\begin{pmatrix}
1 \\
0
\end{pmatrix} \hspace{3em}
1 = 
\begin{pmatrix}
0 \\
1
\end{pmatrix}
$$

**2 Qubits** : column vector size = $2^2$

$$
00 = 
\begin{pmatrix}
1 \\ 
0 \\ 
0 \\ 
0
\end{pmatrix} \hspace{3em}
01 = 
\begin{pmatrix}
0 \\ 
1 \\ 
0 \\ 
0
\end{pmatrix} \hspace{3em}
10 = 
\begin{pmatrix}
0 \\ 
0 \\ 
1 \\ 
0
\end{pmatrix} \hspace{3em}
11 = 
\begin{pmatrix}
0 \\ 
0 \\ 
0 \\ 
1
\end{pmatrix}
$$

> - Mention how the 2-qubit vectors are just binary 00, 01, 10, 11 going down the entries.

General Form:
- Given two qubits $\alpha$ and $\beta$, the combined state of both qubits can be represented like so:

$$
\begin{pmatrix}
\alpha_0 \\
\alpha_1
\end{pmatrix}
\otimes 
\begin{pmatrix}
\beta_0 \\
\beta_1
\end{pmatrix} = 
\begin{pmatrix}
\alpha_0 \beta_0 \\ 
\alpha_0 \beta_1 \\ 
\alpha_1 \beta_0 \\ 
\alpha_1 \beta_1
\end{pmatrix}
$$

> - The operation is called tensor product, but won't be discussed.
> - In essence, take every possible combination of the 2 qubits to form the new column vector.

Example: given a qubit in state 1 and another qubit in state 0, what is their combined state?

$$
\begin{pmatrix}
0 \\
1
\end{pmatrix}
\otimes 
\begin{pmatrix}
1 \\
0
\end{pmatrix} = 
\begin{pmatrix}
0 * 1 \\ 
0 * 0 \\ 
1 * 1 \\ 
1 * 0
\end{pmatrix} =
\begin{pmatrix}
0 \\ 
0 \\ 
1 \\ 
0
\end{pmatrix}
$$

> - Notice how the answer correlates with 10 because the first qubit was 1 and the second was 0.

Exercise: if a single qubit can be used to represent a coin flip, then find the state that represents
the result of flipping two coins.

> - Work out the answer on the whiteboard.
> - Give an example of a 3-qubit state to cement the idea.

Question: why do you think that column vector form isn't used in practice?

> - Answer: too many zeroes.
> - The size of the column vector grows exponentially with the number of qubits.
