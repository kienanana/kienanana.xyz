---
class: practice
tags: [y4s1, IS4226, quiz]
---
Original practice questions based on your three lecture PDFs and the actual `1_yfinance.ipynb` and `2_BASS.ipynb` files. These are practice, not predictions of the lecturer's questions.

Correct options are **bolded**, with a short explanation below each question. Every question is single-answer unless marked **Select all**.

## What to be able to do

- **3A:** distinguish average returns from compounded growth; convert log/simple returns; calculate expected returns and normal-distribution bands; scale mean by N and SD by √N under independent, stable daily-return assumptions.
- **3B:** choose between alpha, beta, SD, Sharpe and correlation; compute them with consistent frequencies; interpret systematic versus company-specific risk and portfolio beta.
- **4:** read OHLC and price-based charts; trace the data → features → signals → P&L → analysis workflow; recognise strategy approaches, skew and leverage tradeoffs.
- **Notebooks:** identify which symbol and dates actually feed each call; distinguish statistics of prices from statistics of returns; trace covariance matrix positions, function output order and sorting.

## Notebook map and traps

Cell numbers below count all cells from **0**, as stored in the notebook JSON.

| Location                       | What matters                                                                                                                                                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| yfinance cells 3–9             | `Ticker` selects an instrument; `.info` gets information; `.history(...)` fetches prices; a later assignment overwrites `hist_stock`.                                                  |
| yfinance cells 15–18           | Calls use `period`, despite defining start/end variables. `describe()` here summarises **close prices**, not returns.                                                                  |
| yfinance cell 23               | `activity_tickers` supplies NVDA data, but the original `tickers[0]` supplies the `AAPL` column name. The comment about Apple is misleading.                                           |
| BASS cell 6 / function cell 13 | Returns are computed before `dropna()`. First return has no preceding price. The function explicitly uses `fill_method=None`; do not assume old and new pandas defaults are identical. |
| BASS cells 7–8                 | Divide stock–benchmark return covariance by **benchmark** return variance. Matrix positions depend on column order.                                                                    |
| BASS cells 9–11 / function     | Alpha: annualised arithmetic return estimate in percentage points, Rf = 0. SD: **daily percentage**. Sharpe: **annualised**, Rf = 0.                                                   |
| BASS cell 16                   | `ascending=False` means highest Sharpe first, despite the “ascending” comment. Bare `except` catches more than missing-symbol errors.                                                  |

The notebooks' “normal returns” wording means regular/simple returns in context; using `pct_change()` does **not** establish a normally distributed return series. Log returns are additive through time, but transforming returns does not guarantee normality either. A normal probability band is conditional on the model, not a guaranteed future range.

## Questions

### Lecture 3A: returns and projections

**1.** A stock moves from $100 to $120 to $100. Which pair is correct: arithmetic mean daily simple return; total holding-period return?

A. 0%; 0%  
**B. 1.67%; 0%**  
C. 1.67%; 3.33%  
D. 10%; −16.67%

**Explanation:** Returns are +20% and −16.67%; their arithmetic mean is +1.67%. End price equals start price, so holding-period return is zero. The mean describes observations, not compounded growth.

**2.** A stock returns +10% and then −10%. An investor says these cancel. What is the actual total simple return?

A. 0%  
B. +1%  
**C. −1%**  
D. −10%

**Explanation:** 1.10 × 0.90 − 1 = −0.01. Simple returns compound multiplicatively.

**3.** The sum of a stock's log returns over a period is 0.10. What simple return should you report?

A. 10% exactly  
B. ln(1.10), approximately 9.53%  
C. 0.10 divided by the number of days  
**D. exp(0.10) − 1, approximately 10.52%**

**Explanation:** Convert total log return with exp(L) − 1. A log return of 0.10 is not exactly a 10% simple return.

**4.** A stock has a 25% probability of returning +20% and a 75% probability of returning −4%. Its expected return is:

**A. 2%**  
B. 8%  
C. 16%  
D. −2%

**Explanation:** 0.25(20%) + 0.75(−4%) = 2%. An unweighted average ignores the state probabilities.

