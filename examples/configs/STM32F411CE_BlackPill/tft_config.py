""" WeAct Studio 132x162 st7735s display

    https://weactstudio.aliexpress.com/store/910567080
    
    This should not be considered as Ads, rather than a
    confirmation for you, that you are using this exact
    tft-display.

"""
from machine import Pin, SPI
import st7789

TFA = 0
BFA = 0

def config(rotation=0, options=0):
    return st7789.ST7789(SPI(1, baudrate=30000000), # cs=A4, sck=A5, miso=A6, mosi=A7
                  132,
                  162,
                  reset=Pin('A3', Pin.OUT),
                  cs=Pin('A4', Pin.OUT),
                  dc=Pin('A2', Pin.OUT),
                  backlight=Pin('A1', Pin.OUT),
                  rotation=rotation,
                  options=options,
                  use_drawbuffer=True, # This takes 40KB RAM.
                  reversed_backlight=True)

