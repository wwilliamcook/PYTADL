# PYTADL (Python YouTube Audio Downloader)

PYTADL is intended for use as an information retrieval tool for analysing the audio of a YouTube video. It's core functionality is to fetch and return the audio in the form of a numpy array. The quality of the resulting audio is noticeably lower than that of the original video, though not so degraded as to be unsuitable for processing.

## Prerequisites

Requires FFmpeg. On Windows, `ffmpeg.exe` must be placed in the same folder as `python.exe` (adding it to `Path` will likely not work).

Run `python -m pip install -r requirements.txt` to install python dependencies.

# Example Usage

Run `python example.py [youtube-url]` to get an idea for what PYTADL does.
