from PIL import Image
import pytesseract


img = Image.open('captcha.jpg')
img1 = Image.open('test.png')
img2 = Image.open('test-digits.png')
img3 = Image.open('Untitled.png')

# c = pytesseract.image_to_string(img)
# print(c)
# c = pytesseract.image_to_string(img1)
# print(c)
# c = pytesseract.image_to_string(img2)
# print(c)
c = pytesseract.image_to_string(img3)
print(c)


# from PIL import Image
# import sys
#
# import pyocr
# import pyocr.builders
#
# tools = pyocr.get_available_tools()
# if len(tools) == 0:
#     print("No OCR tool found")
#     sys.exit(1)
# # The tools are returned in the recommended order of usage
# tool = tools[0]
# print("Will use tool '%s'" % (tool.get_name()))
# # Ex: Will use tool 'libtesseract'
#
# langs = tool.get_available_languages()
# print("Available languages: %s" % ", ".join(langs))
# lang = langs[2]
# print("Will use lang '%s'" % (lang))
#
# img = Image.open('captcha.jpg')
#
# txt = tool.image_to_string(
#     img,
#     lang=lang,
#     builder=pyocr.builders.TextBuilder()
# )
#
# word_boxes = tool.image_to_string(
#     img,
#     lang="eng",
#     builder=pyocr.builders.WordBoxBuilder()
# )
#
# line_and_word_boxes = tool.image_to_string(
#     img,
#     lang="eng",
#     builder=pyocr.builders.LineBoxBuilder()
# )
#
# # Digits - Only Tesseract (not 'libtesseract' yet !)
# digits = tool.image_to_string(
#     img,
#     lang=lang,
#     builder=pyocr.tesseract.DigitBuilder()
# )
