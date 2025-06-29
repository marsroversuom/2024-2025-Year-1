import board
import busio
import adafruit_pca9685
""" 
Where does the i2c = busio.I2C(board.SCL, board.SDA) and hat = adafruit_pca9685.PCA9685(i2c) come from? Some sort of explanation or link/resource would be great.
Moreover, what do they mean? There is an excellant and extensive explanation to how the cycle works down below, but no real mention of what these two lines of code
mean
"""
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
hat.frequency = 5000
motor0 = hat.channels[0]
motor1 = hat.channels[1]
motor2 = hat.channels[2]
motor3 = hat.channels[3]
motor4 = hat.channels[4]
motor5 = hat.channels[5]
# When the PWM signal has 50% duty cycle, the motor stops running. If the PWM has less than 50% duty cycle, the motor will turn CW (or CCW depending on the connection). If the PWM signal has more than 50% duty cycle, motor will turn CCW (or CW depending on the connection).
# The cycle is from 0 to 0xffff(65535)
motor0.duty_cycle = 1000
