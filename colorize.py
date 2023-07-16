from duotone import Duotone
from PIL import Image, ImageColor
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)


# Personal utility script for colorizing images in bulk. Very, very rough around the edges 
# and not meant for public use. Can be used to colorize images using duotone, grayscale, or
# hue shift. You can choose to replace the original files or save the colorized images as
# new files. If you choose to use duotone, you can either enter a valid hex color or use the
# * character to generate all 96 colors. If you choose to use hue shift, you can either enter
# a valid angle or use the -1 character to generate all 360 angles (in increments of 10 degrees).
# If you choose to use grayscale, the script will simply convert the images to grayscale.
# The script will also print out the name of each file as it is colorized and saved.


fred = Fore.RED
fblue = Fore.BLUE
fgreen = Fore.GREEN
fwhite = Fore.WHITE
fblack = Fore.BLACK
fyellow = Fore.YELLOW
fmagenta = Fore.MAGENTA
fcyan = Fore.CYAN
dim = Style.DIM
bold = Style.BRIGHT
ra = Style.RESET_ALL


duotone_color_dict = {
    "purple": "#7e1e9c",
    "green": "#15b01a",
    "blue": "#0343df",
    "pink": "#ff81c0",
    "brown": "#653700",
    "red": "#e50000",
    "light blue": "#95d0fc",
    "teal": "#029386",
    "orange": "#f97306",
    "light green": "#96f97b",
    "magenta": "#c20078",
    "yellow": "#ffff14",
    "sky blue": "#75bbfd",
    "lime green": "#89fe05",
    "light purple": "#bf77f6",
    "violet": "#9a0eea",
    "grey": "#929591",
    "dark green": "#033500",
    "turquoise": "#06c2ac",
    "lavender": "#c79fef",
    "dark blue": "#00035b",
    "tan": "#d1b26f",
    "cyan": "#00ffff",
    "aqua": "#13eac9",
    "forest green": "#06470c",
    "mauve": "#ae7181",
    "dark purple": "#35063e",
    "bright green": "#01ff07",
    "maroon": "#650021",
    "olive": "#6e750e",
    "salmon": "#ff796c",
    "beige": "#e6daa6",
    "royal blue": "#0504aa",
    "navy blue": "#001146",
    "lilac": "#cea2fd",
    "black": "#000000",
    "hot pink": "#ff028d",
    "light brown": "#ad8150",
    "pale green": "#c7fdb5",
    "peach": "#ffb07c",
    "olive green": "#677a04",
    "dark pink": "#cb416b",
    "periwinkle": "#8e82fe",
    "sea green": "#53fca1",
    "lime": "#aaff32",
    "indigo": "#380282",
    "mustard": "#ceb301",
    "light pink": "#ffd1df",
    "rose": "#cf6275",
    "bright blue": "#0165fc",
    "neon green": "#0cff0c",
    "burnt orange": "#c04e01",
    "aquamarine": "#04d8b2",
    "navy": "#01153e",
    "grass green": "#3f9b0b",
    "pale blue": "#d0fefe",
    "dark red": "#840000",
    "bright purple": "#be03fd",
    "yellow green": "#c0fb2d",
    "baby blue": "#a2cffe",
    "gold": "#dbb40c",
    "mint green": "#8fff9f",
    "plum": "#580f41",
    "royal purple": "#4b006e",
    "brick red": "#8f1402",
    "dark teal": "#014d4e",
    "burgundy": "#610023",
    "khaki": "#aaa662",
    "blue green": "#137e6d",
    "seafoam green": "#7af9ab",
    "kelly green": "#02ab2e",
    "puke green": "#9aae07",
    "pea green": "#8eab12",
    "taupe": "#b9a281",
    "dark brown": "#341c02",
    "deep purple": "#36013f",
    "chartreuse": "#c1f80a",
    "bright pink": "#fe01b1",
    "light orange": "#fdaa48",
    "mint": "#9ffeb0",
    "pastel green": "#b0ff9d",
    "sand": "#e2ca76",
    "dark orange": "#c65102",
    "spring green": "#a9f971",
    "puce": "#a57e52",
    "seafoam": "#80f9ad",
    "grey blue": "#6b8ba4",
    "army green": "#4b5d16",
    "dark grey": "#363737",
    "dark yellow": "#d5b60a",
    "goldenrod": "#fac205",
    "slate": "#516572",
    "light teal": "#90e4c1",
    "rust": "#a83c09",
    "deep blue": "#040273",
    "pale pink": "#ffcfdc"
}


def rainbow_text(input_string):
    colors = [fred, fblue, fgreen, fwhite, fyellow, fmagenta, fcyan]

    output = ''
    color_index = 0

    for char in input_string:
        output += colors[color_index] + char
        color_index = (color_index + 1) % len(colors)

    output += ra

    return output


def apply_hue_shift(image, angle, output):
    # Convert image to HSV color space
    hsv_image = image.convert("HSV")

    # Apply hue shift
    hue_shifted_image = hsv_image.copy()
    pixels = hue_shifted_image.load()
    width, height = hsv_image.size

    for y in range(height):
        for x in range(width):
            hue, saturation, value = pixels[x, y]
            hue = (int(hue + angle) % 256)  # Convert hue to integer
            pixels[x, y] = (hue, saturation, value)

    # Convert image back to RGB color space
    result_image = hue_shifted_image.convert("RGB")
    # result_image = darken_colors(result_image, 0.8)
    result_image.save(output, "PNG")


