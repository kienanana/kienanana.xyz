# BT3102 L1–7 MCQ practice

35 single-answer questions. Closed-book practice; no calculator required. Based on the local L1–7 lecture notes. These are practice questions, not predictions of the actual quiz.

## Question 1 · L1

At a point where the gradient is nonzero, which unit direction gives the steepest decrease in the Euclidean norm?

A. The normalised gradient
B. The negative normalised gradient
C. Any direction perpendicular to the gradient
D. The direction with the largest coordinate

## Question 2 · L1

A differentiable function has gradient (2, −1). Which direction is a descent direction?

A. (1, 0)
B. (0, −1)
C. (−1, 0)
D. (1, 1)

## Question 3 · L1

Which statement about a convex function on a convex domain is always true?

A. Every local minimum is global
B. It has exactly one minimiser
C. Every stationary point is a strict minimum
D. Its gradient is constant

## Question 4 · L1

For which class of functions is the second-order Taylor expression exact everywhere?

A. All differentiable functions
B. All convex functions
C. All exponential functions
D. Quadratic functions

## Question 5 · L1

Two matrices related by P⁻¹AP, with P invertible, represent:

A. Necessarily different linear transformations
B. The same linear transformation in different bases
C. The same coordinates in the same basis
D. Only transformations with positive eigenvalues

## Question 6 · L2

For a differentiable unconstrained function, a zero gradient guarantees:

A. A global minimum
B. A local minimum
C. A stationary point
D. A positive definite Hessian

## Question 7 · L2

A stationary point has an indefinite Hessian. It is:

A. A saddle point
B. A strict local minimum
C. A strict local maximum
D. Necessarily a global minimum

## Question 8 · L2

If the design matrix X in ordinary least squares lacks full column rank, which statement is correct?

A. The objective becomes nonconvex
B. No minimiser exists
C. The inverse formula always remains valid
D. The objective is convex, but minimisers need not be unique

## Question 9 · L2

Why can maximum likelihood logistic regression be expressed as minimising negative log-likelihood?

A. Logarithms turn any nonconvex function into a convex one
B. Log is strictly increasing, and negation reverses maximisation into minimisation
C. Taking logs removes the need for independent observations
D. The log-likelihood equals squared error

## Question 10 · L2

For gradient descent at a nonstationary point, which claim is correct?

A. Every positive step size decreases the objective
B. The gradient must have positive coordinates
C. The negative gradient is descent, but an excessively large step can increase the objective
D. A fixed step size ensures convergence for every smooth function

## Question 11 · L3

An interior exact line-search minimum along direction p satisfies:

A. The new gradient is perpendicular to p
B. The new gradient is necessarily zero
C. The next step size is zero
D. The entire objective is globally minimised

## Question 12 · L3

Armijo backtracking fails at the current trial step. What does the algorithm do?

A. Reverse the search direction
B. Increase the step size
C. Accept any objective decrease
D. Multiply the step size by a factor between zero and one

## Question 13 · L3

What does the ordinary Wolfe curvature condition add to Armijo sufficient decrease?

A. It guarantees a global minimum
B. It rules out excessively short steps by requiring the directional slope to flatten sufficiently
C. It requires exact line minimisation
D. It eliminates all Hessian computation

## Question 14 · L3

What distinguishes Nesterov acceleration from the basic momentum formulation in the lectures?

A. It never uses past updates
B. It always uses exact line search
C. It evaluates the gradient at a look-ahead point
D. It computes the exact Hessian

## Question 15 · L3

What does “global convergence” of an optimisation method usually mean in this context?

A. Convergence towards stationarity from general starting points under assumptions
B. Guaranteed convergence to the global minimum of every nonconvex function
C. One-step convergence
D. Convergence without any assumptions

## Question 16 · L4

One example is freshly sampled uniformly from the full dataset for an SGD update. Conditional on the current history, its gradient is:

A. Always identical to the full gradient
B. Always a descent direction for the full objective
C. Zero with probability one
D. An unbiased estimate of the full gradient

## Question 17 · L4

Increasing mini-batch size generally:

A. Reduces both per-update cost and sampling noise
B. Reduces sampling noise but increases per-update cost
C. Guarantees every update decreases the full loss
D. Makes the Hessian unnecessary for Newton’s method

