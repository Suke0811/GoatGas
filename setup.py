from setuptools import setup, find_packages
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='GOAT Gas Gripper Driver',
    version='0.1',
    description='Gas operated GOAT gripper driver for python.',
    author='Yusuke Tanaka',
    license='LGPLv3',
    packages=find_packages(include=['GoatGasDriver', 'GoatGasDriver.*']),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Robot Framework'
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3',
    ],
)
