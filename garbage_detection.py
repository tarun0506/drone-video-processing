import cv2
import os
import time

# Define paths
dataset_folder = "Dataset"  # Path to the folder containing the video
video_file = "DJI_20240905151401_0007_D_FLYING.mp4"  # Name of your video file

# Create full path to the video
video_path = os.path.join(dataset_folder, video_file)

# Create a directory to save frames if it doesn't exist
frames_folder = os.path.join(dataset_folder, "frames")
os.makedirs(frames_folder, exist_ok=True)  # Create the frames folder if it doesn't exist

# Load the video
cap = cv2.VideoCapture(video_path)

# Check if the video loaded successfully
if not cap.isOpened():
    print(f"Error: Could not open video {video_path}")
    exit()

frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
frame_count = 0

start_time = time.time()  # Start timing

# Loop to read and save frames
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_count += 1
        if frame_count % int(frame_rate) == 0:
            # Save frame to the frames folder
            frame_file = os.path.join(frames_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_file, frame)
            print(f"Saved {frame_file}")
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

end_time = time.time()  # End timing
print(f"Processing time: {end_time - start_time} seconds")
