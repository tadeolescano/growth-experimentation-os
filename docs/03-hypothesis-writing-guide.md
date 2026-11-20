# Hypothesis writing guide

A good hypothesis makes a risky prediction that the data can prove wrong, and says why you expect it. A bad hypothesis is a task with a question mark.

## Format

> **Because** we observed [evidence],
> **we believe** that [change] for [audience]
> **will** [move metric] by [expected size]
> **because** [mechanism: the behavioural reason].
> **We will know** when [primary metric] changes by at least [MDE] at [confidence], without [guardrail] getting worse.

## Example

**Weak:** "Test a new checkout page."

**Strong:** Because 41% of mobile users who reach the address step abandon there, and recordings show repeated failed lookups, we believe that replacing free-text address entry with postcode lookup for mobile users will increase checkout completion by 8 to 12% relative, because it removes the step where users fail and give up. We will know when mobile checkout completion rises by at least 6% relative at 95% confidence, without the share of orders with invalid addresses increasing.

## Checklist

- [ ] Grounded in a specific observation (data point, recording, quote), not an opinion
- [ ] One change, so the result can be attributed
- [ ] Named audience or segment
- [ ] Mechanism stated (friction, clarity, motivation, trust, anchoring, loss aversion, social proof)
- [ ] Primary metric is the closest one to the change that still matters to the business
- [ ] Guardrail metric named
- [ ] Expected effect size written down before launch (this is what makes the prediction risky)
- [ ] Decision stated: what we do if it wins, loses or is inconclusive

## Common mistakes

| Mistake | Why it hurts | Fix |
|---|---|---|
| Several changes in one variant | You cannot tell what worked | Split, or call it a redesign test and accept the trade-off |
| Metric too far from the change | Effect is diluted, test never reaches significance | Use the nearest meaningful metric, keep revenue as a guardrail |
| No expected effect size | Any result can be rationalised | Write the MDE before launch |
| Hypothesis written after the result | Turns noise into a story | Brief is locked before launch |
| "Learn more about users" as the goal | Not falsifiable | Do research separately; experiments test predictions |

## Mechanism library

Use these to make the "because" explicit:

- **Friction**: fewer steps, fewer fields, defaults, autofill
- **Clarity**: comparison tables, plain-language plan names, total cost upfront
- **Motivation**: benefit-led headlines, outcome framing
- **Trust**: reviews, guarantees, installation promises, recognisable payment methods
- **Anchoring**: order of plans, reference prices
- **Loss aversion**: framing what the customer keeps or avoids losing
- **Commitment**: small first step before the big ask
- **Timing**: triggers at the moment of hesitation, not on a schedule
