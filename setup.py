from setuptools import setup, find_packages

with open('README.md', "r") as fh:
    long_description = fh.read()

setup(
    name='trademaster',
    version='0.0.1',
    description='TradeMaster - A platform for algorithmic trading',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='NTU_trademaster',
    author_email='TradeMaster.NTU@gmail.com',
    url='https://github.com/TradeMaster-NTU/TradeMaster',
    packages=find_packages(include=["trademaster*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[],
)
