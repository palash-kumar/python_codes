from PIL import Image

def extract_lsb_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    binary = ''
    for y in range(img.height):
        for x in range(img.width):
            pixel = pixels[x, y]
            for channel in pixel[:3]:  # RGB channels
                binary += bin(channel)[-1]  # LSB
    message = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        if char == '\0':  # End of message marker
            break
        message += char
    return message

print(extract_lsb_message('https://www.evya.in/key.jpg'))
