# This file will be resposible for creating machine learning application as a package
# And deploy bin Py py - from where anyone can do the installation and use it.
from setuptools import find_packages, setup
from typing import List

hyphen_e = "-e ."

def get_requirements(file_path:str)->List[str]:
    """
    Return a list of requirements. -e . in requirement file triggers the setup file
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements



setup(
name = "e2eml_project",
version="0.0.1",
author="Gargi",
author_email="gargisharma13.29@gmail.com",
packages=find_packages(),
install_requires = get_requirements("requirement.txt")
)