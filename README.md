# Python tutorial
This brief tutorial was made by Bryan Ostdiek at the University of Oregon. It is only a very brief crash course, aimed at helping physicists use python for their analyses. For now, we will cover installation (and how to get other packages), basic Python (doing thing the pythonistic way), numerical python (NumPy), data tables (Pandas), plotting (matplotlib), and machine learning techniques and/or ROOT (pyROOT) if interested.

# Installing
We will use the [Anaconda Distribution package manager](https://docs.anaconda.com/anaconda/) for nearly everything (a few packages are easier to use pip instead).

 * Go to the [installation](https://www.anaconda.com/download/) page to download and install. I use Python 2.7, but most packages now work with both. If you don't already have python, get version 3, and I will try to learn the updates too.
 * This should already include
  * [SciPy](https://scipy.org)
    * [NumPy](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html): NumPy is the fundamental package for scientific computing with Python.
    * [Matplotlib](https://matplotlib.org/users/pyplot_tutorial.html): Everything for plotting
    * [Sympy](http://www.sympy.org/en/index.html): Symbolic mathematics. I haven't used this yet, but it could be really cool!
    * [Pandas](http://pandas.pydata.org/pandas-docs/stable/): Data structures & analysis
   * Jupyter notebooks: Looks like Mathematica. Allows for code to be run line by line.
 * New packages will be installed with  
  * ```conda install package-name```
 * Packages are updated with
  * ```conda update package-name```

To see this in action, we will check if there are any needed updates some of the SciPy packages. Type into the command line ```conda update scipy numpy pandas``` If any of the packages need to be updated, enter 'y'.

Lastly, before we get started with coding, install the jupyter notebook extensions with:
```
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge jupyter_nbextensions_configurator
```
which will allow us to make our notebooks look nicer by adding folding code and a table of contents.

# Getting started
Now that everything is installed, let's get started with our first examples.
In your terminal, type in ```jupyter notebook```. This should open a window in your default web browser. It looks similar to a finder window, where we can see our different files. In the upper part of the window, there should be a set of tabs such as "Files", "Running", and "Nbextensions". Click on "Nbextensions". Then, check the box next to Table of Contents (2). This will now be the default you **do not** need to do this every time.

## Make a new notebook
Go back to the "Files" menu. In the upper-right hand corner, click on "New", then under Notebooks, click on "Python [default]". This opens a new notebook with a name of *Untitled*. It is automatically saved, so we should re-name it to something useful. To do this, double click on *Untitled* right next to the **jupyter** logo. Name your notebook "MyFirstNotebook"

## Notebook basics
Each cell of the notebook can contain either code or markdown. With markdown, we can use LaTeX and build our table of contents to make moving around the notebook very easily.
 * Click on the first cell. Then on the menu option "Cell > Cell Type > Markdown". (Note that there are keyboard hotkeys to do this automatically.) Make a section by typing

 ```
 # Starting with python and markdown
We can use $\LaTeX$ to make our code look very nice.
Here is an example equation: $(i \gamma^{\mu} \partial_{\mu} -m) \psi = 0$
```
Hit 'shift+return' to run the cell.

 * The default new cell should always be a coding cell. If for some reason you don't have code cell, you can change it with the "Cell > Cell Type" menu. We will go over more of the basic python syntax in person. For now, in the cell, type in  ```AUTHOR = 'put your name'``` and run the cell.

  * In the next cell, we will print the name stored in AUTHOR. This is different for Python 2 and Python 3.
    * Python 2

    ``` print 'Hello,', AUTHOR ```

    * Python 3

    ```print('Hello,', AUTHOR)```

    * In python 2, print is a statement, not a function. In python 3, it must have the parenthesis, where it is optional for 2.

# Links for more information
 * [Pythonistic coding](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html) This is more than just a style guide, and has examples on how to do loops and other things in the most pythonic way. Doing things the right way can save a lot of time.

 * [Hacker Rank](https://www.hackerrank.com) has free coding lessons (well homework type problems and tutorials).

 * [Python.org](https://www.python.org): official website and documentation. Even just the opening sequence shows some syntax and the power of python.
