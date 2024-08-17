# You can use OpenCV to annotate the original images with the mismatches:

import cv2

def annotate_image(image_path, errors):
    image = cv2.imread(image_path)

    for error in errors:
        x, y, w, h, correct_text, ocr_text = error
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(image, f'{ocr_text}->{correct_text}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Annotated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

