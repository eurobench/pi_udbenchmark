from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.adoc')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.adoc'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'pi_FPM', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='pi_FPM',
    version=version['__version__'],
    description=('Constructing a statistical foot placement model and returns YAMLs with Performance Indicators.'),
    long_description=long_description,
    author='Nick Kluft',
    author_email='n.kluft@vu.nl',
    url='https://github.com/',
    license='Apache 2.0',
    packages=['pi_FPM'],
    scripts=['script/run_fpm'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
