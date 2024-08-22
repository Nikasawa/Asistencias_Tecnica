# Capture the fingerprint image
# This will depend on the Python library you use to interact with the 4500 fingerprint reader
# For example, using the `pyuareu` library:
import grpc
import pyuareu
device = pyuareu.UareU(4500)
image = device.get_image()

# Convert the image to a bytes object
image_bytes = image.tobytes()
