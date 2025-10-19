# **Uvic Mining Club**

## Project Description

The purpose of this project is to design and develop a preventive maintenance system for Motor Control Center (MCC) units. The system will enable early detection of thermal hotspots (referred to as “spotting”) on the internal wiring of 600V MCC units. By identifying anomalies before failure occurs, this solution aims to improve equipment reliability, extend asset lifespan, and reduce downtime.

## Table of Contents

- [Installation](#installation)

## Installation

1. Install Raspberry Pi OS Lite on your Raspberry Pi. -> likely need a microSD card.

   - Follow the official guide: [Raspberry Pi OS Installation](https://www.raspberrypi.com/software/)

2. Wire in the MLX90640 Thermal Camera to the Raspberry Pi using I2C interface.

   - Refer to the [MLX90640 Datasheet](./docs/MLX90640-Datasheet-Melexis.pdf) for pin connections.
   - Refer to the [Raspberry Pi Guide](../docs/raspberry-pi-zero-2-w-reduced-schematics.pdf)

3. SSH into the Raspberry Pi from your computer after it has been powered on.

4. Set up the software environment on the Raspberry Pi:

   Run the following commands in the terminal of the Raspberry Pi:

   ```bash
   git clone <repository_url>

   sudo raspi-config         // Enable I2C interface under Interfacing Options
   sudo reboot

   sudo apt update
   sudo apt install -y i2c-tools python3-smbus python3-pip

   sudo i2cdetect -y 1       // Verify camera connection, should show 0x33

   cd MMC%20Thermal%20Fault%20Monitoring%20System/python/
   python3 -m venv venv    // Create virtual environment   source venv/bin/activate    // Activate virtual environment
   pip3 install -e .         // Install required python packages
   ```

5. Run the main application:

   ```bash
   python3 src/main.py
   ```
