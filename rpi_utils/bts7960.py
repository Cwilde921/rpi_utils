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
            GPIO.setup(self.L_IS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.R_IS = R_IS
        if self.R_IS is not None:
            GPIO.setup(self.R_IS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def __del__(self):
        self.LPWM_OUT.stop()
        self.RPWM_OUT.stop()
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

    def forward(self, duty_cycle):
        if self.L_EN is not None:
            GPIO.output(self.L_EN, GPIO.LOW)
        of self.R_EN is not None:
            GPIO.output(self.R_EN, GPIO.HIGH)
        self.LPWM_OUT.ChangeDutyCycle(0)
        self.RPWM_OUT.ChangeDutyCycle(duty_cycle)

    def reverse(self, duty_cycle):
        of self.R_EN is not None:
            GPIO.output(self.R_EN, GPIO.LOW)
        if self.L_EN is not None:
            GPIO.output(self.L_EN, GPIO.HIGH)
        self.RPWM_OUT.ChangeDutyCycle(0)
        self.LPWM_OUT.ChangeDutyCycle(duty_cycle)

    def stop(self):
        self.LPWM_OUT.ChangeDutyCycle(0)
        self.RPWM_OUT.ChangeDutyCycle(0)

