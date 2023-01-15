import os
import speech_recognition as sr
import ffmpeg

from os import path
from grammar import grammar_check

def speech_to_text_func():

    video_name = "1"

    command2wav = f"ffmpeg -i {video_name}.mp4 {video_name}.wav"

    os.system(command2wav)

    r = sr.Recognizer()
    with sr.AudioFile(f"{video_name}.wav") as source:
        audio = r.record(source, duration=120) 
    print(r.recognize_google(audio))

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), f"{video_name}.wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        
        try:
            final_text = r.recognize_google(audio)
            print(final_text) #still need to import write_video
            grammar_check(final_text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


speech_to_text_func()
