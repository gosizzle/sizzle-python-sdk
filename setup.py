from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='sizzle',
      version='0.0.1',
      description=u"Python package for development with the S!zzle API",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Bradley Wogsland",
      author_email='bwogsland@gosizzle.io',
      url='https://github.com/gosizzle/sizzle-python-sdk',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      sizzle=src.scripts.cli:cli
      """
      )
