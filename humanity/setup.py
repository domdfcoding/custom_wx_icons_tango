#!/usr/bin/env python
"""
custom_wx_icons Setup script
"""

#  Copyright (C) 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py


# stdlib
import pathlib

# 3rd party
from setuptools import find_packages, setup

# this package
from __pkginfo__ import (
	author, author_email, general_trove_classifiers, get_requirements_and_readme, prepare_data_files, web,
	)


theme_name = "Humanity"
VERSION = "0.1.0"
modname = f"wx_icons_{theme_name.lower()}"
license = 'GPLv2'
short_desc = 'description goes here'

install_requires, long_description = get_requirements_and_readme(pathlib.Path.cwd())

classifiers = [
		# "Development Status :: 1 - Planning",
		# "Development Status :: 2 - Pre-Alpha",
		"Development Status :: 3 - Alpha",
		# "Development Status :: 4 - Beta",
		# "Development Status :: 5 - Production/Stable",
		# "Development Status :: 6 - Mature",
		# "Development Status :: 7 - Inactive",
		
		"License :: OSI Approved :: GNU General Public License 2 or later (GPLv2)",
		] + general_trove_classifiers


data_files = prepare_data_files(modname, theme_name)
data_files += prepare_data_files(modname, f"{theme_name}_Dark")


setup(
		author=author,
		author_email=author_email,
		classifiers=classifiers,
		description=short_desc,
		install_requires=install_requires,
		license=license,
		long_description=long_description,
		name=modname,
		packages=find_packages(exclude=("tests",)),
		url=web,
		version=VERSION,
		package_data={modname: data_files},
		include_package_data=True,
		# data_files=[
		# 	(theme_name, data_files),
		# 	]
		)