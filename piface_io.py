# import pifaceio
import time

relay_index = 1
input_pin_index = 0


class IOController():
    #  def __init__(self):
    #     self.pi_face = pifaceio.PiFace()

    def trigger_door(self):
        # self.pi_face.write_pin(relay_index, 1)
        # time.sleep(.2)
        # self.pi_face.write_pin(relay_index, 0)
        pass

    def get_door_position(self):
        # if self.pi_face.read_pin(input_pin_index) != 0:
        #     return False
        return True
