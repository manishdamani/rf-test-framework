import yaml
from instruments.spectrum_analyzer import SpectrumAnalyzer
from instruments.signal_generator import SignalGenerator
from tests.power_test import PowerTest
from utils.logger import setup_logger

from instruments.network_analyzer import PnaX
from tests.noise_figure_test import NoiseFigureTest


def load_config():
    with open('config/instruments.yaml', 'r') as f:
        return yaml.safe_load(f)

def main():
    logger = setup_logger()
    logger.info("Starting RF Test Framework")

    config = load_config()
    sa = SpectrumAnalyzer(config['spectrum_analyzer']['ip'])
    sg = SignalGenerator(config['signal_generator']['ip'])

    sa.connect()
    sg.connect()

    test = PowerTest(sa, sg)
    test.run()
    
        
    pna = PnaX(config['network_analyzer']['ip'])
    pna.connect()

    nf_test = NoiseFigureTest(pna)
    nf_result = nf_test.run()


    logger.info("Test completed")

if __name__ == "__main__":
    main()
