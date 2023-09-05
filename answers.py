# Question 1
# To install an external Python package using “pip”, follow these step-by-step instructions.
#
# Step 1: Open a Command Prompt or Terminal
#
# First, you need to open a command prompt or terminal window on your computer.
#
# Step 2: Check if pip is Installed
#
# Before installing any packages, it's a good idea to check if pip is already installed on your system. You can do this by running the following command:
# pip - -version
# If pip is installed, you will see its version number. If it's not installed, you'll need to install it first. You can follow the official documentation for installing pip on your system: https://pip.pypa.io/en/stable/installation/
# Step 3:After Installing pip next you can install requests packages:
# pip install requests
# Step 4: Verify the Installation After the installation process is complete, you can verify that the requests package has been successfully installed by running the following command:
import requests
print(requests.__version__)
# Questions :2
# virtual environments in Python are used to create isolated spacesfor different projects,so that the packages and dependencies for one project don('t interfere with another. They help keep your projects organized, prevent conflicts between packages, and make it easier to manage and control the versions of packages used in each project. Virtual environments keep your Python environment'
# ' clean and secure, making Python development more efficient and reliable.)
# step:1
# Open a Command Prompt and run the following commands:
# Create a virtual environment named "myenv"
# python -m venv myenv

# Activate the virtual environment
# myenv\Scripts\activate

# Question:3
# A "requirements.txt" file is a text file commonly used in Python development to specify a list of required
# Python packages and their versions. It's often used to document and automate the installation of dependencies for a Python project. This file can be read by tools like pip to install the specified packages and their versions, ensuring consistency and reproducibility across different environments.
