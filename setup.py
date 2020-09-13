from setuptools import setup

setup(name='sopy',
      version='1.0',
      description='A neat way to write SOPs using python',
      url='https://github.com/AakashSasikumar/SOPy',
      author='Aakash Sasikumar and Sourav Johar',
      author_email='aakash.sasikumar@protonmail.com',
      license='MIT',
      packages=['./'],
      install_requires=[
          "jinja2",
          "beautifulsoup4"
      ],
      zip_safe=False)
