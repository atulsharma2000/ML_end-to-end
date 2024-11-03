from setuptools import find_packages, setup  # Import necessary functions from setuptools
from typing import List  # Import List for type hinting
import os  # Import os for file handling

HYPEN_E_DOT = "-e ."  # "onstant for editable install specifier

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements specified in the requirements.txt file.
    It removes any newline characters and filters out the editable install specifier '-e .'.
    '''
    if not os.path.exists(file_path):  # Check if the requirements file exists
        raise FileNotFoundError(f"{file_path} not found.")  # Raise an error if not found
    
    requirements = []  # Initialize an empty list to hold requirements
    with open(file_path) as file_obj:  # Open the requirements file
        requirements = file_obj.readlines()  # Read all lines from the file
        # Remove newline characters and filter out any empty lines
        requirements = [req.replace("\n", "") for req in requirements if req.strip()]
        
        # Remove '-e .' if present in the requirements list
        if HYPEN_E_DOT in requirements:  
            requirements.remove(HYPEN_E_DOT)  

    return requirements  # Return the processed list of requirements

# Setup function to configure the package
setup(
    name="ML_end-to-end",  # Name of the package
    version='0.0.1',  # Version of the package
    author='atul',  # Author of the package
    author_email='atullsharma2000@gmail.com',  # Author's email address
    packages=find_packages(),  # Automatically find all packages available in the project (those containing __init__.py)
    install_requires=get_requirements("requirements.txt")  # Get and install required packages from requirements.txt
)