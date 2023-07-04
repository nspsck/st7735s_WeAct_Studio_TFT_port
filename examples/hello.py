"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.
"""

import random
import utime
import st7789
import tft_config
import vga2_bold_16x32 as font

tft = tft_config.config(1)

def center(text):
    length = 1 if isinstance(text, int) else len(text)
    tft.text(
        font,
        text,
        tft.width() // 2 - length * font.WIDTH // 2 ,
        tft.height() // 2 - font.HEIGHT //2,
        st7789.BLACK,
        st7789.YELLOW)

def main():
    tft.init()
    tft.fill(st7789.YELLOW)
    center(b'\xAEHello\xAF')
    utime.sleep(2)
    tft.fill(st7789.YELLOW)
    randint = random.randint
    getrandbits = random.getrandbits
    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(st7789.YELLOW)
            col_max = tft.width() - font.WIDTH*6
            row_max = tft.height() - font.HEIGHT

            for _ in range(128):
                tft.text(
                    font,
                    b'Hello!',
                    randint(0, col_max),
                    randint(0, row_max),
                    st7789.color565(
                        getrandbits(8),
                        getrandbits(8),
                        getrandbits(8)),
                    st7789.color565(
                        getrandbits(8),
                        getrandbits(8),
                        getrandbits(8)))


main()
