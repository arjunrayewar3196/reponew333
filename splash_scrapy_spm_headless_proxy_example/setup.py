# Automatically created by: shub deploy
from setuptools import setup, find_packages

setup(
    name = 'project',
    version = '1.0',
    packages = find_packages(),
    package_data = {'splash_scrapy_spm_headless_proxy_example': ['scripts/*.lua',]},
    entry_points = {'scrapy': ['settings = splash_scrapy_spm_headless_proxy_example.settings']},
)
