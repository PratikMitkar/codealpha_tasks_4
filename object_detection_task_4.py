import cv2
from ultralytics import YOLO
import streamlit as st
import numpy as np
import time

# Load the model
yolo = YOLO('yolov8s.pt')

# Streamlit UI setup
st.title("YOLO Object Detection")
start_button = st.button("Start Video Stream")
stop_button = st.button("Stop Video Stream")

# Function to get class colors
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
             (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)

# Video capture setup
videoCap = cv2.VideoCapture(0)

# Streamlit UI for control
frame_placeholder = st.empty()  # Placeholder for video stream

if start_button:
    while True:
        ret, frame = videoCap.read()
        if not ret:
            continue
        
        # Detect objects
        results = yolo.track(frame, stream=True)

        for result in results:
            # Get class names
            classes_names = result.names

            for box in result.boxes:
                if box.conf[0] > 0.4:  # Confidence threshold
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Get the class index
                    cls = int(box.cls[0])

                    # Get the class name
                    class_name = classes_names[cls]

                    # Get the respective color for the class
                    color = getColours(cls)

                    # Draw bounding box and label on the image
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, f'{class_name} {box.conf[0]:.2f}', (x1, y1),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # Convert frame to RGB for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display frame on Streamlit
        frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

        # Handle stop condition with the stop button
        if stop_button:
            st.warning("Video stream stopped.")
            break

        # Handle exit condition when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close OpenCV windows
videoCap.release()
cv2.destroyAllWindows()
