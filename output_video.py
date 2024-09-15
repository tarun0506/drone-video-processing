import cv2
import os

# Define the folder containing the output frames and the path to save the video
frames_folder = 'D:/Drone_Git/drone-video-processing/Dataset/output'  # Folder with processed frames
output_video = 'D:/Drone_Git/drone-video-processing/Dataset/output_video_2.mp4'  # Path to save the final video

# Get the list of frames in the folder
frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith(('.jpg', '.jpeg', '.png'))])

# Ensure there are frames to process
if len(frame_files) == 0:
    print("No frames found in the output folder.")
    exit()

# Load the first frame to get the frame size
first_frame = cv2.imread(os.path.join(frames_folder, frame_files[0]))
height, width, layers = first_frame.shape

# Set a reasonable FPS for smooth playback, then slow down by duplicating frames
fps = 10  # Reasonable FPS for smooth playback

# Define the codec and create VideoWriter object to write the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Loop through each frame and write it to the video
for frame_file in frame_files:
    frame_path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(frame_path)

    # Check if the frame is loaded correctly
    if frame is None:
        print(f"Warning: Could not read frame {frame_file}")
        continue

    # Write the same frame multiple times to make the video slower and smoother
    for _ in range(10):  # Increase the number to make the video slower
        video_writer.write(frame)

# Release the VideoWriter object
video_writer.release()

print(f"Video saved as {output_video}")
