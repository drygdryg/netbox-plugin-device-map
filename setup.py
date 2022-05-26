from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netbox-plugin-device-map',
    version='0.1.0',
    description='A simple device map with filter criteria',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor Golovanenko',
    author_email='drygdryg2014@yandex.com',
    license='GPL-3.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
