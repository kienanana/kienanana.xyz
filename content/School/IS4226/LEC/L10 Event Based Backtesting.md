---
class: note
tags:
  - finance/backtesting
source:
related:
author:
date: 2026-10-27
updated: 2026-10-27 13:05:40
aliases:
---
## Backtesting Issues 
1. indicators are subjective
	- the indicator itself (ROC or MOM or MA or others?)
	- the combination of indicators
	- parameters within the indicators like lookback period 
- Rule Based
	- aim to test with minimal indicators - 1 stochastic and 1 trend
	- test across variations [50-200, 60-200, 70, 200...]
	- out of sample testing

2. supports / resistances are subjective 
	- timeframes (5m, 15m, 1h?)
	- zone or a line 
	- candlestick or line chart prices 
- Holistic View
	- consistent definition 
	- confirmation from indicators 

3. sensitive to many parameters (symbol, date, quantity etc)
- test in all markets (bull, bear, range)
- a check for overfitting 
- different symbols or different dates 

 4. returns are not normal
    - risk reward metrics like sharpe ratio assume normality of returns 
    - same shape but different risks 
- strategy returns analysis 
- position sizing adjustments 
- Monte Carlo Simulations 

5. correlation among parameters or strategies 
	- overfitting risks 
	- poor diversification 
- remove highly correlated ones 
- PCA when implementing ML models 

6. heteroscedasticity (variability of variance)
	- risk is not constant 
- Rolling Statistics 
- volatility adjusted position sizing 
- regime filtering and adjusting strategies 

7. correction due to traders 
	- irrational behaviour 
	- investor psychology 
	- different participants with different needs 
- robust risk management at all times 

8. computing challenges 
	- implementation risk - leverage, transaction, slippage 
- scalable design 
- rigorous code testing 

### What you get after backtesting?
![[Screenshot 2026-10-27 at 1.21.01 PM.png]]
- use backtesting data for...
	- monte carlo simulations 
	- others: bootstrapped returns OR adding noise to returns 

## Monte Carlo 
![[Screenshot 2026-10-27 at 1.22.32 PM.png]]
- Uses repeated random sampling to simulate many possible outcomes.
- Here, resample backtested trade returns or add random noise to generate alternative equity curves (portfolio value over time).
- Compare outcomes to estimate possible losses, maximum drawdowns and the chance of losing money.
- Results depend on the sampling assumptions; they do not guarantee future performance.

### When to stop? 
- Drawdown = fall from the portfolio's previous peak (e.g. $100k → $70k = 30%).
	- Slide example: maximum backtested drawdown = 15%, but live trading drawdown = 30%. Should you stop?
- The backtested maximum is only the worst observed historically, not a guaranteed future limit.
- Use Monte Carlo to assess whether a 30% drawdown is plausible or unusually severe under the simulation assumptions.
- Set stop/review thresholds beforehand using simulated drawdowns and loss tolerance; investigate unusually severe losses for changes in the strategy, market or execution.

### Set Target / Rebalance 
- at all times - maintain the risk levels 
	- check the risk of your positions and adjust the weights periodically 
	- calculate risk per trade (1-2% capital) 
	- think of halting the strategy in choppy range 
- set of indicators to get a holistic view
	- ATR, VWAP, Divergence, VIX

## Average True Range
$$
TR = Max[(H-L),Abs(H-C_{P}),Abs(L-C_{P})]\\
ATR = \left( \frac{1}{n} \right) \sum_{i=1}^{n} TR_{i} \\
\text{where:} \\
TR_{i} = \text{a particular true range}\\
n = \text{the time period employed}
$$
- measure of recent volatility 
- stop loss = 1.5 to 2 * ATR

## VWAP 
$$
VWAP = \frac{\sum_{i=1}^{n} P_i V_i}{\sum_{i=1}^{n} V_i}
$$
- for intraday analysis 
![[Screenshot 2026-10-27 at 1.47.24 PM.png]]
- Red/green candles = actual price movements; white line = VWAP.
- VWAP is the average price so far in the session, weighted by volume; higher-volume trades have more influence.
- Price above VWAP suggests intraday strength; price below VWAP suggests intraday weakness.
- VWAP is smoother because it accumulates trades throughout the session.
- A crossing alone is not a reliable buy/sell signal; repeated crossings can produce false signals.

## VIX
- volatility index 
- Measures expected S&P 500 volatility over the next 30 days, using option prices.
- Higher VIX = larger expected swings; lower VIX = calmer expectations (not price direction).
- Greater willingness to pay for option protection typically raises VIX: the "fear gauge".
- VIX futures/options can hedge volatility risk.
- Use as a market-condition filter: backtest smaller positions or adjusted rules when VIX is high.
![[Screenshot 2026-10-27 at 1.48.56 PM.png]]
- Horizontal axis = year; right vertical axis = VIX level.
- Higher line = larger expected market swings; lower line = calmer expectations.
	- Peaks around 2008 and 2020 show sharp increases in expected volatility.

