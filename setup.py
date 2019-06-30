from setuptools import setup, find_packages

exec(open('ancli/version.py').read())

dev_requirements = {'dev': [
    'pytest'
]}

setup(
    name='ancli',
    version=__version__,
    maintainer='devforfu',
    description='Small utility to convert functions into CLI',
    long_description=open('README.md').read(),
    url='https://github.com/devforfu/ancli',
    download_url='https://github.com/devforfu/ancli/archive/v0.1.1.tar.gz',
    install_requires=[],
    packages=find_packages(),
    extra_require=dev_requirements,
    tests_require=['pytest']
)
