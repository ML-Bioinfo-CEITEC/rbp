[![PyPI version](https://badge.fury.io/py/rbp.svg)](https://badge.fury.io/py/rbp) 
[![Travis-CI status](https://travis-ci.org/ML-Bioinfo-CEITEC/rbp.svg?branch=master)](https://travis-ci.org/ML-Bioinfo-CEITEC/rbp?branch=master)
[![codecov](https://codecov.io/gh/ML-Bioinfo-CEITEC/rbp/branch/master/graph/badge.svg)](https://codecov.io/gh/ML-Bioinfo-CEITEC/rbp)
[![ReviewNB](https://img.shields.io/badge/render-reviewnb-orange.svg)][https://app.reviewnb.com/ML-Bioinfo-CEITEC/rbp/]

## RNA Biology Package

This package contains Python tools for RNA Biology, frequently used at the Panagiotis Alexiou's group at CEITEC (Brno, Czechia).

### For lab members
 - We use Python3 (ideally 3.7.4)   
 - For testing, we use pytest. (For automated testing, we use [Travis CI](https://travis-ci.org/ML-Bioinfo-CEITEC/rbp?branch=master).)
 - To make your life easier, get GitHub account, ask to be added to `ML-Bioinfo-CEITEC` organization and set up [GitHub SSH keys](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) (if you have never done that, let me help you).
 - Please, use virtualenv / pyenv / conda environments for everybody's sake.
 - Ask for forgiveness, not for permission. We are currently all admins, you are allowed to push to the master branch.

### Install

From [GitHub](https://github.com/ML-Bioinfo-CEITEC/rbp):
 - Clone this repository
   - `git clone git@github.com:ML-Bioinfo-CEITEC/rbp.git`
 - Cd into the folder and install `rbp` package with `make/setuptools`
   - `cd rbp`
   - `make develop` (or `make install`) 

From [PyPi](https://pypi.org/project/rbp/) (do not use for development):
 - `pip install rbp`

### Structure of the package
We describe just high-level structure of package. Details related to particular modules etc. find in dedicated READMEs.
 - `examples` - Examples should be kept up to date. They demonstrate package functionalities.
 - `notebooks` - Notebooks are excluded from tests, showcasing best practices and interesting experiments. Those notebooks can become obsolete during the time. Notebooks may use packages not included in `requirements.txt`.
 - `tests` - Test coverage of rbp package.
 - `src/rbp`  - Contains the package itself.
   - `encoding` -   functions to encode/decode genomic sequences into numeric vectors
   - `preprocessing` - conversion between formats (bed -> fasta, bed -> conservation)
   - `random` -   random genomic coordinates, permutations (shuffling) of genomic sequences
   - `utils` -   system utilities (file i/o, parsing arguments, ...)

## Development
 - Update master: `git checkout master`, `git pull` 
 - Modify the code (e.g. add a new module).
 - **Always** write tests.
 - Run tests as `make test` to check everything works, you can also test a specific file or tests in a specific folder with `pytest -v ./tests/test_specific_file.py`.
 - If you added a new dependence, update `setup.py` and `requirements.txt` (ask for help if you need it).
 - Commit the changes to git and push them to GitHub: `git push` (Never `push --force` to master!)
 - Consider adding an example or a notebook (be nice to future self and the others).
 - Ask somebody else from the lab to discuss the changes you made. Document what have you done.
 
### How to rock
If you develop something big or refactor the whole package, create a new branch `git checkout -b my_huge_feature` and pull request. Ask for review before merging to master. 

If you have a problem, probably everyone has a similar problem. Ask for help, add more documentation, fix it globally and for everyone.

If you have an idea how to improve the package, put it as an [Issue](https://github.com/ML-Bioinfo-CEITEC/rbp/issues). If you have time, check the issues and fix/implement something. 

### Codestyle
Linters are your friends. For Visual Studio, I recommend [PEP-8 and FLAKE8](https://code.visualstudio.com/docs/python/linting#_specific-linters) with minor relaxations (e.g. allow longer lines).

### Pushing to Python Package Index 

I am following [this guide](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56). To push a new version to PyPI, first check that all tests are passing (`make test`), then increase the version of `rbp` in `setup.py` and finally run the following:

```
  python setup.py sdist
  twine upload dist/*
```

You need to have an account at [PyPI](https://pypi.org/) and be registered as the package's maintainer.

### GitLab Mirror

This repository has a mirror on GitLab [RBP_Bioinformatics/rbp](https://gitlab.com/RBP_Bioinformatics/rbp). Push to this repository using `git push --mirror gitlab`. Create a new mirror from an empty repository by `git remote add NAME_OF_MIRROR git@gitlab.com:USER_NAME/rbp.git`.
