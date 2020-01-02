try:
    # Importing Pillow for image processing
    from PIL import Image
except ImportError:
    import Image
    # Importing Tesseract for OCR engine
import pytesseract

def ocr_core(filename):
    # Path of the tesseract engine
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    # Pillow's Image class to open the image and pytesseract to detect the string in the image
    # Extracts when both English and Tamil language present in the image
    text = pytesseract.image_to_string(Image.open(filename), lang='eng+tam')
    return text

# print(ocr_core(r"E:\Coding\Python\OCR\Images\captured_english.PNG"))