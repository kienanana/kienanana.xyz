---
tags:
  - y4s1
  - matlab
class: note
source: A Quick Tutorial on MATLAB (Gowtham Bellala) — BT3102 TUT1
related:
  - "[[BT3102]]"
author: Gowtham Bellala
date: 2026-08-26
updated: 2026-08-26
aliases:
  - MATLAB Cheatsheet
---
MATLAB = **MAT**rix **LAB**oratory. Originally built for linear algebra with matrices, now covers data analysis, signal processing, optimisation, and 2-D/3-D graphics.

## Variables
- Variable names are **case sensitive**
- Up to 63 characters (MATLAB 6.5+)
- Must **start with a letter**, then letters / digits / underscores

```matlab
>> x = 2;
>> abc_123 = 0.005;
>> 1ab = 2;          % Error: Unexpected MATLAB expression
```

### Special variables

| Name | Meaning |
| --- | --- |
| `pi` | value of π |
| `eps` | smallest incremental number |
| `inf` | infinity |
| `NaN` | not a number (e.g. `0/0`) |
| `i`, `j` | square root of −1 |
| `realmin` | smallest usable positive real |
| `realmax` | largest usable positive real |

## Operators
### Relational

| Operator | Meaning                               |
| -------- | ------------------------------------- |
| `<`      | less than                             |
| `<=`     | less than or equal                    |
| `>`      | greater than                          |
| `>=`     | greater than or equal                 |
| `==`     | equal to                              |
| `~=`     | not equal to (**not** `!=` like in C) |

### Logical

| Operator | Meaning | Precedence                 |
| -------- | ------- | -------------------------- |
| `~`      | not     | highest                    |
| `&`      | and     | equal precedence with `\|` |
| `\|`     | or      | equal precedence with `&`  |

## Matrices
MATLAB treats **all variables as matrices**:
- **Vectors** — only one row OR one column
- **Scalars** — one row AND one column
Indices start from **1** (unlike C). `A(2,4)` is row 2, column 4; `A(17)` is linear (column-wise) indexing.

### Generating matrices

```matlab
>> x = 23;                  % scalar

>> y = [12,10,-3]           % row vector (commas)
y =
    12   10   -3

>> z = [12;10;-3]           % column vector (semicolons)
z =
    12
    10
    -3

>> X = [1,2,3;4,5,6;7,8,9]  % matrix: commas = columns, semicolons = rows
X =
     1    2    3
     4    5    6
     7    8    9
```

Row vectors and column vectors are treated **very differently**. Matrices must be **rectangular**.

### Extracting a sub-matrix

```matlab
sub_matrix = matrix(r1:r2, c1:c2);
```

where `r1`/`r2` are the beginning/ending rows and `c1`/`c2` the beginning/ending columns.

```matlab
>> X = [1,2,3;4,5,6;7,8,9];

>> X22 = X(1:2, 2:3)
X22 =
     2    3
     5    6

>> X13 = X(3, 1:3)
X13 =
     7    8    9

>> X21 = X(1:2, 1)
X21 =
     1
     4
```

### Extension, tiling, concatenation

```matlab
% assigning out of bounds auto-extends (pads with zeros)
>> a = [1,2i,0.56];
>> a(2,4) = 0.1
a =
     1   0+2i   0.56    0
     0    0      0     0.1

% repmat - replicates and tiles a matrix
>> b = [1,2;3,4];
>> b_rep = repmat(b,1,2)
b_rep =
     1   2   1   2
     3   4   3   4

% concatenation (result must still be rectangular)
>> a = [1,2;3,4];
>> a_cat = [a,2*a; 3*a,2*a]
a_cat =
     1    2    2    4
     3    4    6    8
     3    6    2    4
     9   12    6    8
```

### Arithmetic

```matlab
>> x = [1,2;3,4];

% scalar addition increments every element
>> y = x + 5
y =
     6   7
     8   9

% matrix addition - dimensions must agree
>> xsy = x + y
xsy =
      7    9
     11   13

>> x + [1,0.3]
??? Error using => plus
Matrix dimensions must agree
```

```matlab
% matrix multiplication - inner dimensions must agree
>> a = [1,2;3,4];   % (2x2)
>> b = [1,1];       % (1x2)
>> c = b*a
c =
     4   6

>> c = a*b
??? Error using ==> mtimes
Inner matrix dimensions must agree.
```

Element-wise operations use a **dot prefix**:

