# Day 13: Claw Contraption

## Star 1

We can solve this by modelling it as a system of linear equations. Let $X_a$ and $Y_a$ be the number of X and Y units Button A moves the claw respectively. Let $X_b$ and $Y_b$ be the same for Button B. Then we have the system:

$$
X_aA + X_bB = X\\
Y_aA + Y_bB = Y
$$

where $A$ and $B$ are the number of times Button A and B are pressed respectively.

We can solve for $A$ and $B$ given these two equations via any technique (e.g. [Gaussian Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)). If no integer solution can be found, it means that the prize cannot be found.

Make sure to account for floating point precision issues when checking for integer answers.

Note that there is only one solution that satisfies the system of equations, so the question asking for `fewest tokens` is a bit of a red herring

## Star 2

We can simply add the required `10000000000000` to the $X$ and $Y$ values, and solve the new system of equations.