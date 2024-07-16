from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Generate Random Numbers & Distributions directly using Mathematics'
LONG_DESCRIPTION = 'A Python library designed to make random number generation and working with various distributions intuitive and easy. Whether you're a student, hobbyist, or developer, rerandom provides a simple interface for generating random numbers and simulating different statistical distributions'

# Setting up
setup(
    name="rerandom",
    version=VERSION,
    author="Rudransh Pratap Singh",
    author_email="tosylfluoride@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'random', 'distribution', 'maths', 'poisson', 'binomial', 'random numbers'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)