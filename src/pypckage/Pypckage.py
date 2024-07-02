"""
Pypckage is a tool that facilitates the configuration of a python package. 
You just need to run a command in the terminal and enter some information and Pypckage takes care of everything. 
It creates the "setup.py, LICENSE, README.md, etc", all preconfigured. All you have to do is to customize the created files.
"""


__copyright__  = """
Copyright (c) 2024 LixNew; lixnew2@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = '1.0.11'
__title__ = 'Pypckage'
__description__ = "Pypckage is a tool to facilitate the configuration of a python package."
__autor__ = 'LixNew'
__twitter__ = '@LixNew2'
__url__ = "https://github.com/LixNew2/Pypckage"


#Import
import os, shutil

def _src(path, name, init) -> None:
    """

    """
    try:
        os.mkdir(path)
        os.mkdir(name)
        open(init, "x")
    except:
        print("Error : The directory/files already exists !")

             
def _check_files(path, name, module) -> None:
    #Src
    src_dir = f"{path}\\src"
    package = f"{path}\\src\\{name}"
    init = f"{path}\\src\\{name}\\__init__.py"
    
    #Files
    readme = f"{path}\\README.md"
    setup = f"{path}\\setup.py"
    license_file = f"{path}\\LICENSE"
    
    #Module
    module_file = f"{path}\\{module}.py"
    
    if os.path.exists(path) == True:
        pass
    else:
        print("Error : Path not found !")
        exit()
    
    if os.path.exists(src_dir) != True:
        pass
    else:
        print("Error : 'scr' directory already exists !")
        exit()
        
    if os.path.exists(license_file) != True:
        pass
    else:
        print("Error : 'LICENSE' file already exists !")
        exit()
        
    if os.path.exists(readme) != True:
        pass
    else:
        print("Error : 'README.md' file already exists !")
        exit()
        
    if os.path.exists(setup) != True:
        pass
    else:
        print("Error : 'setup.py' file already exists !")
        exit()
    
    if os.path.exists(f"{module_file}") == True:
        pass
    else:
        print("Error : package file not found ! Your package file must be in the same directory as the setup.py file.")
        exit()
        
    _src(path=src_dir, name=package, init=init)
    with open(f"{path}\\LICENSE", "w") as ls:
        ls.write("""Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
        
    open(f"{path}\\README.md", "x")
    with open(f"{path}\\setup.py", "w") as _cf:
        _cf.write("""from setuptools import setup, find_packages
                    
setup(
name="mylib",
version="0.1.0",
author="myname",
author_email="exemple@example.com",
description="A description of my library",
long_description=open("README.md", encoding="utf-8").read(),
long_description_content_type="text/markdown",
url="https://github.com/exemple/mylib",
packages=find_packages("src"),
package_dir={"": "src"},
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
python_requires=">=3.6",
install_requires=[
    # List of dependencies here
],
)""")
        
    try:
        shutil.move(module_file, f"{path}\\src\\{name}")
    except FileNotFoundError:
        print("Error : file not found !")


def package() -> str:
    path = str(input("Path : "))
    package_name = str(input("Package name : "))
    module_name = str(input("Module name : "))
    _check_files(path=path, name=package_name, module=module_name)


if __name__ == "__main__":
    package()
