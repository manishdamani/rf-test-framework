import pyvisa

class PnaX:
    def __init__(self, ip):
        self.ip = ip
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(f'TCPIP0::{self.ip}::INSTR')

    def connect(self):
        print("Connecting to PNA-X...")
        print(self.inst.query("*IDN?"))

    def setup_noise_figure(self):
        # Preset and configure NF measurement
        self.inst.write("SYST:PRES")  # Preset
        self.inst.write("CALC:MEAS:TYPE NOIS")  # Create NF measurement
        self.inst.write("SENS:NOIS:AVER:STAT ON")
        self.inst.write("SENS:NOIS:AVER 20")
        self.inst.write("SENS:NOIS:TEMP:AMB 290")  # Ambient temperature in Kelvin

    def calibrate_nf(self):
        # Start calibration (you may need to adjust based on setup)
        self.inst.write("CALC:MEAS:TYPE NOIS")
        self.inst.write("SENS:NOIS:CAL:TYPE SCAL")  # Scalar calibration
        self.inst.write("SENS:NOIS:CAL:INIT")
        self.inst.write("*WAI")

    def measure_noise_figure(self):
        self.inst.write("INIT:IMM")
        self.inst.write("*WAI")
        nf = self.inst.query("CALC:DATA? SDATA")
        print(f"Noise Figure Data: {nf}")
        return nf
