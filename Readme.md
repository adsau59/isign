# iSign
iSign is a sign language recognition system from the perspective of the signer. Get the most updated code from [GitHub](https://github.com/adsau59/isign). 

You can also view the Black Book for the project [here](https://1drv.ms/b/s!Aj0862zYCr_-_VLgPKh7VcHyTcti?e=pSVj22).

![Signing](https://i.postimg.cc/nx61KzGf/wearing.jpg?dl=1)

### Objective:
- To create a system, affordable and usable by mute to reduce the communication barrier between them and the people who don't understand sign language.
   
### Technology Stack
iSign is made using,
- [Python v3.5.x](https://www.python.org/downloads/release/python-357/)
- [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [Keras](https://keras.io/) (with [Tenserflow](https://www.tensorflow.org/) backend)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Matplotlib](https://matplotlib.org/)
- [Unity](https://unity.com/)

### Hardware Requirements
- Controller: [Rasberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
- DPU: A Powerful Computer for realtime performance (Tested on i7-4700HQ, Nvidia Gtx 860m, 8GB DDR3 RAM).
- Gyroscope: [MPU-6050 Triple Axis Accelerometer and Gyro Breakout Board](https://www.amazon.in/REES52-GY-521-Mpu6050-Accelerometer-Arduino/dp/B008BOPN40)
- Webcam (atleast with 480p resolution)
- Touch Sensor: [Standalone 5-Pad Capacitive Touch Sensor Breakout - Adafruit](https://www.adafruit.com/product/1362)

### Features
- Realtime performance, use the sign language recognition system in real time to translate gestures made into text.
- Portable, take the system on the road with you, to help you talk to other people.

### Project Structure
The project is divided into 3 parts
- `component-test` contains the scripts to test out the different components of the system.
- `phone-screen-show` contains the unity project which is used to receive the output sent by the DPU in realtime translation.
- `sensor-data-sender` contains scripts which are used to send data from the controller to the DPU, and also scripts to process the data. 

### How to Use?

#### Hardware Setup
- You can check out the images for the assembled system [here](https://postimg.cc/gallery/mfo16sr4/).
- You will need a solid mask, electrical tape, 20m copper wire, double sided tape, hot glue gun.
- Connect MPU-6050 Triple Axis Accelerometer and Gyro Breakout Board to the Raspberry Pi 3 B+  in this configuration:

| MPU-6050 | Raspberry Pi |
|:--------:|:------------:|
|    VCC   |    5V pin    |
|    GND   |  Ground pin  |
|    SCL   |      SCL     |
|    SDA   |      SDA     |

- Position MPU-6050 behind the mask on the forehead, and tape it.
- Connect the 5-Pad Capacitive Touch Breakout to raspberry pi, in this configuration: 

 
| Touch Breakout | Raspberry PI |
|:--------------:|:------------:|
|       VCC      |    5V pin    |
|       GND      |  Ground pin  |
|   Pad0 Output  |    GPIO 22   |
|   Pad1 Output  |    GPIO 27   |
|   Pad2 Output  |    GPIO 17   |
|   Pad3 Output  |    GPIO 24   |
|   Pad4 Output  |    GPIO 23   |

- Use copper wire to expose the input pins, on the mask in this configuration, and tape it:

| Touch Breakout | Raspberry Pi |
|:--------------:|:------------:|
|      Pad0      |   Forehead   |
|      Pad1      |     Nose     |
|      Pad2      |     Chin     |
|      Pad3      |      Ear     |
|      Pad4      |    Cheeks    |

- Tape the sensor on the left cheek, and all the exposed wire on the right side of the mask. (Opposite if the user is a left handed signer)
- Make sure the copper wires have enough padding with the mask so that, when the user wears the mask, the users face does interfere with the sensor.
- Glue the webcam to the top of the mask, such that it is positioned, where the signer hand is in the FOV of the camera, when the signer does hand gestures.
- Connect the webcam with a USB cord (use a USB wire extender if the wire is not long enough)
- Wear a colored glove on the non dominant hand, so that open pose doesn't get confused while detecting hand keypoints.

#### Software Setup

Installing Requirements

- Setup OpenPose using these [steps](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md)
- Install the `phone-screen-show/APK/phone.apk` on an android phone.
- Install all the required python libraries using, `requirements_controller.txt` in the controller and `requirements_dpu.txt` in the DPU.

Configuration
- Configure the project by editing `sensor-data-sender/config.json` file as per the description below
 
|        Variable       |                 Description                |         Type        |
|:---------------------:|:------------------------------------------:|:-------------------:|
|          dev          |       Use mock data for developement       |       Boolean       |
|         dpu-ip        |            IP address of the DPU           | String (Local IPv4) |
|         rpi-ip        |        IP address of the controller        | String (Local IPv4) |
| openpose-build-python | Build location of openpose python binaries |  String (Directory) |
|     openpose-build    |         Build location of openpose         |  String (Directory) |
|      openpose-bin     |          Bin directory of openpose         |  String (Director)  |
|     openpose-model    |         location of openpose model         |       Boolean       |
|      right-handed     |         Is the signer right handed?        |       Boolean       |

- Rest of the configuration variables acts as constants in the code base, to understand what they do properly, refer the python docstrings in the code.

Execution:
- Run `data_sender.py` on the controller, once it says `wating` in the console, it is ready to get commands from the DPU.
- On DPU you can use the following scripts for their respective description,

|        Script        |                                              Description                                              |
|:--------------------:|:-----------------------------------------------------------------------------------------------------:|
|   reciver_debug.py   |                         Simply receives data from controller and displays it.                         |
|     data_saver.py    |                            Saves the data received from controller in file.                           |
|    file_player.py    |                             Shows the data of the target file in a Player.                            |
|     count_rdf.py     |                               Counts all the Raw Data Frames collected.                               |
|  extract_features.py |                   Extract features of the collected data and saves it in a csv file.                  |
|     dnn_train.py     |                  Trains a neural network model with the extracted data and saves it.                  |
| predict_from_file.py |  Runs prediction for a target file, (use for testing instead of realtime prediction for weak Systems) |
| predict_real_time.py | Runs prediction in realtime by receiving data from controller (Can only be used by Powerful Systems). |

- To configure, double click to play using `file_player.py`, simply double click on a data file and use `view_data.bat` to open it.
- Use the scripts to,  `Record Data > Extract Feature > Train > Predict RealTime/File`
- Note: if the `data_sender` becomes unresponsive, restart it in the controller.

### Roadmap
Development for iSign has finished, but if the community requests new features or some bad design is noticed, I will try my best to add/change it.

### How to contribute?
You can contribute this project by,
- Using the System and creating issue when any bug is encountered.
- Helping me in the development by bug squashing or developing new features. (If you want to do this, contact me so that we can collaborate.)
- Let me know if you have any good feature ideas.

### Contact
If you have any problems or you want to contact me for feature ideas or want to collaborate in development you can contact me on [DefineX Community discord server](http://discord.definex.in).

### Feeling generous?
You can donate me on [PayPal](https://www.paypal.me/AdamSaudagar).

### License
This project is license to the Apache License 2.0, check out the full license over [here](https://github.com/adsau59/isign/blob/master/LICENSE).
 
