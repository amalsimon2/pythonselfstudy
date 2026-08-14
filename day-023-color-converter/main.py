def hex_to_rgb(hex_code):
    if len(hex_code) != 7:
        raise ValueError('Invalid hexadecimal format')
    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:7], 16)
    return (r, g, b)

def rgb_to_hex(rgb):
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError('Invalid RGB values')
    hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_code

hex_code = input('Enter a hexadecimal color code (e.g., #FF5733): ')
try:
    rgb = hex_to_rgb(hex_code)
    print(f'RGB values: {rgb}')
except ValueError as e:
    print(e)

r, g, b = map(int, input('Enter RGB values (e.g., 255 167 51): ').split())
try:
    hex_code = rgb_to_hex((r, g, b))
    print(f'Hexadecimal code: {hex_code}')
except ValueError as e:
    print(e)
