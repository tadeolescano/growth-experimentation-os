# Prioritisation: impact vs effort and ICE

One backlog across acquisition, activation and retention, ranked with one method. Two methods are described; pick one and stick with it for at least a quarter so scores are comparable.

## Option A: impact vs effort (2x2)

Fast, visual, good for workshops.

```
            high impact
                 |
   BIG BETS      |    QUICK WINS
   (plan, size   |    (do first)
    carefully)   |
-----------------+-----------------  effort
   MONEY PITS    |    FILL-INS
   (drop)        |    (when idle)
                 |
            low impact
   high effort          low effort
```

Impact is estimated in customers or revenue per month if the hypothesis is right. Effort is estimated in person-days across design, engineering, analytics and approvals.

## Option B: ICE score

Better for a long backlog. Score each item 1 to 10:

| Factor | Question | Anchors |
|---|---|---|
| **Impact** | If it works, how much does the primary business metric move? | 1 = negligible, 5 = noticeable at stage level, 10 = moves company revenue |
| **Confidence** | How strong is the evidence that it will work? | 1 = hunch, 5 = qualitative evidence, 8 = quantitative evidence, 10 = won elsewhere in a similar context |
| **Ease** | How cheap and fast is it to run? | 1 = multi-team, weeks, 5 = one team, a sprint, 10 = config change, a day |

`ICE = (Impact x Confidence x Ease) / 10`

### Make impact less subjective

Translate impact into expected customers per month before scoring:

```
expected_gain = users_reaching_step_per_month x baseline_rate x expected_relative_lift x probability_of_success
```

Then map expected gain to the 1 to 10 scale with fixed bands agreed by the team (for example 1 = under 5 customers per month, 10 = over 500).

### Make confidence honest

Confidence must cite evidence. If the evidence column is empty, confidence is capped at 3.

### Add a feasibility check

Before a test is scheduled, run the sample-size calculator. If the test cannot reach its MDE within four weeks on available traffic, either raise the expected effect (bigger change), move to a higher-traffic step, or drop it.

```bash
python3 scripts/abtest.py size --baseline 0.048 --mde 0.10 --daily-traffic 6000
```

## Calibration

Every quarter, compare predicted ICE with actual outcomes for finished tests:

- If high-confidence tests lose as often as low-confidence ones, the team's confidence scores carry no information. Tighten the evidence rules.
- If ease is consistently underestimated, add a fixed overhead for approvals and QA.
- Track win rate by funnel stage; it tells you where the team understands customers best.

## Tie-breakers

1. The test that unblocks other tests (for example, a tracking fix or a page rebuild).
2. The stage with the biggest absolute leak from the diagnostic.
3. The test with the cheaper failure.
