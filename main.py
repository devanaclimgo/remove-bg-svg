import svgwrite
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import easygui
from PIL import Image
from rembg import remove

def remove_svg_background(input_path, output_path):
    """Removes the background from an SVG file and saves the result as a PNG image.

    Args:
        input_path (str): The path to the input SVG file.
        output_path (str): The path to save the output PNG file.
    """

    # Load the SVG file using svgwrite
    drawing = svgwrite.Drawing(input_path)

    # Convert the SVG to a ReportLab drawing object
    rlg_drawing = svg2rlg(input_path)

    # Remove the background using rembg
    with Image.open(input_path) as img:
        img_without_bg = remove(img)
        img_without_bg.save("temp.png")

    # Load the modified image back into the SVG drawing
    drawing.add(svgwrite.image.Image("temp.png", insert=(0, 0), size=("100%", "100%")))

    # Save the modified SVG as a PNG image
    renderPM.drawToFile(rlg_drawing, output_path, fmt="PNG")

if __name__ == "__main__":
    input_path = easygui.fileopenbox(title="Select image file")
    output_path = easygui.filesavebox(title="Save file to...")

    remove_svg_background(input_path, output_path)