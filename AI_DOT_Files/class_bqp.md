## Class BQP

*BQP (Bounded-Error Quantum Polynomial-Time)*     
: the class of decision problems for which there exists a polynomial-time quantum algorithm
that accepts with probability greater than $\frac{2}{3}$ if yes, or less than $\frac{1}{3}$ if no.

> - $\frac{2}{3}$ is any constant greater than $\frac{1}{2}$     
> - $\frac{1}{3}$ is any constant less than $\frac{1}{2}$

- {Add BQP to diagram}
- BPP $\subseteq$ BQP. Why?
  - Anything that can be done on a classical probabilistic computer can be done on a quantum computer.
> - This is because Coin Flip = Hadamard gate.

A problem in BQP but not in BPP: integer factorization.
- Problem statement: find an integer's prime factors.
  - Randomized time complexity $2^{O( n^{\frac{1}{3}}(\log{n})^{\frac{2}{3}} )}$
  - Can be solved in quantum polynomial time.
- Importance: multiplying two prime numbers is a key part of RSA encryption, so being able to
factor a number into two primes is the first step to decrypt a message.
