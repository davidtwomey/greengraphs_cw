from setuptools import setup, find_packages

setup(
    name = "Greengraphs",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'geopy', 'numpy', 'requests', 'matplotlib', 'mock']
)