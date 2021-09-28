# Self-balancing-robot-tracking-tennis-ball
The concept of this two-wheel self-balancing robot is based on Inverted pendulum theory.

[![Self balancing robot tracking tennis ball](https://user-images.githubusercontent.com/50642442/135050872-7a297032-2a62-49a5-9276-f3c8aaf1fd55.png)](https://youtu.be/2faSF5KY5KM "Self balancing robot tracking tennis ball")

# How Does Balancing Work?

To keep the robot balanced, the motors must counteract the robot falling. This action requires feedback and correcting elements. The feedback element is the MPU6050 gyroscope + accelerometer, which gives both acceleration and rotation in all three axes. The Arduino controller uses this method to “understand” the current orientation of the robot. The correcting element is the motor and wheel combination.
A self balancing algorithm is programmed into the controller and the controller drives the motors either clockwise or anticlockwise to balance the basement by a pulse width modulation (PWM) control signal.

![image](https://user-images.githubusercontent.com/50642442/135051867-a174e2c1-a4c6-4ab9-a670-ddeb289a6c2d.png)

# Hardware

Arduino Nano

MPU6050- Accelerometer and Gyroscope  

Nema 17 Stepper motors 12V

90mm Wheels

A4988 Stepper driver IC

HC-05 Bluetooth module

2 x 100 uF capacitor

12V Li-Po Battery

# Schematic diagram
![image](https://user-images.githubusercontent.com/50642442/135047363-df6c507f-63e2-46bc-9546-df0e2e77d219.png)

# CONTROL TECHNIQUE

To deal with the non-equilibrium problem, a PID controller is employed using tilt feedback to control the torque of the motors and keep the robot balanced.
A PID controller continuously measures a process variable and calculates an error value (angle from the vertical), which is the deviation of the process variable from some desired value.

**The PID controller**

The PID controller try to minimize this type of error over time by continuously adjusting a control variable (motor torque) according to the following equation:

![image](https://user-images.githubusercontent.com/50642442/135047823-99682262-b244-4218-a87d-d6b4fb599d87.png)

u(t) - the control variable

e(t) - the current error in the process variable

Kp, Ki, and Kd - coefficients that must be tuned to achieve the desired behavior of the controller.

**The PID coefficients**

The motor power increases by the proportional term as the system leans further over and decreases the motor power as the system approaches the upright position. A gain factor, Kp, determines how much power to apply to the motor for any given lean, as follows:

**Proportional Term = Kp*Error**
   
The differential term of the PID algorithm acts as a damper reducing oscillation. Another gain factor, Kd, determines how much power is applied to the motor according to the following equation

****Differential Term = Kd*(Error- Last Error)***
   
neither the proportional nor differential terms of the algorithm will remove all of the lean because both terms go to zero as the orientation of the system settles near vertical. The integral term sums the accumulated error tries to drive the lean to zero as follows:

****Output Integral Term = Ki*(Sum of Error)***

# Image processing

The robot identifies the ball and tracks it by using a USB camera placed on it’s top. Image processing techniques are implemented using OpenCV libraries on Raspberry Pi 4. By using an edge detection algorithm and an appropriate color filter the tennis ball is detected.

[![Self balancing robot tracking tennis ball](https://user-images.githubusercontent.com/50642442/135051174-f36bfeb7-e5b2-4f8a-80b4-c83aa5e6d35b.png)](https://youtu.be/NNahzWm346I "Self balancing robot tracking tennis ball")

# Hardware:

8GB RAM Raspberry Pi 4 Model B 

LifeCam Studio USB  webcam 

5A DC-DC Step Down Adjustable Power Supply Module 

Type C cable  0.20m 

Type A Female USB 

![image](https://user-images.githubusercontent.com/50642442/135049120-00da217e-9639-45e8-b8e0-b9331effa0a4.png)


**STEP 1 - RGB TO HSV CONVERSION**

The first step is converting the image to HSV format since working with HSV values is much easier for isolation of colors. 
In the HSV representation of color, hue determines the color you want, saturation determines how intense the color is and value determines the lightness of the image. 
Then define the lower and upper boundaries of the color green in the HSV color space, these color boundaries will allow us to detect the green ball in our video file. 

greenLower = (29, 86, 6) , greenUpper = (64, 255, 255)

![image](https://user-images.githubusercontent.com/50642442/135049326-540a830b-aca1-4ada-8e91-c7d1e50c970e.png)

**STEP 2 - Masks**

The next step is selecting all pixels that we think might be part of a tennis ball.
We'll do this based on their HSV values purely. 
OpenCV provides a InRanage function that can be used to pick out pixels based on their values. 
This generates a mask; a binary image where the foreground pixels (white) were within the specified range. 

![image](https://user-images.githubusercontent.com/50642442/135049722-89845e1f-06f7-4a8c-9052-24d6d9a3774a.png) ![image](https://user-images.githubusercontent.com/50642442/135049671-3e5d78d1-fafd-4dc6-849d-12efa6432f78.png) 

# STEP 3 - ﬁnding the contours of the ball

Contours are a feature of OpenCV library. Contours can be explained simply as a curve joining all the continuous points (along the boundary) that are having the same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition. The function to ﬁnd the contour of the ball in python is cv.findContours. This function retrieves contours from the binary image using the algorithm.

# Calculation the center of ball

After ﬁnding the contours of the ball the position coordinates of the centroid of the ball can be found by using the function moments in OpenCV. 
Image moments helps to calculate some features like the center of mass of the object, area of the object etc. The function cv.moments gives access to moment features.

![image](https://user-images.githubusercontent.com/50642442/135050197-050680e6-cd27-4365-9759-f15a2493bc4b.png)





































