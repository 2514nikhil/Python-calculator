from app.logger import get_logger

logger = get_logger()


class Calculator:
    def add(self, a: float, b: float) -> float:
        logger.info(f"Adding {a} and {b}")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        logger.info(f"Subtracting {b} from {a}")
        return a - b

    def multiply(self, a: float, b: float) -> float:
        logger.info(f"Multiplying {a} and {b}")
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            logger.error("Attempted division by zero")
            raise ValueError("Cannot divide by zero")
        logger.info(f"Dividing {a} by {b}")
        return a / b