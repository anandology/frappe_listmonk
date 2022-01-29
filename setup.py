from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_listmonk/__init__.py
from frappe_listmonk import __version__ as version

setup(
	name="frappe_listmonk",
	version=version,
	description="Listmonk interface for Frappe.",
	author="Anand Chitipothu",
	author_email="anandology@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
