from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.readlines()

with open('README.md') as f:
  long_description = f.read()

setup(
		name ='corgi-cli',
		version ='1.0.0',
		author ='Raleigh Wise',
		author_email ='vibhu4agarwal@gmail.com',
		url ='https://github.com/l3gacyb3ta/corgi',
		description ='A modern doggo.ninja cli.',
		long_description = long_description,
		long_description_content_type ="text/markdown",
		license ='UNLICENSE',
		packages = find_packages(),
		entry_points ={
			'console_scripts': [
				'corgi = corgi_cli.corgi:parser'
			]
		},
		classifiers =(
			"Programming Language :: Python :: 3",
			"Operating System :: OS Independent",
		),
		keywords ='doggo.ninja doggo ninja cli bone',
		install_requires = requirements,
		zip_safe = False
)
