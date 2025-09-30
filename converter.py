import ffmpeg
import os

FFMPEG_PATH = os.path.join(
    os.path.dirname(__file__),
    "ffmpeg-2025-09-28-git-0fdb5829e3-essentials_build",
    "bin",
    "ffmpeg.exe"
)

def mp4_to_wav(input_file, output_file):
    input_file = os.path.abspath(input_file)
    output_file = os.path.abspath(output_file)

    (
        ffmpeg
        .input(input_file)
        .output(output_file, ac=1, ar=16000, format='wav')
        .run(cmd=FFMPEG_PATH)
    )
    print(f"[OK] Convertido: {output_file}")
