#!/usr/bin/python3
import ffmpeg
(
ffmpeg
.input('brit.mp3').audio
.filter("volume", 3)
.filter("volume", 3)
.filter("volume", 3)
.filter("volume", 3)
.filter("bass", 5)
.output('out.mp3')
.run()
)
