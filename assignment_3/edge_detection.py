#!/usr/bin/python


#Loading packages:
import os 
import sys
sys.path.append(os.path.join(".."))
import cv2
import argparse # for parsing arguments
from pathlib import Path # for dealing with filepaths

# OCR tool
import pytesseract

# NLP
import wordsegment
from autocorrect import Speller

#configuring how to read image:
custom_oem_psm_config = r'--oem 2 --psm 4'

#Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A function designed to read text from image-files. The following parameters can be specified but you can also run the code with default parameters:")
ap.add_argument("-i", "--image_path", default = os.path.join("data","WHTT.jpg"), type = str, help = "string, path to input file. Be weary of difference in operating systems in terms of spcifying path with \" / \" or \" \ \" [DEFAULT]: data/WHHT.jpg")
ap.add_argument("-l", "--lower", default = 110, type = int, help = "integer, lower limit for thresholding (i.e. if pixel < 0 make it white). [DEFAULT]: 110")
ap.add_argument("-u", "--upper", default = 255, type = int, help = "integer, lower limit for thresholding (i.e. if pixel > 0 make it white). [DEFAULT]: 255")

args = vars(ap.parse_args())

def main(image_path, lower, upper):
    print("[INFO]: Loading and preprocessing image")
    #Load the image:
    image = cv2.imread(image_path)
    #Make the image greyscale (for canny edge detection):
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Blur the image:
    blurred = cv2.GaussianBlur(grey_image, (5,5), 0)
    print("[INFO]: Finding and drawing contours")
    #Use canny edge detection:
    canny = cv2.Canny(blurred, 80, 150) #Parameters specified through trial and error.
    #Find contours and save them as "contours":
    (contours, _) = cv2.findContours(canny.copy(), 
                 cv2.RETR_EXTERNAL,
                 cv2.CHAIN_APPROX_SIMPLE)
    #Draw contours on cropped image and save the new image as "image_contour":
    image_contour = cv2.drawContours(image.copy(), #Draw contours on copy of original image
                                   contours, #our list of contours
                                   -1, #Which contours to draw
                                   (0,0,200), #Contour colout
                                   2) #contour pixel width
    
    print("[INFO]: Writing \"image_letters.jpg\" to the \"data\"-folder")
    #Writing file:
    filepath, _ = os.path.split(image_path) #Specifying that the image should be saved in the same folder as specified in the image_path
    outfile = os.path.join(filepath, "image_letters.jpg") #Specifying that the image should be titled "image_letter.jpg"
    cv2.imwrite(outfile, image_contour) #Write file
    
    print("[INFO]: Reading text")
    #Reading the text: (CHECK ROSS COMMENTS)
    
    # Thresholding the blurred image to remove noise and thereby improve readability:
    (T, thres) = cv2.threshold(blurred, lower, upper, cv2.THRESH_BINARY) 
    #Use canny edge detection:
    canny = cv2.Canny(thres, 80, 150) #Parameters specified through trial and error.
    #Find contours and save them as "contours":
    (contours, _) = cv2.findContours(canny.copy(), 
                     cv2.RETR_EXTERNAL,
                     cv2.CHAIN_APPROX_SIMPLE)
    #Draw contours on thresholded image and save the new image as "image_contour2":
    image_contour2 = cv2.drawContours(thres.copy(), #Draw contours on copy of original image
                                       contours, #our list of contours
                                       -1, #Which contours to draw
                                       (0,0,200), #Contour colout
                                       2) #contour pixel width
    
    #Use pytesseract to read text and save it as "text"
    text = pytesseract.image_to_string(image_contour2)
    
    #Define spellcheck function:
    def ocr_correct(ocr_text):
        # Segment based on unigram and bigram frequency
        ocr = wordsegment.segment(ocr_text)
        # join list as string
        ocr = " ".join(ocr)
        # spellcheck string
        ocr = check(ocr)

        return ocr
    #Define funcion which replaces odd characters with " ".
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
    
    #Intitialise autocorrect and wordsegment classes
    check = Speller(lang='en')
    wordsegment.load()
    
    #Print the text in the terminal
    print(f"[INFO]: The text on the image says: \"{ocr_correct(text)}\"") 
    
    #Write the text to a .txt-file (with the same name as the image).
    filename = Path(image_path).stem
    doc = open(f"{filename}_text.txt", "w")
    doc.write(f"{ocr_correct(text)}")
    doc.close()
    print(f"[INFO]: \"{filename}_text.txt\" successfully written to the \"assignment_3\"-folder") 
    
if __name__ =="__main__":
    main(
      args["image_path"],
      args["lower"],
      args["upper"])