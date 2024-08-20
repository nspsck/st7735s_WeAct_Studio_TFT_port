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
    """
    For BlackPill:
    
    Fast SPI:
    SPI1: cs=A4  sck=A5  mosi=A7  miso=A6
    SPI4: cs=B12 sck=B13 mosi=A1  (miso=A11) # Do not use USART6 anymore.
    SPI5: cs=B1  sck=B0  mosi=A10 (miso=A12) # Do not use USART1 anymore.
    
    Slow SPI:
    SPI2: 
    SPI3:
    
    """
    return st7789.ST7789(SPI(5, baudrate=60000000), # cs=B1  sck=B0  mosi=A10
                  132,
                  162,
                  reset=Pin('B2', Pin.OUT),
                  cs=Pin('B1', Pin.OUT),
                  dc=Pin('A9', Pin.OUT),
                  backlight=Pin('A8', Pin.OUT),
                  rotation=rotation,
                  options=options,
                  inversion=True,
                  use_drawbuffer=False, # This takes 40KB RAM.
                  reversed_backlight=True)

