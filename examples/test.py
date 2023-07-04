import st7789
import tft_config
import time
import random
import machine
import vga2_bold_16x32 as font

machine.freq(240_000_000)


def color(tft):
    count = 0
    start = time.ticks_ms()
    for i in range(0, 65535, 256):
        tft.fill(i)
        count += 1
        if time.ticks_ms() - start >= 1000:
            print(count)
            count = 0
            start = time.ticks_ms()
            
def on_off(tft):
    delay = 1000
    for i in range(6):
        tft.off()
        print("off")
        time.sleep_ms(delay)
        tft.on()
        print("on")
        time.sleep_ms(delay)
        

def sleep_on_off(tft):
    delay = 1000
    for i in range(6):
        tft.sleep_mode(True)
        print("sleep in")
        time.sleep_ms(delay)
        tft.sleep_mode(False)
        print("sleep out")
        time.sleep_ms(delay)
        
        
def pixel_color(tft):
    for y in range(tft.height()):
        for x in range(tft.width()):
            tft.pixel(x, y,
                      st7789.RED)
            
def line_color(tft):
    width = tft.width()
    height = tft.height()
    for x in range(width):
        tft.line(x, 0, width - x, height, st7789.GREEN)
    for y in range(height):
        tft.line(width, y, 0, height - y, st7789.GREEN)

def hvline_color(tft):
    width = tft.width()
    height = tft.height()
    half = int(width // 2)
    for x in range(half):
        tft.vline(x, 0, height, st7789.MAGENTA)
        time.sleep(0.01)
    for y in range(height):
        tft.hline(half, y, half, st7789.MAGENTA)
        time.sleep(0.01)
        
def rect_color(tft):
    width = tft.width()
    height = tft.height()
    halfw = int(width // 2)
    halfh = int(height // 2)
    y = 0
    for x in range(halfw):
        if y < halfh:
            y += 1
        tft.rect(x, y, width - 2 * x, height - 2 * y, st7789.CYAN)
        time.sleep(0.01)
    for x in range(halfw, 0, -1):
        if y > 1:
            y -= 1
        tft.rect(x, y, width - 2 * x, height - 2 * y, st7789.YELLOW)
        time.sleep(0.01)
        

def fill_rect_color(tft):
    width = tft.width()
    height = tft.height()
    for x in range(0, width, 2):
        tft.fill_rect(x, height // 2, 2, height // 2, st7789.CYAN)
        time.sleep(0.01)
    for y in range(0, height // 2, 2):
        tft.fill_rect(0, y, width, 2, st7789.GREEN)
        time.sleep(0.01)
        
def fd_circle_color(tft):
    width = tft.width()
    x = tft.width() // 2
    y = tft.height() // 2
    for r in range(x):
        tft.circle(x, y, r, st7789.color565(96, 67, 71))
    for r in range(y):
        tft.fill_circle(x, y, r, st7789.color565(87, 76, 76))
        
def center(text, tft):
    length = 1 if isinstance(text, int) else len(text)
    tft.text(
        font,
        text,
        tft.width() // 2 - length * font.WIDTH // 2,
        tft.height() // 2 - font.HEIGHT //2,
        st7789.BLACK,
        st7789.YELLOW)

def main():
    tft = tft_config.config(1)
    tft.init()
    tft.fill(st7789.YELLOW)
    time.sleep(1)
    on_off(tft)
    sleep_on_off(tft)
    pixel_color(tft)
    line_color(tft)
    hvline_color(tft)
    rect_color(tft)
    fill_rect_color(tft)
    fd_circle_color(tft)
    color(tft)
    tft.fill(st7789.YELLOW)
    center(b'Done!', tft)
    
    
main()
