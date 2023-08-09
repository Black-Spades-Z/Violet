import json, pyaudio
import os
import time
import datetime
import subprocess

import pvporcupine, pvrhino
from vosk import Model, KaldiRecognizer
from playsound import playsound
from audioplayer import AudioPlayer
from pathlib import Path
from time import sleep
from pvrecorder import PvRecorder

access_key = 'W5t7/xMFAQB8MV74mUf10H3N5btbpqW0QDGYkSVSeSMfDf7WPkMSgg=='

def play(name):
    PATH = f"D:\\Programming\\Python\\Violet\\Violet 1.0\\sounds_ready\\{name}"
    p = AudioPlayer(PATH)
    p.play()

def wake_up_word():
    condition = True
    print('Wake Word is running')
    access_key = 'W5t7/xMFAQB8MV74mUf10H3N5btbpqW0QDGYkSVSeSMfDf7WPkMSgg=='

    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=['D:\Programming\Python\Violet\models\слушай-ви_ru_windows_v2_2_0.ppn'],
        model_path='D:\Programming\Python\Violet\models\porcupine_params_ru.pv'
    )
    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

    try:
        recoder.start()

        while condition:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                print(datetime.datetime.now())
                condition = False
                commands(recoder)

        print('Out')



    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()

def commands(recorder):
    rhino = pvrhino.create(
       access_key= access_key,
       context_path= 'D:\Programming\Python\Violet\models\слушай-ви_ru_windows_v2_2_2.rhn',
        model_path = 'D:/Programming/Python/Violet/models/rhino_params_ru.pv'
    )

    try:
        print(datetime.datetime.now())
        while True:

            is_finalized = rhino.process(recorder.read())
            if is_finalized:
                inference = rhino.get_inference()
                if inference.is_understood:
                    print('{')
                    print("  intent : '%s'" % inference.intent)
                    print('}\n')
                   # subprocess.Popen(f'ahk/open/{inference.intent}.ahk')
                    #subprocess.call(r'f"D:\Programming\Python\Violet\Violet 1.0\ahk\open\\{inference.intent}.ahk"')
                    PATH = "D:\\Programming\\Python\\Violet\\Violet 1.0\\ahk\\"
                    os.chdir(PATH)
                    os.system(f"{inference.intent}.ahk")
                    recorder.stop()
                    break
                else:
                    print("Didn't understand the command.\n")

        wake_up_word()
    except KeyboardInterrupt:
        print('Stopping ...')
    finally:
        recorder.delete()
        rhino.delete()



wake_up_word()