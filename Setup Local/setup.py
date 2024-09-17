import os
import subprocess
import sys
import distutils.core

def run_command(command):
    """Run a system command and print the output."""
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode().strip()}")
        sys.exit(1)
    else:
        print(stdout.decode().strip())

def check_conda_env():
    """Check if a Conda environment is activated."""
    conda_prefix = os.getenv("CONDA_PREFIX")
    if conda_prefix is None:
        print("Error: No Conda environment is activated. Please activate a Conda environment and try again.")
        sys.exit(1)
    else:
        print(f"Conda environment activated: {conda_prefix}")
        return conda_prefix

def install_packages():
    """Install required packages in the currently active Conda environment."""
    run_command("pip install pyyaml==5.1")
    run_command("pip install ultralytics")

def clone_and_install_detectron2():
    """Clone the Detectron2 repository and install its dependencies."""
    if not os.path.exists("detectron2"):
        run_command("git clone https://github.com/facebookresearch/detectron2.git")
    
    # Install Detectron2 dependencies
    dist = distutils.core.run_setup("./detectron2/setup.py")
    run_command(f"pip install {' '.join([f'{x}' for x in dist.install_requires])}")
    sys.path.insert(0, os.path.abspath('./detectron2'))

def main():
    check_conda_env()
    install_packages()
    clone_and_install_detectron2()
    
    print("Setup complete.")

if __name__ == "__main__":
    main()
