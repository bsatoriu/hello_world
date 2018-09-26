from PIL import Image
import requests
import sys


def main():

    print(sys.argv[1:][0])

    img_base = 'input.jpg'
    img_overlay = 'fatcat.jpg'
    img_composite = 'output.jpg'
    image_url = sys.argv[1:][0]
    img_data = requests.get(image_url).content
    with open(img_base, 'wb') as handler:
        handler.write(img_data)

    # Relative Path
    # Image on which we want to paste
    img = Image.open(img_base)

    # Relative Path
    # Image which we want to paste
    img2 = Image.open(img_overlay)
    img.paste(img2, (50, 50))

    # Saved in the same relative location
    img.save(img_composite)


if __name__ == "__main__":
    main()
