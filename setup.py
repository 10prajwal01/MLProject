from setuptools import find_packages, setup
from typing import List

HYPEN_R_DOT = '-e .'

def get_requirements(file_path: str)->List[str]:
    """
    This function return the list of requiremnts
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_R_DOT in requirements:
            requirements.remove(HYPEN_R_DOT)

    return requirements

setup(
    name = 'mlproject',
    version ='0.0.1',
    author ='Prajwal',
    author_email ='prajwal15301@gmail.com',
    packages = find_packages(),
    install_required = get_requirements('requirements.txt')

)