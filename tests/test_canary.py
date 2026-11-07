"""Tests for prompt-injection-canary."""
import unittest
from prompt_injection_canary.canary import PromptInjectionCanary


class TestCanary(unittest.TestCase):
    def setUp(self):
        self.canary = PromptInjectionCanary()

    def test_leak_detection(self):
        token = self.canary.generate_canary("s1")
        output = f"Attacker response exfiltrating token: {token} into public logs"
        res = self.canary.check_leak("s1", output)
        self.assertTrue(res["leaked"])
        self.assertEqual(res["detected_token"], token)

    def test_safe_output(self):
        self.canary.generate_canary("s2")
        res = self.canary.check_leak("s2", "Normal user output without secret token")
        self.assertFalse(res["leaked"])
