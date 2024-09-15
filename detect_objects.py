import torch
import os
import shutil

# Load the model (YOLOv5 pretrained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Define the paths
frames_folder = 'D:/Drone_Git/drone-video-processing/Dataset/frames'  # Path to the folder containing frames
output_folder = 'D:/Drone_Git/drone-video-processing/Dataset/output'  # Path to save all processed images

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all the files in the frames folder
for frame_file in os.listdir(frames_folder):
    # Check if the file is an image (you can add more image extensions if needed)
    if frame_file.endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(frames_folder, frame_file)  # Full path to the image

        # Perform inference on the frame
        results = model(img_path)

        # Save the result in a temporary folder (as YOLOv5 saves results in a subfolder)
        temp_folder = "runs/detect/exp"  # YOLOv5 default save path
        results.save()  # This saves the result temporarily to "runs/detect/exp"

        # Move the processed image to the actual output folder
        for processed_file in os.listdir(temp_folder):
            src_file = os.path.join(temp_folder, processed_file)
            dst_file = os.path.join(output_folder, processed_file)
            shutil.move(src_file, dst_file)  # Move the file from temp to output folder

        # Clean up the temporary folder
        shutil.rmtree(temp_folder)

        print(f"Processed and saved results for {frame_file}")

print("Finished processing all frames.")
