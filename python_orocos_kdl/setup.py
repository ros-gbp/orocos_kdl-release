#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.package import parse_package_for_distutils

d = parse_package_for_distutils()

d['packages'] = ['python_orocos_kdl']
d['package_dir'] = {'': 'lib'}
d['install_requires'] = []

setup(**d)
