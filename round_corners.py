from PIL import Image, ImageDraw

def round_corners(image_path, output_path, radius_percent=0.2):
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    radius = int(min(width, height) * radius_percent)
    
    # Create mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=255)
    
    # Apply mask
    img.putalpha(mask)
    img.save(output_path, "PNG")
    print(f"Rounded {image_path} -> {output_path}")

# Round both logos
round_corners("assets/lifeos-logo.jpg", "assets/lifeos-logo.png", radius_percent=0.15)
round_corners("assets/flowos-logo.png", "assets/flowos-logo-rounded.png", radius_percent=0.15)
