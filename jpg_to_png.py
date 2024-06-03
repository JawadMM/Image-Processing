import sys
import os
from PIL import Image

images_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
  os.makedirs(output_folder)
  print(f"Created Folder with path {output_folder}.")

for filename in os.listdir(images_folder):
  img = Image.open(f"{images_folder}{filename}")
  name, extension = os.path.splitext(filename)
  img.save(f"{output_folder}{name}.png", "png")
  print(f"Converted {filename} from JPG to PNG")
  # print(os.path.splitext(filename))

print(images_folder, output_folder, type(output_folder))