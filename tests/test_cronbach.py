#!/usr/bin/env python

"""Tests for `cronbach` package."""


import unittest
import pandas
import numpy

from cronbach import alpha


class TestCronbach(unittest.TestCase):
    """Tests for `cronbach` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_alpha(self):
        """
        Results using Stata/SE 14.2:

        .. code-block:: stata

          foreach i of varlist m1-p9 {
              replace `i' = . if `i' == 0
          }
          alpha m1-m9, gen(m)
          * Test scale = mean(unstandardized items)
          * Average interitem covariance:     .5370971
          * Number of items in the scale:            9
          * Scale reliability coefficient:      0.8603

        """
        # raise(Exception(os.getcwd()))
        df = pandas.read_csv('cronbach/data/SD3/data.tsv', sep='\t')
        df_m = df[[i for i in df if i.startswith('M')]]
        # consider values of zero to be missing values
        df_m_dropzero = df_m.replace(0, numpy.NaN)
        # df_n = df[[i for i in df if i.startswith('N')]]
        # df_p = df[[i for i in df if i.startswith('P')]]

        # machiavellianism is the only factor without reversed items
        a, ci = alpha(df_m_dropzero)
        # verify we have the expected number of observations
        assert df_m_dropzero['M1'].count() == 18177
        assert df_m_dropzero['M2'].count() == 18156
        assert df_m_dropzero['M3'].count() == 18162
        assert df_m_dropzero['M4'].count() == 18165
        assert df_m_dropzero['M5'].count() == 18167
        assert df_m_dropzero['M6'].count() == 18163
        assert df_m_dropzero['M7'].count() == 18163
        assert df_m_dropzero['M8'].count() == 18159
        assert df_m_dropzero['M9'].count() == 18159
        # assert 0.860353691107797 == 1
        assert round(a, 4) == 0.8604
