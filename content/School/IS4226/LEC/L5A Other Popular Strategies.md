---
class: note
tags:
  - y4s1
  - finance/trading
source:
related:
  - "[[L4 Trading Strategies and Systems]]"
author:
date: 2026-09-22
updated: 2026-09-22 18:14:50
aliases:
---
## Other Popular Strategies
- pairs trading 
	- disturbed correlation between pairs
- arbitrage
	- inefficiencies in amrkets
- grid trading
	- prices fluctuate in range
- candlesticks patterns 
	- trading sentiment 

## Statistical Arbitrage / Pairs Trading
![[Screenshot 2026-09-22 at 3.50.16 PM.png|375]]
- correlated pairs tend to move in tandem 
- find opportunities if the deviation occurs
- $x = \text{Difference of returns}$
- $z = (x-\mu) / \sigma$
#### Example:
![[Screenshot 2026-09-22 at 3.56.23 PM.png]]
- At $t=0$, highly correlated stocks A and B move in tandem and maintain a roughly constant spread, $x$.
- At $t=1$, A rises while B falls, causing the spread to widen to $x'$. 
	- This temporary deviation is the potential trading opportunity, provided the relationship has not changed fundamentally.
- The spread can return to normal in three ways:
	- A continues rising while B rises faster to catch up.
	- B continues falling while A falls faster to catch up.
	- A falls and B rises, so both positions converge toward each other.
![[Screenshot 2026-09-22 at 4.00.35 PM.png]]
- Track the spread over time and standardise it using the z-score, $z = \frac{x-\mu}{\sigma}$, which measures how many standard deviations the current spread is from its mean.
- A large absolute z-score indicates a larger deviation and hence a stronger potential mean-reversion opportunity.
- When A is unusually high relative to B, short A and long B simultaneously; this avoids taking a naked directional position.
	![[Pasted image 20260922160225.png|292]]
- Convergence does not require both trades to be profitable: the gain on the stock moving more strongly toward convergence should exceed the loss on the other position.
- The strategy fails if the stocks have diverged for fundamental reasons rather than because of a temporary market inefficiency.

## Arbitrage
![[Screenshot 2026-09-22 at 4.04.27 PM.png]]
- buy at cheaper exchange and sell at expensive exchange

## Grid Trading
![[Screenshot 2026-09-22 at 4.32.15 PM.png|376]]
- place both "buy" and "sell" orders in a range

![[Screenshot 2026-09-22 at 4.36.51 PM.png]]
- Grid trading is suited to range-bound, [[L4 Trading Strategies and Systems#Mean Reversion or Momentum|mean-reverting]] instruments such as forex pairs: although prices are volatile, they tend to return to a recurring range.
- Place several sell limit orders above the current price ($S_1,S_2,\ldots$) and several buy limit orders below it ($B_1,B_2,\ldots$).
	- This is not a directional or momentum bet: the trader does not predict whether price will first rise or fall, only that it will continue oscillating within the range.
- The grid boundaries can be informed by the probability bands from [[L3A Risk and Returns#Projections|return projections]] (e.g. the expected 68% or 95% price range).
- As price fluctuates through the grid, the orders are filled at different levels, repeatedly **selling high and buying low**.
- The key risk is a sustained breakout: if price keeps rising after the sell orders execute, or keeps falling after the buy orders execute, it may never return to fill the opposite side profitably.
	- Manage this risk by allocating only part of the capital to grid trading and diversifying with a trend-following strategy, which may profit when the range breaks into strong momentum.
- Once a grid has completed, or price has moved to a new area, rebalance and reset a new grid around the prevailing range with appropriate risk limits.

## Candlestick Patterns
![[Screenshot 2026-09-22 at 4.40.50 PM.png|169]]
- **Bullish** candlestick patterns
	- hammer
	- inverted hammer
	- bullish engulfing
	- morning star
	- piercing line
	- three white soldiers
- *Bearish* candlestick patterns
	- shooting star
	- hanging man
	- bearish engulfing
	- evening star
	- dark cloud cover
	- three black crows
- others:
	- doji
	- spinning top
	- rising three methods
	- falling three methods
	- bullish harami
	- bearish harami

![[Screenshot 2026-09-22 at 4.43.00 PM.png]]
- The candlestick body, determined by the open and close, helps reveal trader sentiment. Its size indicates the strength of buying or selling pressure.
- A candlestick should not usually be interpreted alone. Read it in the context of the preceding trend and wait for the following candle when confirmation is needed.
- In the example, price has been moving upward before a doji appears. The doji has approximately equal open and close prices, so its body is very small.
	- The doji represents **market indecision**, not an automatic reversal signal.
	- Wait for the next candle to clarify the market's direction:
		- a bullish candle suggests a bullish move or continuation;
		- a bearish candle suggests a possible bearish move or reversal.
- Confirm candlestick signals using the broader trend, technical indicators, or relevant fundamental information before making a trading decision.
