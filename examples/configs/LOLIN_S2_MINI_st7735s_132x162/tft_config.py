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

def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(1, baudrate=30000000, sck=Pin(36), mosi=Pin(35), miso=None),
        132,
        162,
        reset=Pin(1, Pin.OUT),
        cs=Pin(34, Pin.OUT),
        dc=Pin(38, Pin.OUT),
        backlight=Pin(6, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size= buffer_size)
