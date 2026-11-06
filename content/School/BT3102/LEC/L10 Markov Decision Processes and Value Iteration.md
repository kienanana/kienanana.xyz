---
class: lecture
tags:
  - y4s1
  - bt3102
source: "[[School/BT3102/LEC/PDFs/Lecture10_2026_extended.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-10-28
updated: 2026-10-28
aliases:
  - BT3102 Lecture 10
---
Source: [[School/BT3102/LEC/PDFs/Lecture10_2026_extended.pdf|Lecture PDF]] · [[BT3102#Lecture study notes|Lecture index]]

## MDP ingredients and objective

A **Markov decision process (MDP)** models sequential choices under uncertainty:

| Ingredient | Meaning |
| --- | --- |
| State $s\in\mathcal S$ | Fully observed information needed for the next decision |
| Action $a\in\mathcal A(s)$ | Choice available in state $s$ |
| Transition $P(s'\mid s,a)$ | Probability of next state $s'$ after taking $a$ in $s$ |
| Reward $R(s,a)$ | Immediate reward for the state/action |
| Discount $\rho$ | Weight on future rewards; here $0<\rho<1$ for the infinite-horizon result |

The Markov property now conditions on **current state and action**. For every $(s,a)$, probabilities over next states sum to one. An action chooses a transition distribution, not necessarily the next state: the gridworld's intended move can fail or slip. If multiple outcomes lead to the same cell, add their probabilities.

Starting from $S_0=s$, a policy's value is
$$
U^\pi(s)=\mathbb E_\pi\!\left[\sum_{t=0}^{\infty}\rho^tR(S_t,A_t)\mid S_0=s\right],
\qquad U^*(s)=\max_\pi U^\pi(s).
$$
Optimise **expected total discounted reward**, not just immediate reward or one simulated path. With finite horizon, $\rho=1$ can be allowed because the sum has finitely many terms; infinite-horizon undiscounted problems need additional conditions.

## Policies and evaluation

A **deterministic stationary policy** assigns one fixed action to each state: $\pi(s)\in\mathcal A(s)$. “Stationary” means independent of time, not that the system stays still. General policies may depend on history, time or randomisation.

For a finite state/action infinite-horizon MDP with bounded rewards and $0<\rho<1$, there exists a deterministic stationary policy optimal from **every starting state**. The optimal value still depends on the starting state. A finite-horizon optimum may depend on time remaining.

A fixed stationary policy induces a Markov chain with transitions $P^\pi(s'\mid s)=P(s'\mid s,\pi(s))$. Its value satisfies the **policy evaluation** equations:
$$
U^\pi(s)=R(s,\pi(s))+\rho\sum_{s'}P(s'\mid s,\pi(s))U^\pi(s').
$$
These equations are linear in $U^\pi$ for a fixed policy. Simulation provides another evaluation method: average the discounted returns of many trajectories from the same initial state. A time cutoff approximates an infinite horizon, and finite replications introduce Monte Carlo error.

With $m$ actions at each of $n$ decision states, there are $m^n$ deterministic stationary policies. More generally the count is $\prod_s|\mathcal A(s)|$. The lecture's $4^9=262{,}144$ illustrates why exhaustive policy simulation is expensive.

## Bellman optimality equation

Split the optimal return into immediate reward and optimal continuation:
$$
U^*(s)=\max_{a\in\mathcal A(s)}\left\{R(s,a)+\rho\sum_{s'}P(s'\mid s,a)U^*(s')\right\}.
$$
For the gridworld's state-only reward, $R(s,a)=R(s)$, so
$$
U^*(s)=R(s)+\rho\max_a\sum_{s'}P(s'\mid s,a)U^*(s').
$$
The **sum averages over random next states; the maximum chooses an action**. You cannot select a different current action after seeing which random next state occurs. One equation per state gives a coupled system; the maximisation makes it generally nonlinear.

An optimal policy is greedy with respect to the optimal values:
$$
\pi^*(s)\in\arg\max_a\left\{R(s,a)+\rho\sum_{s'}P(s'\mid s,a)U^*(s')\right\}.
$$
Ties permit multiple optimal actions. The same optimal continuation from a state can be used regardless of the route taken to reach it: this is the dynamic-programming principle.

## Value iteration

1. Initialise $U_0(s)$ arbitrarily for nonterminal states and set terminal boundary values consistently with the reward convention.
2. Update every nonterminal state using the preceding iteration:
$$
U_{k+1}(s)=\max_a\left\{R(s,a)+\rho\sum_{s'}P(s'\mid s,a)U_k(s')\right\}.
$$
3. Compute $\delta_k=\max_s|U_{k+1}(s)-U_k(s)|$ and repeat until $\delta_k\le\epsilon$, then extract a greedy policy using the same action comparison.

For the finite discounted setting, the Bellman operator is a contraction:
$$
\|TU-TV\|_\infty\le\rho\|U-V\|_\infty.
$$
Thus value iteration converges to the unique $U^*$ from any initial values. This guarantee uses $\rho<1$; it does not automatically extend to arbitrary undiscounted infinite-horizon models. **The lecture's numerical gridworld on p. 16 uses $\rho=1$**, terminal values $+1,-1$ and step reward $-0.01$; treat it as the terminating example, separately from the discounted contraction theorem.

**One backup:** if an action has next-state probabilities $(0.8,0.1,0.1)$, current successor values $(5,2,0)$, immediate reward $-0.04$ and $\rho=0.9$, its candidate value is
$$
-0.04+0.9(0.8\cdot5+0.1\cdot2+0.1\cdot0)=3.74.
$$
Calculate this for each available action and keep the largest. Use $U_k$ throughout a synchronous sweep; changing values mid-sweep is a different update schedule.

## Terminal rewards and parameter changes

**Terminal accounting:** reward must be counted once. If terminal payoff is stored as a fixed boundary value $U(s_T)=r_T$, stop updating that state. If instead the payoff is awarded on the transition into a terminal state, use zero continuation after termination. Do not both pay on entry and repeatedly collect the same reward in an absorbing state.

- **Discount:** smaller $\rho$ places less weight on distant rewards; larger $\rho$ values future outcomes more and weakens the contraction, potentially slowing convergence.
- **Step reward:** a larger per-step penalty encourages shorter routes; a smaller penalty can make safer detours worthwhile.
- **Transition risk:** a policy must trade off route length and the probability of a bad terminal outcome; the visually shortest route need not maximise expected return.

## Connections

- **[[L8 Markov Chains and PageRank#Markov property and transition matrix|L8]]:** actions control transitions; fixing a stationary policy leaves a Markov chain. Here $P(s'\mid s,a)$ states direction explicitly, avoiding matrix-orientation ambiguity.
- **[[L9 Random Variable Generation and MCMC#Inverse CDF sampling|L9]]:** simulate a policy by drawing each next state from $P(\cdot\mid s,\pi(s))$.
- **[[L2 Optimisation and Gradient Descent|L2]]:** both seek an optimum, but Bellman recursion exploits sequential state structure rather than differentiating a parameterised loss.

For lecture examples: [[Lecture10_2026_extended.pdf#page=1|state/actions/transitions/rewards, pp. 1–6]] · [[Lecture10_2026_extended.pdf#page=7|policies and exhaustive simulation, pp. 7–12]] · [[Lecture10_2026_extended.pdf#page=13|Bellman/value iteration, pp. 13–17]] · [[Lecture10_2026_extended.pdf#page=18|parameter changes, pp. 18–19]].
