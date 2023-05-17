import pytest
import unittest
"""Base Test for other classes"""


@pytest.mark.usefixtures("init_driver")
class BaseTest(unittest.TestCase):
    """Use to initiating the driver from the configurationtest.py"""
