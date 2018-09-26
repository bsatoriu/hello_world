from PIL import Image
import requests
import sys


def main():

    img_base = 'input.jpg'
    image_base_url = sys.argv[1:][1]
    img_base_data = requests.get(image_base_url).content
    with open(img_base, 'wb') as handler:
        handler.write(img_base_data)

    # Relative Path
    # Image on which we want to paste
    img = Image.open(img_base)

    
    
    
    img_overlay = 'overlay.jpg'
    img_overlay_url = sys.argv[1:][0]
    img_overlay_data = requests.get(img_overlay_url).content
    with open(img_overlay, 'wb') as handler:
        handler.write(img_overlay_data)
    
    
    
    
    # Relative Path
    # Image which we want to paste
    img2 = Image.open(img_overlay)
    img.paste(img2, (50, 50))

    img_composite = 'output.jpg'
    # Saved in the same relative location
    img.save(img_composite)


if __name__ == "__main__":
    main()
