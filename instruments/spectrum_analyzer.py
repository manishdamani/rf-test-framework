
class SpectrumAnalyzer:
    def __init__(self, ip):
        self.ip = ip

    def connect(self):
        print(f"Connecting to Spectrum Analyzer at {self.ip}")

    def measure_power(self):
        print("Measuring power...")
