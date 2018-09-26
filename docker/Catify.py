from PIL import Image
import requests


def main():

    img_base = 'input.jpg'
    img_overlay = 'fatcat.jpg'
    img_composite = 'output.jpg'

    #TODO: Get from s3
    image_url = "http://www.dumpaday.com/wp-content/uploads/2018/06/random-pictures-10.jpg"
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

    #TODO: Write to s3
    # Saved in the same relative location
    img.save(img_composite)


if __name__ == "__main__":
    main()

