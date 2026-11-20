#!/usr/bin/env python3
"""Two-proportion significance test and sample-size calculator for A/B tests.

Standard library only (Python 3.8+).

Examples:
    python3 abtest.py test --control 480 10000 --variant 552 10000
    python3 abtest.py size --baseline 0.048 --mde 0.10
    python3 abtest.py size --baseline 0.048 --mde 0.10 --absolute
    python3 abtest.py size --baseline 0.048 --mde 0.10 --daily-traffic 6000 --variants 2
"""

import argparse
import math
import sys
from statistics import NormalDist

_N = NormalDist()


def _z(p):
    return _N.inv_cdf(p)


def two_proportion_test(conv_a, n_a, conv_b, n_b, alpha=0.05, two_sided=True):
    """Pooled two-proportion z-test of B against A.

    Returns a dict with rates, absolute and relative lift, z, p-value,
    a confidence interval for the absolute difference (unpooled SE) and
    a significance flag.
    """
    for conv, n, name in ((conv_a, n_a, "control"), (conv_b, n_b, "variant")):
        if n <= 0:
            raise ValueError(f"{name}: sample size must be positive")
        if conv < 0 or conv > n:
            raise ValueError(f"{name}: conversions must be between 0 and n")

    p_a = conv_a / n_a
    p_b = conv_b / n_b
    diff = p_b - p_a

    pooled = (conv_a + conv_b) / (n_a + n_b)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
    if se_pooled == 0:
        z = 0.0
        p_value = 1.0
    else:
        z = diff / se_pooled
        if two_sided:
            p_value = 2 * (1 - _N.cdf(abs(z)))
        else:
            p_value = 1 - _N.cdf(z)

    se_unpooled = math.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
    z_crit = _z(1 - alpha / 2) if two_sided else _z(1 - alpha)
    ci = (diff - z_crit * se_unpooled, diff + z_crit * se_unpooled)

    return {
        "rate_control": p_a,
        "rate_variant": p_b,
        "abs_lift": diff,
        "rel_lift": (diff / p_a) if p_a > 0 else float("nan"),
        "z": z,
        "p_value": p_value,
        "ci_abs": ci,
        "confidence": 1 - alpha,
        "significant": p_value < alpha,
    }


def sample_size_per_variant(baseline, mde, relative=True, alpha=0.05, power=0.8,
                            two_sided=True, variants=2):
    """Users needed per variant to detect `mde` on `baseline`.

    `mde` is relative (0.10 = +10%) unless relative=False, in which case it is
    an absolute change in rate (0.005 = +0.5 points). With more than two
    variants, alpha is Bonferroni-corrected across the comparisons with control.
    """
    if not 0 < baseline < 1:
        raise ValueError("baseline must be between 0 and 1")
    if mde <= 0:
        raise ValueError("mde must be positive")
    if variants < 2:
        raise ValueError("variants must be at least 2 (control + 1)")
    p1 = baseline
    p2 = baseline * (1 + mde) if relative else baseline + mde
    if not 0 < p2 < 1:
        raise ValueError("baseline plus mde must stay between 0 and 1")

    comparisons = variants - 1
    a = alpha / comparisons
    z_a = _z(1 - a / 2) if two_sided else _z(1 - a)
    z_b = _z(power)
    p_bar = (p1 + p2) / 2
    numerator = (z_a * math.sqrt(2 * p_bar * (1 - p_bar))
                 + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(numerator / (p2 - p1) ** 2)


def _pct(x, digits=2):
    return f"{x * 100:.{digits}f}%"


def _cmd_test(args):
    r = two_proportion_test(args.control[0], args.control[1],
                            args.variant[0], args.variant[1],
                            alpha=args.alpha, two_sided=not args.one_sided)
    lo, hi = r["ci_abs"]
    print(f"Control rate:   {_pct(r['rate_control'])}  ({args.control[0]}/{args.control[1]})")
    print(f"Variant rate:   {_pct(r['rate_variant'])}  ({args.variant[0]}/{args.variant[1]})")
    print(f"Absolute lift:  {r['abs_lift'] * 100:+.2f} pts")
    print(f"Relative lift:  {r['rel_lift'] * 100:+.1f}%")
    print(f"z = {r['z']:.3f}   p = {r['p_value']:.4f}")
    print(f"{r['confidence'] * 100:.0f}% CI (abs): [{lo * 100:+.2f}, {hi * 100:+.2f}] pts")
    verdict = "SIGNIFICANT" if r["significant"] else "NOT significant"
    print(f"Result: {verdict} at alpha = {args.alpha}")
    return 0


def _cmd_size(args):
    n = sample_size_per_variant(args.baseline, args.mde, relative=not args.absolute,
                                alpha=args.alpha, power=args.power,
                                two_sided=not args.one_sided, variants=args.variants)
    target = args.baseline * (1 + args.mde) if not args.absolute else args.baseline + args.mde
    total = n * args.variants
    print(f"Baseline: {_pct(args.baseline)} -> target {_pct(target)}")
    print(f"Alpha {args.alpha}, power {args.power}, variants {args.variants}")
    print(f"Sample per variant: {n:,}")
    print(f"Total sample:       {total:,}")
    if args.daily_traffic:
        days = math.ceil(total / args.daily_traffic)
        weeks = math.ceil(days / 7)
        print(f"Duration at {args.daily_traffic:,}/day: {days} days (run {weeks} full week(s))")
    return 0


def build_parser():
    p = argparse.ArgumentParser(description="A/B test significance and sample size (stdlib only).")
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("test", help="two-proportion z-test")
    t.add_argument("--control", nargs=2, type=int, required=True, metavar=("CONV", "N"))
    t.add_argument("--variant", nargs=2, type=int, required=True, metavar=("CONV", "N"))
    t.add_argument("--alpha", type=float, default=0.05)
    t.add_argument("--one-sided", action="store_true")
    t.set_defaults(func=_cmd_test)

    s = sub.add_parser("size", help="sample size per variant")
    s.add_argument("--baseline", type=float, required=True, help="baseline rate, e.g. 0.048")
    s.add_argument("--mde", type=float, required=True, help="minimum detectable effect (relative by default)")
    s.add_argument("--absolute", action="store_true", help="treat --mde as an absolute change in rate")
    s.add_argument("--alpha", type=float, default=0.05)
    s.add_argument("--power", type=float, default=0.8)
    s.add_argument("--one-sided", action="store_true")
    s.add_argument("--variants", type=int, default=2, help="total arms including control")
    s.add_argument("--daily-traffic", type=int, default=0, help="eligible users per day across all arms")
    s.set_defaults(func=_cmd_size)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
