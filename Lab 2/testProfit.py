import unittest
from profit import profit


class TestProfit(unittest.TestCase):
    def test_example_a(self):
        ip = {"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}
        self.assertAlmostEqual(profit(ip), 14796)

    def test_example_b(self):
        ip = {"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}
        self.assertAlmostEqual(profit(ip), 32411)

    def test_example_c(self):
        ip = {"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}
        self.assertAlmostEqual(profit(ip), 44030)

    def test_missing_cost(self):
        with self.assertRaises(Exception):
            profit({"sell_price": 7.95, "inventory": 85001})

    def test_missing_sell(self):
        with self.assertRaises(Exception):
            profit({"cost_price": 2.77, "inventory": 85001})

    def test_missing_inventory(self):
        with self.assertRaises(Exception):
            profit({"cost_price": 2.77, "sell_price": 7.95})

    def test_negative_cost(self):
        ip = {"cost_price": -225.89, "sell_price": 550.00, "inventory": 100}
        with self.assertRaises(Exception):
            profit(ip)

    def test_negative_sell(self):
        ip = {"cost_price": 225.89, "sell_price": -550.00, "inventory": 100}
        with self.assertRaises(Exception):
            profit(ip)

    def test_negative_inventory(self):
        ip = {"cost_price": 225.89, "sell_price": 550.00, "inventory": -100}
        with self.assertRaises(Exception):
            profit(ip)

    def test_empty_dict(self):
        with self.assertRaises(Exception):
            profit({})
