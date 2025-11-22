import os
import time

print("Starting Annotation Script...")

# 1. Get the input filename
input_file = os.environ.get('S3_KEY', 'unknown.json')
print(f"Processing input: {input_file}")

# 2. Simulate FFmpeg usage (We just print it to prove it's installed)
print("Checking FFmpeg version...")
os.system("ffmpeg -version")

# 3. Create Dummy Output Files
os.makedirs("frames", exist_ok=True)
os.makedirs("predict", exist_ok=True)

# Create a fake image
with open("frames/frame1.jpg", "w") as f:
    f.write("This is a dummy image file")

# Create a fake CSV
with open("inspection.csv", "w") as f:
    f.write("id,status\n1,ok")

print("Processing Complete. Files created.")