def colorize(image, light_color, dark_color, output):
    light_values = ImageColor.getrgb(light_color)
    dark_values = ImageColor.getrgb(dark_color)
    result = Duotone.process(image, light_values, dark_values)
    # result = darken_colors(result, 0.8)
    result.save(output, "PNG")


print(fcyan + "Welcome to the " + rainbow_text('colorize') + fcyan +
      " script! This script will colorize all images in a folder of your choice.")
print(fgreen + "++ Please note that this script only works with " + bold + "PNG files.")
print()

# Make sure folder, light color, and dark color are accessible globally
folder = ""
light_color = "#ffffff"
dark_color = ""
angle = 190

ready = False
while not ready:
    folder = input(fblue + bold + "Please enter the folder name: ")

    # Check if folder is a valid directory
    if not os.path.isdir(folder):
        print(fred + bold + "Sorry, that's an invalid directory! Please try again.")
        continue

    # Check if folder contains any PNG files
    if not any(filename.endswith(".png") for filename in os.listdir(folder)):
        print(fred + bold +
              "Sorry, that folder doesn't contain any PNG files! Please try again.")
        continue

    grayscale = False

    # Check if user wants to use duotone or hue shift
    duotone = input(
        fblue + bold + "Would you like to use duotone, grayscale, or hue shift? (d/g/h): ")
    if duotone == "d":
        duotone = True
    elif duotone == "g":
        duotone = False
        grayscale = True
    else:
        duotone = False

    # Get Valid dark color
    while True and duotone:
        dark_color = input(
            fblue + bold + "Please enter a valid color in hex rgb format (ie. #539d2e or * for 96 colors): ")
        try:
            if dark_color == "*":
                break
            if dark_color[:1] != "#":
                dark_color = "#" + dark_color
            ImageColor.getrgb(dark_color)
            break
        except ValueError:
            print(fred + bold + "Sorry, that's not a valid color! Please try again.")
            continue

    # Get Valid angle
    while True and not duotone and not grayscale:
        angle = input(
            fblue + bold + "Please enter a valid angle (0-360 or -1 for all angles): ")
        try:
            angle = int(angle)
            if angle < -1 or angle > 360:
                raise ValueError
            break
        except ValueError:
            print(fred + bold + "Sorry, that's not a valid angle! Please try again.")
            continue

    # Ask if user wants to replace the original files if all angles or all colors hasn't been selected
    if angle == -1 or dark_color == "*":
        replace = True
    else:
        replace = input(
            fmagenta + "Would you like to replace the original files? (y/n): ")
        if replace == "y":
            replace = True
        else:
            replace = False

    ready = True

# Inform user that the script is running with the given parameters
print()
print(fcyan + "Ok, now running script with the following parameters:")
print(fgreen + "Folder: " + bold + folder)
if duotone:
    print(fgreen + "Color: " + bold + dark_color)
elif grayscale:
    print(fgreen + "Color: " + bold + "Grayscale")
else:
    print(fgreen + "Angle: " + bold + "All" if (angle == -1) else str(angle))
print(fgreen + "Replace?: " + bold + str(replace))
print()

# Cycle through all files in the directory and colorize them
for filename in os.listdir(folder):
    if filename.endswith(".png"):
        image = Image.open(folder + "/" + filename)
        # Create output file name by appending _colorized to the original file name
        # if replace is True, otherwise just use the original file name
        if replace:
            output = folder + "/" + filename
        else:
            output = folder + "/" + filename[:-4] + "_colorized.png"
        if duotone:
            if dark_color != "*":
                colorize(image, light_color, dark_color, output)
            else:
                for name, color in duotone_color_dict.items():
                    temp_output = output.split('.')[0] + f"_{name}.png"
                    colorize(image, light_color, color, temp_output)
                    print("\r" + " " * 130, end='')
                    print("\r" + rainbow_text("Colorized ") + fblue + filename + fgreen +
                          " and saved as " + fmagenta + temp_output + fgreen + "...", end='')
        elif grayscale:
            grayscale_image = image.convert("L")
            grayscale_image.save(output, "PNG")
        else:
            if angle == -1:
                # run loop over all angles in 10 degree increments
                for i in range(10, 350, 10):
                    temp_output = output.split('.')[0] + f"_{i}.png"
                    apply_hue_shift(image, i, temp_output)
                    print("\r" + " " * 130, end='')
                    print("\r" + rainbow_text("Colorized ") + fblue + filename + fgreen +
                          " and saved as " + fmagenta + temp_output + fgreen + "...", end='')
            else:
                apply_hue_shift(image, angle, output)
        print("\r" + " " * 130, end='')
        print("\r" + rainbow_text("Colorized ") + fblue + filename + fgreen +
              " and saved as " + fmagenta + output + fgreen + "...", end='')
    else:
        continue

print("\n")
print(fcyan + bold + "Done! All images in the " + fwhite + bold +
      folder + fcyan + bold + " folder have been " + rainbow_text("colorized!"))
