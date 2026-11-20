# growth-experimentation-os

A full-funnel, hypothesis-driven experimentation system: how to find where growth is leaking, turn that into testable hypotheses, decide what to run first, run it with enough statistical discipline to trust the result, and report it in a way that changes decisions.

## The problem

Most growth teams optimise channels in isolation. Paid media tunes CPA, the website team tunes conversion rate, CRM tunes open rates, and nobody owns the customer's journey from first click to the third bill. The result is local wins that do not add up: cheaper leads that never activate, discounts that convert and then churn.

The fix is to treat growth as **one funnel and one backlog**, where every test is grounded in data, written as a falsifiable hypothesis, quantified before it runs and judged on a metric that leadership actually cares about.

## The system

```
 1. ACQUISITION OPTIMISATION     2. ACTIVATION & CONVERSION      3. RETENTION & COHORTS
    channel mix refinement          friction analysis               cohort tracking
    creative testing                offer framing experiments       churn detection
    landing page CRO                behavioural triggers            post-purchase journey
                 \                           |                            /
                  +---- analytics and tag data · cohort and behavioural analysis ----+
                                             |
                       document -> quantify -> prioritise -> report
```

Every experiment goes through the same four steps:

1. **Document**: a written brief with the observation, the hypothesis, the metric and the decision it will drive.
2. **Quantify**: baseline, minimum detectable effect, sample size and expected value, before anything is built.
3. **Prioritise**: impact versus effort (or ICE) across the whole funnel, not per team.
4. **Report**: a readout to stakeholders with the result, the confidence and the business implication.

Programmes it covers: A/B and multivariate testing, funnel diagnostics, offer positioning tests and messaging validation experiments.

## Structure

```
docs/
  01-full-funnel-system-map.md         mermaid map of stages, metrics and levers
  02-funnel-diagnostic-checklist.md    where is the leak, step by step
  03-hypothesis-writing-guide.md       observation -> hypothesis -> prediction
  04-prioritization-ice-impact-effort.md  ICE and impact/effort, with calibration
  05-experiment-lifecycle.md           document, quantify, prioritise, report
  06-cohort-and-churn-analysis.md      cohort tables, churn signals, retention tests
  07-messaging-and-offer-test-protocol.md  how to test words and offers safely
templates/
  experiment-brief.md
  results-readout.md
  experiment-backlog.csv
scripts/
  abtest.py                            two-proportion significance and sample-size calculator
tests/
  test_abtest.py
examples/
  parallel-fibre/                      a fictional UK broadband provider
```

## How to use it

1. Map your funnel with `docs/01-full-funnel-system-map.md` and pull one baseline number per stage.
2. Run the diagnostic in `docs/02-funnel-diagnostic-checklist.md` to find the two or three biggest leaks.
3. Write hypotheses for those leaks with `docs/03-hypothesis-writing-guide.md` and log them in `templates/experiment-backlog.csv`.
4. Size each candidate with the calculator, then score and rank the backlog with `docs/04-prioritization-ice-impact-effort.md`.
5. For each test you run, fill `templates/experiment-brief.md` before launch and `templates/results-readout.md` after.
6. Review the backlog weekly; review cohorts monthly (`docs/06-cohort-and-churn-analysis.md`).

### The calculator

Python 3.8+, standard library only.

```bash
# Is the difference significant?
python3 scripts/abtest.py test --control 480 10000 --variant 552 10000

# How many users per variant do I need to detect a 10% relative lift on a 4.8% baseline?
python3 scripts/abtest.py size --baseline 0.048 --mde 0.10

# How long will that take with 6,000 eligible users a day, split 50/50?
python3 scripts/abtest.py size --baseline 0.048 --mde 0.10 --daily-traffic 6000

# Run the tests
python3 -m unittest discover -s tests
```

## What it is not

- **Not an experimentation platform.** It works with whatever tool splits your traffic.
- **Not a substitute for judgement.** A significant result on the wrong metric is still the wrong decision.
- **Not only for websites.** The same lifecycle applies to sales scripts, onboarding calls, pricing pages and retention offers.

## Case note

Designed for a UK telecom challenger brand: a high-consideration, price-sensitive market with long decision cycles and high CAC pressure, where growth had to come from the whole funnel rather than from cheaper clicks.

All numbers and company names in this repository are illustrative.

## License

MIT, see [LICENSE](LICENSE).

---

Built by [Tadeo Lescano](https://www.linkedin.com/in/tadeo-lescano/), GTM Engineer & Growth Marketer. More at [github.com/tadeolescano](https://github.com/tadeolescano).
