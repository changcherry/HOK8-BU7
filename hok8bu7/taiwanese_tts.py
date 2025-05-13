import os
from hok8bu7.fake_g2pPoj import G2p

# 1. 輸入白話字
input_text = input("請輸入白話字（例：hok8-bu7）: ")

# 2. 用 moedict-g2p 轉成台語音標
g2p = G2p()
phonemes = g2p(input_text)

# 3. 整理成可以輸出的音標
phoneme_text = " ".join(phonemes)
print(f"轉換成台語音標: {phoneme_text}")

# 4. 暫時使用 Mac 內建的 say 指令朗讀
# 但是 Mac say 預設沒有台語聲音，這裡先拿梅佳(Mei-Jia)模擬
# 如果要更像台語，需要後面接真正台語TTS

# 把輸入文字清理掉 8, 7 這種音調標記
say_text = input_text.replace('8', '').replace('7', '').replace(' ', '')

# 使用 Mac 內建語音朗讀（注意：目前是中文腔調）
print(f"使用 Mei-Jia 聲音朗讀: {say_text}")
os.system(f'say -v Mei-Jia "{say_text}"')

# 5. 輸出成音檔
output_path = "output.wav"
os.system(f'say -v Mei-Jia -o {output_path} "{say_text}"')

print(f"\n台語語音儲存成功：{output_path}")
print(f"你可以用以下指令播放聽聽看：\n   afplay {output_path}")


# 進入虛模擬器source venv/bin/activate 退出 deactivate

#cd HOK8-BU7  PYTHONPATH=. python3 -m hok8bu7.taiwanese_tts