```matlab
>> a = [1,2;1,3];
>> b = [2,2;2,1];

>> a./b        % element-wise division
     0.5   1
     0.5   3

>> a.*b        % element-wise multiplication
     2    4
     2    3

>> a.^2        % element-wise power
     1   4
     1   9

>> a.^b
     1   4
     1   3
```

### Matrix manipulation functions

| Function | Purpose |
| --- | --- |
| `zeros` | array of all zeros — `x = zeros(3,2)` |
| `ones` | array of all ones — `x = ones(2)` |
| `eye` | identity matrix — `x = eye(3)` |
| `rand` | uniform random numbers in [0,1] |
| `diag` | diagonal matrices / diagonal of a matrix |
| `size` | array dimensions |
| `length` | length of a vector (row or column) |
| `det` | matrix determinant |
| `inv` | matrix inverse |
| `eig` | eigenvalues and eigenvectors |
| `rank` | rank of a matrix |
| `find` | searches for given values in an array/matrix |

## Built-in math functions

**Elementary:**

| Function | Purpose |
| --- | --- |
| `abs` | absolute value of all elements |
| `sign` | signum function |
| `sin`, `cos`, … | trigonometric functions |
| `asin`, `acos`, … | inverse trigonometric functions |
| `exp` | exponential |
| `log`, `log10` | natural log, log base 10 |
| `ceil`, `floor` | round towards +inf / −inf |
| `round` | round to nearest integer |
| `real`, `imag` | real and imaginary parts of a complex matrix |
| `sort` | sort elements in ascending order |

**Aggregation:**

| Function | Purpose |
| --- | --- |
| `sum`, `prod` | summation and product of elements |
| `max`, `min` | maximum and minimum of arrays |
| `mean`, `median` | average and median |
| `std`, `var` | standard deviation and variance |

## Graphics

### 2-D plotting

Plot `sin(x)` and `cos(x)` over `[0,2π]` on the same axes, in different colours.

```matlab
% Method 1 - hold on / hold off
>> x = linspace(0,2*pi,1000);
>> y = sin(x);
>> z = cos(x);
>> hold on;
>> plot(x,y,'b');
>> plot(x,z,'g');
>> xlabel 'X values';
>> ylabel 'Y values';
>> title 'Sample Plot';
>> legend('Y data','Z data');
>> hold off;
```

```matlab
% Method 2 - multiple series in one plot call
>> x = 0:0.01:2*pi;
>> y = sin(x);
>> z = cos(x);
>> figure
>> plot(x,y,x,z);
>> xlabel 'X values';
>> ylabel 'Y values';
>> title 'Sample Plot';
>> legend('Y data','Z data');
>> grid on;
```

### Piecewise functions

For `y = t` on `0 ≤ t ≤ 1` and `y = 1/t` on `1 < t ≤ 6`:

```matlab
% Method 1 - build each piece separately and concatenate
>> t1 = linspace(0,1,1000);
>> t2 = linspace(1,6,1000);
>> y1 = t1;
>> y2 = 1./t2;
>> t = [t1,t2];
>> y = [y1,y2];
>> figure
>> plot(t,y);
>> xlabel 't values', ylabel 'y values';
```

```matlab
% Method 2 - logical indexing
>> t = linspace(0,6,1000);
>> y = zeros(1,1000);
>> y(t()<=1) = t(t()<=1);
>> y(t()>1)  = 1./t(t()>1);
>> figure
>> plot(t,y);
>> xlabel 't values';
>> ylabel 'y values';
```

### Subplots

```matlab
subplot(rows, columns, index)

>> subplot(4,1,1)
>> ...
>> subplot(4,1,2)
>> ...
>> subplot(4,1,3)
>> ...
>> subplot(4,1,4)
```

## Importing / exporting data

### `load` and `save`

```matlab
load filename        % loads all variables from "filename"
load filename x      % loads only the variable x
load filename a*     % loads all variables starting with 'a'

save filename        % saves all workspace variables to filename.mat (binary)
save filename x,y    % saves only x and y

% help load / help save for more
```

### Excel

```matlab
>> x = xlsread(filename);

% if the file contains numeric values, text and raw data values
>> [numeric,txt,raw] = xlsread(filename);

% write A into the region A2:C4 of data.xls
>> x = xlswrite('c:\matlab\work\data.xls', A, 'A2:C4');
% x = 1 on success, 0 on failure
```

### Text files

