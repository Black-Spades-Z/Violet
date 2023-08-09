import json, pyaudio
import os
from vosk import Model, KaldiRecognizer
from playsound import playsound
from audioplayer import AudioPlayer
from pathlib import Path
from time import sleep
#from wakeword_recognition import wake_word
#from play_sound import play_it



def main():
    model = Model('../models/vosk-model-small-ru-0.4')

    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    stream.start_stream()

    def listen():
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if (rec.AcceptWaveform(data)) and len(data) > 0:
                answer = json.loads(rec.Result())
                if answer['text']:
                    yield answer['text']

    print('Main Listenning')
    for text in listen():
        if text == 'ви':
            audio = Path().open('sounds_mp3') / 'sounds_mp3/Хах! А вы ещё кто7 Уборщики7.mp3'
            playsound(audio)
        elif text == 'привет':
            audio = Path().cwd() / 'sounds_mp3/Привет.mp3'
            playsound(audio)
        elif text == 'извинись':
            audio = Path().cwd() / 'sounds_mp3/Фу….mp3'
            playsound(audio)
        elif text == 'пока' or text == 'отключайся':
            audio = Path().cwd() / 'sounds_mp3/Я пойду первой.mp3'
            playsound(audio)
            quit()
        else:
            print(text)


# if wake_word() == True:
#     p = AudioPlayer('D:\Programming\Python\Violet\Violet 1.0\sounds_mp3\Здесь.mp3')
#
#     p.play(block=True)
#     # time.sleep(3)
#     p.stop()
#
#     main()
#