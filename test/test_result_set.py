# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import ultracart
from ultracart.rest import ApiException
from ultracart.models.result_set import ResultSet


class TestResultSet(unittest.TestCase):
    """ ResultSet unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResultSet(self):
        """
        Test ResultSet
        """
        model = ultracart.models.result_set.ResultSet()


if __name__ == '__main__':
    unittest.main()
