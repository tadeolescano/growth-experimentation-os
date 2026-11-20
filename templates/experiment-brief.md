# Experiment brief: [EXP-ID] [short name]

> Owner: · Analyst: · Stakeholders: · Funnel stage: acquisition / activation / retention · Status: draft / approved / running
> Locked on: [date]. Nothing below changes after launch.

## 1. Observation

What we saw, with evidence (dashboards, recordings, survey quotes, tickets).

## 2. Hypothesis

Because we observed ___, we believe that ___ for ___ will ___ by ___ because ___.
We will know when ___ changes by at least ___ at ___% confidence, without ___ getting worse.

## 3. Design

| Item | Value |
|---|---|
| Audience | |
| Exclusions | |
| Variants | A (control): / B: |
| Traffic split | 50 / 50 |
| Randomisation unit | user / session / account |
| Touchpoints changed (message match) | |

## 4. Metrics

| Type | Metric | Definition |
|---|---|---|
| Primary | | |
| Secondary | | |
| Guardrail | | |

## 5. Quantification

| Item | Value |
|---|---|
| Baseline (last 4 to 8 weeks) | |
| MDE (relative / absolute) | |
| Alpha / power | 0.05 / 0.80 |
| Sample per variant | |
| Eligible traffic per day | |
| Planned duration (full weeks) | |
| Expected value if it wins (per month) | |

Command used:

```bash
python3 scripts/abtest.py size --baseline ___ --mde ___ --daily-traffic ___
```

## 6. Priority

Impact __ · Confidence __ (evidence: ___) · Ease __ · ICE __

## 7. Decision rule

| Outcome | Action |
|---|---|
| Win (primary significant, guardrails flat) | |
| Loss | |
| Inconclusive | |
| Guardrail breached | Stop early, investigate |

## 8. Risks and QA

- [ ] Variants QA'd on main devices and browsers
- [ ] Tracking verified for every metric above
- [ ] Sample ratio check scheduled after 24 hours
- [ ] Contact-centre and sales briefed (if customer-facing copy or offer changes)
