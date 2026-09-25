---
class: guide
tags:
  - math/latex
source:
related:
author:
date: 2026-09-11
updated: 2026-09-11 17:02:54
aliases:
---
LaTeX is a markup-based typesetting system where you write plain text with formatting commands, and a TeX engine compiles it into a polished PDF.

I use LaTeX in many of my classes to take down formulae in my notes, and I have recently been trying to improve my efficiency in writing in LaTeX so as to be a better note-taker for my Math-heavy content. 

### Useful Triggers:

Based on my current LaTeX Suite snippets. Most triggers below expand automatically **inside math mode**. Triggers are case-sensitive. In the examples, `□` marks a field to fill in; it is not literal output. Use `Tab` to move through snippet fields. Entries marked **manual** require snippet expansion rather than expanding automatically.

#### Math mode and text

| Trigger       | Result / use                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------- |
| `mk`          | Inline math: `${}□{}$` in normal text; `\(□\)` in a text environment inside math                  |
| `dm`          | Display math between `$$` on separate lines; also handles text before it and indentation in lists |
| `text` or `"` | `\text{□}` inside math                                                                            |
| `beg`         | `\begin{□} … \end{□}` with linked environment names; the regex requires a preceding character     |

#### Powers, roots, fractions and subscripts

| Trigger | Result / example |
| --- | --- |
| `sr`, `cb` | `^{2}`, `^{3}` — e.g. `xsr` → `x^{2}` |
| `rd` | `^{□}` |
| `_` | `_{□}` |
| `sts` | `_\text{□}` for a text subscript |
| `sq` | `\sqrt{□}` |
| `3rt` | `\sqrt[3]{□}`; any single digit works before `rt` |
| `//` | `\frac{□}{□}` |
| `ee` | `e^{□}` at a word boundary |
| `invs` | `^{-1}` |
| `conj` | `^{*}` |
| `x3`, `x34` | Automatically become `x_{3}`, `x_{34}`; also works with Greek letters and accented variables |
| `xnn`, `xjj`, `xp1` | `x_{n}`, `x_{j}`, `x_{n+1}` |
| `\xii` | `x_{i}` — this trigger includes a leading backslash |
| `ynn`, `yii`, `yjj` | `y_{n}`, `y_{i}`, `y_{j}` |

#### Greek letters

| Trigger | Result | Uppercase trigger | Result |
| --- | --- | --- | --- |
| `@a` | $\alpha$ | — | — |
| `@b` | $\beta$ | — | — |
| `@g` | $\gamma$ | `@G` | $\Gamma$ |
| `@d` | $\delta$ | `@D` | $\Delta$ |
| `@e`, `:e` | $\epsilon$, $\varepsilon$ | — | — |
| `@z` | $\zeta$ | — | — |
| `@t`, `:t` | $\theta$, $\vartheta$ | `@T` | $\Theta$ |
| `@i` | $\iota$ | — | — |
| `@k` | $\kappa$ | — | — |
| `@l` | $\lambda$ | `@L` | $\Lambda$ |
| `@s` | $\sigma$ | `@S` | $\Sigma$ |
| `@u` | $\upsilon$ | `@U` | $\Upsilon$ |
| `@o` or `ome` | $\omega$ | `@O` or `Ome` | $\Omega$ |

#### Accents and fonts

| Trigger | Result / example |
| --- | --- |
| `xhat`, `xbar`, `xtilde` | `\hat{x}`, `\bar{x}`, `\tilde{x}` |
| `xdot`, `xddot` | `\dot{x}`, `\ddot{x}` |
| `xvec`, `xund` | `\vec{x}`, `\underline{x}` |
| `hat`, `bar`, `tilde`, `dot`, `ddot`, `vec`, `und` | The same accents with an empty field to fill in |
| `\alpha hat` | `\hat{\alpha}`; Greek letters also support space + `dot`, `bar`, `vec`, `tilde`, `und` |
| `x,.` or `x.,` | `\mathbf{x}`; Greek macros use `\boldsymbol`, e.g. `\alpha,.` |
| `bf`, `rm` | `\mathbf{□}`, `\mathrm{□}` |
| `Re`, `Im`, `trace` | `\mathrm{Re}`, `\mathrm{Im}`, `\mathrm{Tr}` |

#### Operators, relations and arrows

| Trigger | Result |
| --- | --- |
| `ooo` | $\infty$ |
| `sum` | `\sum_{□}^{□}` |
| `prod` | `\prod` |
| `\sum`, `\prod` (**manual**) | Indexed templates with defaults: `\sum_{i=1}^{N} □`, `\prod_{i=1}^{N} □` |
| `lim` | `\lim_{n \to \infty} □` with editable fields |
| `+-`, `-+` | $\pm$, $\mp$ |
| `xx`, `**` or `cdot` | $\times$, $\cdot$ |
| `...`, `nabl` | $\dots$, $\nabla$ |
| `para`, `deg` | `\parallel`, `\degree` |
| `===`, `!=` | $\equiv$, $\neq$ |
| `>=`, `<=`, `>>`, `<<` | $\geq$, $\leq$, $\gg$, $\ll$ |
| `simm`, `sim=`, `prop` | $\sim$, $\simeq$, $\propto$ |
| `->`, `<->`, `!>` | $\to$, $\leftrightarrow$, $\mapsto$ |
| `=>`, `=<` | $\implies$, $\impliedby$ |
| `pmod` | `\pmod{n}` with editable modulus |

