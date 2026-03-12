import unittest
from swarmpulse.telemetry import calculate_cost

class TestTelemetry(unittest.TestCase):
    def test_cost_calculation(self):
        cost = calculate_cost(1000, "openai", "gpt-4")
        self.assertEqual(cost, 0.03)
        
    def test_unknown_provider_cost(self):
        cost = calculate_cost(1000, "unknown", "unknown")
        self.assertEqual(cost, 0.01)

if __name__ == "__main__":
    unittest.main()