**5.** Use the lecture's simple-return approximation. Daily mean is 0.2%, daily SD is 1.2%, and the horizon is five days. Assuming independent, identically distributed normal daily returns, the approximate 68% return band is:

A. −5% to +7%  
**B. −1.68% to +3.68%**  
C. −1% to +1.4%  
D. −2.68% to +2.68%

**Explanation:** Mean = 5×0.2% = 1%; SD = √5×1.2% ≈ 2.68%. The band is 1% ± 2.68%. At price 100, the simple approximation gives 98.32–103.68.

**6.** Under the same assumptions, daily mean is 0.1% and daily SD is 2%. The approximate 95% return band over 25 days is:

A. −1.5% to +6.5%  
B. −97.5% to +102.5%  
**C. −17.5% to +22.5%**  
D. −7.5% to +12.5%

**Explanation:** Mean = 2.5%; SD = √25×2% = 10%. Approximate 95% band = 2.5% ± 20%.

**7. Select all.** Which statements about return modelling are correct?

**A. Log returns add through time.**  
B. Applying a logarithm guarantees a normal distribution.  
**C. A 95% normal-model band still allows observations outside it.**  
D. Summing simple returns always gives exact compounded return.

**Explanation:** Log returns add. Neither normality nor exact compounding by summing simple returns follows from the calculation.

**8.** A forecast uses daily **log** mean 0.001 and daily log SD 0.02. The initial price is $100. Which gives the model's 95% price band after four days?

A. 100 × [1 + 4(0.001) ± 2√4(0.02)] exactly  
B. 100 × exp[0.001 ± 2(0.02)]  
C. 100 × exp[4(0.001) ± 2×4(0.02)]  
**D. 100 × exp[4(0.001) ± 2√4(0.02)]**

**Explanation:** Aggregate log mean = 0.004 and SD = 0.04; exponentiate endpoints 0.004 ± 0.08. Prices are about 92.68–108.76. A is only a simple-return approximation.

### Lecture 3B: choosing and calculating metrics

**9.** Stock A returned 18% with beta 2. Stock B returned 12% with beta 0.8. Market return was 10%; Rf = 0. Which had higher alpha?

A. A, because it had higher raw return  
**B. B: its alpha is +4%, while A's is −2%**  
C. A: its alpha is +8%  
D. Both have positive alpha

**Explanation:** A: 18% − 2(10%) = −2%. B: 12% − 0.8(10%) = +4%. Higher raw return need not mean higher risk-adjusted alpha.

**10.** A fund returned 14%, with beta 1.5. Market return was 10% and risk-free return was 2%, all for the same year. Its CAPM alpha is:

**A. 0%**  
B. −1%  
C. +2%  
D. +4%

**Explanation:** CAPM required return = 2% + 1.5(10%−2%) = 14%. Alpha = realised 14% minus required 14% = 0%. The notebook's simplified formula assumes Rf = 0.

**11.** A portfolio allocates 60% to an asset with beta 0.5 and 40% to an asset with beta 2. Its beta is:

A. 1.25  
B. 2.5  
**C. 1.1**  
D. 0.8

**Explanation:** 0.6(0.5) + 0.4(2) = 1.1. Use investment weights, not an unweighted mean or sum.

**12.** A stock has high daily SD but beta close to zero. What is the best interpretation?

A. It is almost risk-free.  
B. Beta must be calculated incorrectly.  
C. Its returns must be uncorrelated with every other stock.  
**D. It can have substantial total volatility with little linear sensitivity to this benchmark.**

**Explanation:** SD measures total dispersion; beta measures sensitivity to the chosen market benchmark. Beta near zero does not imply low total volatility.

**13.** Annual return and annual SD are 15% and 20% for A, and 10% and 10% for B. With annual Rf = 2%, which has the higher Sharpe?

A. A: 0.75 versus 1.0  
**B. B: 0.80 versus 0.65**  
C. A: 1.30 versus 0.80  
D. They are equal because B has a lower return

**Explanation:** A = (15−2)/20 = 0.65; B = (10−2)/10 = 0.80. Match frequencies and subtract Rf.

**14.** A stock has correlation 0.5 with the market, daily SD 4%, and market daily SD 2%. Its beta is:

