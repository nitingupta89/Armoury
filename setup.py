import io
from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()


setup(
    name='PyUtils',
    version='0.1.dev',
    packages=['pyutils',],
    license='MIT',
    author='Nitin Gupta',
    author_email='nitinguptawebdev@gmail.com',
    description='Collection of utility methods.',
    long_description=readme
)
