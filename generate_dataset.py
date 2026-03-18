import os
import random
from PIL import Image, ImageDraw, ImageFont

# Configuration
DATASET_DIR = "dataset"
REAL_DIR = os.path.join(DATASET_DIR, "real")
FAKE_DIR = os.path.join(DATASET_DIR, "fake")
NUM_SAMPLES = 50  # Number of samples per class

def setup_directories():
    if not os.path.exists(REAL_DIR):
        os.makedirs(REAL_DIR)
    if not os.path.exists(FAKE_DIR):
        os.makedirs(FAKE_DIR)

def generate_authentic_image(index):
    img = Image.new('RGB', (600, 400), color='white')
    d = ImageDraw.Draw(img)
    
    # Variations for authentic images
    font_color = 'black'
    
    d.text((50, 50), "OFFICIAL CERTIFICATE", fill=font_color)
    d.text((50, 100), f"This document certifies {random.randint(1000,9999)}", fill=font_color)
    d.text((50, 150), f"Name: User_{index}", fill=font_color)
    d.text((50, 200), "is validated.", fill=font_color)
    d.text((50, 300), "Signed: Authority", fill='darkblue')
    
    # Save
    img.save(os.path.join(REAL_DIR, f"real_{index}.png"))

def generate_fake_image(index):
    img = Image.new('RGB', (600, 400), color='white')
    d = ImageDraw.Draw(img)
    
    # Base text (looks like authentic)
    d.text((50, 50), "OFFICIAL CERTIFICATE", fill='black')
    d.text((50, 100), f"This document certifies {random.randint(1000,9999)}", fill='black')
    
    # Tampering: Changed font size/color slightly to simulate edit
    # OR adding a "patch"
    
    tamper_type = random.choice(['color', 'patch', 'alignment'])
    
    if tamper_type == 'color':
        # Name is slightly different color (pasted text simulation)
        d.text((50, 150), f"Name: User_{index}", fill=(20, 20, 20)) 
    elif tamper_type == 'patch':
        # White rectangle to hide something, then text over it
        d.rectangle([48, 148, 200, 165], fill='white', outline=None)
        d.text((50, 150), f"Name: User_{index}", fill='black')
    else:
        # Misalignment
        d.text((52, 152), f"Name: User_{index}", fill='black')

    d.text((50, 200), "is validated.", fill='black')
    d.text((50, 300), "Signed: Authority", fill='darkblue')
    
    # Add an obvious anomaly sometimes
    if random.random() > 0.5:
         d.rectangle([400, 300, 550, 350], outline="red", width=2)
         d.text((420, 315), "MODIFIED", fill='red')

    img.save(os.path.join(FAKE_DIR, f"fake_{index}.png"))

def main():
    print("Generating dataset...")
    setup_directories()
    
    for i in range(NUM_SAMPLES):
        generate_authentic_image(i)
        generate_fake_image(i)
        
    print(f"Dataset generated in '{DATASET_DIR}': {NUM_SAMPLES} real, {NUM_SAMPLES} fake.")

if __name__ == "__main__":
    main()
