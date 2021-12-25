from gtts import gTTS
from scipy.signal import lfilter, butter
from scipy.io.wavfile import read,write
from numpy import array, int16
from pydub import AudioSegment
import file_converter


def voice_maker(ko_script, en_script):
    for i in range((len(ko_script) - 1)):
        print('Generating Announcement Audio File...')
        ko_tts = gTTS(text=ko_script[i], lang='ko', slow=False)
        en_tts = gTTS(text=en_script[i], lang='en', slow=False)
        f = open('./data/'+str(i)+'.mp3', 'wb')
        ko_tts.write_to_fp(f)
        en_tts.write_to_fp(f)

        if i == 5:
            ko_tts = gTTS(text=ko_script[7], lang='ko', slow=False)
            en_tts = gTTS(text=en_script[7], lang='en', slow=False)
            ko_tts.write_to_fp(f)
            en_tts.write_to_fp(f)

        f.close()
        file_converter.from_mp3_to_wav('./data/'+str(i))
        speaker_effect('./data/'+str(i))
        print('Announcement File Generated.')


def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


def butter_params(low_freq, high_freq, fs, order=5):
    nyq = 0.5 * fs
    low = low_freq / nyq
    high = high_freq / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, low_freq, high_freq, fs, order=5):
    b, a = butter_params(low_freq, high_freq, fs, order=order)
    y = lfilter(b, a, data)
    return y


def speaker_effect(filename):
    fs, audio = read(filename + '.wav')
    low_freq = 300.0
    high_freq = 3000.0
    filtered_signal = butter_bandpass_filter(audio, low_freq, high_freq, fs, order=6)
    write(filename +'.wav', fs, array(filtered_signal, dtype=int16))