from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='nanth',
	version='0.01',
	description='Personal tools for use in scientific analysis',
	url='https://github.com/Nickroll/nanth',
	author='Nick Roller',
	author_email='rick.nickroller@gmail.com',
	license='MIT',
	packages=['nanth'],
	install_requires=[
		'pandas',
		'numpy',
		'scipy',
		],
	zip_safe=False)

