import time
import pyaudio
from playsound import playsound
from audioplayer import AudioPlayer

def play_it():
    p = AudioPlayer('D:\Programming\Python\Violet\Violet 1.0\sounds_mp3\Omen, я тебе покажу, что такое страх.mp3')

    p.play(block=True)
    #time.sleep(3)
    p.stop()
play_it()