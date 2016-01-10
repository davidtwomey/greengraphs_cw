from setuptools import setup, find_packages

setup(
    name = "Greengraphs",
        author = "David Twomey",
        author_email = "david.twomey.15@ucl.ac.uk",
    version = "1.0",
        license = "MIT",
        description = "Package which generates a graph of the proportion ofgreen pixels in a series of satellite images between two points",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'geopy', 'numpy', 'requests', 'matplotlib', 'mock']
)