# Experiment brief: EXP-014 Postcode lookup on mobile checkout (fictional)

> Owner: web lead · Analyst: growth analyst · Stakeholders: product, contact centre · Funnel stage: activation · Status: approved

## 1. Observation

- 41% of mobile users who reach the address step abandon there, versus 17% on desktop (8-week funnel report).
- 25 session recordings: 19 show repeated failed attempts to type an address that matches the availability record.
- Exit poll at the step: "It kept saying my address was wrong" was the most common free-text answer.

## 2. Hypothesis

Because we observed a 41% mobile abandonment at address entry with repeated failed matches, we believe that replacing free-text entry with postcode lookup and an address picker for mobile users will increase the mobile order rate by 10 to 15% relative, because it removes the step where users fail and give up. We will know when the mobile order rate per passed availability check rises by at least 12% relative at 95% confidence, without the share of orders with invalid addresses increasing.

## 3. Design

| Item | Value |
|---|---|
| Audience | Mobile users who passed the availability check |
| Exclusions | Business customers, existing customers moving home |
| Variants | A: free-text address form / B: postcode lookup + address picker, manual entry as fallback |
| Traffic split | 50 / 50 |
| Randomisation unit | User (first-party ID) |

## 4. Metrics

| Type | Metric |
|---|---|
| Primary | Orders / users who passed the availability check (mobile) |
| Secondary | Address step completion; time on step |
| Guardrail | Share of orders with an address that fails installation validation |

## 5. Quantification

| Item | Value |
|---|---|
| Baseline | 3.1% |
| MDE | 12% relative (3.10% to 3.47%) |
| Sample per variant | 36,050 |
| Eligible traffic | ~4,200 users / day |
| Duration | 18 days, run 3 full weeks |
| Expected value if it wins | ~500 extra orders per month on mobile (126,000 eligible users x 0.37 pts) |

```bash
python3 scripts/abtest.py size --baseline 0.031 --mde 0.12 --daily-traffic 4200
```

## 6. Priority

Impact 8 · Confidence 8 (recordings + exit poll + funnel gap vs desktop) · Ease 6 · ICE 38

## 7. Decision rule

| Outcome | Action |
|---|---|
| Win | Ship to all mobile users; test on desktop as EXP-019 |
| Loss | Investigate lookup failure rate; keep free text |
| Inconclusive | Keep control; revisit after address data provider change |
| Guardrail breached | Stop, investigate matching logic |
