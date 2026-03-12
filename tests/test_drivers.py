import unittest
from swarmpulse.drivers import UnityDriver

class TestDrivers(unittest.TestCase):
    def test_unity_injection(self):
        driver = UnityDriver()
        result = driver.inject_script("void Update() {}")
        self.assertIn("Unity", result)

if __name__ == "__main__":
    unittest.main()
