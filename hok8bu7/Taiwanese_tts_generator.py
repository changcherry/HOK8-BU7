# Taiwanese_tts_generator.py

import torch
import os
import sys
import urllib.request
import zipfile
import torchaudio

# 設定下載的模型網址（這是公開台語Tacotron2模型）
TACOTRON2_MODEL_URL = "https://huggingface.co/voidful/taigi_tts_pretrained/resolve/main/checkpoint_80000.pth"
HIFIGAN_MODEL_URL = "https://huggingface.co/voidful/taigi_tts_pretrained/resolve/main/generator_universal.pth"

# 建立模型資料夾
MODEL_DIR = "Taiwanese_tts_models"
os.makedirs(MODEL_DIR, exist_ok=True)

# 簡單下載器
def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"⬇️ 正在下載 {filename} ...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} 下載完成！")
    else:
        print(f" {filename} 已存在，跳過下載。")

# 下載模型
def download_models():
    download_file(TACOTRON2_MODEL_URL, os.path.join(MODEL_DIR, "tacotron2_taigi.pth"))
    download_file(HIFIGAN_MODEL_URL, os.path.join(MODEL_DIR, "hifigan_taigi.pth"))

# 簡單台語 TTS 流程
def run_taiwanese_tts(text):
    print(f"🗣️ 接收輸入文字：{text}")
    print("⚡模擬語音合成過程（正式版會接入 Tacotron2+HiFiGAN）")
    
    # 這裡暫時模擬，稍後可以真正接入模型
    fake_waveform = torch.randn(1, 16000 * 3)  # 假裝產生3秒音訊
    sample_rate = 16000
    
    output_path = "output_taiwanese.wav"
    torchaudio.save(output_path, fake_waveform, sample_rate)
    print(f"已儲存台語語音檔案到：{output_path}")
    
    # 自動播放（Mac）
    os.system(f"afplay {output_path}")

# 主程式入口
if __name__ == "__main__":
    # 下載模型（如果不存在）
    download_models()
    
    # 讓使用者輸入羅馬拼音
    text_input = input("請輸入台語羅馬拼音（例如：hok8-bu7）：\n> ")
    
    run_taiwanese_tts(text_input)
