from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    it will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            ##process each line
            for line in lines :
                requirement = line.strip()
                 ##ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError as e:
        print("filenot found error")                 
    
    return requirement_list


setup(
    name = "PROJECT2",
    version = "0.0.1",
    author ="Lokesh",
    author_email = "Lokeshs2k6@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)