from setuptools import setup

setup(
    name='YourProjectName',
    version='1.0',
    packages=['your_package'],
    install_requires=[
        # Other dependencies
        'git+https://github.com/abewley/sort.git'
    ],
)
