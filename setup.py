from setuptools import setup, find_packages

setup(
    name='myhack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Analyse Hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/neosenokwane/myhack.git',
    author='Neo Senokwane',
    author_email='neosenokwane@gmail.com'
)
