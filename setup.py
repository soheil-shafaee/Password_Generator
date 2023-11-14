from setuptools import setup, find_packages

setup(
    name= "Password_Generator",
    version="1.0.0",
    packages= find_packages(),
    install_requires = [
        "PyQt5", "PyQt5Designer"
    ],
    entry_points= {
        "console_scripts" :[
            "password_Generator=password_generator:main"
        ]
    }


)
