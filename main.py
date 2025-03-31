import os
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from ttkbootstrap import Style

class PackageInstallerApp:
    def __init__(self, root):
        # Apply modern theme
        self.style = Style(theme="darkly")  # Themes: darkly, solar, cyborg, superhero
        self.root = self.style.master

        self.root.title("CORTEX41 PACKAGE INSTALLER")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E1E")  # Black background

        # Title Label
        title_label = ttk.Label(root, text="Select The Required Packages", 
                                font=("Arial", 14, "bold"), 
                                background="#1E1E1E", foreground="white")
        title_label.pack(pady=10)

        self.packages = {
            "NVIDIA Toolkit and Docker": tk.BooleanVar(),
            "CUDA": tk.BooleanVar(),
            "NVIDIA Driver": tk.BooleanVar(),
            "Docker-Compose": tk.BooleanVar(),
            "RustDesk": tk.BooleanVar(),
            "VSCode": tk.BooleanVar(),
            "CUDNN": tk.BooleanVar(),
        }

        self.check_buttons = []
        for package, var in self.packages.items():
            chk = ttk.Checkbutton(root, text=package, variable=var)
            chk.pack(anchor="w", padx=20)
            self.check_buttons.append(chk)

        # NVIDIA Driver Version Entry
        self.driver_version_label = ttk.Label(root, text="NVIDIA Driver Version:")
        self.driver_version_label.pack(pady=5)
        self.driver_version_entry = ttk.Entry(root)
        self.driver_version_entry.pack(pady=5)

        # Start Button
        self.start_button = ttk.Button(root, text="Start Installation", command=self.start_installation)
        self.start_button.pack(pady=10)

        # Output Text Box
        self.output_text = scrolledtext.ScrolledText(root, width=70, height=12, state="disabled")
        self.output_text.pack(pady=5)

    def log(self, message):
        """Log messages to the GUI output box."""
        self.output_text.config(state="normal")
        self.output_text.insert("end", message + "\n")
        self.output_text.see("end")
        self.output_text.config(state="disabled")

    def install_packages(self):
        """Install selected packages in a separate thread."""
        self.log("\nSTARTING PACKAGES INSTALLATION!\n")
        os.system("sudo apt update")


        # NVIDIA Container Toolkit Installation
        if self.packages["NVIDIA Toolkit and Docker"].get():
            self.log("INSTALLING NVIDIA Container Toolkit...")
            os.system(
                "curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
                && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
                sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
                sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list"
            )
            os.system("sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list")
            os.system("sudo apt-get update")
            os.system("sudo apt-get install -y nvidia-container-toolkit")
            os.system("sudo apt install -y nvidia-docker2")
            self.log("NVIDIA CONTAINER TOOLKIT INSTALLATION DONE!\n")

        # CUDA Installation
        if self.packages["CUDA"].get():
            self.log("Installing NVIDIA CUDA..")
            os.system("wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run")
            os.system("sudo chmod a=rwx cuda_12.1.0_530.30.02_linux.run")
            os.system("sudo ./cuda_12.1.0_530.30.02_linux.run")
            self.log("CUDA 12.1 INSTALLATION DONE!\n")


        # CUDNN Installation
        cookies_file = "cookies.txt"  # Make sure this file is valid
        download_url = "https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.7/local_installers/12.x/cudnn-local-repo-ubuntu2204-8.9.7.29_1.0-1_amd64.deb"
        output_file = "cudnn-local-repo.deb"

        if self.packages["CUDNN"].get():
            self.log("Installing NVIDIA CUDNN...")
            os.system(f'wget --debug -v --progress=bar:force --load-cookies {cookies_file} "{download_url}" -O {output_file}')
            os.system("sudo apt install ./cudnn-local-repo.deb")
            self.log("CUDNN INSTALLATION DONE!\n")


        # NVIDIA Drivers Installation
        if self.packages["NVIDIA Driver"].get():
            version = self.driver_version_entry.get().strip() or "535"
            self.log(f"INSTALLING NVIDIA DRIVER {version}...")
            os.system(f"sudo apt install -y nvidia-utils-{version}")
            os.system(f"sudo apt install -y nvidia-driver-{version}")
            self.log("NVIDIA DRIVER INSTALLATION DONE!\n")

        # Docker-Compose Installation
        if self.packages["Docker-Compose"].get():
            self.log("INSTALLING Docker-Compose-v2...")
            os.system("sudo apt install -y docker-compose-v2")
            self.log("Docker-Compose-v2 INSTALLATION DONE!\n")

        # RustDesk Installation
        if self.packages["RustDesk"].get():
            self.log("INSTALLING RUSTDESK...")
            os.system("wget https://github.com/rustdesk/rustdesk/releases/download/1.3.7/rustdesk-1.3.7-x86_64.deb")
            os.system("sudo apt install ./rustdesk-1.3.7-x86_64.deb")
            self.log("RUSTDESK INSTALLATION DONE!\n")

        # VSCode Installation
        if self.packages["VSCode"].get():
            self.log("INSTALLING VSCode...")
            os.system("sudo apt-get install wget gpg")
            os.system("wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg")
            os.system("sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg")
            os.system('echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null')
            os.system("rm -f packages.microsoft.gpg")
            os.system("sudo apt install apt-transport-https")
            os.system("sudo apt update")
            os.system("sudo apt install -y code")
            self.log("VSCode INSTALLATION DONE!\n")

        self.log("\nALL REQUIRED PACKAGES INSTALLED!\n")
        self.log("Please reboot the system to ensure everything is working.")

    def start_installation(self):
        """Start the installation process in a separate thread to prevent UI freezing."""
        selected_packages = [pkg for pkg, var in self.packages.items() if var.get()]
        if not selected_packages:
            messagebox.showwarning("No Packages Selected", "Please select at least one package to install.")
            return

        self.start_button.config(state="disabled")
        install_thread = threading.Thread(target=self.install_packages)
        install_thread.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = PackageInstallerApp(root)
    root.mainloop()
