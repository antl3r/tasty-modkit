from setuptools import setup, find_packages

setup(
    name='tasty-modkit',
    version='0.1.0',
    author='Lovell D\'Arce',
    author_email=''
    description='A modkit for synchronizing workshop mods with non-steam games.',
    long_description=''
    url='https://github.com/antl3r/tasty-modkit',
    license='MIT',
    packages=['tasty'],
    install_requires=[
        'configparser',
        'requests',
    ],
)
