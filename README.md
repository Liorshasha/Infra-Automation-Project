# Infra Automation By lior Shsaha

## Overview
Infra Automation is a Python-based project designed to simulate and manage virtual machine configurations. It provides tools for creating, validating, and managing machine instances, as well as running installation scripts for automated setup.

## Project Structure
```
infra_simulator.py       # Main entry point for the simulator
README.md                # Project documentation
userinput.py             # Handles user input for machine configurations
config/
  instances.json         # Stores machine instance data (generated at runtime)
logs/
  machine.log            # Logs for machine creation and errors
scripts/
  install.sh             # Installation script for setting up machines
src/
  machine.py             # Core logic for machine creation and validation
```

## Prerequisites
- Python 3.8 or higher
- Windows operating system

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Liorshasha/infra-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd infra-automation
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the simulator:
   ```bash
   python infra_simulator.py
   ```
2. Follow the prompts to create and manage machine instances.

## Logs
All logs are stored in the `logs/machine.log` file. This includes information about machine creation, validation errors, and installation script execution.

## Common Issues
### Error: `[WinError 193] %1 is not a valid Win32 application`
This error occurs when the installation script (`install.sh`) is not compatible with the Windows operating system. Ensure that the script is executable on Windows or replace it with a `.bat` or `.ps1` script.

### Error: `Error saving machine data to ./config/instances.json`
This error occurs if the `config/` directory does not exist. Create the directory manually:
```bash
mkdir config
```

### Validation Error: `RAM must be an even number`
Ensure that the RAM value provided is divisible by 2.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
