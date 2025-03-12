package com.example.myapplication

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.myapplication.ui.theme.AndroidTheme
import tech.brainco.treadmilljna.TreadmillSDK

class MainActivity : ComponentActivity() {
  private fun testMockData() {
    TreadmillSDK.initializeLogging(TreadmillSDK.LOG_LEVEL_INFO)

    // 设置步态数据回调
    TreadmillSDK.setGaitDataCallback { timestamp, leftFoot, pattern, gaitDuration -> println("Gait data received, timestamp: $timestamp, leftFoot: $leftFoot, pattern: $pattern, gaitDuration: $gaitDuration") }

    // 设置异常事件回调
    TreadmillSDK.setAbnormalEventCallback{ timestamp, event -> println("Abnormal event received, timestamp: $timestamp, event: $event") }

    // 获取并处理十六进制数据
    val byteArrays = hexStringsToByteArrays()
    byteArrays.forEachIndexed { index, byteArray ->
      // didReceiveData 需要两个参数：byteArray 和长度
      TreadmillSDK.didReceiveData(byteArray)
    }
  }

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    // 调用测试方法
    testMockData()

    enableEdgeToEdge()
    setContent {
      AndroidTheme {
        Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
          Greeting(
            name = "Android", modifier = Modifier.padding(innerPadding)
          )
        }
      }
    }
  }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
  Text(
    text = "Hello Treadmill for $name!", modifier = modifier
  )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
  AndroidTheme {
    Greeting("Android")
  }
}
