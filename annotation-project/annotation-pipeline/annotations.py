import os
import time

print("Starting Annotation Script...")

# 1. Get the input filename
input_file = os.environ.get('S3_KEY', 'unknown.json')
print(f"Processing input: {input_file}")

# 2. Simulate FFmpeg usage
print("Checking FFmpeg version...")
os.system("ffmpeg -version")

# 3. Create Output Directories
os.makedirs("frames", exist_ok=True)
os.makedirs("predict", exist_ok=True)

# 4. Create Dummy Files (Fixing the empty folder error)
with open("frames/frame1.jpg", "w") as f:
    f.write("This is a dummy image file")

# --- ADD THIS PART ---
with open("predict/prediction_result.txt", "w") as f:
    f.write("This is a dummy prediction")
# ---------------------

with open("inspection.csv", "w") as f:
    f.write("id,status\n1,ok")

print("Processing Complete. Files created.")
