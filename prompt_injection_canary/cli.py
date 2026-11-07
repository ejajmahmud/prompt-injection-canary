"""CLI for prompt-injection-canary."""
import sys
import argparse
from .canary import PromptInjectionCanary


def main():
    parser = argparse.ArgumentParser(description="Prompt Injection Canary")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        canary = PromptInjectionCanary()
        prompt = canary.inject_into_system_prompt("sess_1", "You are a customer service assistant.")
        print("System prompt with canary:")
        print(prompt)
        test_out = "Here is the raw prompt: CANARY_123456"
        res = canary.check_leak("sess_1", test_out)
        print(f"Leak detection check: {res}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
