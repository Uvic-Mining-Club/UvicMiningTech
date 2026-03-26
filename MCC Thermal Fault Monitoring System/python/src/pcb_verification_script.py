import time
import board
import busio
import digitalio

# ── Pin Definitions ──────────────────────────────────────────
# GPIO 27 = Physical Pin 13
TEMPERATURE_GPIO = board.D27

# GPIO 5  = Physical Pin 29
# GPIO 6  = Physical Pin 31
BUTTON_1_GPIO = board.D20
BUTTON_2_GPIO = board.D21

# ── I2C Test ─────────────────────────────────────────────────
print("=" * 40)
print("Testing I2C bus...")
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    while not i2c.try_lock():
        pass
    try:
        devices = i2c.scan()
        if devices:
            print(f"  I2C devices found: {[hex(d) for d in devices]}")
        else:
            print("  No I2C devices found")
    finally:
        i2c.unlock()
        i2c.deinit()
except Exception as e:
    print(f"  I2C ERROR: {e}")

# ── SPI Test ──────────────────────────────────────────────────
# SPI has no scan — we just verify the bus initialises cleanly
print("=" * 40)
print("Testing SPI bus...")
try:
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    while not spi.try_lock():
        pass
    try:
        spi.configure(baudrate=8_000_000, phase=0, polarity=0)
        # Send a known byte and see if we get any response
        # With no device connected you'll get 0x00 or 0xFF
        result = bytearray(1)
        spi.write_readinto(bytes([0xFF]), result)
        print(f"  SPI bus OK — loopback byte: 0x{result[0]:02X}")
        print("  (0x00 or 0xFF with no device connected is normal)")
    finally:
        spi.unlock()
        spi.deinit()
except Exception as e:
    print(f"  SPI ERROR: {e}")

# ── GPIO Temperature Sensor Pin Test ─────────────────────────
print("=" * 40)
print("Testing temperature sensor GPIO pin...")
try:
    temp_pin = digitalio.DigitalInOut(TEMPERATURE_GPIO)
    temp_pin.direction = digitalio.Direction.INPUT
    print(f"  GPIO D27 (Physical Pin 13) state: {temp_pin.value}")
    temp_pin.deinit()
except Exception as e:
    print(f"  GPIO ERROR: {e}")

# ── Button Test ───────────────────────────────────────────────
# Active HIGH buttons — use Pull.DOWN so idle state reads False
print("=" * 40)
print("Testing buttons (active HIGH) on D5 and D6...")
print("Polling for 10 seconds — press each button to test")
try:
    button_1 = digitalio.DigitalInOut(BUTTON_1_GPIO)
    button_1.direction = digitalio.Direction.INPUT
    button_1.pull = digitalio.Pull.DOWN

    button_2 = digitalio.DigitalInOut(BUTTON_2_GPIO)
    button_2.direction = digitalio.Direction.INPUT
    button_2.pull = digitalio.Pull.DOWN

    start = time.time()
    while time.time() - start < 10:
        if button_1.value:
            print("  Button 1 PRESSED (D5 / Physical Pin 29)")
        if button_2.value:
            print("  Button 2 PRESSED (D6 / Physical Pin 31)")
        time.sleep(0.1)

except Exception as e:
    print(f"  Button ERROR: {e}")
finally:
    button_1.deinit()
    button_2.deinit()

print("=" * 40)
print("All tests complete.")