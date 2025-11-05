# 🤖 AI Robotic Arm using OpenCV and Arduino

This project demonstrates a **vision-based robotic arm** that detects **hand gestures** in real time using **OpenCV and MediaPipe** in Python and controls **servo motors** through an Arduino board.

It’s an integration of **Computer Vision**, **Python**, and **Embedded Systems**, showing how human gestures can directly control robotic movement — a simple step toward *human-machine interaction and automation*.

---

## 🚀 Features
- Real-time hand tracking using **MediaPipe Hands**.
- Gesture-based control of a **5-DOF servo-based robotic arm**.
- Communication between **Python (vision)** and **Arduino (actuation)** via **Serial (UART)**.
- Modular and easily extendable design.
- Lightweight — works on basic laptops and standard Arduino Uno/Nano.

---

## 🧠 Project Overview

| Module | Description |
|:-------|:-------------|
| **Python (PC)** | Captures webcam video feed, detects finger states (open/closed) using MediaPipe, and sends binary data to Arduino. |
| **Arduino (Microcontroller)** | Receives binary data over serial and actuates 5 servo motors (one for each finger). |
| **Mechanical Setup** | 5-finger robotic arm made using servo motors and 3D printed or acrylic finger links. |

**Finger Mapping:**
```
[Thumb, Index, Middle, Ring, Pinky]
```
Each value sent from Python is `1` (finger open) or `0` (finger closed).

---

## 🖼️ System Architecture

```
 ┌──────────────┐
 │   Webcam     │
 └──────┬───────┘
        │  (Video Feed)
        ▼
 ┌──────────────┐
 │  Python +    │
 │  OpenCV +    │
 │  MediaPipe   │
 └──────┬───────┘
        │  (Serial Data: 1,0,1,0,1)
        ▼
 ┌──────────────┐
 │   Arduino    │
 │   UNO/Nano   │
 └──────┬───────┘
        │  (PWM Signal)
        ▼
 ┌──────────────┐
 │ Servo Motors │
 └──────────────┘
```

---

## 🧩 Components Required

| Component | Quantity | Description |
|------------|-----------|-------------|
| Arduino Uno / Nano | 1 | Controls the servos |
| SG90 / MG90S Servos | 5 | One for each finger |
| Jumper Wires | As required | For connections |
| External 5V Power Supply | 1 | For servo motors |
| Webcam | 1 | For hand tracking |
| Computer with Python | 1 | Runs OpenCV & MediaPipe |

---

## ⚙️ Circuit Connections

| Servo | Arduino Pin |
|--------|--------------|
| Thumb | D7 |
| Index | D8 |
| Middle | D9 |
| Ring | D10 |
| Pinky | D11 |

> **Note:** Connect all servo GNDs to the Arduino GND. If using an external power source, **connect the grounds together**.

---

## 💻 Software Setup

### 1. Install Python Dependencies
```bash
pip install opencv-python mediapipe pyserial
```

### 2. Upload Arduino Code
Upload the file `robotic_hand_servos.ino` to your Arduino using the **Arduino IDE**.

### 3. Run the Python Script
Make sure to replace `COM5` with the correct port of your Arduino.

```bash
python hand_to_arduino.py
```

> **Press ESC** to exit the program safely.

---

## 🧾 File Structure

```
AI_Robotic_Arm/
│
├── hand_to_arduino.py          # Python hand-tracking + serial communication
├── robotic_hand_servos.ino     # Arduino servo control program
├── README.md                   # Project documentation (this file)
└── media/                      # Images, diagrams, and videos (optional)
```

---

## 🪄 Gesture Mapping Example

| Gesture | Binary Pattern | Action |
|----------|----------------|--------|
| ✊ Fist Closed | 0,0,0,0,0 | All servos at 0° |
| 🖐️ All Fingers Open | 1,1,1,1,1 | All servos at 180° |
| ☝️ Index Only | 0,1,0,0,0 | Index servo moves to 180° |
| 👍 Thumbs Up | 1,0,0,0,0 | Thumb only at 180° |

---

## 🧰 Troubleshooting

| Issue | Possible Cause | Solution |
|--------|----------------|-----------|
| Servo not moving | Wrong COM port | Check `COMx` in Device Manager |
| Python not detecting hand | Low lighting | Improve lighting or adjust webcam angle |
| Servo jittering | Power issue | Use external 5V supply with common ground |
| Thumb movement reversed | Hand orientation | Flip logic using `results.multi_handedness` |

---

## 📷 Demo

> *(Add an image or GIF here showing your arm in action)*

```markdown
![AI Robotic Arm Demo](media/demo.gif)
```

---

## 🧩 Future Improvements
- Add **angle mapping** (proportional servo movement instead of binary open/close).  
- Implement **handedness detection** for left/right hand.  
- Add **Bluetooth/WiFi control** for wireless robotic arm operation.  
- Integrate with **ROS (Robot Operating System)** for advanced robotics applications.

---

## 🧑‍💻 Author
**Anisha Patnaik**  
B.Tech – Electrical Engineering  
[Veer Surendra Sai University of Technology (VSSUT), Burla]  
🌐 *Developed as part of AI & Robotics exploration project.*

---

## 🪪 License
This project is open-source and available under the **MIT License**.

```
MIT License © 2025 Anisha Patnaik
```

---

⭐ **If you like this project, give it a star on GitHub!**
