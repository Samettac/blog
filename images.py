import os
import re
import shutil
import urllib.parse # %20 (boşluk) URL formatını Windows'un anlayacağı formata çevirmek için eklendi

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\samet\OneDrive\Belgeler\SametBlog\content\posts"
attachments_dir = r"C:\Users\samet\OneDrive\Belgeler\Obsidian Vault\0 - Attachments"
static_images_dir = r"C:\Users\samet\OneDrive\Belgeler\SametBlog\static\images"

# Create static images directory if it doesn't exist
os.makedirs(static_images_dir, exist_ok=True)

# --- CALLOUT DÖNÜŞTÜRÜCÜ FONKSİYON ---
def format_callout(match):
    ctype = match.group('type').lower()
    title = match.group('title').strip()
    
    icons = {
        'note': '📝', 'info': '💡', 'warning': '⚠️',
        'danger': '🛑', 'error': '🛑', 'tip': '🎯',
        'success': '✅', 'question': '❓', 'example': '📋',
        'quote': '💬'
    }
    
    translations = {
        'note': 'NOT', 'info': 'BİLGİ', 'warning': 'UYARI',
        'danger': 'TEHLİKE', 'error': 'HATA', 'tip': 'İPUCU',
        'success': 'BAŞARILI', 'question': 'SORU', 'example': 'ÖRNEK',
        'quote': 'ALINTI'
    }
    
    icon = icons.get(ctype, '📌')
    display_title = title if title else translations.get(ctype, ctype.upper())
    
    return f"> {icon} **{display_title}**"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # --- IMAGE PROCESSING 1: Obsidian Wikilinks ( ![[resim.png]] ) ---
        wiki_pattern = re.compile(r'!*\[\[(.*?\.(?:png|jpg|jpeg|gif|webp))(?:\|.*?)?\]\]', re.IGNORECASE)
        wiki_matches = list(wiki_pattern.finditer(content))
        
        for match in wiki_matches:
            full_match = match.group(0)
            image_filename = match.group(1)
            
            safe_url = image_filename.replace(' ', '%20')
            markdown_image = f"![{image_filename}](/images/{safe_url})"
            content = content.replace(full_match, markdown_image)
            
            image_source = os.path.join(attachments_dir, image_filename)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # --- IMAGE PROCESSING 2: Standard Markdown Links ( ![](resim.png) ) ---
        md_pattern = re.compile(r'!\[(.*?)\]\((.*?\.(?:png|jpg|jpeg|gif|webp))\)', re.IGNORECASE)
        md_matches = list(md_pattern.finditer(content))
        
        for match in md_matches:
            full_match = match.group(0)
            alt_text = match.group(1)
            image_url = match.group(2) # Örn: "Pasted%20image%20123.png"
            
            # URL'deki %20'leri gerçek boşluğa çevir ki Windows dosyayı bulabilsin
            real_filename = urllib.parse.unquote(image_url) 
            
            # Eğer yolda klasör falan varsa sadece dosya adını al
            real_filename = os.path.basename(real_filename)
            
            # Hugo için URL'yi güvenli formata (%20'li) geri çevir ve `/images/` yolunu ekle
            safe_url = real_filename.replace(' ', '%20')
            markdown_image = f"![{alt_text}](/images/{safe_url})"
            content = content.replace(full_match, markdown_image)
            
            image_source = os.path.join(attachments_dir, real_filename)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # --- CALLOUT / ADMONITION PROCESSING ---
        callout_pattern = re.compile(r'^>\s*\[!(?P<type>[a-zA-Z]+)\](?P<title>.*)$', re.MULTILINE)
        content = callout_pattern.sub(format_callout, content)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed: Images and Callouts formatted successfully!")