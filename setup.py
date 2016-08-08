from setuptools import setup

setup(name='hubcli',
      version='0.1',
      description='CLI tool for Docker Hub',
      url='http://github.com/larsla/hubcli',
      author='Lars Larsson',
      author_email='lars.la@gmail.com',
      license='MIT',
      scripts=['bin/hubcli'],
      install_requires=[
          'requests',
          'pyyaml'
      ],
      zip_safe=False)
