from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='sopy',
      version='1.6',
      description='A neat way to write SOPs using python',
      url='https://github.com/AakashSasikumar/SOPy',
      author='Aakash Sasikumar and Sourav Johar',
      author_email='aakash.sasikumar@protonmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          "jinja2",
          "beautifulsoup4",
          "requests"
      ],
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
