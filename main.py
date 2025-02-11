from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en') 

def predict(url):
    words = ''
    result = ocr.ocr(url,cls=False)
    for line in result[0]:
        words += line[1][0] + " "
    print(words)

predict('img\\z6307514771633_2feae6e0ce5815bd9b1cf3bae19f75b7.jpg')