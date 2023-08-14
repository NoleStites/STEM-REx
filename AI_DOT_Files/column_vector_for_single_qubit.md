## Column Vector for a Single Qubit

- Classical bits store one value: 0 or 1     
- Quantum bits need to store two values: percents of being 0 and 1
     
> - Solution: use a column vector

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

- The values in a column vector are actually probability amplitudes.

> - We use fractions instead of percents

Example: the result of performing a coin flip can be represented by the folling qubit:

$$
\text{Coin Flip} = 
\begin{pmatrix}
\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}}
\end{pmatrix}
$$

Exercise: draw the state of a qubit with a 25% chance of being measured as a 0 and a 75% chance of being
measured as a 1.

> - Work out the answer on the whiteboard.

The general form of a single qubit is

$$
\begin{pmatrix}
\alpha_0 \\
\alpha_1
\end{pmatrix}
$$

where $\alpha_0$ is the probability amplitude associated with state 0 and $\alpha_1$ is the probability amplitude associated with state 1.
