---
tags:
  - y4s1
---

# IS4226 Week 3 Calculation Practice

Use decimal form in working unless stated otherwise. Try each question without looking at its topic label or solution. The formulas follow L3A and L3B; standard deviation is population SD when the question supplies the full population.

## Questions

1. A stock closes at $48 and then $54. Find its simple return and log return.
2. A stock has a log return of −0.12. Find its simple return. If it began at $75, find its ending price.
3. Prices are $100, $110, $99, and $108.90. Find each simple return, the arithmetic mean simple return, and the total holding-period return.
4. An asset returns −8%, 5%, or 18% with probabilities 0.20, 0.50, and 0.30. Find expected return.
5. A portfolio allocates 25% to A, 45% to B, and 30% to C. Their returns are 16%, 4%, and −6%. Find portfolio return.
6. A portfolio allocates 35% to A returning 12% and the rest to B. Overall return is 5.5%. Find B’s return.
7. The complete population of returns is −2%, 0%, 4%, and 6%. Find mean, variance, and population SD.
8. Daily returns are normal with mean 0.15% and SD 1.1%. Give approximate 68%, 95%, and 99.7% daily-return bands.
9. A $250 asset has an expected 10-day return of 0.5% and a 10-day SD of 3%. Give its approximate 95% return and price bands using the lecture’s simple price conversion.
10. Daily mean is 0.03% and daily SD is 1.4%. Find 20-day mean and SD.
11. An equity has daily mean 0.05% and daily SD 1.25%. Annualise both using 252 days.
12. Crypto annualised volatility is 76.45%. Infer daily volatility using 365 days.
13. Fund A returns 11%, Fund B returns 15%, and the risk-free rate is 3%. Their volatilities are 16% and 30%. Calculate both Sharpe ratios and select the better risk-adjusted performance.
14. A portfolio has Sharpe ratio 0.6, return 11%, and risk-free rate 2%. Find its volatility.
15. Covariance between an asset and market is 0.024; market variance is 0.016. Find beta. If market rises 2%, state the beta-only predicted asset move.
16. A portfolio is 20% in beta 1.8, 50% in beta 0.9, and 30% in beta 0.2. Find portfolio beta.
17. A portfolio targets beta 1.0. It holds 40% in beta 1.4 and 60% in asset B. Find B’s required beta.
18. Risk-free rate is 2.5%, expected market return is 8.5%, and beta is 1.3. Find CAPM expected return.
19. An asset actually returns 12.5%; risk-free rate is 2%; market return is 9%; beta is 1.2. Find alpha using full CAPM.
20. Alpha is −1%, actual return is 6%, risk-free rate is 2%, and market return is 10%. Find beta.
21. Two assets have covariance −0.0036 and SDs 6% and 10%. Find correlation and interpret it.
22. Correlation is 0.25 and SDs are 12% and 20%. Find covariance.
23. A stock goes from $40 to $52 over three days. Its first two log returns are 0.08 and 0.12. Find the third log return.
24. A 5-day 68% return band is −2% to 4%. Infer the 5-day mean and SD, then infer daily mean and SD.

## Worked solutions

1. Simple return: \(54/48-1=0.125=12.5\%\). Log return: \(\ln(54/48)=\ln(1.125)=0.1173\), or 11.73% in log-return units.

2. \(R=e^{-0.12}-1=-0.11308=-11.31\%\). Ending price: \(75e^{-0.12}=$66.52\) (equivalently \(75(1-0.11308)\)).

3. Simple returns: \(110/100-1=10\%\); \(99/110-1=-10\%\); \(108.9/99-1=10\%\). Arithmetic mean = \((10-10+10)/3=3.333\%\). Total return = \(108.9/100-1=8.9\%\). Trap: \(3\times3.333\%=10\%\) is not the compound return.

4. \(E[R]=0.2(-0.08)+0.5(0.05)+0.3(0.18)=-0.016+0.025+0.054=0.063=6.3\%\).

5. \(R_p=0.25(0.16)+0.45(0.04)+0.30(-0.06)=0.04+0.018-0.018=0.04=4\%\).

6. \(0.055=0.35(0.12)+0.65R_B\). Thus \(R_B=(0.055-0.042)/0.65=0.02=2\%\).

