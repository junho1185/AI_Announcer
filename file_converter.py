from pydub import AudioSegment
import os

def from_mp3_to_wav(filename):
    audSeg = AudioSegment.from_mp3(filename + '.mp3')

    if os.path.exists(filename +'.wav'):
        os.remove(filename + '.wav')
    audSeg.export(filename + '.wav', format='wav')
    if os.path.exists(filename + '.mp3'):
        os.remove(filename + '.mp3')

def from_wav_to_mp3(filename):
    audSeg = AudioSegment.from_wav(filename + '.wav')
    audSeg.export(filename + '.mp3', format='mp3')
    if os.path.exists(filename + '.wav'):
        os.remove(filename + '.wav')