from setuptools import setup, find_packages

setup(
    name = "Greengraphs",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/Greengraph'],
    install_requires = ['argparse']
)