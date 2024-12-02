# Day 24: Never Tell Me The Odds 

## Star 1

The path of each hailstone can be represented as a line, and we can solve for the points of intersection between each pair of lines.


## Star 2
 
We can apply some linear algebra to solve this problem. Let the unknown properties of the new rock be $(X, Y, Z, DX, DY, DZ)$, which represents its starting position and its gradient. Given the similar known properties of an arbitary rock $(x, y, z, dx, dy, dz)$, along with an additional time variable $t$, we can form the following equation:

$$
X + DX(t) = x + dx(t)\\
DX(t) - dx(t) = x - X\\
t = \frac{x-X}{DX - dx}
$$

We can similarly do the same for $Y$ and $Z$, which gives us:

$$
\frac{x-X}{DX - dx} = \frac{y-Y}{DY - dy}\\
(x-X)(DY-dy) = (y-Y)(DX - dx)\\
xDY - xdy - XDY + dyX = yDX - ydx - YDX + dxY\\
YDX - XDY = yDX + dxY - xDY - dyX + xdy - ydx 
$$


Given that the LHS remains constant across any arbitary rock, we can formulate a system of equations to solve for the unknowns by taking two rocks and setting the RHS equal to each other:

$$
yDX + dxY - xDY - dyX + xdy - ydx = y'DX + dx'Y - x'DY - dy'X + x'dy' - y'dx'\\
(dy' - dy)X + (dx - dx')Y + (y - y')DX + (x' - x)DY = x'dy' - y'dx' - xdy + ydx
$$


We first solve for $(X, Y, DX, DY)$, then use a similar technique to solve for $(X, Z, DX, DZ)$.