from setuptools import setup, find_packages

setup(
    name="HS_Modules",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.4",
        "psutil>=5.9.0"
    ],
    author="Gratonic, FailurePoint",
    author_email="Gratonic@proton.me, FailurePoint@proton.me"
)