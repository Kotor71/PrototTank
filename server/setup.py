from setuptools import setup

setup(
   name='ProtoTank',
   version='1.0',
   description='Main software for Robot',
   author='Louis Sabatier',
   author_email='ls@ls.fr',
   packages=['Client'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
)