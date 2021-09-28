






import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = int(image.shape[0])
    y2 = int(y1*3/5)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1,y1,x2,y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1,y1,x2,y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2), (y1,y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line,right_line])


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def ROI(image):
    Height = image.shape[0]
    triangle = np.array([[(200,Height), (1100,Height),(550,250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, triangle, 255)
    masked_img = cv2.bitwise_and(image,mask)
    return masked_img

def displayLines(image, lines):
    line_img = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(image, (x1,y1), (x2,y2), (255,0,0),5)
    return line_img

def demoImage():
    image = cv2.imread("test_image.jpg")
    lane_image = np.copy(image)
    canny_image = canny(lane_image)
    cropped_image = ROI(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength = 45, maxLineGap = 5)
    averaged_lines = average_slope_intercept(lane_image, lines)
    line_image = displayLines(lane_image, averaged_lines)
    combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
    cv2.imshow("lanes", combo_image)
    cv2.waitKey(0)


cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    try:
        canny_image = canny(frame)
        cropped_image = ROI(canny_image)
        lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength = 45, maxLineGap = 5)
        averaged_lines = average_slope_intercept(frame, lines)
        line_image = displayLines(frame, averaged_lines)
        combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

        cv2.imshow("lanes", combo_image)
    except:
        pass
    if cv2.waitKey(1) == ord('q'):
        break
