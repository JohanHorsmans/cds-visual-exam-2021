#!/usr/bin/python

# Loading packages:

# Import system tools:
import os 
import sys
sys.path.append(os.path.join(".."))

# Import cv2 for working with images:
import cv2

# Import argparse to specify arguments in the script from the commandline:
import argparse 

# Import Path for dealing with filepaths:
from pathlib import Path 

# Optical character recognition (OCR) tools:
import pytesseract

# NLP tools:
import wordsegment
from autocorrect import Speller

# Configuring how the OCR-tools should "read" image:
custom_oem_psm_config = r'--oem 2 --psm 4'

# Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A function designed to read text from image-files. The following argument can be specified but you can also run the code with default parameters:")
ap.add_argument("-i", "--image_path", default = os.path.join("data","WHTT.jpg"), type = str, help = "string, path to input file. Be weary of difference in operating systems in terms of spcifying path with \" / \" or \" \ \" [DEFAULT]: data/WHHT.jpg")

args = vars(ap.parse_args())

# Define the main function of the script and what parameters it takes: 
def main(image_path):
    
    print("[INFO]: Loading and preprocessing image") 
    
    # Load the image:
    image = cv2.imread(image_path)
    
    # Make the image greyscale (for canny edge detection):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Blur the image:
    blurred = cv2.GaussianBlur(grey_image, (5,5), 0)
    
    print("[INFO]: Finding and drawing contours")
    
    # Use canny edge detection:
    canny = cv2.Canny(blurred, 80, 150) # Parameters specified through trial and error.
    
    # Find contours and save them as "contours":
    (contours, _) = cv2.findContours(canny.copy(), 
                 cv2.RETR_EXTERNAL,
                 cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on cropped image and save the new image as "image_contour":
    image_contour = cv2.drawContours(image.copy(), # Draw contours on copy of original image
                                   contours, # Our list of contours
                                   -1, # Which contours to draw
                                   (0,0,200), # Contour colour (red)
                                   2) # Contour pixel width
    
    print("[INFO]: Writing \"image_letters.jpg\" to the \"data\"-folder")
    
    # Writing image-file:
    filepath, _ = os.path.split(image_path) # Specifying that the image should be saved in the same folder as specified in the image_path
    outfile = os.path.join(filepath, "image_letters.jpg") # Specifying that the image should be titled "image_letter.jpg"
    cv2.imwrite(outfile, image_contour) # Write file
    
    print("[INFO]: Reading text")
    
    # Thresholding the blurred image to remove noise and thereby improve readability:
    (T, thres) = cv2.threshold(blurred, 110, 255, cv2.THRESH_BINARY) # Parameters specified through trial and error.
    
    # Use canny edge detection:
    canny = cv2.Canny(thres, 80, 150) # Parameters specified through trial and error.
    
    # Find contours and save them as "contours":
    (contours, _) = cv2.findContours(canny.copy(), 
                     cv2.RETR_EXTERNAL,
                     cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on thresholded image and save the new image as "image_contour_ocr":
    image_contour_ocr = cv2.drawContours(thres.copy(), # Draw contours on copy of thresholded image
                                       contours, # Our list of contours
                                       -1, # Which contours to draw
                                       (0,0,200), # Contour colour (red)
                                       2) # Contour pixel width
    
    # Use pytesseract to read text and save it as "text":
    text = pytesseract.image_to_string(image_contour_ocr)
    
    # Define spellcheck function:
    def ocr_correct(ocr_text):
        # Segment based on unigram and bigram frequency
        ocr = wordsegment.segment(ocr_text)
        # join list as string
        ocr = " ".join(ocr)
        # spellcheck string
        ocr = check(ocr)

        return ocr
    
    # Define funcion which replaces odd characters with " ".
    def replace(string):
        processed = string.replace("\n"," ")\
                     .replace("\n\n"," ")\
                     .replace("__"," ")\
                     .replace(" - "," ")\
                     .replace('-""' ," ")\
                     .replace("|", "")\
                     .replace("!", "")\
                     .replace("\s"," ")\
                     .lstrip()
        return " ".join(processed.split())
    
    # Intitialise autocorrect and wordsegment classes
    check = Speller(lang='en')
    wordsegment.load()
    
    # Print the text in the terminal
    print(f"[INFO]: The text on the image says: \"{ocr_correct(text)}\"") 
    
    # Write the text to a .txt-file (with the same name as the image).
    filename = Path(image_path).stem
    doc = open(f"{filename}_text.txt", "w")
    doc.write(f"{ocr_correct(text)}")
    doc.close()
    print(f"[INFO]: \"{filename}_text.txt\" successfully written to the \"assignment_3\"-folder") 
    
if __name__ =="__main__":
    main(
      args["image_path"])