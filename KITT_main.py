#MicroPython
import time
from machine import Pin
import neopixel

# Configuration
NUM_LEDS = 16  # Number of LEDs in the NeoPixel Stick
DATA_PIN = 16   # GPIO pin connected to NeoPixel Stick
SEGMENT_SIZE = 4  # Number of LEDs lit at a time

# Initialize NeoPixel Stick
led_strip = neopixel.NeoPixel(Pin(DATA_PIN, Pin.OUT), NUM_LEDS)

def set_leds(position):
    """Set only four LEDs at the given position."""
    for i in range(NUM_LEDS):
        if position <= i < position + SEGMENT_SIZE:
            led_strip[i] = (50, 0, 0)  # Red color with max brightness 50
        else:
            led_strip[i] = (0, 0, 0)  # Turn off other LEDs
    led_strip.write()

def knight_rider():
    """Knight Rider effect with four LEDs moving left to right and back."""
    position = 0
    direction = 1  # 1 for right, -1 for left
    
    while True:
        set_leds(position)
        time.sleep(0.1)
        
        position += direction
        
        # Change direction when reaching the ends
        if position == 0 or position == NUM_LEDS - SEGMENT_SIZE:
            direction *= -1

# Run the effect
knight_rider()
