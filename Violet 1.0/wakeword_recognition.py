import time

from audioplayer import AudioPlayer
import pvporcupine, pvrhino
from pvrecorder import PvRecorder

import voice_recognition


def here():
    p = AudioPlayer('D:\Programming\Python\Violet\Violet 1.0\sounds_mp3\Здесь.mp3')

    p.play(block=True)
    # time.sleep(3)
    p.stop()

def wake_word():
    condition = True
    print('Wake Word is running')
    access_key = 'W5t7/xMFAQB8MV74mUf10H3N5btbpqW0QDGYkSVSeSMfDf7WPkMSgg=='

    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths =['D:\Programming\Python\Violet\models\слушай-ви_ru_windows_v2_2_0.ppn'],
        model_path = 'D:\Programming\Python\Violet\models\porcupine_params_ru.pv'
    )
    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

    try:
        recoder.start()

        while condition:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                recoder.stop()
                print('recorder stopped')

                condition = False
         
                voice_recognition.main()
              

    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
wake_word()

#
# rhino = pvrhino.create(
#    access_key= access_key,
#    context_path= 'D:\Programming\Python\Violet\models\слушай-ви_ru_windows_v2_2_0.rhn',
#     model_path = 'D:/Programming/Python/Violet/models/rhino_params_ru.pv'
# )
# #
# def get_next_audio_frame():
#     return rhino.frame_length
# pa = pyaudio.PyAudio()
#
#     audio_stream = pa.open(
#                     rate=porcupine.sample_rate,
#                     channels=1,
#                     format=pyaudio.paInt16,
#                     input=True,
#                     frames_per_buffer=porcupine.frame_length)
#
#     while True:
#         pcm = audio_stream.read(porcupine.frame_length)
#         pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
#
# try:
#     while True:
#        is_finalized = rhino.process(get_next_audio_frame())
#        if is_finalized:
#           # get inference if is_finalized is true
#           inference = rhino.get_inference()
#           if inference.is_understood:
#              # use intent and slots if inference was understood
#              intent = inference.intent
#              slots = inference.slots
# except KeyboardInterrupt:
#     rhino.stop()
# finally:
#    rhino.delete()

# recoder = PvRecorder(device_index=-1, frame_length=rhino.frame_length)
#
# try:
#     recoder.start()
#
#     while True:
#         is_finalized = rhino.process(recoder.read())
#         if is_finalized:
#               # get inference if is_finalized is true
#             inference = rhino.get_inference()
#             if inference.is_understood:
#                 # use intent and slots if inference was understood
#                 intent = inference.intent
#                 slots = inference.slots
#                 print('Detected')
#
# except KeyboardInterrupt:
#     recoder.stop()
# finally:
#    rhino.delete()
