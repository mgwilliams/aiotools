from setuptools import setup, find_packages
from codecs import open
from os import path
import sys


__version__ = '0.0.1'

if sys.version_info < (3, 5):
        sys.exit('Sorry, Python < 3.5 is not supported')

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in
                    all_reqs if 'git+' not in x]

setup(
    name='aiotools',
    version=__version__,
    description='Miscellaneous asyncio modules.',
    long_description=long_description,
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Matthew Williams',
    url='http://github.com/mgwilliams/aiotools',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email=''
)
