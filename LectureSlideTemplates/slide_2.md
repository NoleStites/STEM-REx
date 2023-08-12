## Slide 2a: Probabilistic Classical Computing

> Quantum computing does not use a deterministic approach; it is all about about probability.
> Because of this, I am going to introduce you to the world of probabilistic computing.

*BPP (Bounded-Error Probabilisitic Polynomial-Time)*    
: the class of decision problems for which there exists a polynomial-time randomized algorithm
that accepts with probability greater than $\frac{2}{3}$ if yes, or less than $\frac{1}{3}$ if no.

> The $\frac{2}{3}$ and $\frac{1}{3}$ constants are really just placeholders. $\frac{1}{3}$, for example, can actually be
> any constant less than $\frac{1}{2}$ just as $\frac{2}{3}$ can be any constant greater than $\frac{1}{2}$.
> 
> Problems in this class are similar to deterministic algorithms, only now they have access to
> a source of randomness. Think of a Turing machine that can use a coin flipper.

> Now a question that you may be asking yourself is "why would anyone use a program that has a
> chance to be wrong?" Well, here is a solution:
>
> Suppose you are given a BPP algorithm that errs with probability $\frac{1}{3}$. We can easily modify the
> algorithm to err with probability (say) $2^{-100}$. All you have to do is rerun the algorithm a
> few hundred times, then output the majority answer!
>
> There is something called the Chernoff bound that tells us that we'll be wrong with a
> probability that decreases exponentially with the number of trials run; this works great for
> most cases.

---
## Slide 2b: BPP's Relation to other Classes

- All problems in P are in BPP

> {interact with class: "why is this?"}. Think about it:
> both solve problems in polynomial time and any problem in P can be made into a BPP problem by
> having access to a source of randomness but never using it.
> {insert P/NP/PSPACE/BPP diagram}

- The Sipser-Lautemann theorem states that if P=NP, then P=BPP

> {in response to the above...}
> But the two classes aren't, as far as we know, equal; there are still problems in BPP that
> don't have an efficient solution in P. Over time, however, problems in BPP have been
> "derandomized" into an efficient deterministic equivalent, but not all of them. It is widely
> believed that P=BPP.

---
## Slide 2c: Polynomial Identity Testing

> Here is an example of a problem that is in BPP but still not known to be in P:

Problem Statement   
: 

> TODO: Understand how best to describe the problem; it is quite difficult at present. Also,
> look into why it's important. I know it has to do with bipartite graphs, but what are their
> significance?
---