7. Mean: \((-2+0+4+6)/4=2\%\). Squared deviations in percentage points: 16, 4, 4, 16; variance = \(40/4=10\) percentage-points², or 0.001 in decimal-return units. SD = \(\sqrt{10}=3.162\%\).

8. 68%: \(0.15\%\pm1.1\%=[-0.95\%,1.25\%]\). 95%: \(0.15\%\pm2.2\%=[-2.05\%,2.35\%]\). 99.7%: \(0.15\%\pm3.3\%=[-3.15\%,3.45\%]\).

9. 95% return band: \(0.5\%\pm2(3\%)=[-5.5\%,6.5\%]\). Prices: \(250(0.945)=$236.25\) to \(250(1.065)=$266.25\).

10. \(\mu_{20}=20(0.03\%)=0.6\%\). \(\sigma_{20}=\sqrt{20}(1.4\%)=6.261\%\).

11. Annual mean: \(252(0.05\%)=12.6\%\). Annual SD: \(\sqrt{252}(1.25\%)=19.84\%\).

12. \(\sigma_d=76.45\%/\sqrt{365}=4.00\%\) (approximately).

13. A: \((11-3)/16=0.50\). B: \((15-3)/30=0.40\). Fund A has better risk-adjusted performance despite the lower raw return.

14. \(0.6=(0.11-0.02)/\sigma\), so \(\sigma=0.09/0.6=0.15=15\%\).

15. \(\beta=0.024/0.016=1.5\). A beta-only prediction for a 2% market rise is \(1.5(2\%)=3\%\). This is a sensitivity estimate, not a guaranteed realised return.

16. \(\beta_p=0.2(1.8)+0.5(0.9)+0.3(0.2)=0.36+0.45+0.06=0.87\).

17. \(1.0=0.4(1.4)+0.6\beta_B\). Therefore \(\beta_B=(1-0.56)/0.6=0.7333\).

18. Market risk premium = \(8.5\%-2.5\%=6\%\). CAPM return = \(2.5\%+1.3(6\%)=10.3\%\).

19. CAPM benchmark = \(2\%+1.2(9\%-2\%)=10.4\%\). Alpha = \(12.5\%-10.4\%=2.1\%\).

20. \(-1\%=6\%-[2\%+\beta(10\%-2\%)]\). Hence \(7\%=2\%+8\%\beta\), so \(\beta=5/8=0.625\).

21. \(\rho=-0.0036/(0.06\times0.10)=-0.6\). The assets have a moderately strong negative linear relationship, which may provide diversification benefit.

22. \(\operatorname{Cov}=\rho\sigma_x\sigma_y=0.25(0.12)(0.20)=0.006\).

23. Total log return = \(\ln(52/40)=\ln(1.3)=0.262364\). Third log return = \(0.262364-0.08-0.12=0.062364\). Its corresponding simple return is \(e^{0.062364}-1\approx6.44\%\).

24. The midpoint gives \(\mu_5=1\%\); half-width gives \(\sigma_5=3\%\). Daily mean: \(\mu_d=1\%/5=0.2\%\). Daily SD: \(\sigma_d=3\%/\sqrt5=1.342\%\).

## Formula selection checklist

- Prices at two times → simple or log return.
- Mutually exclusive states with probabilities → expected return.
- Portfolio allocations → weighted return or weighted beta.
- Raw observations → mean, squared deviations, variance, SD.
- Time-horizon conversion → mean × \(N\), volatility × \(\sqrt N\).
- Excess return per unit of total volatility → Sharpe ratio.
- Covariance with the market divided by market variance → beta.
- Required/benchmark return from market risk → CAPM.
- Actual return minus CAPM benchmark → alpha.
- Standardised co-movement → correlation.

## Assumption and error checklist

- Convert percentages to decimals consistently.
- Do not add simple returns across time; compound them or add log returns.
- Do not call arithmetic mean return the compound growth rate.
- Use \(N\), not \(N-1\), when the question follows the lecture’s population-SD formula.
- Scale variance by \(N\), so SD scales by \(\sqrt N\), under the independence assumption.
- Use 252 for equities and 365 for crypto unless the question specifies otherwise.
- Subtract \(R_f\) in Sharpe and full CAPM alpha unless it is explicitly zero.
- Beta measures benchmark sensitivity/systematic risk, not total volatility.
- Correlation is unitless and bounded by −1 and +1; covariance is not.
- Correlation does not establish causation.
