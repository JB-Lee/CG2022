import numpy as np
import cv2

img = np.zeros((720, 1280, 3), np.uint8)
img.fill(255)

def mouse_click_event(x, y):
    # draw line
    if mouse_click_event.prev_pos is not None:
        cv2.line(img, mouse_click_event.prev_pos, (x, y), (0, 255, 0), 2)
    mouse_click_event.prev_pos = (x, y)

    # draw mark
    r = 5
    cv2.rectangle(img, (x-r, y-r), (x+r, y+r), (255, 0, 0), 3)

mouse_click_event.prev_pos = None

def mouse_move_event(x, y):
    # draw trace
    cv2.circle(img, (x, y), 1, (169, 169, 255), -1)

def mouse_event_listener(event, x, y, flags, param):
    if event is cv2.EVENT_MOUSEMOVE:
        mouse_move_event(x, y)
    elif event is cv2.EVENT_LBUTTONDOWN:
        mouse_click_event(x, y)

cv2.namedWindow('ImagePolylineMouseButton')
cv2.setMouseCallback('ImagePolylineMouseButton', mouse_event_listener)

while True:
    cv2.imshow('ImagePolylineMouseButton', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
