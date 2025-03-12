import SwiftUI
import TreadmillSDK

struct ContentView: View {
  // MARK: - State Properties
  @State private var gaitDataText: String = "Waiting for gait data..."
  @State private var eventText: String = "Waiting for events..."
  
  // 原始文本（示例）
  private let originalText = "Hello, Treadmill!"
  
  // MARK: - Body
  var body: some View {
    VStack(spacing: 20) {
      Image(systemName: "globe")
        .imageScale(.large)
        .foregroundStyle(.tint)
      
      // Original Text
      VStack(alignment: .leading) {
        Text("Original:")
          .font(.headline)
        Text(originalText)
      }
      
      // Event Data
      VStack(alignment: .leading) {
        Text("Event:")
          .font(.headline)
        Text(eventText)
          .font(.system(.body, design: .monospaced))
      }
      
      // Gait Data
      VStack(alignment: .leading) {
        Text("GaitData:")
          .font(.headline)
        Text(gaitDataText)
          .font(.system(.body, design: .monospaced))
      }
    }
    .padding()
    .frame(maxWidth: .infinity)
    .onAppear {
      // 初始化 TreadmillSDK
      TreadmillCore.initializeLogging(level: .info)
      
      // 设置步态数据回调
      TreadmillCore.setGaitDataCallback { timestamp, leftFoot, pattern, gaitDuration in
        self.gaitDataText = "Timestamp: \(timestamp), Left Foot: \(leftFoot), Pattern: \(pattern), Duration: \(gaitDuration)"
      }
      
      // 设置异常事件回调
      TreadmillCore.setAbnormalEventCallback { timestamp, eventType in
        self.eventText = "Timestamp: \(timestamp), Event Type: \(eventType)"
      }
      
      // 定义并发送十六进制数据
      let hexStringData = """
              42524e430213190002010070e083f78ac07e34085eda83310b9199eb73dd1c1706a8e2c35ffe
              42524e4302131c0002010070e383fa8a84757c09ff96f54d2fadac7315521c2da06f6f27c732dfa514
          """
      let hexLines = hexStringData.split(separator: "\n").map { String($0) }
      
      let byteArray1 = hexStringToByteArray(hexLines[0])
      let byteArray2 = hexStringToByteArray(hexLines[1])
      
      TreadmillCore.didReceiveData(byteArray1)
      TreadmillCore.didReceiveData(byteArray2)
    }
  }
  
  // MARK: - Helper Functions
  private func hexStringToByteArray(_ hexString: String) -> [UInt8] {
    var bytes = [UInt8]()
    var startIndex = hexString.startIndex
    
    while startIndex < hexString.endIndex {
      let nextIndex = hexString.index(startIndex, offsetBy: 2, limitedBy: hexString.endIndex) ?? hexString.endIndex
      let byteString = hexString[startIndex..<nextIndex]
      if let byte = UInt8(byteString, radix: 16) {
        bytes.append(byte)
      }
      startIndex = nextIndex
    }
    return bytes
  }
}

// MARK: - Preview
#Preview {
  ContentView()
}
