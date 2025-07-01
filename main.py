import argparse 
from checker.strength_checker import check_password_strength
from utils.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker")
    parser.add_argument("password", type=str, help="Enter the password to evaluate")
    args = parser.parse_args()

    logger.info("Password check strarted.")
    result = check_password_strength(args.password)
    print(f"Strength: {result['score']} / 5 ({result['verdict']})")
    if result['suggestions']:
        print("Suggestions:")
        for s in result['suggestions']:
            print(f"- {s}")
    logger.info("Password check completes.")

if __name__ == "__main__":
    main()