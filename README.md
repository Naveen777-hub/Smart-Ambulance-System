# 🚑 Smart Ambulance System

An AI-powered system to detect vehicle violations and ensure emergency vehicle clearance.

## Features
- Real-time serial communication (ESP32 + NRF)
- Automated image capture using Raspberry Pi Camera
- Lightweight AI-based vehicle detection
- Intelligent filtering to avoid false captures
- Logging system for event tracking

## Tech Stack
- Python
- OpenCV
- Raspberry Pi
- ESP32 + NRF24L01

## Workflow
1. Receiver detects vehicle status
2. Sends signal to Raspberry Pi
3. Camera captures image
4. AI checks for vehicle presence
5. Valid violations stored & processed

## Future Work
- Cloud integration
- Flask dashboard
- Automatic challan system
