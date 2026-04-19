#!/usr/bin/env python3
"""
Generate PWA icons for Athletics Softball Lineup app.
Creates vibrant blue/purple/cyan icons with an 'A' logo.
Requires PIL (pillow): pip install pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    # Vibrant New Colors
    PURPLE = (102, 126, 234)  # #667eea
    CYAN = (0, 242, 254)  # #00f2fe
    BLUE = (79, 172, 254)  # #4facfe
    DARK_PURPLE = (30, 27, 75)  # #1e1b4b
    
    def create_icon(size, filename):
        """Create a square icon with Athletics branding"""
        # Create gradient background (purple to blue)
        img = Image.new('RGB', (size, size), PURPLE)
        draw = ImageDraw.Draw(img)
        
        # Draw a circle for the ball with cyan color
        circle_margin = size // 6
        draw.ellipse([circle_margin, circle_margin, size - circle_margin, size - circle_margin], 
                     fill=CYAN, outline=BLUE, width=size//30)
        
        # Draw letter 'A'
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", size//2)
        except:
            try:
                font = ImageFont.truetype("arial.ttf", size//2)
            except:
                font = ImageFont.load_default()
        
        text = "A"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        text_x = (size - text_width) // 2
        text_y = (size - text_height) // 2 - size // 20
        draw.text((text_x, text_y), text, fill=DARK_PURPLE, font=font)
        
        # Save
        img.save(filename)
        print(f"Created {filename}")
    
    # Create icons
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    create_icon(192, os.path.join(script_dir, 'logo192.png'))
    create_icon(512, os.path.join(script_dir, 'logo512.png'))
    create_icon(64, os.path.join(script_dir, 'favicon.ico'))
    
    print("\n✅ PWA icons created successfully!")
    print("📁 Files: logo192.png, logo512.png, favicon.ico")
    print("💡 Replace with your actual Athletics logo for better branding")
    
except ImportError:
    print("❌ PIL/Pillow not installed")
    print("📦 Install it with: pip install pillow")
    print("Or use online tools like https://realfavicongenerator.net/")
except Exception as e:
    print(f"Error: {e}")
