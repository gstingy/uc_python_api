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
from ultracart.apis.item_api import ItemApi


class TestItemApi(unittest.TestCase):
    """ ItemApi unit test stubs """

    def setUp(self):
        self.api = ultracart.apis.item_api.ItemApi()

    def tearDown(self):
        pass

    def test_delete_item(self):
        """
        Test case for delete_item

        Delete an item
        """
        pass

    def test_get_item(self):
        """
        Test case for get_item

        Retrieve an item
        """
        pass

    def test_get_item_by_merchant_item_id(self):
        """
        Test case for get_item_by_merchant_item_id

        Retrieve an item by item id
        """
        pass

    def test_get_items(self):
        """
        Test case for get_items

        Retrieve items
        """
        pass

    def test_get_pricing_tiers(self):
        """
        Test case for get_pricing_tiers

        Retrieve pricing tiers
        """
        pass

    def test_insert_item(self):
        """
        Test case for insert_item

        Create an item
        """
        pass

    def test_update_item(self):
        """
        Test case for update_item

        Update an item
        """
        pass

    def test_update_items(self):
        """
        Test case for update_items

        Update multiple items
        """
        pass

    def test_upload_temporary_multimedia(self):
        """
        Test case for upload_temporary_multimedia

        Upload an image to the temporary multimedia.
        """
        pass


if __name__ == '__main__':
    unittest.main()
