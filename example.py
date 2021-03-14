import math
import pyaudio
from pytadl import downloadAndDecode
import sys


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = 'https://www.youtube.com/watch?v=DIuKJ1fWmlk'
    print('fetching audio')
    a = downloadAndDecode(url)
    stream = p.open(format=p.get_format_from_width(2, unsigned=False),
                    channels=1,
                    rate=16000,
                    output=True)
    print('playing audio')
    # split up audio for responsive keyboard interrupt
    for i in range(math.ceil(len(a) / 1024)):
        stream.write(a[1024*i:1024*(i+1)].tobytes())
    stream.close()
    p.terminate()
