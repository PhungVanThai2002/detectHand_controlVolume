# Hand Gesture Volume Control

A computer vision application that allows users to control the Windows system volume using hand gestures captured through a webcam.

The project uses **OpenCV** and **MediaPipe Hands** to detect hand landmarks. The distance between the thumb and index finger is mapped to the computer's master volume using **Pycaw**.

## Project Overview

This project provides a touch-free way to control audio volume:

- Move the thumb and index finger closer together to decrease the volume.
- Move them farther apart to increase the volume.
- Press `Q` to exit the application.

The project does not require custom model training. It uses the hand landmark detection solution provided by MediaPipe.

## How It Works

The application follows these steps:

1. Capture live video from the webcam using OpenCV.
2. Convert the image from BGR to RGB.
3. Detect the user's hand with MediaPipe Hands.
4. Extract the coordinates of:
   - Thumb tip — landmark `4`
   - Index finger tip — landmark `8`
5. Calculate the distance between the two fingertips.
6. Map the distance to the available system volume range.
7. Change the Windows master volume using Pycaw.
8. Display the detected hand, fingertip positions, connection line, and FPS.

```text
Webcam
   ↓
OpenCV video capture
   ↓
MediaPipe hand landmark detection
   ↓
Distance between thumb and index finger
   ↓
Distance-to-volume mapping
   ↓
Windows master volume control
```

## Features

- Real-time hand detection
- Hand landmark tracking
- Gesture-based volume control
- Live webcam preview
- FPS display
- Visual feedback for thumb and index finger positions
- Keyboard control to exit the application

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Main programming language |
| OpenCV | Webcam access and image processing |
| MediaPipe Hands | Hand and landmark detection |
| NumPy | Distance-to-volume interpolation |
| Pycaw | Windows audio volume control |
| Comtypes | Communication with the Windows Core Audio API |

## Project Structure

```text
detectHand_controlVolume/
├── volume_control.py
├── HandTrackingModule_new.py
├── HandTrackingMin.py
└── .idea/
```

### Main Files

| File | Description |
| --- | --- |
| `volume_control.py` | Main application for gesture-based volume control |
| `HandTrackingModule_new.py` | Reusable hand detection and landmark tracking module |
| `HandTrackingMin.py` | Basic MediaPipe hand tracking demonstration |

## Requirements

- Windows operating system
- Python 3.7 or later
- A working webcam
- Working system audio output
- Permission to access the camera

The project uses `Pycaw`, which is designed for controlling audio on Windows.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/PhungVanThai2002/detectHand_controlVolume.git
cd detectHand_controlVolume
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or on Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install opencv-python mediapipe numpy pycaw comtypes
```

## Run the Application

Run the main script:

```bash
python volume_control.py
```

A webcam window will open. Show one hand in front of the camera and move the thumb and index finger:

- Fingers close together → lower volume
- Fingers farther apart → higher volume
- Press `Q` → close the application

## Gesture-to-Volume Mapping

The application calculates the Euclidean distance between the thumb and index finger.

```python
length = math.hypot(x2 - x1, y2 - y1)
```

The distance is then mapped to the Windows volume range:

```python
vol = np.interp(
    length,
    [50, 300],
    [minVol, maxVol]
)
```

When the distance is close to `50` pixels, the volume approaches the minimum level. When the distance approaches `300` pixels, the volume approaches the maximum level.

## Limitations

- The current audio control implementation works primarily on Windows.
- The application requires access to a webcam.
- Performance may be affected by poor lighting or partial hand visibility.
- The project currently supports one main hand for volume control.
- There is no graphical settings panel for changing sensitivity or volume ranges.
- The repository does not include a `requirements.txt` file; dependencies must currently be installed manually.

## Possible Improvements

- Add a `requirements.txt` file.
- Add support for macOS and Linux audio systems.
- Add gesture recognition for mute and unmute.
- Add a graphical user interface.
- Allow users to configure gesture sensitivity.
- Support multiple hand gestures and custom commands.
- Improve error handling when the camera or audio device is unavailable.

## Use Cases

This project demonstrates how computer vision and human-computer interaction can be combined to create touch-free interfaces. Potential applications include:

- Accessibility tools
- Smart multimedia controls
- Touchless presentations
- Interactive installations
- Assistive technology
- Gesture-based computer interfaces

## License

No license has been specified for this repository yet. Add a license file before redistributing or using the project commercially.
