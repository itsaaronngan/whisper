import ffmpeg

def extract_audio(video_path, audio_path):
    """
    Extracts audio from a video file and saves it as an MP3 file.
    Args:
    video_path (str): "Path to the video file."
    audio_path (str): Path where the extracted audio will be saved.
    """
    try:
        stream = ffmpeg.input(video_path)
        audio = stream.audio
        ffmpeg.output(audio, audio_path).run()
        print(f"Extracted audio from {video_path} to {audio_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_file = r'/Users/aaronnganm1/Documents/Zoom/2022-10-27 20.52.05 JIC Professional Branding Session/JIC Professional Brand Session.mp4'  # Replace with your video file path
audio_file = 'output_audio_file.mp3'        # Replace with your desired output audio file path
extract_audio(video_file, audio_file)
