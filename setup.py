from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='reg_modules',
      version='0.1',
      description='Basic Registration and Plotting',
      author='Brian Pollack',
      author_email='brianleepollack@gmail.com',
      license='Pitt',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
