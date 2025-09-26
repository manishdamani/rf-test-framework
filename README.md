# RF Test Automation Framework .

## 🚀 Project Overview
This Python-based RF Test Automation Framework is designed to automate wireless testing tasks such as frequency sweeps, power measurements, and signal validation. It is ideal for RF Test Engineers preparing for roles in wireless test automation, including positions at companies like Apple.

## ✨ Features
- Instrument control using PyVISA and SCPI commands
- Modular design with reusable classes for RF instruments
- Automated test execution and logging
- Configurable test parameters via JSON
- Unit testing with `pytest`
- Data visualization with `matplotlib`

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- NI-VISA installed
- Git installed
- Python packages listed in `requirements.txt`

### Installation
```bash
git clone https://github.com/manishdamani/rf-test-framework.git
cd rf-test-framework
pip install -r requirements.txt

## 📂 Folder Structure
rf-test-framework/
│
├── instruments/
│   ├── signal_generator.py
│   └── spectrum_analyzer.py
│
├── tests/
│   ├── test_signal_generator.py
│   └── test_spectrum_analyzer.py
│
├── configs/
│   └── test_config.json
│
├── logs/
│   └── test_run.log
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
