import os
import sys
from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    try:
        with Image.open(input_path) as img:
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(output_path)
            print(f'Image resized and saved to {output_path}')
    except Exception as e:
        print(f'Error resizing image: {e}')

def main():
    if len(sys.argv) != 5:
        print('Usage: python resize_image.py <input_path> <output_path> <new_width> <new_height>')
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    new_width = int(sys.argv[3])
    new_height = int(sys.argv[4])

    if not os.path.isfile(input_path):
        print(f'Error: {input_path} does not exist')
        sys.exit(1)

    resize_image(input_path, output_path, new_width, new_height)

if __name__ == '__main__':
    main()
