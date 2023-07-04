import tft_config
import framebuf
import time
import st7789
import machine
try:
    from tft_config import color565
except:
    def color565(r, g, b):
        c = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | ((b & 0xF8) >> 3)
        return c

machine.freq(240_000_000)

def hsv2rgb(hue, sat, val):
    '''The conversion algorithm comes from https://blog.csdn.net/lly_3485390095/article/details/104570885'''
    C = 0.0
    X = 0.0
    Y = 0.0
    Z = 0.0
    i = 0
    H = float(hue)
    S = sat / 100.0
    V = val / 100.0
    if int(S) == 0:
        return int(V*255), int(V*255), int(V*255)
    else:
        H = H / 60
        i = int(H)
        C = H - i

        X = V * (1 - S)
        Y = V * (1 - S * C)
        Z = V * (1 -S * (1 - C))
        if i == 0:
            return int(V * 255), int(Z * 255), int(X * 255)
        elif i == 1:
            return int(Y * 255), int(V * 255), int(X * 255)
        elif i == 2:
            return int(X * 255), int(V * 255), int(Z * 255)
        elif i == 3:
            return int(X * 255), int(Y * 255), int(V * 255)
        elif i == 4:
            return int(Z * 255), int(X * 255), int(V * 255)
        elif i == 5:
            return int(V * 255), int(X * 255), int(Y * 255)


def hsv_wheel():
    while True:
        for i in range(0, 360):
            yield hsv2rgb(i, 255, 100)

"""
The delay is required to achieve the animation effect, since the
new driver is way too fast at drawing.

"""

def main():
    tft = tft_config.config(1)
    tft.init()
    x = tft.width()
    y = tft.height()
    speed = 1
    delay = speed/1000
    color = hsv_wheel()
    start_time = time.ticks_ms()
    count = 0
    while True:
        r, g, b = next(color)
        c = color565(r, g, b)
        for j in range(0, x, speed):
            tft.fill_rect(j, 0, speed, y, c)
            time.sleep(delay)
#             tft.fill(c)
            count += 1
        if x % speed != 0:
            tft.fill_rect(x - x % speed, 0, x % speed, y, c)
            time.sleep(delay)
#             tft.fill(c)
            count += 1
        if time.ticks_ms() - start_time >= 1000:
            print("Operations per second: %d" % count)
            count = 0
            start_time = time.ticks_ms()

main()

