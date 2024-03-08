from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''this function will return a list of the requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(name='titanic_dataset',
      version='0.0.1', 
      author='Subho', 
      author_email='subhajitdatta.riju@gmail.com', 
      packages=find_packages(), 
      install_requires=get_requirements('requirements.txt'))