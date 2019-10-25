from setuptools import setup

setup(
   name='ProtoTank',
   version='1.0',
   description='Main software for Robot',
   author='Louis Sabatier',
   author_email='ls@ls.fr',
   packages=['server'],  #same as name
   install_requires=['i2c-tools', 'adafruit-pca9685','rpi_ws281x','numpy','imutils'], #external packages as dependencies
)