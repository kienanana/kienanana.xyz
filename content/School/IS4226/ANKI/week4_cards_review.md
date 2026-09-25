# IS4226 L4 recall cards

70 cards drawn from the L4 note and its embedded diagrams. Definitions, distinctions, process recall and formula recall only; no application scenarios or numerical drills. Notebook dates, ticker lists, complete code blocks and chart price examples are not memorisation targets. The terse market-making wording is explicitly attributed to the note.

Deck: `IS4226::Week 4` · Tag: `is4226::w4`

The importer reuses the helpers in `/Users/kienanana/Documents/obsidian-scripts/is4226_import_anki.py`, with separate Week 4 identity tags. It adds/updates these cards without deleting notes. It does not run the Quiz 1 synchronisation routine.

```sh
python3 School/IS4226/ANKI/import_week4.py --validate-only
python3 School/IS4226/ANKI/import_week4.py
python3 School/IS4226/ANKI/import_week4.py --apply
```

### 1. How do time-based and price-based charts differ?

Time-based charts represent fixed time intervals. Price-based charts add entries only after sufficient price movement; equal spacing does not imply equal elapsed time.

Source: L4 Trading Strategies and Systems — Reading Charts

### 2. Which time-based and price-based chart types are listed in L4?

Time-based: line charts and candlesticks. Price-based: Point and Figure, Renko and Kagi.

Source: L4 Trading Strategies and Systems — Reading Charts

### 3. What prices does a line chart show, and what detail does it hide?

Closing prices. It shows the overall trend but hides price swings within each interval.

Source: L4 Trading Strategies and Systems — Line and Candlesticks

### 4. What does OHLC stand for?

Open, High, Low and Close.

Source: L4 Trading Strategies and Systems — Line and Candlesticks

### 5. What do a candlestick's body and wicks represent?

Body: the interval's open-to-close range. Wicks: extend to the interval's high and low.

Source: L4 Trading Strategies and Systems — Line and Candlesticks

### 6. What distinguishes a rising candle from a falling candle?

Rising: close above open. Falling: close below open.

Source: L4 Trading Strategies and Systems — Line and Candlesticks

### 7. What does the interval of a candlestick chart determine?

The period represented by each candle, e.g. 5 minutes, 15 minutes or 1 day.

Source: L4 Trading Strategies and Systems — Line and Candlesticks

### 8. What do X and O columns represent in a Point and Figure chart?

X: rising prices. O: falling prices.

Source: L4 Trading Strategies and Systems — Point and Figure

### 9. What does box size mean in a Point and Figure chart?

The price move represented by each X or O; smaller moves are ignored.

Source: L4 Trading Strategies and Systems — Point and Figure

### 10. What does reversal count mean in a Point and Figure chart?

The number of boxes price must move in the opposite direction to start a new column.

Source: L4 Trading Strategies and Systems — Point and Figure

### 11. What does ATR stand for, and how is it used in the note's Point and Figure chart?

Average True Range. It can set box size based on volatility.

Source: L4 Trading Strategies and Systems — Point and Figure

### 12. What price input is used for the Point and Figure chart described in the note?

Closing prices.

Source: L4 Trading Strategies and Systems — Point and Figure

### 13. What is the stated trade-off of Point and Figure's noise filtering?

Fewer false breakouts, but later signals.

Source: L4 Trading Strategies and Systems — Point and Figure

### 14. Which technical-analysis principles can still be applied to Point and Figure charts?

Trends, support/resistance and breakouts.

Source: L4 Trading Strategies and Systems — Point and Figure

### 15. What is a Renko chart?

A price-based chart made of bricks of a chosen price size. New bricks appear when price crosses the required thresholds; small moves produce no new brick.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 16. How can Renko brick size be set, and what is the effect of larger bricks?

Fixed or based on ATR. Larger bricks filter more noise but delay signals.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 17. In the Renko construction described in L4, how large is the move needed for a reversal brick?

Two brick sizes in the opposite direction from the last brick's closing edge.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 18. What is a Kagi chart?

A price-based chart of connected vertical lines. The current line extends as price continues in the same direction and reverses only when an opposite move reaches the chosen reversal amount.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 19. How are opposite-direction vertical lines connected on a Kagi chart?

By a short horizontal line.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 20. What does a Kagi chart's filtering help reveal?

Larger price swings and support/resistance, by filtering small fluctuations.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 21. Why does the note suggest using chart types together?

Candlesticks show timing and OHLC detail, while price-based charts help reveal the broader trend.

