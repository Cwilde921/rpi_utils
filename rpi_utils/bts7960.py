try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    import Mock.GPIO as GPIO

class bts7960:
    def __init__(self, LPWM=None, RPWM=None, L_EN=None, R_EN=None, L_IS=None, R_IS=None):
        self.LPWM = LPWM
        Gpio.setup(self.LPWM, GPIO.OUT)
        self.LPWM_OUT = GPIO.PWM(self.LPWM, 100)

        self.RPWM = RPWM
        Gpio.setup(self.RPWM, GPIO.OUT)
        self.RPWM_OUT = GPIO.PWM(self.RPWM, 100)

        self.L_EN = L_EN
        if self.L_EN is not None:
            GPIO.setup(self.L_EN, GPIO.OUT)
        self.R_EN = R_EN
        if self.R_EN is not None:
            GPIO.setup(self.R_EN, GPIO.OUT)
        self.L_IS = L_IS
        if self.L_IS is not None:
            GPIO.setup(self.L_IS, GPIO.OUT)
        self.R_IS = R_IS
        if self.R_IS is not None:
            GPIO.setup(self.R_IS, GPIO.OUT)

    def __del__(self):
        GPIO.setup(self.LPWM, GPIO.IN)
        GPIO.setup(self.RPWM, GPIO.IN)
        if self.L_EN is not None:
            GPIO.setup(self.L_EN, GPIO.IN)
        if self.R_EN is not None:
            GPIO.setup(self.R_EN, GPIO.IN)
        if self.L_IS is not None:
            GPIO.setup(self.L_IS, GPIO.IN)
        if self.R_IS is not None:
            GPIO.setup(self.R_IS, GPIO.IN)


