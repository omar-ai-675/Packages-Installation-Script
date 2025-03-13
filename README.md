# CORTEX41 Package Installer

A simple GUI application to easily install common development packages on Linux systems. This tool simplifies the installation of NVIDIA drivers, CUDA, Docker, RustDesk, VSCode and other development tools with a user-friendly interface.

![Screenshot of the application](screenshot.png)

## Prerequisites

Before running this application, make sure you have the necessary dependencies installed:

```bash
sudo apt update
sudo apt install python3-tk python3-pil python3-pil.imagetk python3-pip
pip install ttkbootstrap
```

## Features

- Clean, modern dark interface
- One-click installation of common development tools
- Support for NVIDIA driver selection
- Real-time installation progress display
- Threaded execution to prevent UI freezing

## Packages Available for Installation

- **CUDA** - NVIDIA CUDA toolkit for GPU acceleration
- **NVIDIA Driver** - GPU drivers with customizable version
- **Docker-Compose** - Container orchestration tool
- **NVIDIA Toolkit and Docker** - NVIDIA Container Runtime for Docker
- **RustDesk** - Open source remote desktop software
- **VSCode** - Microsoft's popular code editor

## Usage

1. Run the application with:
   ```bash
   python3 main.py
   ```
2. Select the packages you want to install
3. Enter NVIDIA driver version if needed
4. Click "Start Installation"
5. Reboot your system after installation is complete

## Important Notes

- This application needs to be run with sufficient privileges as it executes sudo commands
- The CUDA installer is interactive and will require user input during installation
- **NVIDIA cuDNN** must be installed separately as it requires an NVIDIA Developer account login
- Some installations may require a system reboot to take full effect

## Requirements

- Python 3.6+
- Ubuntu/Debian-based Linux distribution
- Internet connection for downloading packages

## License

[MIT License](LICENSE)

## Contribution

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.
