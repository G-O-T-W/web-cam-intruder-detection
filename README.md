# Web Cam Intruder Detection

**Web Cam Intruder Detection** is a Python application that uses OpenCV to monitor a webcam for motion. When motion is detected, it captures an image and sends an email notification with the captured image attached. This project is useful for basic security surveillance.

## Features

- **Motion Detection**: Utilizes frame differencing and contour analysis to detect motion.
- **Image Capture**: Saves an image of the detected motion for evidence or review.
- **Email Alerts**: Sends an automated email with the captured image as an attachment.
- **Multi-threading**: Ensures smooth performance by separating email sending and folder cleanup into different threads.

## Technologies Used

- **Python**: Programming language used for the application logic.
- **OpenCV**: Library for real-time computer vision tasks.
- **SMTP (Email Protocol)**: For sending email notifications.
- **Threading**: Improves performance by running tasks concurrently.

## Project Structure

```plaintext
.
├── main.py        # The main application script
├── emailing.py    # Handles email notifications
├── images/        # Directory to store captured images
├── README.md      # Project documentation
```
## How It Works

1. The application uses a webcam to continuously monitor for motion.
2. When motion is detected:
   - An image is saved in the `images/` folder.
   - The image is sent as an email attachment to the configured recipient.
3. The `images/` folder is periodically cleaned to save storage space.

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/g-o-t-w/web-cam-intruder-detection.git
    cd web-cam-intruder-detection
   ```
2. Install the required Python libraries:
    ```bash
    pip install opencv-python-headless
    pip install opencv-python
    pip install numpy
   ```
3. Set up environment variables for email credentials:
    ```bash
    export EMAIL_SENDER="your_email@gmail.com"
    export EMAIL_RECEIVER="receiver_email@gmail.com"
    export EMAIL_PASSWORD="your_email_password"
   ```
## Usage
1. Run the application
    ```bash
    python main.py
   ```
2. Press ```q``` to exit the application.