```matlab
% writing
>> fid = fopen('filename.txt','w');
>> count = fwrite(fid,x);     % count = number of values stored
>> fclose(fid);               % don't forget to close

% reading
>> fid = fopen('filename.txt','r');
>> X = fscanf(fid,'%5d');
>> fclose(fid);
```

Other useful commands: `fread`, `fprintf`.

## Flow control

Five flow control statements: `if`, `switch`, `for`, `while`, `break`.

### `if`

```matlab
if expression
    ...
elseif expression
    ...
else
    ...
end
```

```matlab
% Example 1
>> if i == j
>>     a(i,j) = 2;
>> elseif i >= j
>>     a(i,j) = 1;
>> else
>>     a(i,j) = 0;
>> end

% Example 2
>> if (attn>0.9) & (grade>60)
>>     pass = 1;
>> end
```

### `switch`

```matlab
switch switch_expr
    case case_expr1
        ...
    case case_expr2
        ...
    otherwise
        ...
end
```

```matlab
>> x = 2, y = 3;
>> switch x
>>   case x==y
>>     disp('x and y are equal');
>>   case x>y
>>     disp('x is greater than y');
>>   otherwise
>>     disp('x is less than y');
>> end
x is less than y
```

> Unlike C, MATLAB does **not** need `break` in each case.

### `for`

```matlab
for variable = expression
    ...
end
```

```matlab
% Example 1
>> for x = 0:0.05:1
>>     printf('%d\n',x);
>> end

% Example 2 - nested
>> a = zeros(n,m);
>> for i = 1:n
>>   for j = 1:m
>>     a(i,j) = 1/(i+j);
>>   end
>> end
```

### `while`

```matlab
while expression
    ...
end
```

```matlab
% Example 1
>> n = 1;
>> y = zeros(1,10);
>> while n <= 10
>>     y(n) = 2*n/(n+1);
>>     n = n+1;
>> end

% Example 2
>> x = 1;
>> while x
>>     % execute statements
>> end
```

> In MATLAB `1` is synonymous with TRUE and `0` with FALSE.

### `break`

Terminates execution of `for` and `while` loops. In nested loops it terminates the **innermost loop only**.

```matlab
>> y = 3;
>> for x = 1:10
>>     printf('%5d',x);
>>     if (x>y)
>>         break;
>>     end
>> end
1     2     3     4
```

## Efficient programming

- Avoid nested loops as far as possible — in most cases they can be replaced with matrix manipulation
- **Preallocate** arrays when possible
- Use MATLAB's huge library of built-in functions; they are more likely to be efficient than your own

### Example 1 — non-causal FIR filter

Given input `x` and filter coefficients `h` as column vectors, compute `y[n] = Σ(k=0..19) h[k]·x[n+k]` for `n = 1,2,3`.

```matlab
% Method 1 - two loops
>> y = zeros(1,3);
>> for n = 1:3
>>   for k = 0:19
>>     y(n) = y(n) + h(k)*x(n+k);
>>   end
>> end

% Method 2 - avoids the inner loop (inner product)
>> y = zeros(1,3);
>> for n = 1:3
>>     y(n) = h'*x(n:(n+19));
>> end

% Method 3 - avoids both loops (matrix multiply)
>> X = [x(1:20), x(2:21), x(3:22)];
>> y = h'*X;
```

### Example 2 — cumulative products of cubes

Compute `y(n) = 1³ · (1³+2³) · (1³+2³+3³) · … · (1³+2³+…+n³)` for `n = 1..20`.

```matlab
% Method 1 - two loops
>> y = zeros(20,1);
>> y(1) = 1;
>> for n = 2:20
>>   for m = 1:n
>>     temp = temp + m^3;
>>   end
>>   y(n) = y(n-1)*temp;
>>   temp = 0;
>> end

% Method 2 - avoids the inner loop
>> y = zeros(20,1);
>> y(1) = 1;
>> for n = 2:20
>>     temp = 1:n;
>>     y(n) = y(n-1)*sum(temp.^3);
>> end

% Method 3 - avoids both loops
>> X = tril(ones(20)*diag(1:20));
>> x = sum(X.^3,2);
>> Y = tril(ones(20)*diag(x)) + triu(ones(20)) - eye(20);
>> y = prod(Y,2);
```

## Getting help

At the MATLAB prompt: `help`, `lookfor`, `helpwin`, `helpdesk`, `demos`

On the web:
- http://www.mathworks.com/support
- http://www.mathworks.com/products/demos/#
