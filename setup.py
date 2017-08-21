from setuptools import setup

setup(name='sophora',
      version='0.1',
      description='Python package for Sophora',
      license='...',
      packages=['sophora'],
      zip_safe=False,
      install_requires=[
          'beautifulsoup4',
          'requests',
          'zeep'
      ]
)
