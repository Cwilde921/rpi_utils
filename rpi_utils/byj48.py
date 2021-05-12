from typing import Tuple, List
from time import sleep

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    import Mock.GPIO as GPIO

class Motor:
    def __init__(self, pins:Tuple[int], reverse_dir:bool=False, step_seq:bool=4):
        self.__pins = pins
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
        self.__step_seq = StepSequence(step_seq, reverse_dir=reverse_dir)

    def __del__(self):
        self.release_break()

    def release_break(self):
        self._write_pins([0,0,0,0])

    def apply_break(self):
        self._write_pins(self.__step_seq.current())

    def step(self, stp:int):
        if self.flip_dir:
            stp = -stp
        if   stp ==  0: return self.release_break()
        if   stp ==  1: return self._write_pins(self.__step_seq.next(Dir.CW))
        elif stp == -1: return self._write_pins(self.__step_seq.next(Dir.CCW))

    def _write_pins(self, outpt:List[bool]):
        for i in range(len(self.__pins)):
            GPIO.output(self.__pins[i], GPIO.HIGH if outpt[i] else GPIO.LOW)

    def walk(self, steps:int, delay):
        if self.flip_dir:
            steps = -steps
        if steps > 0:
            dir = 1
        else:
            dir = -1
            steps = abs(steps)
        for _ in range(steps):
            self.step(dir)
            sleep(delay)
        self.release_break()

    def seps_in_rot(self):
        return self.__step_seq.steps_in_rot()

class StepSequence:
    # class Seq(Enum):
    FOUR = 4
    EIGHT = 8

    def __init__(self, step_seq:int, reverse_dir:bool=False):
        if reverse_dir:
            self.CW = -1
            self.CCW = 1
        else:
            self.CW = 1
            self.CCW = -1
        if step_seq == self.FOUR:
            self.step_seq = self.FOUR
        elif step_seq == self.EIGHT:
            self.step_seq = self.EIGHT
        else:
            raise ValueError("for step_seq, got {} expected {} or {}".format(step_seq, self.FOUR, self.EIGHT))
        self.steps = [
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1],
            ]
        self._step_ctr = 0

    def next(self, dir:Dir):
        self._update_ctr(dir)
        return self.steps[self._step_ctr]

    def current(self):
        return self.steps[self._step_ctr]

    def _update_ctr(self, dir:Dir):
        stp = 1 if self.step_seq == self.EIGHT else 2
        if(dir == Dir.CW):
            self._step_ctr += stp
            if(self._step_ctr >= len(self.steps)):
                self._step_ctr = 0
        else:
            self._step_ctr -= stp
            if(self._step_ctr < 0):
                self._step_ctr = len(self.steps) -stp

    def steps_in_rot(self):
        return 2048 if self.steps == self.FOUR else 4096


if __name__ == "__main__":
    ss = StepSequence(StepSequence.FOUR)
    for i in range(20):
        print(ss.next(Dir.CW))
    print("changing direction")
    for i in range(15):
        print(ss.next(Dir.CCW))

    m1 = Motor(config["r_motor_pins_bcm"], True)
    m1.walk(12048, 0.003)
    m1.walk(-12048, 0.003)
    m1.release_break()