A. 0.5  
B. 0.25  
**C. 1.0**  
D. 2.0

**Explanation:** β = Cov/σm² = ρσstock/σm = 0.5(4/2) = 1. Beta and correlation are not interchangeable.

**15. Select all.** Which conclusions are justified?

**A. Diversifying across companies can reduce company-specific risk.**  
B. Diversification eliminates economy-wide market risk.  
**C. A company-specific product failure is an example of unsystematic risk.**  
D. Correlation proves one asset causes another's returns.

**Explanation:** Company-specific exposures can be diversified. Broad market risk remains; correlation is association, not proof of causation.

**16.** The benchmark used to calculate a stock's beta is changed, while its return observations, risk-free rate and sample dates remain fixed. Which metrics can change solely because of this change?

**A. Beta and alpha**  
B. SD and Sharpe only  
C. All four BASS metrics necessarily change  
D. None of them

**Explanation:** Beta depends on benchmark covariance/variance, and alpha uses beta and benchmark returns. SD and Sharpe use the stock's own fixed return sample. If changing benchmark also changes matched dates, SD and Sharpe could change too; the question holds dates fixed.

### Notebook applications and code tracing

**17.** A close-price series is [100, 110, 99]. What does `pct_change(fill_method=None)` produce?

A. [0, 10, −10]  
**B. [NaN, 0.10, −0.10]**  
C. [NaN, 0.10, −0.11]  
D. [100, 110, 99]

**Explanation:** First return is undefined; 110/100−1 = 0.10 and 99/110−1 = −0.10. `pct_change` returns fractions, not already-multiplied percentages.

**18.** You define `start_date` and `end_date`, but the fetch is `.history(period=period)`, where `period='1y'`. Which controls this call's requested range?

A. The named start/end variables automatically  
B. Both the variables and period, even though the variables are not passed  
C. The earlier column rename  
**D. The one-year period passed into the call**

**Explanation:** Defining variables has no effect on a call unless their values are actually passed or otherwise used. Read executable arguments.

**19.** In yfinance cell 23, `tickers=['AAPL','^GSPC']` and `activity_tickers=['NVDA','^GSPC']`. The assignment is:

```python
df[tickers[0]] = tickers_object.tickers[activity_tickers[0]].history(
    start=start_date, end=end_date
)["Close"]
```

`tickers_object` was constructed from `activity_tickers`. What is stored?

**A. NVDA closing prices in a column labelled AAPL**  
B. AAPL closing prices in a column labelled NVDA  
C. AAPL closing prices in a column labelled AAPL  
D. A syntax error because the two lists differ

**Explanation:** Right-hand side chooses NVDA; left-hand side chooses the label AAPL. A column label does not verify the underlying instrument.

**20.** `df` contains only closing-price columns. Its `describe()` output reports `std=12` for one stock. What can you conclude?

A. Annual return volatility is 12%.  
B. Daily return volatility is 12%.  
**C. Sample SD of the observed closing-price levels is 12 price units.**  
D. Sharpe is 12.

**Explanation:** This is dispersion of price levels in price units. For daily return volatility, compute daily returns first, then their SD. For the lecture activity's highest/lowest close, use the price column's max/min.

**21.** The BASS return covariance matrix has column order `['stock_returns','benchmark_returns']`:

```text
                  stock     benchmark
stock             0.0009    0.0003
benchmark         0.0003    0.0004
```

Which correctly computes the stock's beta?

A. `matrix.iat[0,1] / matrix.iat[0,0]` = 0.333  
**B. `matrix.iat[1,0] / matrix.iat[1,1]` = 0.75**  
C. `matrix.iat[0,0] / matrix.iat[1,1]` = 2.25  
D. `matrix.iat[1,1] / matrix.iat[1,0]` = 1.333

**Explanation:** Stock–market covariance is 0.0003 and market variance is 0.0004; beta = 0.75. Diagonal matrix entries are variances.

**22.** An analyst reverses the order to `['benchmark_returns','stock_returns']` but retains `matrix.iat[1,0] / matrix.iat[1,1]`. What is the problem?

