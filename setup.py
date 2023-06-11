from setuptools import setup, find_packages
                    
setup(
name="pypckage",
version="1.0.11",
author="LixNew",
author_email="lixnew2@gmail.com",
description="Pypckage is a tool to facilitate the configuration of a python package.",
long_description=open("README.md", encoding="utf-8").read(),
long_description_content_type="text/markdown",
url="https://github.com/LixNew2/Pypckage",
packages=find_packages("src"),
package_dir={"": "src"},
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
python_requires=">=3.6",
install_requires=[
    "psutil"
],
entry_points={
        'console_scripts': [
            'pypck-build=pypckage:package',
        ]
    },
)

