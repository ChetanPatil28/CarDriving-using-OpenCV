# CarDriving-using-OpenCV

The project is based on Numpy and OpenCV library.
This project is based on capturing the movements of the hand and accordingly controlling the
steering wheel of the car.
The algorithm involves-
1. Considering only the skin colour using HSV format.
2. Making sure that a portion of the frame consists of the palm and call this portion as our new frame.
3. Finding the largest contour in this new frame and its Convexity-Defects followed by its Centroid.
4. Finding the finger-tips from the Convexity-Defect and drawing a line from the Centroid ( centre of the palm )
   to the fingertip.
5. Now, in-order to determine the hand-pose for steering, we find the total number of fingertips on either 
   sides of the centroid by storing them in two variables; Left and Right.
6. Depending on the requirements, if Left>Right, then invoke a KeyPress for 'A' or 'LeftArrowButton' else
   otherwise.
7. If the Contour area for the largest contour is less than a threshold, then invoke a keyPress for 'W' or
   'UpArrowButton'.
8. The invocation for the keyPresses can be done using the Pyautogui library. However, this slows down the performance.
9. Therefore, I've used the directkeys.py file which consists of the wrappers for keyboard press.
   For, more details about this visit https://docs.python.org/3/library/ctypes.html
10. The project can further be improved by using a gesture for the 'Brake' keypress. Still working on it.    

The GIF file attached in the repo shows a demo version. Note that the code doesn't slow down the process as in 
the GIF file.
 
![Alt Text](<videotogif_2018.10.28_21.04.37.gif>)
