class NoiseFigureTest:
    def __init__(self, pna):
        self.pna = pna

    def run(self):
        self.pna.setup_noise_figure()
        nf = self.pna.measure_noise_figure()
        return nf

