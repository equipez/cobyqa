#####################################################################
COBYQA: a derivative-free solver for general nonlinear optimization
#####################################################################

.. image:: https://readthedocs.org/projects/cobyqa/badge/?version=latest
    :target: https://cobyqa.readthedocs.io/en/latest/?badge=latest

.. image:: https://github.com/ragonneau/cobyqa/actions/workflows/wheels.yml/badge.svg
    :target: https://github.com/ragonneau/cobyqa/actions/workflows/wheels.yml

.. image:: https://codecov.io/gh/ragonneau/cobyqa/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/ragonneau/cobyqa

.. image:: https://img.shields.io/badge/license-BSD-blue
    :target: https://github.com/ragonneau/cobyqa/blob/main/LICENSE

.. image:: https://shields.io/pypi/v/cobyqa.svg
    :target: https://pypi.org/project/cobyqa/

COBYQA, named after *Constrained Optimization BY Quadratic Approximation*, is a
derivative-free solver for general nonlinear optimization problems. It can handle 
unconstrained, bound-constrained, linearly constrained, and nonlinearly constrained
problems. It uses only function values of the objective function and nonlinear 
constraint functions, if any. No derivative information is needed. 

The current release of COBYQA contains a Python implementation of the solver. It is 
distributed under the BSD-3-Clause license.

**Documentation:** https://www.cobyqa.com/

Installation
============

COBYQA can be installed on `Python 3.7 or above <https://www.python.org>`_.

Dependencies
------------

The following Python packages are required by COBYQA:

* `NumPy <https://www.numpy.org>`_,
* `SciPy <https://www.scipy.org>`_ 1.1.0 or higher, and
* `Cython <https://cython.org>`_ 0.29.23 or higher

User installation
-----------------

The easiest way to install COBYQA is using ``pip`` ::

    python -m pip install -U cobyqa

To check your installation, you can execute ::

    python -c "import cobyqa; cobyqa.show_versions()"

Testing
-------

After installing `pytest <https://docs.pytest.org>`_ 5.0.1 or higher, you can
execute the test suite of COBYQA via ::

    python -m pytest --pyargs cobyqa

Support
=======

To report a bug or request a new feature, please open a new issue using the
`issue tracker <https://github.com/ragonneau/cobyqa/issues>`_.
