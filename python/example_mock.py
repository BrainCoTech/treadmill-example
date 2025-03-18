"""
Treadmill SDK Demo
演示使用 treadmill_sdk 库解析模拟数据。
"""

from typing import Final
import treadmill_sdk
import logging
from logger import getLogger

# 配置日志记录器
logger = getLogger(logging.INFO)

# 定义常量
MOCK_DATA: Final[bytes] = bytes.fromhex(
    "42524E4302131F000301A55AECA9E08ADA826513D6251C6A2E884645AF4B199A46771B53693280813B557D89"
    "42524E4302131F000301A55AECA9E18AE29A6513D6251C6A2E881E705F9E73E87426A723B80C2B5517672D4C"
    "42524E4302131F000301A55AECA9E68A8A916513D6251C6A2E88F0D68D7283F29480BBFD60D1C5CECBF0EBC4"
)

class TreadmillDataParser:
    """跑步机数据解析器"""

    def __init__(self) -> None:
        """初始化解析器并设置回调"""
        self._setup_callbacks()

    def _setup_callbacks(self) -> None:
        """设置回调函数"""
        treadmill_sdk.set_abnormal_event_callback(self._on_abnormal_event)
        treadmill_sdk.set_gait_data_callback(self._on_gait_data)

    def _on_abnormal_event(self, timestamp: int, event: int) -> None:
        """异常事件回调处理"""
        logger.info(
            f"检测到异常事件:"
            f"\n  - timstamp: {timestamp}"
            f"\n  - 事件类型: {event}"
        )

    def _on_gait_data(
        self,
        timestamp: int,
        left_foot: bool,
        pattern: int,
        gait_duration: int
    ) -> None:
        """步态数据回调处理"""
        logger.info(
            f"收到步态数据:"
            f"\n  - timstamp: {timestamp}"
            f"\n  - 左脚: {left_foot}"
            f"\n  - 模式: {pattern}"
            f"\n  - duration: {gait_duration}ms"
        )

    def parse_data(self, data: bytes) -> None:
        """解析数据"""
        try:
            logger.info(f"开始解析数据: 长度={len(data)}字节")
            logger.debug(f"原始数据(hex): {data.hex()}")

            treadmill_sdk.did_receive_data(data)

        except Exception as e:
            logger.error(f"数据解析失败: {e}")
            raise

def main() -> None:
    """主函数"""
    try:
        parser = TreadmillDataParser()
        parser.parse_data(MOCK_DATA)

    except KeyboardInterrupt:
        logger.info("程序被用户终止")
    except Exception as e:
        logger.error(f"程序运行出错: {e}")
        raise

if __name__ == "__main__":
    main()
