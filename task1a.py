'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         task1a.py
# Functions:        estimate_pose()
# Global variables: DICT
'''


import numpy as np
import cv2

DICT = {
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}


def estimate_pose(frame, mat_coeff, distort_coeff):
    '''
    Purpose: to return frame with detected markers along with pose

    Input Arguments:
    ---
    frame : image
    every frame of video

    DICT_type : dictionary
    size of ArUco Markers

    mat_coeff : list of matrix coefficients for camera

    distort_coeff : list of distortion coefficients for camera

    Returns:
    ---
    frame with detected markers along with pose estimates

    Example call:
    ---
    estimate_pose(frame, cv2.aruco.DICT_4X4_50, np.array(((933.16, 0, 657.6), (0, 933.16, 400.37), (0, 0, 1))), np.array((-0.44, 0.185, 0, 0)))
    '''

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    all_ids = []
    all_corners = []
    for aruco_type in DICT:
        cv2.DICT = cv2.aruco.Dictionary_get(DICT[aruco_type])
        parameters = cv2.aruco.DetectorParameters_create()

        corners, ids, rej_pnts = cv2.aruco.detectMarkers(gray, cv2.DICT, parameters=parameters,
                                                         cameraMatrix=mat_coeff,
                                                         distCoeff=distort_coeff)
        try:
            all_ids.extend(ids)
            all_corners.extend(corners)
        except:
            continue

    if len(all_corners) > 0:
        for i in range(0, len(all_ids)):

            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(all_corners[i], 0.02, mat_coeff,
                                                                           distort_coeff)

            cv2.aruco.drawDetectedMarkers(frame, corners)
            cv2.aruco.drawAxis(frame, mat_coeff,
                               distort_coeff, rvec, tvec, 0.01)

            marker_id = all_ids[i][0]
            cX = int(np.mean(all_corners[i][0][:, 0]))
            cY = int(np.mean(all_corners[i][0][:, 1]))
            cv2.putText(frame, "center", (cX-20, cY-15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.putText(frame, f"id={marker_id}", (cX, cY),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.circle(frame, (cX, cY), 3, (203, 150, 255), -1)

    return frame


intrinsic_cam = np.array(
    ((933.16, 0, 657.6), (0, 933.16, 400.37), (0, 0, 1)))
distort_params = np.array((-0.44, 0.185, 0, 0))


vid_capt = cv2.VideoCapture(0)

vid_capt.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vid_capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while vid_capt.isOpened():

    ret, img = vid_capt.read()
    # img variable holds the current frame

    output = estimate_pose(
        img, intrinsic_cam, distort_params)
    # output variable holds the image along with detected markers with pose

    cv2.imshow('Estimated Pose', output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    # the q key on activation destroys the window

vid_capt.release()
# pointer is released
cv2.destroyAllWindows()
