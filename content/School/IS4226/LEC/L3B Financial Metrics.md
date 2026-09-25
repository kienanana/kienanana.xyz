---
class: note
tags:
  - y4s1
  - finance/metrics
  - finance/risk
  - finance/returns
source:
related:
  - "[[L3A Risk and Returns]]"
author:
date: 2026-08-28
updated: 2026-09-22 16:45:48
aliases:
---
### Important Financial Metrics
> for designing your portfolio, developing strategies and understanding the behaviour 
- beta
- alpha
- standard deviation
- sharpe ratio
- correlation

### Systematic Risk & Unsystematic Risk

| Risk type             | Source and examples                                                                                                                                                          | Also known as                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Systematic risk**   | From events that cannot be planned:<br>• Financial crisis (Lehman Brothers, 2008)<br>• Global pandemics (COVID-19)<br>• Wars (US–Iran, 2026)<br>• ***Undiversifiable risk*** | Market<br>Macro                                  |
| **Unsystematic risk** | From individual companies or sectors:<br>• New technologies<br>• Changes in oil prices<br>• ***Diversifiable risk***                                                         | Individual<br>Idiosyncratic<br>Specific<br>Micro |

## Sharpe Ratio
$$
\begin{gather}
\text{Sharpe Ratio} = \frac{R-R_{f}}{\sigma_{p}}	 \\
\text{where:} \\
\text{R: the return on the portfolio} \\
R_{f} \text{ : the risk free rate of return} \\
\sigma_{p} \text{ : Standard deviation of the portfolio's excess return}
\end{gather}
$$
- risk adjusted performance
- most widely used
- if $R_{f} = 0$ then SR = Returns / SD

## Beta 
$$
\begin{gather}
\text{Beta Coefficient, } \beta = \frac{\text{Covariance}(R,R_{m})}{\text{Variance}(R_{m})}	 \\
\text{where:} \\
\text{R: the return on the portfolio} \\
R_{m} \text{ : the return on the market}
\end{gather}
$$
- measure of systematic risk or volatility against a benchmark
- design portfolio as per risk tolerance 
- drawbacks - historical returns 
- weighted beta of portfolio matters
> covariance - relation between movement of 2 assets

### Overall Beta
![[Screenshot 2026-08-28 at 6.44.07 PM.png]]
$$
\beta_p = \sum_{i=1}^{n} w_i\beta_i
$$
- A portfolio's overall beta is the weighted average of its assets' betas, where $w_i$ is each asset's portfolio allocation. 
- Allocating more to high-beta assets raises systematic risk; allocating more to low-beta assets reduces it. A market beta of $1$ is the benchmark.

## Alpha
$$
\begin{gather}
\text{Alpha Coefficient, } \alpha = R - R_{f} - \text{beta}(R_{m} - R_{f}) \\
\text{where:} \\
\text{R: the return on the portfolio} \\
R_{m} \text{ : the return on the market} \\
R_{f} \text{ : the risk free rate of return} \\
\text{beta: represents the systematic risk of the portfolio} \\
\end{gather}
$$
- from CAPM (Capital Asset Pricing Model)
- portfolio manager's capability
- performance above the benchmark
- used in conjunction with Beta

> expected return = risk-free return + compensation for market risk

$$
\begin{gather}
E(R_{i}) = R_{f} + \beta_{i}[E(R_{m})-R_{f}] \\
\text{Alpha} = R - \beta*R_{m}
\end{gather}
$$

## Correlation
- the degree with which one instrument moves in relation to another 
- ranges from -1 to +1 (standardised)
- tells the relation but not the causation
$$\text{Correlation} = \frac{Cov(x,y)}{\sigma x * \sigma y}$$

