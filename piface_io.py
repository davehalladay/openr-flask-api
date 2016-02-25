import pifacedigitalio
import time

relay_index = 1
input_pin_index = 0


class IOController:
    def __init__(self):
        self.pi_face = pifacedigitalio.PiFaceDigital()

    def trigger_door(self):
        self.pi_face.relays[relay_index].turn_on()
        time.sleep(.2)
        self.pi_face.relays[relay_index].turn_off()
        pass

    def get_door_position(self):
        if self.pi_face.input_pins[input_pin_index].value != 0:
            return False
        return True
