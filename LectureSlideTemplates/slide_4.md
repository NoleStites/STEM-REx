## Slide 4a: Representing the State of Multiple Qubits

> As in classical computing, it isn't very helpful to only have 1 isolated bit. Computation
> becomes more powerful if you allow the use of multiple bits. The same applies to qubits.

> Qubits can represent binary just like classical bits:

1 Qubit
- 0 -> (1 0)
- 1 -> (0 1)

2 Qubits
- Binary under the hood: (00 01 10 11)
- Probability amplitudes:
  - 00 -> (1 0 0 0)
  - 01 -> (0 1 0 0)
  - 10 -> (0 0 1 0)
  - 11 -> (0 0 0 1)

> Notice how there is a 1 at the location corresponding to each respective binary number state.
> To make a combined state, lets first look at the general form of two qubits:

- ({alpha}_0 {alpha}_1) ({beta}_0 {beta}_1)

> Now we just need to enumerate all of the combinations of the two like so in order to make
> the general form of a two qubit state:

- (
- {alpha}_0 * {beta}_0
- {alpha}_0 * {beta}_1
- {alpha}_1 * {beta}_0
- {alpha}_1 * {beta}_1
- )

> Let's try a concrete example.
> If you flipped two coins in a row, what would be the probability of getting HH, HT, TH, TT?
> 25% for all four, right? Now imagine that each coin flip was represented as the state of a
> qubit in the 50/50 state, like so:

- (1/root(2) 1/root(2)) (1/root(2) 1/root(2))

> Each qubit has a 50/50 chance to become a 0 or 1, heads or tails, so we'd expect that the
> combined state would be 25/25/25/25 for the 4 options.

> To represent the combined state of the two, we just need to multiply 1/root(2) * 1/root(2)
> a few times, following the general form above to get:

- (1/2 1/2 1/2 1/2)

> Now this may not look like the options are split in 4, but recall that these are only probability
> *amplitudes*, meaning that we still need to square them to get the actual probability.

- (1/2)^2 = 1/4 chance for all options.

> Make sense? To represent the combined state of three qubits, you'd need a column vector of
> size 8, four qubits 16, and so on.

> Allow me to point out a flaw in this way of representing a qubit. In the majority of calculations,
> you'd find that most of the entries in the vector are 0. Seems like a waste of space, no? Next,
> we'll be introducing the most popular notation for the state of a qubit that only includes the
> non-zero values of the column vector.

---
## Slide 4b: Dirac Notation

---
