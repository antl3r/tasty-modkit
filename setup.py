import distutils.core

setup(
    name='tasty-modkit',
    version='0.1.0',
    author='Lovell D\'Arce',
    author_email='',  # Leave blank as per your input
    description='A modkit for synchronizing workshop mods with non-steam games.',
    long_description='',  # Leave blank as per your input
    url='https://github.com/antl3r/tasty-modkit',
    license='MIT',
    packages=['tasty'],
    install_requires=[
        'configparser',
        'requests',
    ],
)
