"""
Treadmill SDK Demo
Demonstrate parsing of mock data using treadmill_sdk library.
"""

import treadmill_sdk
import logging
from logger import getLogger

# Configure logging
logger = getLogger(logging.INFO)

# Constants
PLAINTEXT = bytes.fromhex(
    "42524E4302131F000301A55AECA9E08ADA826513D6251C6A2E884645AF4B199A46771B53693280813B557D89"
    "42524E4302131F000301A55AECA9E18AE29A6513D6251C6A2E881E705F9E73E87426A723B80C2B5517672D4C"
    "42524E4302131F000301A55AECA9E68A8A916513D6251C6A2E88F0D68D7283F29480BBFD60D1C5CECBF0EBC4"
)


def demonstrate_parse():
    """Demonstrate encryption and decryption process using treadmill_sdk."""
    try:
        treadmill_sdk.set_abnormal_event_callback(
            lambda timestamp, event: logger.info(
                f"timestamp={timestamp}, event={event}"
            )
        )
        treadmill_sdk.set_gait_data_callback(
            lambda timestamp, left_foot, pattern, gait_duration: logger.info(
                f"timestamp={timestamp}, left_foot={left_foot}, pattern={pattern}, gait_duration={gait_duration}"
            )
        )

        # Display original plaintext
        logger.info(f"Plaintext: len={len(PLAINTEXT)}, hex={PLAINTEXT.hex()}")

        # Perform encryption
        treadmill_sdk.did_receive_data(PLAINTEXT)
        # asyncio.sleep(1)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


def main():
    """Main entry point of the script."""
    demonstrate_parse()


if __name__ == "__main__":
    main()
