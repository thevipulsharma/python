# setup.py
from setuptools import setup

'''
name - Identifies the distribution. It's common practice to name the distribution after the module.
py_modules - List of .py files to be included in the module.
'''

setup(
	name = 'vowel_search',
	version = '1.0',
	description = 'My first module.',
	author = 'Vipul Sharma',
	author_email = 'vipuls526@gmail.com',
	url = 'www.example.com',
	py_modules = ['vowel_search']
)