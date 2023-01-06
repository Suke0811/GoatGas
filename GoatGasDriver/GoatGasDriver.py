import time
from rems_arduino import ArduinoCommonApi, PIN_MODE
DEFAULT_PIN_IDs = [(0,2),(1,3),(2,4),(3,5)]#,(4,6),(5,7),(6,8),(7,9)]




class GoatGasDriver:
    def __init__(self, port, IDs, pins=None):
        self.arduino = ArduinoCommonApi()
        self.arduino.connect(port)
        self.id_pin = self._create_id_pin_set(IDs, pins)
        for i, p in self.id_pin:
            self.arduino.set_pin_mode(p, PIN_MODE.OUTPUT)
           # time.sleep(0.2)


    def open_gripper(self, ID, open):
        pin = self.get_pin_from_id(ID)
        if open:
            com = 'h'
        else:
            com = 'l'

        self.arduino.write(pin, com)

    def close(self):
        self.arduino.close()

    def _create_id_pin_set(self, IDs, pins):
        if pins is None:
            return DEFAULT_PIN_IDs

        id_pin = []
        for i, p in zip(IDs, pins):
            id_pin.append((i, p))
        return set(id_pin)


    def get_pin_from_id(self, d_id):
        for i, p in self.id_pin:
            if i == d_id:
                return p

    def get_id_from_pin(self, pin):
        for i, p in self.id_pin:
            if p == pin:
                return i


