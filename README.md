## RBP

This package contains Python tools frequently used at the Panagiotis Alexiou's group at CEITEC (Brno, Czechia).

### Introduction
 - We use Python3 (ideally 3.7.4)   
 - For testing, we use pytest.  
 - Please, use virtualenv / pyenv / conda environments. 
 - To make your life easier, set up [GitLab SSH keys](https://gitlab.com/help/ssh/README#generating-a-new-ssh-key-pair) (if you have never done that, let me help you).
 - Ask for forgiveness, not for permission. We are currently all admins, you are allowed to push to master branch.

### Install
 - Clone this repository
   - `git clone git@gitlab.com:RBP_Bioinformatics/rbp.git`
 - Cd into the folder and install `rbp` package with `make/setuptools`
   - `cd rbp`
   - `make develop` 

### Structure of the package
We describe just high-level structure of package. Details related to particular modules etc. find in dedicated READMEs.
 - `examples` - Examples should be kept up to date. They demonstrate package functionalities.
 - `notebooks` - Notebooks are excluded from tests, showcasing best practices and interesting experiments. Those notebooks can become obsolete during the time. Notebooks may use packages not included in `requirements.txt`.
 - `tests` - Test coverage of rbp package.
 - `src/rbp`  - Contains the package itself.
   - `utils` -   system utilities (file i/o, parsing arguments, ...)

## Development
 - Update master: `git checkout master`, `git pull` 
 - Modify the code (write new module)
 - **Always** write tests, keep the test coverage over 80%.
 - Run tests as `make test` to check everything works, you can also test a specific file or tests in a specific folder with `pytest -v ./tests/test_specific_file.py`.
 - Commit the changes to git and push them to Gitlab: `git push origin HEAD` (Never `push --force` to master!)
 - Consider adding an example or a notebook (be nice to future self and the others).
 - Ask somebody else from the lab to discuss the changes you made. Document what you have done.
 
### How to rock
If you develop something big or refactor the whole package, create a new branch `git checkout -b my_huge_feature` and pull request. Ask for review before merging to master. 

If you have a problem, probably everyone has a similar problem. Ask for help, add more documentation, fix it globally and for everyone.

If you have an idea how to improve the package, put it on [the List](https://docs.google.com/document/d/16rYS_vpz0vdQ3F9lHVQML1CkQCgohLGFX79erP8NYPY/edit?usp=sharing). If you have time, check the List and implement something. 

### Codestyle
Linters are your friends. For Visual Studio, I recommend PEP-8 and FLAKE8 with minor relaxations (e.g. allow longer lines).


