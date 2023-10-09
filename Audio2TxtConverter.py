import os
import speech_recognition as sr
from pydub import AudioSegment

# Function to convert audio files to WAV format
def convert_audio_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_channels(1)  # Set to mono (1 channel)
    audio = audio.set_frame_rate(16000)  # Set sample rate to 16 kHz
    audio.export("temp.wav", format="wav")

# Function to convert audio to text
def audio_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    return ""

# Main function
def main():
    input_audio_file = "input_audio.mp3"
    output_text_file = "output.txt"

    # Convert the input audio to WAV format
    convert_audio_to_wav(input_audio_file)

    # Perform audio-to-text conversion
    text = audio_to_text("temp.wav")

    # Save the text to a file
    with open(output_text_file, "w") as f:
        f.write(text)

    # Clean up temporary files
    os.remove("temp.wav")

if __name__ == "__main__":
    main()
