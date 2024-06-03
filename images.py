from PIL import Image, ImageFilter

img = Image.open("./images/razer_mouse.jpg")

filtered_img = img.convert("L")

filtered_img.save("./images/gray_razer_mouse.jpeg", "jpeg")