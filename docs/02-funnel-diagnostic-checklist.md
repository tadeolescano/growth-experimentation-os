# Funnel diagnostic checklist

Run this before writing a single hypothesis. The goal is to find the two or three places where a fixed amount of effort will move the most customers.

## 0. Data you can trust

- [ ] One definition per funnel event, written down (what counts as a lead, an order, an activation)
- [ ] Event tracking verified end to end on desktop and mobile in the last 30 days
- [ ] Order counts in analytics reconcile with the billing system within 5%
- [ ] Bot and internal traffic filtered
- [ ] Consent mode impact estimated, so you know what share of users is invisible

## 1. Stage-by-stage conversion

Build a table with one row per step and the last 8 to 12 weeks of data.

| Step | Users | Rate from previous | Benchmark or target | Gap |
|---|---|---|---|---|
| Landing | | | | |
| Product or plan view | | | | |
| Eligibility or availability check | | | | |
| Checkout start | | | | |
| Checkout complete | | | | |
| Activated (first value delivered) | | | | |
| Retained month 3 | | | | |

- [ ] Biggest absolute drop identified (users lost, not just lowest rate)
- [ ] Biggest gap versus benchmark identified

## 2. Segment the leak

For the top two drops, split by:

- [ ] Device and browser
- [ ] Channel and campaign
- [ ] New vs returning
- [ ] Geography or eligibility area
- [ ] Plan or product chosen
- [ ] Time of day and day of week

A leak concentrated in one segment is usually a bug or a mismatch; a leak spread evenly is usually a value or clarity problem.

## 3. Qualitative evidence

- [ ] Session recordings for 20 to 30 drop-offs at the leaking step
- [ ] Form analytics: which field causes abandonment or errors
- [ ] On-page poll or exit survey at the step ("What stopped you today?")
- [ ] Contact-centre and chat transcripts tagged for the step
- [ ] Five to eight customer or prospect interviews

## 4. Classify each leak

| Type | Signal | Typical fix |
|---|---|---|
| Technical | Errors, slow load, one browser or device far worse | Fix, do not test |
| Friction | Many fields, unclear steps, forced account creation | Simplify and test |
| Clarity | Users bounce between plans, ask the same questions | Copy, comparison, information architecture |
| Value or trust | Users understand but do not commit | Offer framing, proof, guarantees |
| Expectation mismatch | Ad promise differs from page | Message match across channel and page |

## 5. Output

- [ ] Top three leaks, each with size (users lost per month), type and evidence
- [ ] Two or more hypotheses per leak logged in the backlog
- [ ] Anything technical sent straight to engineering as a fix, not an experiment
