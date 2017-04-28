.. _install-reference-label:

============
Installation
============

Python 3!
---------

.. attention:: Python 3 is needed!
    This is *only Python 3* and does not support Python 2 at all.

On CentOS 7, Follow these steps::

    $ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
    $ sudo yum install -y python36u python36u-devel python36u-pip
    $ sudo ln -si /usr/bin/python3.6 /usr/bin/python3  
    $ sudo ln -si /usr/bin/pip3.6 /usr/bin/pip3 

You *might* want the following installed as well::

    $ sudo pip3 install virtualenv virtualenvwrapper
    $ sudo pip3 install ipython pdbpp

Tests
-----

Once you have the source code cloned somewhere, you can (read: should) run the
tests via `tox` and depending on which version of Python you have
installed.

On the supported version, aka Python 3.6, run::

    $ tox -r -e py36

If you have all of them installed, run::

    $ tox

Any failures is likely to point to something seriously wrong and you should
open a full `mantis bug`_ with as much information as possible.

.. _mantis bug: https://github.com/kierun/npcseed/issues.

Notes on code coverage
----------------------

We should aim for at least 100% of test coverage.  This means that all the
code is run at least once by the tests.  This is a pretty low bar! For this,
we have the `coverage`_ tool installed.

.. _coverage: http://nedbatchelder.com/

Virtual environments install
----------------------------

A quick refresher of `virtual environments`_ in Python might be good
idea.

.. _virtual environments: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Virtualenv
^^^^^^^^^^

If you just have `virtualenv`, then do::

    $ virtualenv env
    $ source env/bin/activate
    $ pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r requirements/devel.txt
    $ make coverage
    $ make docs

You should not be using this method.

Virtualenvwrapper
^^^^^^^^^^^^^^^^^

But there is a better solution with `virtualenvwrapper`. 

Setup
"""""

To install `virtualenvwrapper`::

    $ pip install --user virtualenvwrapper
    $ export WORKON_HOME=~/Envs
    $ source ~/.local/bin/virtualenvwrapper.sh

To permanently save those settings to a Bourne compatible shell::

    $ cat >> ~/.shellrc <<- EOM
    # virtualenvwrapper
    export WORKON_HOME=~/Envs
    source ~/.local/bin/virtualenvwrapper.sh
    EOM

Where `shellrc` is whatever your shell runtime configuration file is
called -- `.zshrc` or `.bashrc` for example.




Install npcseed via virtualenvwrapper
"""""""""""""""""""""""""""""""""""""

Then, or if you already had `virtualenvwrapper` installed and
configured, run the following::

    $ mkvirtualenv -v npcseed --python=`which python3`
    $ workon npcseed
    $ pip install --upgrade pip
    $ pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r requirements/requirements.txt
    $ make coverage
    $ make behave

These steps are optional and only needed if you want to update to the latest
version of everything::

    $ pip install wheelhouse
    $ pip install --upgrade -r requirements/devel.txt
    $ make coverage
    $ make behave
    $ pip freeze > requirements/requirements.txt
    $ git rm requirements/wheelhouse/*.whl
    $ wheelhouse -v build
    $ tox
    $ git add requirements/wheelhouse/*.whl
    $ git status
    $ git commit -m 'Mod: Upgrade Python dependencies to latest version.'

Some wheel files need removing from git and new ones added.

Now, install the rest of the wheels::

    $ pip install --use-wheel --no-index --find-links=requirements/wheelhouse -r requirements/devel.txt

or::

    $ pip install --upgrade --use-wheel --no-index --find-links=requirements/wheelhouse -r requirements/devel.txt

Then::

    $ pip freeze > requirements/requirements.txt

Note that if you have wheelhouse installed, you need to remove it from the 
requirements/requirements.txt file.

Run all the tests::

    $ make coverage
    $ make docs

Autoenv
^^^^^^^

Remembering to switch virtual environments is tedious. Thankfully, there
is `autoenv`_! If not already installed, `install autoenv`_. Then run::

    $ cat > .env <<- EOM
    # Autoenv.
    echo -n "Switching to virtual environment: "
    printf "\e[38;5;93m%s\e[0m\n" "npcseed"
    workon npcseed
    # eof
    EOM

It is that simple [#f1]_.  Now, every time you enter the `/path/to/npcseed`
directory, your virtual environment will switch to npcseed's assuming
that you are using virtualenvwrapper as above. Other use cases are left
as a simple exercise for the reader.

If your shell complains that `shasum` is not found, run::

    $ sudo ln -si /usr/bin/sha512sum /usr/bin/shasum

Note that the `.env` file is not tracked by git because it is a personal
setting. You might have a preferred place for `WORKON_HOME` or whatever
which would render a committed `.env` useless.

Finally, if you want to use `autoenv`_ in most of your repositories but
do not want to add it to all the local `.gitignore` files, you can set
up a `global git ignore file`_ like so::

    $ echo '.env' > ~/.gitignore
    $ git config --global core.excludesfile ~/.gitignore

.. _autoenv: https://github.com/kennethreitz/autoenv
.. _install autoenv: https://github.com/kennethreitz/autoenv#install
.. _global git ignore file: https://help.github.com/articles/ignoring-files/#create-a-global-gitignore

Normal install
--------------

.. warning::
    Doing either of the below methods *might* have strange side effects
    depending on what packages you already have installed and on what
    installed them.

User install
^^^^^^^^^^^^

To install npcseed in `~/.local`, use::

    $ pip install --user -r requirements/requirements.txt
    $ make develop

System wide install
^^^^^^^^^^^^^^^^^^^

To install npcseed system wide, use::

    $ sudo pip install -r requirements/requirements.txt
    $ sudo make install

Makefile
^^^^^^^^

There is a makefile so you can use make for a wide range of often used
commands.  For a list of options::

        $ make

.. [#f1] If your terminal does not support 256 colours, get `a better
    one`_. ☺. If that is too much work, replace the `printf` command with a
    simple echo and continue to live in the XX century⸮ 
.. _a better one: http://st.suckless.org/
