# **VirtualMouse: Mouseless Cursor Control Using Hand Gestures**

### **Overview**
The **VirtualMouse** project enables hands-free control of your computer's cursor using just a camera and hand gestures, eliminating the need for a physical mouse. Powered by Python, OpenCV, and MediaPipe, this innovative solution tracks hand movements in real-time, allowing you to perform actions like cursor movement and left-clicking using intuitive gestures.

### **Features**
- **Cursor Movement**: The tip of your middle finger guides the movement of the on-screen cursor.
- **Left Click Gesture**: Perform a left-click by pinching your index finger and thumb together.

### **Technologies Used**
- **OpenCV**: Real-time image processing and hand tracking.
- **PyAutoGui**: Simulates mouse actions (moving the cursor, clicking).
- **MediaPipe**: Hand landmark detection and tracking.
- **Protobuf**: Manages serialized data for MediaPipe's hand detection models.

### **Installation**
Install the required Python libraries by running the following commands:

```bash
pip install opencv-python
pip install PyAutoGUI
pip install mediapipe
pip install protobuf
```

### **How to Use?**
1. Cursor Movement:
- The tip of your middle finger will control the cursor’s movement across the screen.
2. Left Click Gesture:
- Pinching the index finger and thumb together triggers a left-click action.
