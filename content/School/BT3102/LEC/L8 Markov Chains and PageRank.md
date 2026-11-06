---
class: lecture
tags:
  - y4s1
  - bt3102
source: "[[School/BT3102/LEC/PDFs/Lecture8_2026_extend.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-10-28
updated: 2026-10-28
aliases:
  - BT3102 Lecture 8
---
Source: [[School/BT3102/LEC/PDFs/Lecture8_2026_extend.pdf|Lecture PDF]] · [[BT3102#Lecture study notes|Lecture index]]

## Markov property and transition matrix

A **stochastic process** $\{X_t\}$ is a collection of random variables indexed by time. In a Markov chain, the current state contains the information needed to predict the next state:
$$
\Pr(X_{t+1}=i\mid X_t=j,X_{t-1},\ldots,X_0)=\Pr(X_{t+1}=i\mid X_t=j).
$$
For the time-homogeneous chains here, transition probabilities do not change with $t$.

**Lecture convention: column probability vectors.** Define
$$
M_{ij}=\Pr(X_{t+1}=i\mid X_t=j),\qquad M_{ij}\ge0,\quad\sum_iM_{ij}=1.
$$
Columns are current states; rows are next states. If $p_t$ is the distribution at time $t$,
$$
p_{t+1}=Mp_t,\qquad p_t=M^tp_0.
$$
Starting at state $j$, use $p_0=e_j$; the probability of state $i$ after $t$ steps is $(M^t)_{ij}$. Do not mix this with the row-vector convention $p_{t+1}=p_tP$.

## PageRank: repair the random walk

Following each outgoing link with equal probability defines $M$. Three problems matter:

| Problem | Consequence | Repair |
| --- | --- | --- |
| **Dead end:** no outgoing links | A zero column loses probability mass; the raw matrix is not stochastic | Replace that column by the uniform distribution |
| **Spider trap:** a closed group of pages | A walk cannot leave after entering | Allow teleportation outside the group |
| **Periodicity:** returns occur only at multiples of $d>1$ | State probabilities can oscillate instead of converging | Teleportation introduces positive self-transition probabilities |

For $n$ pages, let $v=\mathbf1/n$, and let $a_j=1$ for a dead-end column, otherwise $0$. First repair dead ends, then add teleportation:
$$
\widetilde M=M+va^T,\qquad
G=\beta\widetilde M+(1-\beta)v\mathbf1^T,\quad 0<\beta<1.
$$
With probability $\beta$, follow the repaired link transition; otherwise jump uniformly to any page. Each column of $G$ sums to one and every entry is positive. Consequently the finite chain is irreducible and aperiodic, with a unique stationary distribution reached from any initial distribution. **PageRank scores are this distribution**, not the distribution after one step.

## Stationary, limiting and long-run distributions

| Quantity | Definition | Key distinction |
| --- | --- | --- |
| **Stationary distribution** $\pi$ | $M\pi=\pi$, $\pi_i\ge0$, $\sum_i\pi_i=1$ | Starting at $\pi$ keeps the distribution unchanged |
| **Limiting distribution** | $\lim_{t\to\infty}M^tp_0$, when it exists | Describes convergence of the distribution at a particular late time |
| **Long-run occupation proportions** | $\lim_{T\to\infty}T^{-1}\sum_{t=0}^{T-1}\mathbf1\{X_t=i\}$ | Describes fractions of time along a sample path |

For a **finite irreducible** chain (every state can reach every other), $\pi$ is unique and occupation proportions converge to $\pi$ almost surely. **Aperiodicity is additionally sufficient for $M^tp_0\to\pi$ from every starting distribution.**

**Essential counterexample:** a deterministic two-state alternation has $\pi=(1/2,1/2)^T$ and spends half its time in each state, but its distribution oscillates when started at a single state. Stationarity does not by itself imply convergence. Reducible chains can have multiple stationary distributions and starting-state-dependent behaviour.

## Computing and simulating

Three ways to obtain $\pi$:

- **Solve:** $(M-I)\pi=0$ together with $\sum_i\pi_i=1$.
- **Iterate:** repeatedly apply $p_{t+1}=Mp_t$, when convergence conditions hold.
- **Simulate:** run a long path and count the fraction of visits to each state, when the occupation result applies.

To simulate from current state $j$, draw $U\sim\mathrm{Uniform}(0,1)$ and select the next state using cumulative probabilities in **column $j$**. A seed makes the path reproducible; finite simulation frequencies remain estimates. The threshold construction is formalised in [[L9 Random Variable Generation and MCMC#Inverse CDF sampling|L9]].

## Hidden Markov models

In an **HMM**, the state $X_t$ follows a Markov chain but is hidden; observations $O_t$ arise through **emission probabilities** $\Pr(O_t=o\mid X_t=i)$. The lecture's example uses hidden mood and observed shopping behaviour. Transition probabilities describe changes in mood; emissions describe shopping conditional on mood. **Viterbi** finds a most probable hidden-state sequence given the observations and model; it does not observe the true states directly.

## Connections

- **[[L9 Random Variable Generation and MCMC#Markov chain Monte Carlo|L9]]:** design a chain whose stationary distribution is a distribution we want to sample.
- **[[L10 Markov Decision Processes and Value Iteration#MDP ingredients and objective|L10]]:** an MDP adds actions and rewards; a fixed stationary policy induces a Markov chain.
- **[[L7 Randomization Tests and Experimental Design#Monte Carlo randomization — HW2 extension|L7]]:** simulation there reproduces treatment assignment; here it reproduces state transitions.

For lecture examples: [[Lecture8_2026_extend.pdf#page=3|random walk/matrix, pp. 3–7]] · [[Lecture8_2026_extend.pdf#page=9|PageRank repairs, pp. 9–18]] · [[Lecture8_2026_extend.pdf#page=19|distributions/simulation, pp. 19–25]] · [[Lecture8_2026_extend.pdf#page=26|HMM, pp. 26–28]].
