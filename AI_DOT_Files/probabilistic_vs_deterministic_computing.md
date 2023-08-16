## Probabilistic Computing vs Deterministic Computing

### Deterministic Classical Computing
*Deterministic*     
: given an input to a function/program/algorithm, you can be certain of the output

> - The types of algorithms that they have been making (for the most part) in CS

*Classical*    
: refers to an object being governed by Newtonian physics

> Quantum computing uses a probabilistic approach, not deterministic.

### Probabilistic Classical Computing

- Similar to deterministic algorithms, only now we have access to a source of perfect randomness
  - Think of a Turing machine with a built-in coin flipper

<ins>Questions</ins>:      
Why would anyone use a program that has a chance to be wrong? Why does probabilistic computing work?

<ins>Example</ins>:    
Imagine you have a probabilistic algorithm that, when run, has a $\frac{1}{3}$ chance to provide the wrong
solution. Running it once will only make you right $\frac{2}{3}$ of the time. What could you do to better
your odds of getting the correct result?

<ins>Answer</ins>:   
Run the algorithm a few hundred times and take the majority answer!

> - The chance of being wrong is incredibly small at this point.

*Chernoff Bound*
: you will be wrong with a probability that decreases exponentially with the number of trials run.
