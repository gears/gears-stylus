gears-stylus
==================

Stylus_ compiler for Gears_. This package already includes the Stylus source
code for you, so you don't need to worry about installing it yourself.

Bundled Stylus version: **0.45.1**

Installation
------------

Install ``gears-stylus`` with pip::

    $ pip install gears-stylus


Requirements
------------

``gears-stylus`` requires node.js_ to be installed in your system.


Usage
-----

Add ``gears_stylus.StylusCompiler`` to ``environment``'s compilers registry::

    from gears_stylus import StylusCompiler
    environment.compilers.register('.styl', StylusCompiler.as_handler())

If you use Gears in your Django project, add this code to its settings::

    GEARS_COMPILERS = {
        '.styl': 'gears_stylus.StylusCompiler',
    }

.. _Stylus: http://learnboost.github.com/stylus/
.. _Gears: https://github.com/gears/gears
.. _node.js: http://nodejs.org/
