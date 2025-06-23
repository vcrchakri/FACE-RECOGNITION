# Face Recognition with DeepFace

This project uses OpenCV and DeepFace to perform real-time face recognition using your webcam. It compares faces detected in the webcam feed to a reference image (`reference.jpg`) and displays whether there is a match.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- DeepFace
- A reference image named `reference.jpg` in the project directory

## Installation

1. Install dependencies:
    ```sh
    pip install opencv-python deepface
    ```

2. Place your reference image as `reference.jpg` in the project folder.

## Usage

Run the script:

```sh
python face_recogni.py
```

- The webcam will open and start face recognition.
- "Face Match" will be displayed if the detected face matches the reference image.
- "No Match" will be displayed otherwise.
- Press `q` to quit.

## Files

- `face_recogni.py` - Main script for face recognition.
- `reference.jpg` - Reference image for face comparison.

## Notes

- Make sure your webcam is connected.
- The script checks for a face match every 30 frames for efficiency.
