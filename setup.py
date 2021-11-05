from setuptools import setup, find_packages
from distutils.core import setup
with open('README.md') as fp:
    DESCRIPTION = fp.read()

setup(
    name="sn-sentinel", 
    install_requires=[],
    version='0.1.0',
    description=DESCRIPTION,
    author='Ben Quek',
    author_email='ben.quek@ben-labs.net',
    maintainer='Ben Quek',
    maintainer_email='ben.quek@ben-labs.net',
    url='https://github.com/ben-labs/sn-sentinel',
    packages=['blab', 'blab.sentinel'],
    package_dir={'':'src'}
)