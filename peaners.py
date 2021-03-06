from devices import DEVICES_MAP

class Peaner(object):
    '''
    This class represents the Thermo Peanut
    '''
    def __new__(cls, address):
        if address in DEVICES_MAP:
            return super(Peaner, cls).__new__(cls)
        raise Exception("Unknown device!")

    def __init__(self, address):
        self.address = address
        self.name = DEVICES_MAP[address]["name"]
        self.description = DEVICES_MAP[address]["description"]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_address(self):
        return self.address
