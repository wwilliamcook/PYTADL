import ffmpeg
import numpy as np
import os
from pytube import YouTube


def downloadMP4(youtube_url, output_path=None, filename=None):
    """Downloads an MP4 of the given YouTube video.

    :param str: youtube_url: URL of YouTube video to download
    :param str: output_path: directory to save file
    :param str: filename: base name to save file as
    :return: the path to the saved file
    """
    return (
        YouTube(youtube_url)
        .streams
        .filter(file_extension='mp4')
        .first()
        .download(output_path=output_path, filename=filename)
    )


def downloadAndDecode(youtube_url):
    """Returns the audio data for the given YouTube video.

    :param str: youtube_url: URL of YouTube video to download
    :return: the mono audio samples as an int16 numpy array
    """
    filename = downloadMP4(youtube_url, filename='pytadl-temp')
    buffer, _ = (
        ffmpeg
        .input(filename)
        .output('-', format='s16le', acodec='pcm_s16le', ac=1, ar='16k')
        .overwrite_output()
        .run(capture_stdout=True)
    )
    os.remove(filename)
    return np.frombuffer(buffer, dtype='int16')
