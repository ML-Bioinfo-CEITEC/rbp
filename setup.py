import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='rbp',
    version='0.1',
    description='Python utils of RBP Bioinformatics.',
    author='',
    author_email='lamparna@gmail.com',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=[],
    setup_requires=['pytest-runner'],
    install_requires=[
        'pip==19.2.2',
        'pytest>=4.6.1',
        'codecov>=2.0.15',
        'pytest-cov>=2.6.1',
        'numpy>=1.17.0',
        'pandas>=0.25.0',
        'pyaml>=18.11.0',
        'seaborn>=0.9.0',
        'matplotlib>=3.1.1',
        'jupyter>=1.0.0',
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    include_package_data=True,
    package_data={},
)
