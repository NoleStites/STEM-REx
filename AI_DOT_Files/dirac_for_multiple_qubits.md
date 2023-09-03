## Dirac Notation for Multiple Qubits

Coming up with the general form:

$\hspace{8em}$ $| \psi \rangle = ( \alpha_0 | 0 \rangle + \alpha_1 | 1 \rangle ) \cdot ( \beta_0 | 0 \rangle + \beta_1 | 1 \rangle )$

[//]: # (We must combine the two qubits into one state with algebra.)
[//]: # (FOIL)

General Form:  

$\hspace{8em}$ $| \psi \rangle = \alpha_0\beta_0 | 00 \rangle + \alpha_0\beta_1 | 01 \rangle + \alpha_1\beta_0 | 10 \rangle + \alpha_1\beta_1 | 11 \rangle$

[//]: # (Compare this to the column vector for multiple qubits.)
[//]: # (First value in ket represents the state of the first qubit and the second value the second.)

Example 1: Find the combined state in Dirac notation of two qubits: the first is in state 0 and the second is
in state 1.

$\hspace{8em}$ Dirac for first qubit $\to |0\rangle$     
$\hspace{8em}$ Dirac for second qubit $\to |1\rangle$    

$\hspace{8em}$ Combined state = $|0\rangle \cdot |1\rangle = |01\rangle$

Example 2: Find the combined state in Dirac notation of two qubits: the first is in state 1 and the second is in the coin-flip state.

$\hspace{8em}$ Dirac for first qubit $\to |1\rangle$     
$\hspace{8em}$ Dirac for second qubit $\to \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$  

$\hspace{8em}$ Combined state = $|1\rangle\cdot ( \frac{1}{\sqrt{2}} |0\rangle + \frac{1}{\sqrt{2}} |1\rangle ) = \frac{1}{\sqrt{2}} |10\rangle + \frac{1}{\sqrt{2}} |11\rangle$

[//]: # (The order/placement of the ket values matters with Dirac notation)

Exercise: Find the combined state in Dirac notation of two qubits, both of which are in the coin-flip
state.

[//]: # (Work out the answer on the whiteboard.)

Question: Why do you think that this notation is prefered over column vectors?

[//]: # (Answer: because we only include non-zero probability amplitudes.)
