## Slide 3a: Probability in Quantum Computing

- Quantum computing is probabilistic, not deterministic

> Because quantum computing is probabilistic and not deterministic, it has both the potential power
> of randomness and the curious quirks of quantum computing, which we will be discussing later.

- Instead of classical bits, quantum computing uses quantum bits (also known as qubits)

> It is important to note the difference between the role of probability in BPP problems
> and quantum computation. In BPP problems, you only use randomness alongside classical bits to
> *help* with computation, whereas quantum computing merges probability the classical bit, making
> a whole new type of computer all together.

---
## Slide 3b: Classical Bit vs. Quantum Bit (Qubit)

- A classical bit is deterministic
- {Insert a classic NOT gate here}

> If I input a 0 into this circuit, what will the state of the output be? (Class: "1")
> Right! When we look at the output bit, which we will call "measuring", we know what state the
> bit will be in. A classical bit can be thought of representing this output state; that is,
> either 0 or 1.

- A qubit is probabilistic
- {Insert a "coin flip" gate here}

> Imagine that this gate simulates a perfectly fair coin flip.
> 
> Now I will ask you the same question: if I input a 0 into this circuit, what will the state of
> the output be when I measure it? (await some answers)
> 
> We don't know! There is a 50/50% chance that the output will be measured as either a 0 or a 1.
> A qubit represents this output state: not necessarily a 0 or a 1, but rather a percent chance
> of both.
>
> It is important to keep in mind, however, that when a qubit is measured, it will still be either
> 0 or 1, there is just a 50%/50% chance of either.

---
## Slide 3c: Representing the State of a Qubit

- Classical bit: 0 or 1

> So as a recap, a classical bit only needs space to store one value: 0 or 1.

- Qubit: 25%/75%, 50%/50%, 20%/80%, ...

> While a qubit still, in the end, represents either 0 or 1, we need enough space to store
> *two* values: the percentages for each.
>
> So what kind of mathematical data structure can be used to store these two values? We prefer to
> use a column vector. For those of you that don't know what that is, no worries! It is quite
> simple.

- (25% 75%)   (50% 50%)   (20% 80%) <- formatted as column vectors

> These are a few example column vectors for the state of a qubit. The percentage on the top
> represents the chance that a qubit will be zero when measured, and the bottom percentage is the
> chance it will be a 1. This means that:

- 0 = (100% 0%)  1 = (0% 100%)

- Normalization Constraint: (percentage to be 0) + (percentage to be 1) = 100%

> The chances of each event occurring, when added together, should equal 100%.
> I know that this is, perhaps, a bit obvious, but it is important nonetheless.

---
## Slide 3d: Qubits Continued

> I am going to more formally define the state of a qubit now that you all know the general
> concept behind it.

- Born's Rule: the probability of any given state = |probability amplitude|^2

> Immediately you might be wondering "what is a probability amplitude". I will tell you now
> that the values inside of a column vector are probability *amplitudes*, and to calculate the
> actual probability, you must use Born's rule. Let's see an example.

- (1 0)

> We will be using fractions between 0 and 1 to represent our probability amplitudes.

- Using Born's rule, what is the probability that this qubit, when measured, will be in
- state 0? State 1?

> If the top value corresponds to the 0 state, then we can use Born's rule as such:

- |1|^2 = 1 = 100% chance of being in state 0
- |0|^2 = 0 = 0% chance of being in state 1

> Now what do you think the 50/50 state would look like?
> We know by Born's rule that 1/2 = |prob. amplitude|^2
> We can take the square root of both sides to get the probability amplitude 1/root(2)
> So this should be the 50/50 state:

- (1/root(2) 1/root(2))

> Checking our work, if we square 1/root(2), we get 1/2, which is 50%. 

---
## Slide 3e: Generalizing the Qubit

- A qubit can be written as a column vector ({alpha}_0 {alpha}_1)
  - {alpha}_0 = probability amplitude associated with state 0
  - {alpha}_1 = probability amplitude associated with state 1

> This is the general form of a qubit using a column vector. We simply have variables in
> place of the fractions used in the previous slide.

- Normalization Constraint: P = 1 = |{alpha}_0|^2 + |{alpha}_1|^2

> This has the same intuition and standard probability, only now we are applying that same
> logic to probability amplitudes. You calculate the probability of a single event occuring,
> such as being in state 0, and you can combine all of those probabilities to get 100% for
> *something* to happen.

---