A. Covariance changes sign solely because of the order.  
B. Nothing: the denominator remains benchmark variance.  
C. `.iat` always selects by name.  
**D. The denominator is now stock variance, so the expression generally no longer computes stock beta.**

**Explanation:** `.iat` is positional. After reordering, [1,1] is stock variance. Covariance symmetry does not protect the denominator.

**23.** BASS prints `(1.20, 3.50, 2.00, 0.80)`. Which is the correct interpretation?

**A. Beta 1.20; annualised alpha 3.50 percentage points; daily SD 2%; annualised Sharpe 0.80**  
B. Beta 1.20%; daily alpha 3.50%; annual SD 2%; daily Sharpe 0.80  
C. Correlation 1.20; alpha 3.50%; SD 2%; Sharpe 0.80%  
D. All four outputs are annual percentages

**Explanation:** Function order is beta, alpha, daily SD, annual Sharpe. Alpha and SD are multiplied by 100; beta and Sharpe are dimensionless.

**24.** Mean daily simple stock return is 0.001, market mean is 0.0005, beta is 1.2, and stock daily SD is 0.02. Using the BASS function's 252-day convention and Rf = 0, what are annualised alpha and Sharpe, approximately?

A. 0.04%; 0.05  
B. 10.08%; 12.60  
**C. 10.08%; 0.79**  
D. 25.20%; 0.79

**Explanation:** Stock annual mean estimate = 25.2%; market = 12.6%. Alpha = 25.2%−1.2(12.6%) = 10.08%. Sharpe = (0.001/0.02)√252 ≈ 0.79. Daily SD output would be 2%.

**25. Select all.** Which observations about the notebook are correct?

**A. `sort_values(by='sharpe', ascending=False)` places the highest Sharpe first.**  
B. `mean_daily_return * 252` is the exact realised compounded return of any 252-day series.  
**C. A bare `except` can print “symbol not found” for errors unrelated to an invalid symbol.**  
D. Multiplying daily SD by 100 annualises it.

**Explanation:** Descending sort puts largest values first. Annualising a mean does not compound a path. ×100 changes decimal returns to percentage units; √252 changes daily SD to annual SD under the scaling assumptions.

**26.** You have eight months of daily returns. The function uses `returns.mean()*252`. What does this produce?

A. The exact realised return over the eight-month sample  
**B. An annualised arithmetic mean return estimate based on that sample**  
C. CAGR, calculated from endpoint prices  
D. A forecast guaranteed to equal next year's return

**Explanation:** The function extrapolates the sample's arithmetic daily mean to an annual rate. Realised sample return uses compounded daily returns or endpoint prices; CAGR additionally accounts for elapsed years.

### Lecture 4: charts, workflow and strategies

**27.** A daily candle has open 100, high 110, low 95 and close 98. Which reading is correct?

A. Rising body from 95 to 110  
B. Falling body from 110 to 95  
C. Rising body from 98 to 100  
**D. Falling body from 100 to 98, with wicks reaching 110 and 95**

**Explanation:** Close is below open; body spans open/close and wicks mark high/low. A close-only line chart would hide this intraday range.

**28.** A point-and-figure chart has $2 boxes and a six-box reversal. The latest X is at $110. Under the lecture's convention, how far must price fall to initiate an O column?

A. To $108  
B. To $104  
**C. To $98**  
D. Any decline after six days

**Explanation:** Six boxes × $2 = $12 down from $110, so $98. Reversal is triggered by price movement, not elapsed days.

**29.** Prices fluctuate in a narrow range for ten days without crossing a price-chart threshold. Which statement is correct?

**A. A daily time-based chart can add observations while a price-based chart adds no new entry.**  
B. Both chart types must add ten entries.  
C. Both must add zero entries.  
D. Equal spacing on a price-based chart implies equal elapsed time.

**Explanation:** Time-based charts use fixed intervals. Price-based charts require threshold moves; spacing does not establish elapsed time. Larger boxes filter noise but can delay signals.

**30.** A trader first proposes that investor herding creates persistence in returns, tests that hypothesis, then buys assets whose prices continue rising. This combines:

A. Data first and mean reversion  
**B. Idea first and momentum**  
C. Passive investing and arbitrage  
D. Data first and market making

