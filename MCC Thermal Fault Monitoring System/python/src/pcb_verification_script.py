import time
import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# ── Pin Definitions ──────────────────────────────────────────
TEMPERATURE_GPIO = board.D27
BUTTON_1_GPIO = board.D20
BUTTON_2_GPIO = board.D21

# ── OLED Display Setup ────────────────────────────────────────
OLED_WIDTH  = 128
OLED_HEIGHT = 64  # use 32 if you have a 128x32 display

print("=" * 40)
print("Initialising OLED display at 0x3C...")
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=0x3C)

    # Clear the display
    oled.fill(0)
    oled.show()

    # Draw using Pillow
    image = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))
    draw  = ImageDraw.Draw(image)

    # Optional: load a TTF for nicer text, fallback to default bitmap font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except IOError:
        font = ImageFont.load_default()

    draw.text((0,  0), "Hello, OLED!", font=font, fill=255)
    draw.text((0, 16), "I2C: 0x3C",   font=font, fill=255)
    draw.text((0, 32), "GPIO D27 OK",  font=font, fill=255)
    draw.text((0, 48), "Btns: D20 D21",font=font, fill=255)

    oled.image(image)
    oled.show()
    print("  Display OK — content shown")

except Exception as e:
    print(f"  OLED ERROR: {e}")

# ── GPIO Temperature Sensor Pin Test ─────────────────────────
print("=" * 40)
print("Testing temperature sensor GPIO pin...")
try:
    temp_pin = digitalio.DigitalInOut(TEMPERATURE_GPIO)
    temp_pin.direction = digitalio.Direction.INPUT
    state = temp_pin.value
    print(f"  GPIO D27 state: {state}")

    # Update display with live reading
    draw.rectangle((0, 48, OLED_WIDTH, OLED_HEIGHT), fill=0)  # clear last line
    draw.text((0, 48), f"D27: {'HIGH' if state else 'LOW'}", font=font, fill=255)
    oled.image(image)
    oled.show()

    temp_pin.deinit()
except Exception as e:
    print(f"  GPIO ERROR: {e}")

# ── Button Test with live OLED feedback ───────────────────────
print("=" * 40)
print("Testing buttons — polling 10 s, display updates live...")
try:
    button_1 = digitalio.DigitalInOut(BUTTON_1_GPIO)
    button_1.direction = digitalio.Direction.INPUT
    button_1.pull = digitalio.Pull.DOWN

    button_2 = digitalio.DigitalInOut(BUTTON_2_GPIO)
    button_2.direction = digitalio.Direction.INPUT
    button_2.pull = digitalio.Pull.DOWN

    start = time.time()
    while time.time() - start < 10:
        b1 = button_1.value
        b2 = button_2.value

        # Refresh only the button status line to avoid full redraws
        draw.rectangle((0, 48, OLED_WIDTH, OLED_HEIGHT), fill=0)
        status = f"B1:{'ON' if b1 else '--'} B2:{'ON' if b2 else '--'}"
        draw.text((0, 48), status, font=font, fill=255)
        oled.image(image)
        oled.show()

        if b1: print("  Button 1 PRESSED (D20)")
        if b2: print("  Button 2 PRESSED (D21)")
        time.sleep(0.1)

except Exception as e:
    print(f"  Button ERROR: {e}")
finally:
    button_1.deinit()
    button_2.deinit()

# ── Done ──────────────────────────────────────────────────────
draw.rectangle((0, 0, OLED_WIDTH, OLED_HEIGHT), fill=0)
draw.text((0, 20), "  Tests complete", font=font, fill=255)
oled.image(image)
oled.show()

print("=" * 40)
print("All tests complete.")