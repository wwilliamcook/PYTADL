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
    stream = (
        YouTube(youtube_url)
        .streams
        .order_by('abr')
        .last()
    )
    download_path = stream.download(output_path=output_path, filename=filename)

    return download_path


def loadAudio(path, sample_rate=16000):
    """Returns the audio data loaded from a file.

    :param int: audio sample rate in Hz
    :return: the mono audio samples as an int16 numpy array
    """
    if not isinstance(sample_rate, int):
        raise TypeError('sample_rate must be of type int')
    channels = 1
    buffer, _ = (
        ffmpeg
        .input(path)
        .output('-',
                format='s16le',
                acodec='pcm_s16le',
                ac=channels,
                ar=sample_rate)
        .overwrite_output()
        .run(capture_stdout=True)
    )

    return np.frombuffer(buffer, dtype='int16')


def downloadAudio(youtube_url, **load_kwargs):
    """Returns the audio data for the given YouTube video.

    :param str: youtube_url: URL of YouTube video to download
    :return: the mono audio samples as an int16 numpy array
    """
    filename = downloadMP4(youtube_url, filename='pytadl-temp')
    try:
        audio_data = loadAudio(filename, **load_kwargs)
    finally:
        os.remove(filename)
    return audio_data
