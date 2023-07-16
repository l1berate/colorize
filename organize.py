import os
import shutil

for file in os.listdir("AllHue"):
    number = file.split(".")[0].split("_")[-1]
    if number.isdigit():
        shutil.copyfile(f"AllHue/{file}", f"angle_{number}/{file}.png")
