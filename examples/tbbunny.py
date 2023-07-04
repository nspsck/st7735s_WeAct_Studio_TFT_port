"""
tbbunny.py

    Reads, decodes and displays movie frames from individual JPG's stored on
    a SD Card. See https://github.com/russhughes/TinyBigBuckBunny for JPG's.
"""

import tft_config
import uos
import st7789
import time
import gc

gc.collect()

tft = tft_config.config(1)

tft.init()
tft.fill(st7789.BLACK)

for i in range(1, 2387):
    last = time.ticks_ms()
    frame = "/sd/160x120/{:04d}.jpg".format(i)
    tft.jpg(frame, 80, 60, st7789.FAST)
    if time.ticks_diff(time.ticks_ms(), last) < 250:
        time.sleep_ms(10)