#### Sets and number systems

| Trigger | Result |
| --- | --- |
| `and`, `orr` | $\cap$, $\cup$ (`and` requires a word boundary) |
| `inn`, `notin` | $\in$, $\not\in$ |
| `\\\` (three backslashes) | $\setminus$ |
| `sub=`, `sup=` | $\subseteq$, $\supseteq$ |
| `eset`, `set` | `\emptyset`, `\{ □ \}` (`set` requires a word boundary) |
| `RR`, `NN`, `ZZ`, `QQ`, `CC` | $\mathbb{R}$, $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{C}$ |
| `LL`, `HH` | $\mathcal{L}$, $\mathcal{H}$ |

#### Calculus

| Trigger | Result / example |
| --- | --- |
| `par` (**manual**) | `\frac{\partial y}{\partial x}` with editable fields |
| `par2` | `\frac{\partial^{2} y}{\partial x^{2}}`; any single digit works |
| `parn` | General partial derivative with editable order, function and variable |
| `payx` (**manual**) | `\frac{\partial y}{\partial x}`; pattern is `pa` + function letter + variable letter |
| `ddt` | `\frac{d}{dt}` |
| `\int` (**manual**) | `\int □ \, dx` with editable variable |
| `dint` | `\int_{0}^{1} □ \, dx` with editable bounds and variable |
| `oint`, `iint`, `iiint` | `\oint`, `\iint`, `\iiint` |
| `oinf` | `\int_{0}^{\infty} □ \, dx` |
| `infi` | `\int_{-\infty}^{\infty} □ \, dx` |
| `tayl` | Taylor expansion of `f(x+h)` through the second-order term, followed by `\dots`; `f`, `x` and `h` are linked editable fields |

#### Brackets and environments

| Trigger | Result / use |
| --- | --- |
| `avg` | `\langle □ \rangle` |
| `norm`, `Norm` | `\lvert □ \rvert` (absolute value), `\lVert □ \rVert` (norm) |
| `mod` | A pair of plain vertical bars; use `pmod` for modular arithmetic |
| `ceil`, `floor` | `\lceil □ \rceil`, `\lfloor □ \rfloor` |
| `(`, `[`, `{` | Insert a matching closing bracket and a field inside |
| `lr(`, `lr[`, `lr{` | Automatically sized brackets using `\left` and `\right` |
| `lr` + a vertical bar | Automatically sized absolute-value bars |
| `lra` | `\left< □ \right>` |
| `pmat`, `bmat`, `Bmat`, `vmat`, `Vmat` | Matrix environments with parentheses, square brackets, braces, single bars or double bars |
| `matrix`, `cases`, `align`, `array` | Matching `\begin{…}` and `\end{…}`; display math uses new lines, inline math stays on one line |
| `iden3` | A filled-in $3\times3$ identity matrix in a `pmatrix`; accepts a single-digit size |

#### Operations on selected math

Select the expression first, then use the visual trigger.

| Trigger | Wrap selection in |
| --- | --- |
| `U`, `O` | An underbrace with a label below, or an overbrace with a label above |
| `B` | `\underset{□}{selection}` |
| `C`, `K` | `\cancel{selection}`, `\cancelto{□}{selection}` |
| `S` | `\sqrt{selection}` |
| `(`, `[`, `{` | Matching brackets |

#### Physics and chemistry

| Trigger | Result |
| --- | --- |
| `kbt`, `msun` | `k_{B}T`, `M_{\odot}` |
| `dag`, `o+`, `ox` | `^{\dagger}`, `\oplus`, `\otimes` (`ox` requires a word boundary) |
| `bra`, `ket`, `brk` | `\bra{□}`, `\ket{□}`, `\braket{□ \vert □}` (the snippet uses a literal vertical bar) |
| `outer` | `\ket{\psi} \bra{\psi}` with the state linked between both fields |
| `pu`, `cee` | `\pu{□}`, `\ce{□}` |
| `he4`, `he3` | `{}^{4}_{2}He`, `{}^{3}_{2}He` |
| `iso` | `{}^{4}_{2}He` with editable mass number, atomic number and element |

#### Automatic helpers
- Recognised Greek names and symbols get a backslash automatically when preceded by a non-backslash character. Similar rules handle `exp`, `log`, `ln`, `det`, `int` and standard trig functions such as `sin`, `cos`, `tan` and their listed inverses.
- `arccsc`, `arcsec` and `arccot` expand using `\operatorname{…}`.
- After a Greek or symbol macro, space + `sr`, `cb` or `rd` applies a power without retaining the space: `\alpha sr` → `\alpha^{2}`.
- Digits after variables and Greek letters become subscripts; digits after other macros get a separating space, e.g. `\leq1` → `\leq 1`. The digit rule excludes `\pu` and `\ce`.
- Macro protection helps prevent snippets from expanding partway through recognised commands. A separating space is inserted when an appended letter no longer matches a known macro prefix.
