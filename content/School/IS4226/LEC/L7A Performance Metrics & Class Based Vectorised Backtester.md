---
class: note
tags:
  - y4s1
  - finance/metrics
  - finance/backtesting
  - finance/risk
  - finance/returns
  - finance/trading
source:
related:
author:
date: 2026-10-05
updated: 2026-10-05 16:40:03
aliases:
---
## Vectorised Backtesting Till Now
![[Screenshot 2026-10-05 at 5.07.40 PM.png]]

### Other Important Metrics
- Calmar Ratio = Returns / Drawdown 	![[Screenshot 2026-10-05 at 5.21.23 PM.png]]
	- Measures **return per unit of maximum drawdown**; a higher ratio is preferred.
	- [[L6 Systematic Trading Strategies and Systems#Drawdown|Drawdown]] is the fall in equity from a previous peak to a subsequent trough. Use the **largest drawdown** over the backtest: in the screenshot, 2% and 3% declines → maximum drawdown = **3%**.
		- Helps distinguish strategies with similar returns: at 30% return, a 5% drawdown gives Calmar = **6**, while a 20% drawdown gives **1.5**.
	- Prof's **15% drawdown limit is a rule of thumb**, depending on the trader's risk appetite; larger drawdowns indicate greater losses from a peak.

- Sortino Ratio = Returns / Neg_std_dev
	- aka. Returns / Downside Std Dev
	- aka. Returns / Downside Risk	![[Screenshot 2026-10-05 at 5.30.35 PM.png]]
	- **[[L3B Financial Metrics#Sharpe Ratio|Sharpe Ratio]] counts both upside and downside volatility as risk**: 
		- the screenshot's large +80% return increases standard deviation. Sortino excludes upside fluctuations from its risk measure, since higher returns are desirable.
	> - Downside means **returns below a chosen threshold $T$** (e.g. 0%, a target return, or the risk-free rate). Only when $T = 0$ does this mean negative returns.
		- Sortino treats risk as **falling below your required return**. A large gain (e.g. +80%) exceeds that requirement, so it is excluded from downside risk. Use this perspective when you care mainly about disappointing returns rather than overall variability.
	
	- *Downside deviation*: $\sqrt{\frac{1}{N}\sum_{i=1}^{N}[\min(0, R_i-T)]^2}$. 
		- T: Threshold. Generally 0
		- Set returns above the threshold to 0; square the shortfalls, average over **all $N$ observations**, then take the square root. This differs from taking the standard deviation of only negative returns.
	- Measures **return per unit of downside risk**; *higher is preferred*. 
		- eg. if two strategies both have Sharpe = 1.5, Sortino of 2 vs 1.6 helps favour the first for better return relative to downside risk.

- Treynor Ratio = Returns / [[L3B Financial Metrics#Beta|Beta]]
	> A **benchmark is the market reference** used to compare your strategy against, e.g. the STI for Singapore stocks.
	> 
	> Beta measures how your strategy responds to movements in that benchmark: **beta = 1** means it tends to move about as much as the market; **beta = 2** means about twice as much.
	
	- Treynor therefore asks: **how much return am I earning for the market risk I take?** 
		- Sharpe and Sortino measure risk from the strategy's own returns; Treynor uses its sensitivity to a benchmark (beta).
		- For the same positive return and **positive betas**, lower beta gives a higher Treynor ratio: at 10% return, beta = 1 gives **10% per unit of beta**, while beta = 2 gives **5%**. *Higher is preferred* in this comparison.
	- Prof assumes $R_f = 0$; with a nonzero risk-free rate, use **$(R_p-R_f)/\beta_p$**.

- Information Ratio = (Rp - Rb) / Tracking Error
	- Tracking Error = std dev of (Rp - Rb)
	- $R_{p}: \text{Portfolio Return}$
	- $R_{b}: \text{Benchmark Return}$	![[Screenshot 2026-10-05 at 5.53.20 PM.png]]
	- Asks: **how consistently does the portfolio outperform its benchmark?** The numerator is the **average extra return** earned over the benchmark; tracking error measures how much that extra return varies over time.
		- In the screenshot, benchmark returns of 10%, 8%, −1% vs portfolio returns of 12%, 10%, 1% give **+2 percentage points each time**: consistent outperformance, so tracking error is 0 in this hypothetical example (the ratio is then undefined).
		- By contrast, portfolio returns of 100% then −50% against benchmark returns of 10% then 8% give differences of **+90 then −58 percentage points**: inconsistent performance relative to the market, so tracking error is high.
	- **Higher is preferred**: more average outperformance per unit of tracking error. Commonly used by fund managers who aim to beat a benchmark consistently.

- assumption: Rf = 0
	- else Returns -> Returns - Rf
- points to keep in mind:
	- what's in the numerator, what's in the denominator
	- what will happen if they incr / decr 
	- does the metric compare to a benchmark?

## Glossary
- **Annualised Return:** Yearly equivalent of a strategy's return.
- **[[L6 Systematic Trading Strategies and Systems#Drawdown|Maximum Drawdown]]:** Largest percentage fall in portfolio value from a previous peak.
- **Calmar Ratio:** Annualised return divided by maximum drawdown.
- **[[L3B Financial Metrics#Sharpe Ratio|Sharpe Ratio]]:** Excess return over the risk-free rate per unit of total volatility.
- **Sortino Ratio:** Return above a target per unit of downside deviation.
- **Treynor Ratio:** Excess return over the risk-free rate per unit of systematic risk (beta).
- **Information Ratio:** Average return above a benchmark divided by tracking error.
- **[[L3B Financial Metrics#Beta|Beta]]:** Sensitivity of portfolio returns to market movements.
- **[[L3B Financial Metrics#Alpha|Alpha]]:** Return above what is expected after accounting for market risk.
- **R-squared:** Proportion of variation in portfolio returns explained by benchmark returns.
- **Skewness:** Asymmetry of the return distribution.
- **Kurtosis:** Tail heaviness of the return distribution; indicates the tendency for extreme outcomes.
- **Omega Ratio:** Expected gains above a minimum acceptable return divided by expected shortfalls below it.
- **Downside Deviation:** Measures shortfalls below a chosen return threshold; used in the Sortino ratio.
- **Value at Risk (VaR):** Loss threshold exceeded with a specified small probability over a given period, e.g. 5% for 95% confidence.
- **Conditional Value at Risk (CVaR) / Expected Shortfall:** Average loss in the worst tail beyond the VaR threshold.
- **Profit Factor:** Gross profit divided by the absolute value of gross loss.
- **Recovery Factor:** Net profit divided by maximum drawdown, measured in the same units.
- **Ulcer Index:** Measures the depth and persistence of percentage drawdowns.
- **Win Rate:** Percentage of trades that are profitable.
- **Reward-to-Risk Ratio:** Average winning trade divided by the absolute value of the average losing trade.
- **Expectancy:** Average profit or loss per trade.
- **Trade Duration:** Average time a position is held.
- **Number of Trades:** Total trades made during the measured period.
- **Turnover Rate:** How frequently portfolio holdings are bought and sold.

### Prof's Notebook
#### Calmar Ratio
```python
annual_regular_ret
"""
Stock_Returns        0.348629
Strategy_Returns     0.607541
Benchmark_Returns    0.270756
dtype: float64
"""
```

```python
# We have already stored all the annualised risk return metrics for the stock[0] and strategy[1]
Calmar_ratio = annual_regular_ret[1] / max_drawdown
```

#### Tracking Error and Information Ratio
```python
# Storing the difference of stock returns and benchmark returns
bt_data["Strategy-Benchmark"] = bt_data['Strategy_Returns'] - bt_data['Benchmark_Returns']

# Average of difference
average_of_difference = bt_data["Strategy-Benchmark"].mean()

# Standard deviation of the difference, also known as Tracking Error. The lower the better
std_dev_of_difference = bt_data["Strategy-Benchmark"].std()

# Information Ratio daily
IR_daily = average_of_difference / std_dev_of_difference

# Convert to annual
IR_annual = IR_daily * (252**0.5)

IR_annual
```

#### Treynor Ratio
```python
# Similar to what we did in the BASS notebook. Prepare a covariance matrix
matrix = bt_data[['Strategy_Returns', 'Benchmark_Returns']].cov()

# Beta = Cov(Strategy, benchmark) / Var(benchmark)
Beta = matrix.iat[0, 1] / matrix.iat[1, 1]

Treynor_ratio = annual_regular_ret[1] / Beta

Treynor_ratio
```

#### Sortino Ratio
```python
# Create a new series with positive returns converted to 0 and negative returns as is
converted_returns = bt_data['Strategy_Returns'].apply(lambda x: 0 if x > 0 else x)
converted_reg_returns = np.exp(converted_returns) - 1

squared_converted_returns = converted_reg_returns ** 2

squared_sum = np.sum(squared_converted_returns)
len_squared_sum = len(converted_returns)

downside_deviation = np.sqrt(squared_sum / len_squared_sum)

# Calculate annualised downside dev
annual_converted_sd = downside_deviation * np.sqrt(252)

# Calculate Sortino
sortino = annual_regular_ret[1] / annual_converted_sd
```

## Class Based System
![[Screenshot 2026-10-05 at 7.23.09 PM.png]]

### Previous Strategy in One Class
- **New class-based approach**, reusing the [[L6 Systematic Trading Strategies and Systems#MA Cross in python|Lec 6 strategy]]. Modular methods share the object's data/settings.
- Change constructor inputs to test other stocks/parameters. `...` represents code hidden in the slide.

```python
class MA_Crossover:
    def __init__(self, symbol, start, end, STMA_window, LTMA_window, interval):
        ...

    def prepare_data(self):
        ...

    def strategy(self):
        ...

    def visualise_strategy(self):
        ...

    def performance(self):
        ...

    def returns_plot(self):
        ...

    def drawdown_plot(self):
        ...
```

```python
if __name__ == "__main__":
    output = MA_Crossover("AAPL", "2022-06-01", "2022-07-01", 5, 21, "1d")

    output.strategy()
    output.visualise_strategy()
    output.performance()
    output.returns_plot()
    output.drawdown_plot()
```
