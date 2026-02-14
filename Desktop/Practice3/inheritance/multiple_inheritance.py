class Camera:
    def take_photo(self):
        print("Click! Photo taken.")

class Phone:
    def make_call(self):
        print("Dialing...")

# Inherits from BOTH Camera and Phone
class Smartphone(Camera, Phone):
    pass

device = Smartphone()
device.take_photo()  # From Camera
device.make_call()   # From Phone