**Explanation:** Theory precedes testing: idea-first/deductive. Buying continued strength is momentum/trend following. Mean reversion would instead bet on a return toward an average.

**31.** A strategy wins small amounts frequently but occasionally suffers a large loss. Which conclusion is strongest?

A. It has positive skew and must have high Sharpe.  
B. Its high win rate guarantees profitability.  
C. It eliminates risk by winning often.  
**D. Its payoff pattern suggests negative skew; win rate alone cannot establish profitability.**

**Explanation:** Frequent small wins and rare large losses suggest a left tail. Expected profit also depends on magnitudes and probabilities; win frequency alone is insufficient. These are characteristic patterns, not universal guarantees for named strategies.

**32. Select all.** A vectorised strategy builds signals from prices and evaluates performance. Which statements are correct?

**A. Its workflow can run raw data → features → signals/positions → P&L/equity curve → metrics.**  
**B. Under the lecture's typical convention, +1/0/−1 can represent long/flat/short positions.**  
**C. In an ideal model with Rf = 0 and no costs, multiplying exposure by positive leverage scales mean and SD equally, leaving Sharpe unchanged.**  
D. A signal calculated only after today's close can legitimately earn the return from yesterday's close to today's close.

**Explanation:** P&L must use positions available before the returns they earn. Applying a close-derived signal to the return ending at that close creates look-ahead bias. Ideal positive leverage leaves mean/SD unchanged as a ratio, but scales losses; financing, costs and constraints can alter real Sharpe.

### Code-snippet applications: both notebooks

These additional questions use notebook code or small adaptations. Any supplied market data or BASS outputs are hypothetical; you do not need to download prices.

**33.** Assume both calls succeed. Which data does the final plot use?

```python
period = "1y"
start = "2024-01-01"
end = "2024-08-31"
stock_data = yf.Ticker("D05.SI")
hist_stock = stock_data.history(period=period)
hist_stock = stock_data.history(start=start, end=end)
hist_stock["Close"].plot()
```

A. Both datasets concatenated  
**B. Closing prices from the explicit start/end request**  
C. The first request's one-year closing prices  
D. Company information from `.info`

**Explanation:** The second assignment replaces `hist_stock`; the plot reads that replacement's `Close` column.

**34.** You want the highest close, lowest close and SD of closing prices, as requested in the lecture activity. Which replacement for `???` fits?

```python
hist = yf.Ticker("NVDA").history(start=start, end=end)
close = hist["Close"]
result = ???
```

**A. `(close.max(), close.min(), close.std())`**  
B. `(close.mean(), close.min(), close.std())`  
C. `(close.pct_change().max(), close.pct_change().min(), close.std())`  
D. `(hist["High"].max(), hist["Low"].min(), close.std())`

**Explanation:** The activity asks about closing-price levels. High/Low columns include within-interval extremes, and percentage changes answer return questions.

**35.** What will `r.tolist()` contain?

```python
prices = pd.Series([80.0, 100.0, 90.0])
r = prices.pct_change(fill_method=None).dropna()
```

A. `[20.0, -10.0]`  
B. `[0.20, -0.10]`  
C. `[0.25, -0.125]`  
**D. `[0.25, -0.10]`**

**Explanation:** Each change uses the previous price: 20/80 = 0.25 and −10/100 = −0.10. `dropna()` removes the first undefined return.

**36.** All prices are present and both instruments share the same three dates. How many rows remain, and what is the first retained stock return?

```python
df = pd.DataFrame({
    "benchmark": [100.0, 102.0, 101.0],
    "stock": [50.0, 55.0, 54.0]
})
df["benchmark_returns"] = df["benchmark"].pct_change(fill_method=None)
df["stock_returns"] = df["stock"].pct_change(fill_method=None)
df = df.dropna()
```

A. Three rows; 0%  
B. One row; approximately −1.82%  
**C. Two rows; 10%**  
D. Two rows; 5%

**Explanation:** Only the first row lacks previous prices. The next stock return is 55/50 − 1 = 10%.

**37.** Which rows survive? `None` represents a missing price.