Source: L4 Trading Strategies and Systems — Renko and Kagi

### 22. What is the sequence in the vectorised backtesting system shown in L4?

Database → raw OHLC data via yfinance API → prepare data → strategy signals → PNL/equity curve → analysis.

Source: L4 Trading Strategies and Systems — Vectorised Backtesting System — embedded workflow screenshot

### 23. What happens in the 'Prepare data' stage of vectorised backtesting?

Create a dataframe to store features and prepare the indicators/features required by the strategy.

Source: L4 Trading Strategies and Systems — Vectorised Backtesting System — embedded workflow screenshot

### 24. How does the shown backtesting system register strategy signals?

Use if-else statements to record buy/hold/sell in a dataframe column, typically as 1/0/−1.

Source: L4 Trading Strategies and Systems — Vectorised Backtesting System — embedded workflow screenshot

### 25. What determines PNL or the equity curve in the shown backtesting system?

Actual returns and the position held.

Source: L4 Trading Strategies and Systems — Vectorised Backtesting System — embedded workflow screenshot

### 26. What is produced in the analysis stage of the shown backtesting system?

Metrics, graphs and figures.

Source: L4 Trading Strategies and Systems — Vectorised Backtesting System — embedded workflow screenshot

### 27. What does an API do, according to L4?

Connects two systems/programs; APIs are bundled in libraries.

Source: L4 Trading Strategies and Systems — API's

### 28. Which API/data-library examples are listed in L4?

Yahoo Finance, Google Finance, Quandl, AlphaVantage and pandas datareader.

Source: L4 Trading Strategies and Systems — API's

### 29. What is the difference between yf.Ticker(...) and yf.Tickers(...) in the notebook?

Ticker creates an object for one symbol. Tickers handles multiple symbols.

Source: L4 Trading Strategies and Systems — Notebook Screenshots

### 30. Which ticker attributes/methods retrieve stock information and historical prices in the notebook?

stock_data.info retrieves stock information; stock_data.history(...) retrieves historical prices.

Source: L4 Trading Strategies and Systems — Notebook Screenshots

### 31. What two ways of specifying a historical-data window are shown in the notebook?

A lookback period, e.g. period = '1y', or explicit start and end dates.

Source: L4 Trading Strategies and Systems — Notebook Screenshots

### 32. Which column is selected when plotting the notebook's line chart?

The Close column.

Source: L4 Trading Strategies and Systems — Notebook Screenshots

### 33. Which four metrics does the BASS function return, in order?

Beta, alpha, standard deviation and annualised Sharpe ratio.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Prepare prices and returns

### 34. What inputs does the BASS function take?

Stock symbol, benchmark symbol, start date and end date.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Prepare prices and returns

### 35. What does pct_change() calculate from the closing-price columns in the BASS notebook?

Regular/simple returns between consecutive observations.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Prepare prices and returns

### 36. What is the role of dropna() in the BASS data preparation?

Remove rows containing missing values.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Prepare prices and returns

### 37. How is beta calculated in the BASS notebook?

Covariance of stock and benchmark returns divided by the variance of benchmark returns.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Beta

### 38. How does the alternative beta calculation use the returns covariance matrix?

Divide the stock–benchmark covariance entry by the benchmark-variance entry.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Beta

### 39. How does the BASS notebook estimate annual returns from daily returns?

Mean daily return × 252.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Alpha and standard deviation

### 40. How does the notebook calculate annualised alpha in percentage units, assuming a zero risk-free rate?

(Annualised stock return − beta × annualised benchmark return) × 100.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Alpha and standard deviation

### 41. How is the notebook's standard deviation calculated, and what are its units?

Standard deviation of daily stock returns × 100. It is daily standard deviation in percentage units, not annualised.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Alpha and standard deviation

### 42. What CAGR formula is stated in the notebook comments for data spanning more than a year?

CAGR = (final price / initial price)^(1/t) − 1, where t is the number of years.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Alpha and standard deviation

### 43. How does the notebook calculate daily Sharpe ratio, assuming a zero risk-free rate?

Mean daily stock return / standard deviation of daily stock returns.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Sharpe ratio

### 44. How does the notebook annualise daily Sharpe ratio?

Daily Sharpe ratio × √252.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Sharpe ratio

### 45. What risk-free-rate assumption is used for alpha and Sharpe in the notebook?

A zero risk-free rate.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Sharpe ratio

### 46. Does the notebook's Sharpe calculation require benchmark returns?

No. It uses the stock's own returns and standard deviation and can be used to compare stocks/portfolios.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Sharpe ratio