## Question 18 · L4

Why is a single tiny mini-batch gradient an unreliable stopping criterion?

A. Mini-batch gradients cannot be computed
B. It proves the full gradient is large
C. Sampling noise may give a tiny estimate even when the full gradient is not tiny
D. It always means the learning rate is zero

## Question 19 · L4

At a point with nonzero gradient and positive definite Hessian, the Newton direction:

A. Is a descent direction, although its full step may increase the true objective
B. Always reaches a global minimum in one step
C. Is perpendicular to the gradient
D. Is undefined

## Question 20 · L4

For minimising a scalar function f, Newton’s update uses which ratio?

A. f divided by f′
B. f′′ divided by f′
C. f divided by f′′
D. f′ divided by f′′

## Question 21 · L5

A positive definite quadratic Hessian has very unequal eigenvalues. Its contours are typically:

A. Circular, making steepest descent fastest
B. Elongated, potentially causing slow zigzagging
C. Nonconvex
D. Flat in every direction

## Question 22 · L5

Why can an invertible change of coordinates improve gradient descent?

A. It changes the objective’s minimum value
B. It removes every stationary point
C. It changes conditioning and the update trajectory
D. It makes every function quadratic

## Question 23 · L5

If H approximates the inverse Hessian, which secant equation is correct? Let s be the step and y the gradient change.

A. H_new y = s
B. H_new s = y
C. H_new y = −s
D. H_new s = −y

## Question 24 · L5

Which condition preserves positive definiteness in a BFGS update starting from a positive definite H?

A. sᵀy = 0
B. sᵀy < 0
C. Only a smaller final loss
D. sᵀy > 0

## Question 25 · L5

How does L-BFGS reduce storage compared with full BFGS?

A. It stores the exact Hessian at every iteration
B. It stores a limited number of recent step/gradient-change pairs
C. It uses every previous gradient forever
D. It stores only the objective value

## Question 26 · L6

What is the fundamental problem of causal inference?

A. Treatment cannot be randomised
B. Average effects cannot be defined
C. Only one potential outcome is observed for each unit at the specified time
D. Every correlation is causal

## Question 27 · L6

A unit has Y(1) = 8 and Y(0) = 5, but receives control. Its causal effect is:

A. 3
B. 5
C. 8
D. Undefined because treatment was not received

## Question 28 · L6

A treated student shares intervention materials with an untreated classmate, affecting the classmate’s outcome. This threatens:

A. Random sampling only
B. The definition of a gradient
C. No hidden versions only
D. The no-interference part of SUTVA

## Question 29 · L6

Under complete random assignment with fixed nonempty group sizes, the observed difference in means is unbiased. This means:

A. Every realised estimate equals the true average effect
B. Its expectation over assignments equals the experimental units’ average causal effect
C. Every assignment perfectly balances all covariates
D. Individual causal effects become observable

## Question 30 · L6

Why can a before/after outcome increase fail to establish a treatment effect?

A. The same person can never be measured twice
B. An increase always implies negative treatment effects
C. Time trends or other changes may explain the increase
D. Causal effects must be identical across people

## Question 31 · L7

Why is Fisher’s no-effect null called “sharp”?

A. It specifies each unit’s effect and allows all missing potential outcomes to be imputed
B. It only specifies that the average effect is zero
C. It guarantees a small p-value
D. It requires all observed outcomes to be equal

## Question 32 · L7

A randomisation-test p-value is:

A. The probability that the null is true
B. The probability that treatment was assigned randomly
C. The probability of a measurement mistake
D. The probability of an equally or more extreme statistic under the null and assignment design

## Question 33 · L7

Four units form two matched pairs, with exactly one treated unit in each pair. How many assignments are allowed?

A. 2
B. 4
C. 6
D. 16

## Question 34 · L7

An experiment uses paired random assignment. Its randomisation test should:

A. Use all assignments with any number treated
B. Ignore the pairing and use every fixed-size subset
C. Reproduce the allowed within-pair assignments
D. Permute observed outcomes only within the treated group

## Question 35 · L7

Random assignment among volunteers primarily supports which conclusion?

A. Causal inference for the experimental units; wider generalisation requires more justification
B. The volunteers represent the entire population
C. The treatment effect is identical for everyone
D. The null hypothesis must be false
