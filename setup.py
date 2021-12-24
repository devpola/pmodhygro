from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pmodhygro',
    version='1.0.1',
    description='pmodhygro is python library to read PmodHYGRO that is relative humidity sensor with integrated temperature sensor on a Raspberry Pi',
    long_description  = read('README.md'),
    long_description_content_type='text/markdown',
    author='devpola',
    author_email='sonamoo9771@gmail.com',
    url='https://github.com/devpola/pmodhygro',
    license='MIT',
    py_modules=['pmodhygro'],
    install_requires=['smbus2'],
    packages=['pmodhygro'],
    classifier=[
        'Operating System :: POSIX :: Linux',
        'Environment :: Raspberry Pi'
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Sensor',
    ],)