```python
df = pd.DataFrame({
    "benchmark": [100.0, 101.0, 102.0, 103.0],
    "stock": [50.0, None, 55.0, 56.0]
})
df["benchmark_returns"] = df["benchmark"].pct_change(fill_method=None)
df["stock_returns"] = df["stock"].pct_change(fill_method=None)
clean = df.dropna()
```

**A. Only row index 3**  
B. Row indices 2 and 3  
C. Row indices 1, 2 and 3  
D. No rows

**Explanation:** Row 0 lacks previous prices; row 1 lacks a stock price; row 2's stock return lacks a previous price. Row 3 has valid prices and returns for both instruments.

**38.** The code runs, but its beta formula has a conceptual error. Which line fixes it?

```python
cov = df["stock_returns"].cov(df["benchmark_returns"])
var = df["stock_returns"].var()
beta = cov / var
```

A. `beta = var / cov`  
**B. `var = df["benchmark_returns"].var()`**  
C. `cov = df["stock"].cov(df["benchmark"])`  
D. `beta = cov / df["benchmark_returns"].std()`

**Explanation:** Stock beta divides stock–market return covariance by market return **variance**, not stock variance or market SD.

**39.** The variables below already contain annual return estimates in decimal units. What is printed?

```python
stock_yearly_returns = 0.18
benchmark_yearly_returns = 0.10
beta = 1.5
alpha = (stock_yearly_returns - beta * benchmark_yearly_returns) * 100
print(round(alpha, 2))
```

A. 8.0  
B. 0.03  
C. 15.0  
**D. 3.0**

**Explanation:** Alpha with Rf = 0 is 0.18 − 1.5×0.10 = 0.03. Multiplying by 100 reports 3 percentage points.

**40.** Suppose daily stock-return SD is 0.015. Which interpretation of these calculations is correct under the usual scaling assumptions?

```python
daily_std = 0.015
x = daily_std * 100
y = daily_std * (252 ** 0.5) * 100
```

A. x is annual SD and y is daily SD.  
B. Both are annual SD because they multiply by 100.  
**C. x is 1.5% daily SD; y is approximately 23.81% annual SD.**  
D. y is 378% annual SD.

**Explanation:** ×100 converts units; ×√252 scales daily SD to annual SD. They perform separate operations.

**41.** With Rf = 0, what does the code print, approximately?

```python
avg_returns = 0.0008
std = 0.016
daily_SR = avg_returns / std
annual_SR = daily_SR * (252 ** 0.5)
print(round(annual_SR, 2))
```

**A. 0.79**  
B. 0.05  
C. 12.60  
D. 79.37

**Explanation:** Daily Sharpe = 0.05; annual Sharpe = 0.05√252 ≈ 0.79. Sharpe is a ratio, not a percentage.

**42.** Assume `BASS(...)` returns `(0.9, 4.0, 1.8, 1.1)`. What is stored by this snippet, and how should it be fixed to collect Sharpe?

```python
BASS_output = BASS(symbol, benchmark_symbol, start, end)
sharpe_value.append(BASS_output[2])
```

A. It stores beta; use index 1.  
**B. It stores daily SD, 1.8; use index 3.**  
C. It stores alpha; use index 0.  
D. It correctly stores Sharpe, 1.1.

**Explanation:** The function returns beta, alpha, SD, Sharpe in positions 0, 1, 2, 3. A misleading list name does not change the selected value.

**43.** Which stock order does the printed result have?

```python
output_df = pd.DataFrame({
    "stock": ["A", "B", "C"],
    "sharpe": [0.4, -0.2, 1.1]
})
# print stocks with ascending Sharpe
print(output_df.sort_values(by="sharpe", ascending=False))
```

A. B, A, C  
B. A, B, C  
C. C, B, A  
**D. C, A, B**

**Explanation:** `ascending=False` sorts 1.1, 0.4, −0.2 from highest to lowest. The executable argument controls behaviour; the comment is incorrect.

**44.** Assume each `BASS(...)` call either returns four values successfully or raises before any `append` executes. What happens if the middle symbol raises?

