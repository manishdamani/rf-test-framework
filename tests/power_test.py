class PowerTest:
    def __init__(self, sa, sg):
        self.sa = sa
        self.sg = sg

    def run(self):
        self.sg.set_frequency(1e9)
        self.sg.set_power(-10)
        self.sa.measure_power()
