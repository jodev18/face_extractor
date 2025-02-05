import cv2
import dlib
from imutils import face_utils
import os

"""
    Based (stolen) from:
    https://github.com/kenryu42/Face-Detection-And-Auto-Crop/blob/master/auto_crop.py
"""

def crop_boundary(top, bottom, left, right, faces):
    if faces:
        top = max(0, top - 200)
        left = max(0, left - 100)
        right += 100
        bottom += 100
    else:
        top = max(0, top - 50)
        left = max(0, left - 50)
        right += 50
        bottom += 50

    return (top, bottom, left, right)

image = cv2.imread('Source.jpg')

if image is None:
    print("Image not present")

frame = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = gray.astype('uint8')

detector = dlib.get_frontal_face_detector()
rects = detector(gray,1)

if not len(rects):
    print("No faces detected")

print(len(rects))
for (i, rect) in enumerate(rects):
    (x, y, w, h) = face_utils.rect_to_bb(rect)

    top, bottom, left, right = crop_boundary(y, y + h, x, x + w, len(rects) <= 2)
    crop_img_path = os.path.join('result', f"data_crop_{i}.jpg")
    crop_img = frame[top: bottom, left: right]
    cv2.imwrite(crop_img_path, cv2.cvtColor(crop_img, cv2.COLOR_RGB2BGR))

print("SUCCESS.")
# cv2.imshow('gray',gray)
# cv2.waitKey(0)