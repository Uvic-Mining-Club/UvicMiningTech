# Uvic Mining Club Design Document

## Introduction / Project Overview

Short description of the system.

## Table of Contents

- [Design Diagram](#design-diagram-&-highlevel-overveiw)
- [Tech Stack](#tech-stack)
  - [Software](#software)
  - [Hardware](#hardware)

## Design Diagram & Highlevel Overview

- I/O primary cat 5 or cat 6 ethernet
  - maybe make some consideration for how much power ethernet with require.

## Project Breakdown

### Software

### Mech

### Elec

## Tech Stack

### Software

#### Libaries -> Dependency List

- i2c-tools python3-smbus python3-pip

#### OS -> Raspberry Pi OS Lite

- Lightweight linux distribution optimized for the Raspberry Pi hardware platform. runs headless (no GUI) to conserve system resources.
- [Raspberry Pi OS](https://www.raspberrypi.com/software/)

### Hardware

#### Camera -> MLX90640 Thermal Camera Wide Angle

##### Features

- 32 x 24 pixels
- I2C Interface
- 0.1°C temperature resolution
- -40°C to 300°C temperature range
- [datasheet](./docs/MLX90640-Datasheet-Melexis.pdf)

##### Quick Reference Pin Guide

| Pin Number | Pin Name | Description         | Conroller Connection     |
| ---------- | -------- | ------------------- | ------------------------ |
| 1          | VDD      | Power Supply (3.3V) | Raspberry Pi 3.3V        |
| 2          | SDA      | I2C Data            | Raspberry Pi GPIO 2      |
| 3          | SCL      | I2C Clock           | Raspberry Pi GPIO 3      |
| 4          | NSS      | Reset               | Any GPIO (Non-essential) |
| 5          | GND      | Ground              | GND                      |

#### Controller -> Raspberry Pi Zero 2 W

- [datasheet](./docs/Raspberry-Pi-Zero-2-W-Product-Brief.pdf)
- [pin-map](./docs/raspberry-pi-zero-2-w-reduced-schematics.pdf)
- [test-pads](./docs/raspberry-pi-zero-2-w-test-pads.pdf)
