# Cohort and churn analysis outline

Acquisition tests are judged in days; retention is judged in months. Cohorts are how you connect the two and avoid buying customers who leave.

## 1. Build the cohort table

- **Cohort**: customers grouped by the month they activated (first bill, first install, first order).
- **Columns**: months since activation (M0, M1, M2 ...).
- **Values**: share still active (logo retention) and share of starting revenue still billed (revenue retention).

| Cohort | Size | M1 | M2 | M3 | M6 | M12 |
|---|---|---|---|---|---|---|
| Jan | | | | | | |
| Feb | | | | | | |

Add the same table split by acquisition channel, plan, offer and region. Differences between these splits are where the hypotheses come from.

## 2. Read it

- **Shape of the curve**: a steep early drop then flat means an onboarding or expectation problem; a steady decline means an ongoing value problem.
- **Cohort over cohort**: are newer cohorts retaining better or worse at the same age? If worse, check what changed in acquisition (channel, offer, audience) at that time.
- **Channel quality**: compare M3 retention by channel; adjust CAC targets by channel to reflect lifetime value, not just first-order cost.
- **Offer quality**: discount-led cohorts often convert better and churn earlier. Measure margin per customer at M12, not conversion.

## 3. Churn detection

Define leading signals and check how well each predicts churn in the next 60 days:

| Signal family | Examples |
|---|---|
| Usage | Usage drop versus own baseline, no logins, fewer sessions |
| Service | Repeat contact-centre calls, unresolved tickets, installation delays, outages in the area |
| Billing | Failed payments, first bill higher than expected, end of promotional price approaching |
| Intent | Visits to cancellation or contract pages, requests for a final bill or porting codes |

For each signal, report precision (share of flagged customers who churn) and recall (share of churners who were flagged). Act on the signals with the best balance first.

## 4. Retention experiments

| Moment | Example hypothesis |
|---|---|
| Onboarding (first 30 days) | A proactive "what to expect" sequence reduces first-month contacts and M1 churn |
| First bill | Explaining the first bill before it arrives reduces bill-shock contacts and M2 churn |
| Promotion end | A targeted renewal offer two months before price change retains more margin than a reactive save offer |
| At-risk signal | A service recovery message after an outage reduces churn in affected areas |

Use holdout groups for retention tests: keep a random 10 to 20% of eligible customers out of the treatment so you can measure the real incremental effect.

## 5. Reporting cadence

- Monthly: cohort tables updated, newest cohorts compared to the trailing average.
- Quarterly: CAC targets by channel revisited using observed retention.
