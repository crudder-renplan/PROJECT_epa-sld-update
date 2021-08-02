from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='epa-sld-update',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='EPA Access to Jobs',
    long_description=long_description,
    author='Renaissance Planning',
    license='Apache 2.0',
)
