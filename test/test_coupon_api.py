# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import ultracart
from ultracart.rest import ApiException
from ultracart.apis.coupon_api import CouponApi


class TestCouponApi(unittest.TestCase):
    """ CouponApi unit test stubs """

    def setUp(self):
        self.api = ultracart.apis.coupon_api.CouponApi()

    def tearDown(self):
        pass

    def test_delete_coupon(self):
        """
        Test case for delete_coupon

        Delete a coupon
        """
        pass

    def test_generate_coupon_codes(self):
        """
        Test case for generate_coupon_codes

        Generates one time codes for a coupon
        """
        pass

    def test_generate_one_time_codes_by_merchant_code(self):
        """
        Test case for generate_one_time_codes_by_merchant_code

        Generates one time codes by merchant code
        """
        pass

    def test_get_coupon(self):
        """
        Test case for get_coupon

        Retrieve a coupon
        """
        pass

    def test_get_coupon_by_merchant_code(self):
        """
        Test case for get_coupon_by_merchant_code

        Retrieve a coupon by merchant code
        """
        pass

    def test_get_coupons(self):
        """
        Test case for get_coupons

        Retrieve coupons
        """
        pass

    def test_get_coupons_by_query(self):
        """
        Test case for get_coupons_by_query

        Retrieve coupons by query
        """
        pass

    def test_get_editor_values(self):
        """
        Test case for get_editor_values

        Retrieve values needed for a coupon editor
        """
        pass

    def test_insert_coupon(self):
        """
        Test case for insert_coupon

        Insert a coupon
        """
        pass

    def test_update_coupon(self):
        """
        Test case for update_coupon

        Update a coupon
        """
        pass


if __name__ == '__main__':
    unittest.main()
