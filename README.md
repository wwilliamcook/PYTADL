# PYTADL (Python YouTube Audio Downloader)

PYTADL is intended for use as an information retrieval tool for analysing the audio of a YouTube video. It's core functionality is to fetch and return the audio in the form of a NumPy array. The quality of the resulting audio is noticeably lower than that of the original video, though not so degraded as to be unsuitable for processing.

## Prerequisites

Requires [FFmpeg](https://www.ffmpeg.org/). On Windows, `ffmpeg.exe` must be placed in the same folder as `python.exe` (adding it to `Path` will likely not work).

[PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) is used for audio playback in `example.py` but is not required to use PYTADL. If you do not need this feature, you may skip to the next paragraph. Python 3.6 is recommended. See [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) for details on supported versions. Run `python -m pip install PyAudio` to install.

Run `python -m pip install -r requirements.txt` to install Python dependencies.

# Example Usage

Run `python example.py [youtube-url]` to get an idea for what PYTADL does.