### 47. In which order does sort_values(by='sharpe', ascending=False) rank stocks?

Highest to lowest Sharpe ratio (descending).

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Calculate and rank the stocks

### 48. Why does the notebook wrap each stock's BASS calculation in try/except?

To continue processing the remaining stocks if a symbol has no available data or raises an exception.

Source: L4 Trading Strategies and Systems — BASS Notebook Screenshots — Calculate and rank the stocks

### 49. What is a passive (static) strategy, and what is its objective?

Buy and hold with minimal security/strategy selection; capture market returns without frequent adjustments.

Source: L4 Trading Strategies and Systems — Passive vs Active

### 50. What passive-strategy examples does L4 give?

Index funds and ETFs tracking the S&P 500.

Source: L4 Trading Strategies and Systems — Passive vs Active

### 51. What is an active (dynamic) strategy, and what is its objective?

Frequent decision-making and trading; beat the market, outperform benchmarks or exploit inefficiencies.

Source: L4 Trading Strategies and Systems — Passive vs Active

### 52. What active-strategy examples does L4 give?

Hedge funds, discretionary traders and quant funds.

Source: L4 Trading Strategies and Systems — Passive vs Active

### 53. What is the idea-first (deductive) approach to strategy development?

Start with a hypothesis, intuition or theory, then use data to test or validate it.

Source: L4 Trading Strategies and Systems — Idea First or Data First

### 54. What is the data-first (inductive) approach to strategy development?

Start by mining patterns/signals in large datasets; a theory may come afterward to explain the pattern.

Source: L4 Trading Strategies and Systems — Idea First or Data First

### 55. Which idea-first examples are listed in L4?

Momentum due to investor herding; activity before weekends/lunch breaks; the first hour of trading.

Source: L4 Trading Strategies and Systems — Idea First or Data First

### 56. Which data-first approaches are listed in L4?

Machine learning and extensive quantitative research.

Source: L4 Trading Strategies and Systems — Idea First or Data First

### 57. What timescale and sources of advantage characterize fast strategies in L4?

Seconds to minutes; microstructure, speed and execution edge.

Source: L4 Trading Strategies and Systems — Fast vs Slow

### 58. Which fast-strategy examples does L4 give?

High-frequency trading, scalping and intraday strategies.

Source: L4 Trading Strategies and Systems — Fast vs Slow

### 59. What timescale and signals characterize slow strategies in L4?

Hours to days to months; broader economic, fundamental or trend signals.

Source: L4 Trading Strategies and Systems — Fast vs Slow

### 60. Which slow-strategy examples does L4 give?

Intraday trades, swing trades, position trades and macro bets.

Source: L4 Trading Strategies and Systems — Fast vs Slow

### 61. How does L4 contrast the win patterns associated with negative and positive skew?

Negative skew: more wins, but small wins. Positive skew: fewer wins, but big wins.

Source: L4 Trading Strategies and Systems — Positive or Negative Skew — text and embedded screenshots

### 62. Which examples does L4 associate with negative skew?

Mean reversion, selling options, market making and an insurance seller.

Source: L4 Trading Strategies and Systems — Positive or Negative Skew — text and embedded screenshots

### 63. Which examples does L4 associate with positive skew?

Trend/momentum strategies, buying options and an insurance buyer.

Source: L4 Trading Strategies and Systems — Positive or Negative Skew — text and embedded screenshots

### 64. What is mean reversion?

Asset prices return to their long-term average.

Source: L4 Trading Strategies and Systems — Mean Reversion or Momentum

### 65. What is momentum, according to L4?

Continued rate of change of prices in the same direction.

Source: L4 Trading Strategies and Systems — Mean Reversion or Momentum

### 66. What information distinguishes technical and fundamental approaches in L4?

Technical: price action. Fundamental: micro-to-macro data.

Source: L4 Trading Strategies and Systems — Trading Strategies

### 67. What does L4 associate pairs trading with?

Disturbed correlation between pairs.

Source: L4 Trading Strategies and Systems — Other Popular Strategies

### 68. What does L4 associate arbitrage with?

Inefficiencies in markets.

Source: L4 Trading Strategies and Systems — Other Popular Strategies

### 69. What phrase does L4 use to describe market making?

“Spread betting.” (The wording used in the note.)

Source: L4 Trading Strategies and Systems — Other Popular Strategies

### 70. What do candlestick-pattern strategies reflect, according to L4?

Trading sentiment.

Source: L4 Trading Strategies and Systems — Other Popular Strategies

