import whisper

# 配置
MODEL_SIZE = "base"
AUDIO_PATH = "./test_audio/dub.wav"

def main():
    print("正在加载模型...")
    model = whisper.load_model(MODEL_SIZE)

    print("开始识别音频...")
    result = model.transcribe(
        AUDIO_PATH,
        language="zh",
        verbose=True
    )

    # 保存识别结果
    with open("transcribe_result.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])

    print("\n识别完成，结果已保存至 transcribe_result.txt")
    print("\n识别内容：")
    print(result["text"])

if __name__ == "__main__":
    main()