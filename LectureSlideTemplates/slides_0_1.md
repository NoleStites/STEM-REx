## Slide 0: Intro to Quantum Computing   

Presented by Nole Stites

---
## Slide 1a: Deterministic Classical Computing 

> Because we'll be discussing them a lot, and they are important when trying to understand
> complexity theory, I am going to define a couple of important words real quick:  

*Deterministic*     
: given an input to a function/program/algorithm, you can be certain of the output

*Classical*    
: refers to an object being governed by Newtonian physics

---
## Slide 1b: P and NP Review

> The complexity of an algorithm is commonly based on the input size and
> is most often defined by its efficiency.

*P (Polynomial)*     
: the class of problems solvable by a Turing machine in polynomial time     

ex: Searching for an item in a linked list

*NP (Non-Deterministic Polynomial)*    
: the class of decision problems for which, if the answer is yes, then there is a polynomial-size
proof of the fact that you can check in polynomial time     

ex: Given an assignment of variables for a SAT problem, you can easily verify the solution

> This diagram shows the relationship between P and NP {insert P/NP diagram}. The relationship
> between the two is not strict because it is possible that P=NP

---
## Slide 1c: Complexity Class: PSPACE

> The complexity of an algorithm isn't always defined by its efficiency, however. Sometimes it is
> important to measure an algorithm based on how much memory they take up.

*PSPACE (Polynomial-Space)*    
: the class of problems solvable in polynomial space, but unlimited time

> Most of the time, the space used by a program cannot be exponentially more than the running
> time. Let's imagine that it takes 1 unit of time to access a spot in memory. Then, for example,
> a O(n^2) algorithm wouldn't be able to access much more than O(n^2) spots in memory.
>
> Because of this, anything that runs in polynomial time will have to belong to the PSPACE class.
> {insert P/NP/PSPACE diagram}

---

