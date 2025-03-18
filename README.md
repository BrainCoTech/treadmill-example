# Treadmill-SDK Example

本项目包含 Treadmill-SDK 的示例代码，支持多种编程语言和平台。

## Java/Kotlin
请查看 `android` 文件夹中的内容。

## Objective-C/Swift
请查看 `ios` 文件夹中的内容。

## Unity
请查看 `unity` 文件夹中的 README 文件。

## Python
请查看 `python` 文件夹中的 README 文件。

## API

### 枚举类型

#### AbnormalGait
异常步态类型枚举。

| 值 | 名称 | 描述 |
|---|---|---|
| 0 | ABNORMAL_GAIT_UNSPECIFIED | 未指定的异常步态 |
| 1 | ABNORMAL_GAIT_NO_LOAD | 未检测到负重 |
| 2 | ABNORMAL_GAIT_HANDRAIL_SUPPORTED | 检测到扶手支撑 |
| 3 | ABNORMAL_GAIT_UNILATERAL_DRAGGING | 检测到单侧拖动 |

#### GaitPattern
步态模式枚举。

| 值 | 名称 | 描述 |
|---|---|---|
| 0 | GAIT_PATTERN_UNSPECIFIED | 未指定的步态模式 |
| 1 | GAIT_PATTERN_WALK | 步行模式 |
| 2 | GAIT_PATTERN_RUN | 跑步模式 |

#### LogLevel
日志级别枚举。

| 值 | 名称 | 描述 |
|---|---|---|
| 0 | LOG_LEVEL_ERROR | 错误级别 |
| 1 | LOG_LEVEL_WARN | 警告级别 |
| 2 | LOG_LEVEL_INFO | 信息级别 |
| 3 | LOG_LEVEL_DEBUG | 调试级别 |
| 4 | LOG_LEVEL_TRACE | 追踪级别 |

### 回调函数类型

#### GaitDataCallback

```c
typedef void (*GaitDataCallback)(
    uint32_t timestamp,    // 时间戳（秒）
    bool left_foot,        // 是否为左脚
    uint32_t pattern,      // 步态模式，参考 GaitPattern 枚举
    uint32_t gait_duration // 步态持续时间（毫秒）
);
```

#### AbnormalEventCallback

```c
typedef void (*AbnormalEventCallback)(
    uint32_t timestamp,  // 时间戳（秒）
    uint32_t event_type  // 异常事件类型，参考 AbnormalGait 枚举
);
```

### 函数

#### initialize_logging
初始化日志记录功能。

```c
void initialize_logging(LogLevel level);
```

**参数**
- `level`: 日志记录的级别，参考 LogLevel 枚举

#### set_gait_data_callback

设置步态分析结果的回调函数。

```c
void set_gait_data_callback(GaitDataCallback cb);
```

**参数**
- `cb`: 接收步态分析结果数据的回调函数

#### set_abnormal_event_callback
设置异常事件的回调函数。

```c
void set_abnormal_event_callback(AbnormalEventCallback cb);
```

**参数**
- `cb`: 接收异常事件数据的回调函数

#### did_receive_data
接收数据的函数。

```c
void did_receive_data(const uint8_t *data, uintptr_t len);
```

**参数**

- `data`: 数据指针，指向接收到的数据
- `len`: 数据长度

**注意**: 该函数不会释放传入的数据，调用方负责内存管理。
