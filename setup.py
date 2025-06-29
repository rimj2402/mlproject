from setuptools import find_packages, setup
import os
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """
    requirements = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            # Skip blank lines or comments
            if not line or line.startswith("#"):
                continue
            # Skip editable install
            if line.startswith("-e") or line.startswith("--editable"):
                continue
            requirements.append(line)
    return requirements

      
setup(
    name="mlproject",
    version="0.1.0",
    author="Rimjhim",
    author_email="rimj2402@gmail.com",
    packages=find_packages(),
    # install_requires=[
    #     # Add your project dependencies here, e.g.:
    #      "numpy>=1.21.0",
    #      "scikit-learn>=1.0.0",
    # ],
    description="A machine learning project.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/rimj2402/mlproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires=">=3.6",
    install_requires=get_requirements("requirements.txt"),
)

