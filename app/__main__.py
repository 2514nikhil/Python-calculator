import argparse

from .calculator import Calculator


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculator Service CLI")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform",
    )
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")
    args = parser.parse_args()

    calculator = Calculator()
    operation_map = {
        "add": calculator.add,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
    }

    result = operation_map[args.operation](args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()