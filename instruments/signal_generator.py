
class SignalGenerator:
    def __init__(self, ip):
        self.ip = ip

    def connect(self):
        print(f"Connecting to Signal Generator at {self.ip}")

    def set_frequency(self, freq):
        print(f"Setting frequency to {freq} Hz")

    def set_power(self, power):
        print(f"Setting power to {power} dBm")
