from PIL import Image, ImageDraw, ImageFont
import os

def create_test_images():
    # Ensure directory exists
    if not os.path.exists('test_documents'):
        os.makedirs('test_documents')

    # 1. Create 'Original' Image
    img_orig = Image.new('RGB', (600, 400), color='white')
    d_orig = ImageDraw.Draw(img_orig)
    # Draw some text
    d_orig.text((50, 50), "OFFICIAL CERTIFICATE", fill='black')
    d_orig.text((50, 100), "This document certifies that", fill='black')
    d_orig.text((50, 150), "John Doe", fill='black')
    d_orig.text((50, 200), "is the owner of this property.", fill='black')
    d_orig.text((50, 300), "Signed: Autority", fill='darkblue')
    
    img_orig.save('test_documents/original_document.png')
    print("Created test_documents/original_document.png")

    # 2. Create 'Forged' Image (Fake)
    img_fake = Image.new('RGB', (600, 400), color='white')
    d_fake = ImageDraw.Draw(img_fake)
    # Draw original looking text
    d_fake.text((50, 50), "OFFICIAL CERTIFICATE", fill='black')
    d_fake.text((50, 100), "This document certifies that", fill='black')
    
    # Change the name with a slightly different 'color' or 'position' to simulate edit
    # In a real scenario, we'd analyze metadata or pixel inconsistencies.
    d_fake.text((50, 150), "Jane Smith", fill='black') # Changed name
    
    d_fake.text((50, 200), "is the owner of this property.", fill='black')
    d_fake.text((50, 300), "Signed: Autority", fill='darkblue')
    
    # Add a visible "stamp" or mark that looks suspicious
    d_fake.rectangle([400, 300, 550, 350], outline="red", width=3)
    d_fake.text((420, 315), "URGENT", fill='red')

    img_fake.save('test_documents/forged_document.png')
    print("Created test_documents/forged_document.png")

if __name__ == "__main__":
    create_test_images()