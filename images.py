import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\samet\OneDrive\Belgeler\SametBlog\content\posts"
attachments_dir = r"C:\Users\samet\OneDrive\Belgeler\Obsidian Vault\0 - Attachments"
static_images_dir = r"C:\Users\samet\OneDrive\Belgeler\SametBlog\static\images"

# Create static images directory if it doesn't exist
os.makedirs(static_images_dir, exist_ok=True)

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links (handles ![[image.png]], [[image.png]], and sizes like |492)
        # Regex captures the filename in group 1, and matches the full string (including sizes) to replace it
        pattern = re.compile(r'!*\[\[(.*?\.(?:png|jpg|jpeg|gif|webp))(?:\|.*?)?\]\]', re.IGNORECASE)
        
        # Step 3: Iterate over matches and replace
        matches = list(pattern.finditer(content))
        
        for match in matches:
            full_match = match.group(0)       # e.g., ![[Pasted image 20260424.png|492]]
            image_filename = match.group(1)   # e.g., Pasted image 20260424.png
            
            # Prepare the Markdown-compatible link with %20 replacing spaces
            safe_url = image_filename.replace(' ', '%20')
            markdown_image = f"![{image_filename}](/images/{safe_url})"
            
            # Replace the old Obsidian link with the new standard Hugo link
            content = content.replace(full_match, markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image_filename)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully. Regex matched all parameters!")