## Divergence 
- Divergence = price and an indicator (or two related indices) move differently, warning of possible trend weakness.
- DJIA–DJTA: a new high/low in one index without confirmation from the other suggests divergence.
- Use with other signals to support a decision; divergence alone does not guarantee a reversal.
![[Screenshot 2026-10-27 at 1.52.36 PM.png|247]]
- Top panel = price candles; bottom panel = momentum indicator (appears to be RSI).
- White lines connect the lows: price makes a lower low, but the indicator makes a higher low.
	- This is bullish divergence: price falls further, but downward momentum weakens.
	- Price subsequently rallies in this example; the divergence warned of a possible upward reversal.

### Portfolio Returns 
![[Screenshot 2026-10-27 at 1.54.11 PM.png]]
$R_{P} = \sum_{i=1}^{n}(w_{i)}) \times (R_{i)}$


# Event Based System
## Event Based
- last time -> vectorised backtesting 
	- fast (numpy and pandas)
	- concise (all data at once - *look ahead bias*)
	- easy to understand (no complexities - *simplification bias*)
- many assumptions:
	- no transaction fees / slippage / spread 
	- trade executes at desired close prices 
	- trade at close prices / opening prices 
- now -> event based backtesting 
	- event: new information 
		- bar - OHLCV + other info

### The design steps 
1. create a common class:
	- trading capital 
	- dates
	- place order
	- fetch balances
	- prepare data 
	- store data for result 
2. strategy class 
	- logic for buy and sell 
	- execution logic 
- calculate 'returns' from daily account balance change instead of stock returns 

## The Structure of Backtester
### Structure (slide 25)
- `Common_Class` handles data, cash, positions and orders; `MA_Strategy` inherits it and adds trading rules.
- `close_graph()` can also be called from `prepare_data()`.

```python
class Common_Class:
    def __init__(self, symbol, start, end, interval, capital,
                 transaction_cost, verbose=True): ...
    def prepare_data(self): ...
    def close_graph(self): ...
    def return_date_price(self, bar): ...
    def realised_balance(self, bar): ...
    def unrealised_balance(self, bar): ...
    def total_balance(self, bar): ...
    def buy_order(self, bar, quantity=None, dollar=None): ...
    def sell_order(self, bar, quantity=None, dollar=None): ...
    def last_trade(self, bar): ...


class MA_Strategy(Common_Class):
    def go_long(self, bar, quantity=None, dollar=None): ...
    def go_short(self, bar, quantity=None, dollar=None): ...
    def run_strategy(self, STMA_window, LTMA_window): ...


if __name__ == "__main__":
    A = MA_Strategy("AAPL", "2010-04-10", "2022-07-01", "1d", 10000, 0.01, True)
    A.run_strategy(50, 200)
```

### Initialise the base class (slide 26)
- Required imports added below. Methods in slides 27–30 belong inside `Common_Class`.

```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator


class Common_Class:
    def __init__(self, symbol, start, end, interval, capital,
                 transaction_cost, verbose=True):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.interval = interval
        self.initial_capital = capital
        self.capital = capital  # Cash balance; changes with trades.
        self.transaction_cost = transaction_cost
        self.quantity = 0      # Positive = long; negative = short.
        self.position = 0      # 0 = flat, 1 = long, -1 = short.
        self.trades = 0
        self.verbose = verbose
        self.prepare_data()
```

### Prepare and visualise data (slide 27)

```python
    def prepare_data(self):
        # Strategy-specific moving averages are calculated later.
        stock_data = yf.Ticker(self.symbol)
        hist_stock = stock_data.history(
            start=self.start, end=self.end, interval=self.interval
        )
        bt_data = pd.DataFrame()
        bt_data["Close_Price"] = hist_stock["Close"]
        bt_data["Return"] = np.log(
            bt_data["Close_Price"] / bt_data["Close_Price"].shift(1)
        )
        bt_data = bt_data.dropna()
        self.data = bt_data

    def close_graph(self):
        plt.figure(figsize=(15, 5))
        plt.plot(self.data["Close_Price"], color="black",
                 label="Price", linestyle="dashed")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.title("Close Prices of {}".format(self.symbol))
        plt.legend()
        plt.grid()
        plt.show()
```

### Fetch bar values and balances (slide 28)
- Here, “realised balance” means cash; “unrealised balance” means signed position value, not unrealised profit. These methods print rather than return balances.

```python
    def return_date_price(self, bar):
        # bar is the row number for the chosen time interval.
        date = str(self.data.index[bar])[:10]
        price = self.data.Close_Price.iloc[bar]
        return date, price

    def realised_balance(self, bar):
        date, price = self.return_date_price(bar)
        print("Date :{} | Realised Balance: {:0.1f}".format(date, self.capital))

    def unrealised_balance(self, bar):
        date, price = self.return_date_price(bar)
        ub = self.quantity * price
        print("Date :{} | Unrealised Balance: {:0.1f}".format(date, ub))

    def total_balance(self, bar):
        date, price = self.return_date_price(bar)
        tb = self.quantity * price + self.capital
        print("Date :{} | Total Balance: {:0.1f}".format(date, tb))
```

