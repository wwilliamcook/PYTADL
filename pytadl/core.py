import ffmpeg
import io
import numpy as np
import os
from pytube import YouTube


def downloadMP4(youtube_url):
    return (
        YouTube(youtube_url)
        .streams
        .filter(file_extension='mp4')
        .first()
        .download(filename='youtube-dl_temp')
    )


def downloadAndDecode(youtube_url):
    filename = downloadMP4(youtube_url)
    buffer, _ = (
        ffmpeg
        .input(filename)
        .output('-', format='s16le', acodec='pcm_s16le', ac=1, ar='16k')
        .overwrite_output()
        .run(capture_stdout=True)
    )
    os.remove(filename)
    return np.frombuffer(buffer, dtype='int16')
