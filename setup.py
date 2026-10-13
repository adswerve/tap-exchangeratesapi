from setuptools import setup, find_packages

setup(name='tap-exchangeratesapi',
      version='1.0.1',
      description='Singer.io tap for extracting currency exchange rate data from the exchangeratesapi.io API',
      author='Stitch',
      url='http://github.com/adswerve/tap-exchangeratesapi',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_exchangeratesapi'],
      install_requires=['singer-python==6.8.0',
                        'backoff==2.2.1',
                        'requests==2.34.2'],
      extras_require={
          'dev': [
              'ipdb==0.13.13'
          ]
      },
      entry_points='''
          [console_scripts]
          tap-exchangeratesapi=tap_exchangeratesapi:main
      ''',
      packages=['tap_exchangeratesapi'],
      include_package_data=True
)
