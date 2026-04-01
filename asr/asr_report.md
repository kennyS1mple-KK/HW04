# ASR 语音识别方案对比报告
本次对比三种主流开源 ASR 方案：OpenAI Whisper、FunASR、Vosk。

## 1. OpenAI Whisper
- 协议：MIT
- 语言：支持99种语言，中文效果优秀
- 模型大小：tiny/base/small/medium/large
- 优点：安装简单、准确率高、无需额外环境
- 缺点：流式支持较弱
- 本次选用原因：部署最简单，无需 FFmpeg，适合作业

## 2. FunASR
- 协议：MIT
- 语言：中文专项优化
- 优点：流式识别强
- 缺点：环境配置相对复杂

## 3. Vosk
- 协议：Apache 2.0
- 优点：极轻量、可嵌入式
- 缺点：中文准确率一般

## 选型结论
选择 Whisper，无需音视频环境，安装即用，适配本次作业场景。