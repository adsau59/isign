import cv2
import sys
import os
import time

res = 320.

try:
    sys.path.append(r'C:\Work\Projects\fyp\openpose\build\python\openpose\Release');
    os.environ['PATH'] = os.environ[
                             'PATH'] + ';' + r'C:\Work\Projects\fyp\openpose\build\x64\Release' + ";" + r'C:\Work\Projects\fyp\openpose\build\bin'
    import pyopenpose as op
except ImportError as e:
    print(
        'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

params = dict()
params["model_folder"] = r'C:\Work\Projects\fyp\openpose\openpose\models'
params["hand"] = True
params["hand_detector"] = 2
params["body"] = 0

opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

handRectangles = [
    # Left/Right hands person 0
    [
        op.Rectangle(0., 0., 0., 0.),
        op.Rectangle(0., 0., res, res)
    ]
]

datum = op.Datum()
datum.handRectangles = handRectangles

cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (int(res), int(res)), interpolation=cv2.INTER_AREA)

    # todo remove
    startTime = time.time()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop([datum])
    print(datum.handKeypoints[1])
    print(str(1 / (time.time() - startTime)) + "fps taken to process")

    out = cv2.resize(datum.cvOutputData, (640, 480), interpolation=cv2.INTER_AREA)

    cv2.imshow('frame', out)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()