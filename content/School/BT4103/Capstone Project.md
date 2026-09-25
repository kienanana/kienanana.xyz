---
class: project
tags:
  - y4s1
source:
related:
  - "[[BT4103]]"
author:
date: 2026-08-20
updated: 2026-09-11
aliases:
  - CFTC Positioning Nowcast
---
# BT4103 Business Analytics Capstone Project Proposal
*Industry Partner: Dymon Asia*

## Latest Sponsor Direction
- Start with **FX**, then expand to **fixed income (FI) and commodities** later. The cross-asset proposal below describes the broader ambition; FX is the initial scope.
- Initial workstreams, as relayed from the discussion with Dymon:
  1. “pull CFTC pipeline query” — begin with the CFTC data pipeline for FX; clarify whether Dymon has an existing query/pipeline to use.
  2. “Survey Positioning data provided by Dymon” — work with the survey positioning data supplied by Dymon; its format, coverage, frequency and intended role still need clarification.
- Open questions: Which FX markets should be included first? How should the survey data be used alongside CFTC positioning (comparison, model input, or validation)?

## Part 1: Project Information
### Project Name
CFTC Positioning Nowcast and Price-Action Crowding Dashboard
### Project Description
- Develop a cross-asset analytics platform that combines weekly CFTC Commitments of Traders data with daily price action to estimate how speculative positioning evolves between official releases.
- Create a standardized data pipeline across FX, rates, equity indices, energy, metals and agricultural futures, mapping relevant participant categories such as Managed Money and Leveraged Funds.
- Engineer features from returns, momentum, volume, open interest, volatility, futures-curve structure and cross-asset macro variables; compare regularized regression and tree-based models using time-series cross-validation.
- Produce interpretable positioning and crowding indicators, including historical percentile/z-score, new-long versus short-covering classification, long-liquidation versus new-short classification, price-positioning divergence and squeeze/reversal-risk scores.
- The platform will be a research and decision-support tool, not an autonomous trading or execution system.
### Total Workload
Approximately 16 hours per week per student for 12 weeks (team of 3-5 students).
### Project Data Sources
Public CFTC historical Commitments of Traders data; Price/Volume per instrument yfinance api.
### Platform and Tools
Python (pandas, NumPy, scikit-learn, statsmodels, XGBoost/LightGBM, SHAP), SQL, Git, Jupyter, and Streamlit or Power BI for dashboard development.

### Project Deliverables
- Automated and reusable data ingestion, cleaning and contract-mapping pipeline.
- Validated positioning-nowcast models with walk-forward testing, confidence ranges and feature interpretation.
- Interactive cross-asset dashboard showing reported positions, estimated current positions, crowding scores, divergences and regime classifications.
- Reusable codebase, technical documentation, model evaluation report and final presentation.

## Reference Repositories
- [CFTC COT Viewer](https://github.com/proprietary/cftc-cot-viewer) — Dashboard reference for net positioning, open-interest normalization, z-scores and historical percentiles.
- [cot_reports](https://github.com/NDelventhal/cot_reports) — Python data-ingestion reference for downloading historical CFTC reports into pandas DataFrames, including Traders in Financial Futures (TFF) reports for the FX workstream.

## Definitions
- **CFTC (Commodity Futures Trading Commission):** The US regulator that publishes the market-position data used by this project.
- **Commitments of Traders (COT) data:** A weekly CFTC snapshot of the futures positions held by different categories of traders.
- **Futures:** Exchange-traded contracts tied to the future price of an asset, such as a currency, stock index, oil, or gold.
- **Contract mapping:** Matching instrument identifiers and expiring futures contracts to the correct market and CFTC series.
- **Cross-asset:** Covering multiple types of markets instead of only one.
- **FX:** Foreign-exchange or currency markets.
- **Rates:** Interest-rate markets, including government-bond and short-term interest-rate futures.
- **Equity indices:** Measurements of groups of stocks, such as the S&P 500.
- **Price action:** How a market's price moves over time.
- **Position / positioning:** A trader's market exposure and whether it benefits from prices rising or falling.
- **Speculative positioning:** Positions intended mainly to profit from price movements rather than to reduce an existing business risk.
- **Nowcast:** An estimate of the current state when the official data arrives late. Here, it means estimating positioning between weekly COT releases.
- **Managed Money:** A CFTC trader category generally covering professional money managers in commodity futures.
- **Leveraged Funds:** A CFTC category generally covering hedge funds and similar leveraged managers in financial futures.
- **Return:** The percentage change in an asset's price over a period.
- **Momentum:** The strength and direction of recent price movement.
- **Volume:** The number of contracts traded during a period.
- **Open interest:** The number of futures contracts that remain open and unsettled.
- **Volatility:** The size and variability of price movements.
- **Futures-curve structure:** The relationship between prices of futures on the same asset with different expiry dates.
- **Cross-asset macro variables:** Wider economic or market indicators—such as interest rates or the US dollar—used to help explain another asset's positioning.
- **Regularized regression:** A regression model penalized for unnecessary complexity, helping it generalize beyond its training data.
- **Tree-based model:** A model that learns decision rules from the data and can capture nonlinear relationships. XGBoost and LightGBM are examples.
- **Time-series cross-validation:** Testing a model on later periods after training it only on earlier periods, so future information cannot leak into the past.
- **Historical percentile:** The percentage of past observations below the current value; the 95th percentile is higher than about 95% of past values.
- **Z-score:** How many standard deviations a value is above or below its historical average.
- **New long:** Traders opening positions that benefit from rising prices.
- **Short covering:** Traders buying to close positions that benefited from falling prices.
- **Long liquidation:** Traders selling to close positions that benefited from rising prices.
- **New short:** Traders opening positions that benefit from falling prices.
- **Price-positioning divergence:** Price and positioning moving in conflicting directions.
- **Crowding:** An unusually large concentration of traders positioned in the same direction.
- **Squeeze risk:** The risk of a rapid move caused by many losing traders exiting similar positions at once.
- **Reversal risk:** The risk that the current price trend changes direction.
- **Autonomous trading or execution system:** Software that independently decides and places trades; this project explicitly is not one.