```python
stock_name, beta_value = [], []
for symbol in ["A", "BAD", "C"]:
    try:
        result = BASS(symbol, benchmark_symbol, start, end)
        beta_value.append(result[0])
        stock_name.append(symbol)
    except:
        print("The symbol {} not found".format(symbol))
```

A. The loop stops and C is never attempted.  
B. BAD is added with beta zero.  
**C. The loop attempts C; the two lists contain matching entries for A and C.**  
D. The message proves that the ticker is invalid.

**Explanation:** The exception skips BAD's appends and execution continues with C. The message does not establish the cause: network or calculation errors could also be caught.

**45.** A student wants the realised total return, rather than the arithmetic mean of daily returns. Which expression belongs at `???`?

```python
r = pd.Series([0.10, -0.10])
realised_return = ???
```

**A. `(1 + r).prod() - 1`**  
B. `r.mean()`  
C. `r.sum()`  
D. `r.mean() * 252`

**Explanation:** Multiplying growth factors gives 1.10×0.90 − 1 = −1%. The sum and mean are both zero for this example and miss the compounding loss.

**46.** Which replacement estimates the lecture's approximate 95% **N-day simple-return band**, using independent daily-return assumptions?

```python
mu_daily = 0.001
sigma_daily = 0.02
N = 25
lower, upper = ???
```

A. `(mu_daily - 2*sigma_daily, mu_daily + 2*sigma_daily)`  
**B. `(N*mu_daily - 2*(N**0.5)*sigma_daily, N*mu_daily + 2*(N**0.5)*sigma_daily)`**  
C. `(N*mu_daily - 2*N*sigma_daily, N*mu_daily + 2*N*sigma_daily)`  
D. `(mu_daily/N - 2*sigma_daily/N, mu_daily/N + 2*sigma_daily/N)`

**Explanation:** Mean scales by N and SD by √N. Here the return band is −17.5% to +22.5%, using the lecture's approximation rather than exact compounded simple-return modelling.

## Final revision checklist

Explain these without looking at the highlighted options or explanations:

1. Why a stock can beat the market in raw return but have negative alpha.
2. Why low beta is compatible with high SD.
3. Why `mean()*252`, `std()*100` and `Sharpe*sqrt(252)` do three different things.
4. Why a covariance-matrix formula can break after changing column order.
5. Why `describe()` of prices does not answer a return-risk question.
6. Why a column named AAPL might actually contain NVDA prices.
7. Why a normal-model band is not a guarantee, and why log-space bands need exponentiation.
8. Why larger price-chart thresholds can give fewer false breakouts but later signals.
9. Why a high win rate can coexist with negative skew and losses.
10. Why a signal must exist before the return to which it is applied.

Also distinguish passive buy-and-hold from active adjustment; technical price-based inputs from fundamental company/macro inputs; fast execution-focused strategies from slower strategies; pairs trading (relative-value divergence), arbitrage (pricing inefficiencies), and market making (quoting bid/ask and seeking the spread). The lecture's “spread betting” phrase for market making should be understood in its bid–ask-spread context.

## Sources and precision notes

Primary course sources: `Lecture-3A_Video_Lesson_Risk and Returns.pdf` (especially slides 5–10); `L3B_Financial Metrics.pdf` (slides 9–17); `L4_TradingStrategies.pdf` (slides 6–12, 16–32); and the two notebooks at `/Users/kienanana/Documents/SCHOOL/Y4S1/IS4226/notebooks/`.

Notebook results were traced from source code; no live market downloads were needed. Numbers in practice scenarios are constructed examples.

The lecture's SD formula displays a population denominator N, while pandas `.std()` defaults to sample SD with N−1 (`ddof=1`). Follow the stated convention in calculation questions. [Official pandas SD documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html).

Despite its name, `pct_change()` returns fractional changes. Missing-value handling has differed across pandas versions; the BASS function explicitly sets `fill_method=None`, avoiding implicit filling before calculation. [Official pandas change documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html?highlight=pct_change).

Sharpe does not require a market benchmark, but generally does use a risk-free return; the notebook assumes this is zero. The function rounds beta before calculating alpha, so manually calculated alpha using unrounded beta can differ slightly. Its annualised alpha is an arithmetic-return-based estimate, not a claim about exact compounded annual performance.
