from sys import flags
import time
import cv2
import pyautogui as p


def AuthenticateFace():
    # Camera access disabled - return success flag directly
    print("Face authentication skipped (camera disabled)")
    return 1
