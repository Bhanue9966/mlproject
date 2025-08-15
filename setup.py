from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_job:
        requirements=file_job.readlines()
        requirements=[req.replace("\,"," ") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(

    name='mlproject',
    version='0.0.1',
    author='Bhanu',
    author_email='bhanue9966@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')

)