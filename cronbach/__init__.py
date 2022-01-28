"""
Compute Cronbach's alpha statistic

* Crude fork of cronbach_alpha from pingouin

Features
--------

* Works on pandas.DataFrame objects

Examples
--------

.. code-block:: python

  >>> from cronbach import alpha
  >>>

License
-------

* Free software: GPL-3.0 (because pingouin is)

Documentation
-------------

* https://cronbach.readthedocs.io/
"""

__author__ = """Brendan Strejcek"""
__email__ = 'brendan@datagazing.com'
__version__ = '0.1.0'

from .cronbach import alpha # noqa F401
