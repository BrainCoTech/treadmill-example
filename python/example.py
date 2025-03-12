"""
Treadmill SDK Demo
Demonstrates how to use treadmill_sdk to process data.
"""

import treadmill_sdk
import logging
from logger import getLogger

# Configure logging
logger = getLogger(logging.INFO)


def demonstrate_func():
    """Demonstrate data process using treadmill_sdk."""
    logger.info("Start to demonstrate data process using treadmill_sdk.")


def main():
    """Main entry point of the script."""
    demonstrate_func()


if __name__ == "__main__":
    main()
