# YOLO Object Detection with Streamlit

This project demonstrates real-time object detection using the **YOLOv8 model** and displays the results in a **Streamlit** web interface. The application uses a live video feed from a webcam to detect objects and draws bounding boxes with class labels and confidence scores.

---

## Features

- **Real-Time Object Detection**:
  - Utilizes **YOLOv8** for high-accuracy object detection.
- **Streamlit Integration**:
  - Web-based UI for controlling the video stream and viewing detection results.
- **Dynamic Bounding Boxes**:
  - Bounding boxes with color-coded labels based on object classes.
- **Confidence Threshold**:
  - Filters detections with confidence scores below a defined threshold.

---

## Prerequisites

### 1. Install Required Libraries
Install the dependencies using:
```bash
pip install ultralytics opencv-python-headless streamlit numpy
```

### 2. Download YOLOv8 Model Weights
Ensure you have the YOLOv8 weights file (`yolov8s.pt`). You can download it from the [Ultralytics YOLO GitHub Repository](https://github.com/ultralytics/ultralytics).

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/PratikMitkar/codealpha_tasks_4.git
cd codealpha_tasks_4
```

### 2. Start the Streamlit Application
Run the Streamlit app:
```bash
streamlit run object_detection_task_4.py
```

### 3. Control the Video Stream
- Click **Start Video Stream** to begin object detection.
- Click **Stop Video Stream** to stop the video feed.

### 4. Quit the Application
- Press the `q` key to exit the program at any time.

---

## Program Walkthrough

1. **Model Loading**:
   - Loads the **YOLOv8 small model (`yolov8s.pt`)** using the `ultralytics` library.

2. **Web Interface**:
   - Provides **Start** and **Stop** buttons for controlling the video stream.
   - Displays the video feed with bounding boxes in real-time.

3. **Object Detection**:
   - Processes each video frame to detect objects.
   - Draws bounding boxes around detected objects with:
     - **Class Name**: Object type (e.g., person, car).
     - **Confidence Score**: Detection confidence.
     - **Dynamic Colors**: Unique colors for each class.

4. **Video Handling**:
   - Captures video from the default webcam.
   - Uses OpenCV for frame processing.

---

## Example Output

### Streamlit Interface
- Displays a live video feed with real-time detection.
- Objects are labeled with confidence scores, and bounding boxes are drawn dynamically.

### Sample Detection
- **Person**: Bounding box with label and confidence score.
- **Car**: Bounding box with a distinct color and label.

---

## Customization

### Confidence Threshold
Adjust the confidence threshold for detections by modifying:
```python
if box.conf[0] > 0.4:  # Confidence threshold
```

### Detection Colors
Colors for classes are dynamically generated based on class indices. Customize the `getColours` function to modify color schemes.

### Detection Classes
The program automatically supports all classes defined in the YOLO model. To restrict detection to specific classes, you can filter them in the detection loop.

---

## Troubleshooting

1. **Camera Not Detected**:
   - Ensure your webcam is properly connected and accessible.
   - Change the video capture device index if needed:
     ```python
     videoCap = cv2.VideoCapture(0)  # Replace 0 with 1 or higher for other cameras
     ```

2. **Slow Performance**:
   - Use a lighter YOLO model (e.g., `yolov8n.pt`).
   - Reduce the video resolution for faster processing.

3. **Streamlit Not Loading**:
   - Ensure all dependencies are installed.
   - Run the app in a Python environment compatible with Streamlit.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for bug fixes, new features, or improvements.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- Built with the **Ultralytics YOLO** library.
- Inspired by the power of real-time object detection and Streamlit's simplicity.

---

Enjoy real-time object detection with YOLO and Streamlit! 🚀
