import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import abtest  # noqa: E402


class TwoProportionTest(unittest.TestCase):
    def test_known_significant_result(self):
        r = abtest.two_proportion_test(480, 10000, 552, 10000)
        self.assertAlmostEqual(r["rate_control"], 0.048)
        self.assertAlmostEqual(r["rate_variant"], 0.0552)
        self.assertAlmostEqual(r["rel_lift"], 0.15, places=6)
        self.assertAlmostEqual(r["z"], 2.300, places=2)
        self.assertAlmostEqual(r["p_value"], 0.0214, places=3)
        self.assertTrue(r["significant"])
        lo, hi = r["ci_abs"]
        self.assertGreater(lo, 0)
        self.assertLess(lo, r["abs_lift"])
        self.assertGreater(hi, r["abs_lift"])

    def test_not_significant(self):
        r = abtest.two_proportion_test(100, 2000, 108, 2000)
        self.assertFalse(r["significant"])
        lo, hi = r["ci_abs"]
        self.assertLess(lo, 0)
        self.assertGreater(hi, 0)

    def test_identical_arms(self):
        r = abtest.two_proportion_test(50, 1000, 50, 1000)
        self.assertEqual(r["z"], 0)
        self.assertAlmostEqual(r["p_value"], 1.0)

    def test_zero_conversions_both(self):
        r = abtest.two_proportion_test(0, 500, 0, 500)
        self.assertEqual(r["p_value"], 1.0)
        self.assertFalse(r["significant"])

    def test_one_sided_halves_p(self):
        two = abtest.two_proportion_test(480, 10000, 552, 10000)["p_value"]
        one = abtest.two_proportion_test(480, 10000, 552, 10000, two_sided=False)["p_value"]
        self.assertAlmostEqual(one, two / 2, places=6)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            abtest.two_proportion_test(10, 0, 5, 100)
        with self.assertRaises(ValueError):
            abtest.two_proportion_test(200, 100, 5, 100)


class SampleSize(unittest.TestCase):
    def test_textbook_value(self):
        # 10% -> 12% (20% relative), alpha 0.05 two-sided, power 0.8: ~3,841 per arm
        n = abtest.sample_size_per_variant(0.10, 0.20)
        self.assertTrue(3800 <= n <= 3900, n)

    def test_absolute_equals_relative(self):
        rel = abtest.sample_size_per_variant(0.10, 0.20)
        ab = abtest.sample_size_per_variant(0.10, 0.02, relative=False)
        self.assertEqual(rel, ab)

    def test_smaller_mde_needs_more(self):
        self.assertGreater(abtest.sample_size_per_variant(0.05, 0.05),
                           abtest.sample_size_per_variant(0.05, 0.10))

    def test_more_power_needs_more(self):
        self.assertGreater(abtest.sample_size_per_variant(0.05, 0.10, power=0.9),
                           abtest.sample_size_per_variant(0.05, 0.10, power=0.8))

    def test_more_variants_needs_more_per_arm(self):
        self.assertGreater(abtest.sample_size_per_variant(0.05, 0.10, variants=3),
                           abtest.sample_size_per_variant(0.05, 0.10, variants=2))

    def test_invalid(self):
        for kwargs in ({"baseline": 0, "mde": 0.1}, {"baseline": 0.5, "mde": -0.1},
                       {"baseline": 0.9, "mde": 0.2}, {"baseline": 0.1, "mde": 0.1, "variants": 1}):
            with self.assertRaises(ValueError):
                abtest.sample_size_per_variant(**kwargs)


class Cli(unittest.TestCase):
    def test_cli_runs(self):
        self.assertEqual(abtest.main(["test", "--control", "480", "10000", "--variant", "552", "10000"]), 0)
        self.assertEqual(abtest.main(["size", "--baseline", "0.048", "--mde", "0.1", "--daily-traffic", "6000"]), 0)

    def test_cli_error_code(self):
        self.assertEqual(abtest.main(["size", "--baseline", "1.5", "--mde", "0.1"]), 2)


if __name__ == "__main__":
    unittest.main()
