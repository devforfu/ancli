from setuptools import setup, find_packages

exec(open('loop/version.py').read())

dev_requirements = {'dev': [
    'pytest'
]}

setup(
    name='ancli',
    maintainer='devforfu',
    description='Small utility to convert functions into CLI',
    install_requires=[],
    packages=find_packages(),
    extra_require=dev_requirements,
    tests_require=['pytest']
)
