## CNOT Gate

- Like the X gate only now another bit controls whether the other gets reversed
- 2-qubit gate

The CNOT gate mappings:

$$
|00\rangle \to |00\rangle \hspace{5em}
|01\rangle \to |01\rangle \hspace{5em}
|10\rangle \to |11\rangle \hspace{5em}
|11\rangle \to |10\rangle \hspace{5em}
$$

- If the first bit (control bit) is 1, then apply the X gate to the second bit
- The probability amplitudes remain unaffected

Example: Apply the CNOT gate to the qubits in the following state: 
$\frac{1}{\sqrt{3}}|01\rangle + \sqrt{\frac{2}{3}}|11\rangle$

$$
CNOT(\frac{1}{\sqrt{3}}|01\rangle + \sqrt{\frac{2}{3}}|11\rangle) = 
\frac{1}{\sqrt{3}}|01\rangle + \sqrt{\frac{2}{3}}|10\rangle
$$

Exercise: Apply the CNOT gate to two qubits, one of which was in state 0 and is in the coin flip state and the
other is in state 0.

> - Work out the answer on the whiteboard.