### Buy and sell orders (slide 29)
- `transaction_cost` is proportional to trade value: `0.01` = 1% per order. Dollar sizing excludes fees, so spending `"all"` can overdraw cash.

```python
    def buy_order(self, bar, quantity=None, dollar=None):
        date, price = self.return_date_price(bar)
        if quantity is None:
            quantity = int(dollar / price)
        self.capital = self.capital - quantity * price * (1 + self.transaction_cost)
        self.quantity = self.quantity + quantity
        self.trades = self.trades + 1
        if self.verbose:
            print("Bought {} shares of {} at {:0.1f} per share worth {:0.1f} $".format(
                quantity, self.symbol, price, quantity * price))
            self.realised_balance(bar)
            self.unrealised_balance(bar)
            self.total_balance(bar)

    def sell_order(self, bar, quantity=None, dollar=None):
        date, price = self.return_date_price(bar)
        if quantity is None:
            quantity = int(dollar / price)
        self.capital = self.capital + quantity * price * (1 - self.transaction_cost)
        self.quantity = self.quantity - quantity
        self.trades = self.trades + 1
        if self.verbose:
            print("Sold {} shares of {} at {:0.1f} per share worth {:0.1f} $".format(
                quantity, self.symbol, price, quantity * price))
            self.realised_balance(bar)
            self.unrealised_balance(bar)
            self.total_balance(bar)
```

### Close the final position (slide 30)
- As shown in the slide, final liquidation omits transaction costs and increments the trade count even if already flat; summary output is conditional on `verbose`.

```python
    def last_trade(self, bar):
        date, price = self.return_date_price(bar)
        last_quantity = self.quantity
        self.capital = self.capital + self.quantity * price
        self.quantity = 0
        self.trades = self.trades + 1
        if self.verbose:
            print("Closed open trades for {} shares of {} at {:0.1f} per share worth {:0.1f} $".format(
                last_quantity, self.symbol, price, last_quantity * price))
            self.total_balance(bar)
            returns = (self.capital - self.initial_capital) / self.initial_capital * 100
            print("The total capital at end of strategy: {:0.1f}".format(self.capital))
            print("The strategy returns on investment are {:0.1f} %".format(returns))
            print("Total trades by strategy {:0.1f}".format(self.trades))
```

### Check the base class (slide 31)

```python
if __name__ == "__main__":
    A = Common_Class("AAPL", "2015-01-01", "2022-07-01", "1d", 10000, 0.0, True)
    A.close_graph()
```

### Strategy: long and short orders (slide 32)
- **Slide correction:** covering a short requires buying `-self.quantity` (a positive amount); the slide incorrectly passes the negative holding directly.

```python
class MA_Strategy(Common_Class):
    def go_long(self, bar, quantity=None, dollar=None):
        if self.position == -1:
            self.buy_order(bar, quantity=-self.quantity)  # Corrected sign: cover short.
        if quantity:
            self.buy_order(bar, quantity=quantity)
        elif dollar:
            if dollar == "all":
                dollar = self.capital
            self.buy_order(bar, dollar=dollar)

    def go_short(self, bar, quantity=None, dollar=None):
        if self.position == 1:
            self.sell_order(bar, quantity=self.quantity)  # Close existing long.
        if quantity:
            self.sell_order(bar, quantity=quantity)
        elif dollar:
            if dollar == "all":
                dollar = self.capital
            self.sell_order(bar, dollar=dollar)
```

### Strategy: moving-average rules (slide 33)
- Add `run_strategy()` inside `MA_Strategy`: STMA = short-term MA; LTMA = long-term MA.
- Signals use the current close and execute at that same close: an idealised fill assumption. Shorting also omits margin and borrowing costs.

```python
    def run_strategy(self, STMA_window, LTMA_window):
        self.position = 0
        self.trades = 0
        self.capital = self.initial_capital

        indicator_1 = SMAIndicator(
            close=self.data["Close_Price"], window=STMA_window, fillna=False
        )
        STMA = indicator_1.sma_indicator()
        indicator_2 = SMAIndicator(
            close=self.data["Close_Price"], window=LTMA_window, fillna=False
        )
        LTMA = indicator_2.sma_indicator()
        self.data["STMA"] = STMA
        self.data["LTMA"] = LTMA
		
		# read this
        for bar in range(LTMA_window, len(self.data)):
            if self.position in [0, -1]:
                if self.data["STMA"].iloc[bar] > self.data["LTMA"].iloc[bar]:
                    self.go_long(bar, dollar="all")
                    self.position = 1
                    print("--------")

            if self.position in [0, 1]:
                if self.data["STMA"].iloc[bar] < self.data["LTMA"].iloc[bar]:
                    self.go_short(bar, dollar="all")
                    self.position = -1
                    print("--------")
        print("--------")
        self.last_trade(bar)


if __name__ == "__main__":
    A = MA_Strategy("AAPL", "2010-04-10", "2022-07-01", "1d", 10000, 0.01, True)
    A.run_strategy(50, 200)
```


![[Screenshot 2026-10-27 at 2.08.25 PM.png]]




