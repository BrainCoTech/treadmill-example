"""
Treadmill SDK Demo
演示使用 treadmill_sdk 库解析串口数据流
"""

import treadmill_sdk
import asyncio
import serial
import logging
from logger import getLogger
from typing import Optional

# 配置日志
logger = getLogger(logging.INFO)

class SerialReader:
    def __init__(self, port_name: str = '/dev/ttyUSB0', baudrate: int = 115200):
        self.port_name = port_name
        self.baudrate = baudrate
        self.port: Optional[serial.Serial] = None

    async def start(self):
        """启动串口读取"""
        try:
            self.port = serial.Serial(
                self.port_name,
                self.baudrate,
                timeout=1
            )
            logger.info(f"串口已打开: {self.port_name}")

            # 设置回调
            treadmill_sdk.set_abnormal_event_callback(self._on_abnormal_event)
            treadmill_sdk.set_gait_data_callback(self._on_gait_data)

            await self._read_loop()

        except serial.SerialException as e:
            logger.error(f"串口错误: {e}")
        finally:
            self.stop()

    def stop(self):
        """停止串口读取"""
        if self.port and self.port.is_open:
            self.port.close()
            logger.info("串口已关闭")

    def _on_abnormal_event(self, timestamp: int, event: int):
        """异常事件回调"""
        logger.info(f"异常事件: timestamp={timestamp}, event={event}")

    def _on_gait_data(self, timestamp: int, left_foot: bool,
                      pattern: int, gait_duration: int):
        """步态数据回调"""
        logger.info(
            f"步态数据: timestamp={timestamp}, left_foot={left_foot}, "
            f"pattern={pattern}, duration={gait_duration}"
        )

    async def _read_loop(self):
        """串口读取循环"""
        while True:
            try:
                if self.port and self.port.in_waiting:
                    data = self.port.read(self.port.in_waiting)
                    if data:
                        treadmill_sdk.did_receive_data(data)
                await asyncio.sleep(0.1)  # 等待新数据
            except Exception as e:
                logger.error(f"读取错误: {e}")
                break

async def main():
    """主函数"""
    reader = SerialReader()
    try:
        await reader.start()
    except KeyboardInterrupt:
        logger.info("程序被用户终止")
    except Exception as e:
        logger.error(f"程序异常终止: {e}")
    finally:
        reader.stop()

if __name__ == "__main__":
    asyncio.run(main())
