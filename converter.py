from PIL import Image
import os

def convertImage(file_path, output_format):
    image_input = Image.open(file_path)
    output_name = file_path.split(".")[0]
    image_input.save(output_name+'.'+output_format.lower())