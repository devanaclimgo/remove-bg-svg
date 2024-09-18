from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import easygui
from PIL import Image
from rembg import remove

inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Save file to...')

# Process the SVG using svglib
drawing = svg2rlg(inputPath)
# (Apply background removal logic here using PIL or other libraries)
renderPM.drawToFile(drawing, outputPath)  # Save the modified SVG