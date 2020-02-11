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
    version='0.1.2',
    description='Python utils of RBP Bioinformatics.',
    author='RBP Bioinformatics',
    author_email='lamparna@gmail.com',
    license='MIT',
    keywords=['bioinformatics', 'genome', 'dna'],
    url='https://gitlab.com/RBP_Bioinformatics/rbp',
    download_url='https://gitlab.com/RBP_Bioinformatics/rbp/-/archive/master/rbp-master.tar.gz',
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
        'tqdm>=4.41.1',
        'pybedtools>=0.8.1',
        'pyBigWig>=0.3.17'
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    include_package_data=True,
    package_data={},
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
