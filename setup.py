from typing import List
from setuptools import find_packages,setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List:
    '''
    This Function Will return the list of requirements

    '''
    requirements=  []
    with open('requirements.txt') as f:
        requirements = f.readline()
        requirements = [req.replace('/n','') for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
name = 'MLPROJECT',
version = '0.0.1',
author = 'Vasu',
author_email = 'vasunavadiya21@gmail.com',
packages = find_packages(),
install_packages = get_requirements('requirements.txt') )