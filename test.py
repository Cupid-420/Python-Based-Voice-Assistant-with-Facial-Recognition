"""
import struct
import pvporcupine
import pyaudio
import time
import pyautogui as autogui

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    keywords = ["assistant arise"]  # Custom label for clarity

    try:
        porcupine = pvporcupine.create(
            keyword_paths=["assistant-arise_en_windows_v3_0_0.ppn"],
            access_key="2KmScchu5QmYJI2ytJfMSQXp5BT7SocH4ED8TDgN22Y1Ct3ZJr/pRQ==",
            sensitivities=[0.5]
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for hotword: assistant arise")

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print(f"Hotword detected: {keywords[keyword_index]}")
                autogui.hotkey("win", "j")
                time.sleep(2)

    except Exception as e:
        print("Error:", e)

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

if __name__ == "__main__":
    hotword()

"""

from googlesearch import search

query = "google"
for result in search(query, num_results=3):
    print(result)
