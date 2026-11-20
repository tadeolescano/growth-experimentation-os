# Results readout: EXP-014 Postcode lookup on mobile checkout (fictional)

> Dates run: 3 full weeks · Decision: ship

## TL;DR

Postcode lookup raised the mobile order rate by 13.4% relative (95% CI +0.15 to +0.67 points), with no increase in invalid addresses. Shipping to all mobile users; worth roughly 500 extra orders per month.

## Result

| Metric | Control | Variant | Lift (relative) | 95% CI (absolute) | p-value | Verdict |
|---|---|---|---|---|---|---|
| Primary: mobile order rate | 3.09% (1,120 / 36,200) | 3.51% (1,268 / 36,150) | +13.4% | +0.15 to +0.67 pts | 0.002 | Win |
| Guardrail: invalid address share | 2.1% of orders | 1.6% of orders | -24% | n/a (directional) | n/a | Held |
| Secondary: address step completion | 59% | 78% | +32% | | | Supports mechanism |

Sample reached: 36,200 / 36,150 per variant (planned 36,050). Sample ratio check: pass.

```bash
python3 scripts/abtest.py test --control 1120 36200 --variant 1268 36150
```

## What happened during the test

One evening outage of the address provider (40 minutes); variant fell back to manual entry as designed. No pricing or campaign changes.

## Business implication

- Expected impact: about 500 extra mobile orders per month (126,000 eligible users x 0.41 pts) at current traffic.
- Cost: address lookup fees, small relative to margin per order.
- Decision: ship to 100% of mobile users. Desktop test scheduled as EXP-019.

## Learning

The biggest activation leak was technical friction, not motivation. This raises confidence on other friction items (EXP-015 install date) and suggests checking the same data-matching problem in the moving-home journey.
