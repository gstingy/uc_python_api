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

from pprint import pformat
from six import iteritems
import re


class ItemAutoOrder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, auth_future_amount=None, auth_test_amount=None, auto_order_cancel_item_id=None, auto_order_cancel_item_oid=None, auto_order_downgrade_items=None, auto_order_paused=None, auto_order_schedules=None, auto_order_upgrade_items=None, auto_order_upsell=None, auto_order_upsell_no_easy_cancel=None, auto_order_upsell_one_per_customer=None, auto_orderable=None, cancel_other_auto_orders=None, free_shipping_auto_order=None, steps=None):
        """
        ItemAutoOrder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'auth_future_amount': 'float',
            'auth_test_amount': 'float',
            'auto_order_cancel_item_id': 'str',
            'auto_order_cancel_item_oid': 'int',
            'auto_order_downgrade_items': 'list[str]',
            'auto_order_paused': 'bool',
            'auto_order_schedules': 'list[str]',
            'auto_order_upgrade_items': 'list[str]',
            'auto_order_upsell': 'bool',
            'auto_order_upsell_no_easy_cancel': 'bool',
            'auto_order_upsell_one_per_customer': 'bool',
            'auto_orderable': 'bool',
            'cancel_other_auto_orders': 'bool',
            'free_shipping_auto_order': 'bool',
            'steps': 'list[ItemAutoOrderStep]'
        }

        self.attribute_map = {
            'auth_future_amount': 'auth_future_amount',
            'auth_test_amount': 'auth_test_amount',
            'auto_order_cancel_item_id': 'auto_order_cancel_item_id',
            'auto_order_cancel_item_oid': 'auto_order_cancel_item_oid',
            'auto_order_downgrade_items': 'auto_order_downgrade_items',
            'auto_order_paused': 'auto_order_paused',
            'auto_order_schedules': 'auto_order_schedules',
            'auto_order_upgrade_items': 'auto_order_upgrade_items',
            'auto_order_upsell': 'auto_order_upsell',
            'auto_order_upsell_no_easy_cancel': 'auto_order_upsell_no_easy_cancel',
            'auto_order_upsell_one_per_customer': 'auto_order_upsell_one_per_customer',
            'auto_orderable': 'auto_orderable',
            'cancel_other_auto_orders': 'cancel_other_auto_orders',
            'free_shipping_auto_order': 'free_shipping_auto_order',
            'steps': 'steps'
        }

        self._auth_future_amount = auth_future_amount
        self._auth_test_amount = auth_test_amount
        self._auto_order_cancel_item_id = auto_order_cancel_item_id
        self._auto_order_cancel_item_oid = auto_order_cancel_item_oid
        self._auto_order_downgrade_items = auto_order_downgrade_items
        self._auto_order_paused = auto_order_paused
        self._auto_order_schedules = auto_order_schedules
        self._auto_order_upgrade_items = auto_order_upgrade_items
        self._auto_order_upsell = auto_order_upsell
        self._auto_order_upsell_no_easy_cancel = auto_order_upsell_no_easy_cancel
        self._auto_order_upsell_one_per_customer = auto_order_upsell_one_per_customer
        self._auto_orderable = auto_orderable
        self._cancel_other_auto_orders = cancel_other_auto_orders
        self._free_shipping_auto_order = free_shipping_auto_order
        self._steps = steps

    @property
    def auth_future_amount(self):
        """
        Gets the auth_future_amount of this ItemAutoOrder.
        Amount to try and authorize for the future rebill

        :return: The auth_future_amount of this ItemAutoOrder.
        :rtype: float
        """
        return self._auth_future_amount

    @auth_future_amount.setter
    def auth_future_amount(self, auth_future_amount):
        """
        Sets the auth_future_amount of this ItemAutoOrder.
        Amount to try and authorize for the future rebill

        :param auth_future_amount: The auth_future_amount of this ItemAutoOrder.
        :type: float
        """

        self._auth_future_amount = auth_future_amount

    @property
    def auth_test_amount(self):
        """
        Gets the auth_test_amount of this ItemAutoOrder.
        Amount to try and test authorize

        :return: The auth_test_amount of this ItemAutoOrder.
        :rtype: float
        """
        return self._auth_test_amount

    @auth_test_amount.setter
    def auth_test_amount(self, auth_test_amount):
        """
        Sets the auth_test_amount of this ItemAutoOrder.
        Amount to try and test authorize

        :param auth_test_amount: The auth_test_amount of this ItemAutoOrder.
        :type: float
        """

        self._auth_test_amount = auth_test_amount

    @property
    def auto_order_cancel_item_id(self):
        """
        Gets the auto_order_cancel_item_id of this ItemAutoOrder.
        Item id to attempt charging the customer for if they cancel

        :return: The auto_order_cancel_item_id of this ItemAutoOrder.
        :rtype: str
        """
        return self._auto_order_cancel_item_id

    @auto_order_cancel_item_id.setter
    def auto_order_cancel_item_id(self, auto_order_cancel_item_id):
        """
        Sets the auto_order_cancel_item_id of this ItemAutoOrder.
        Item id to attempt charging the customer for if they cancel

        :param auto_order_cancel_item_id: The auto_order_cancel_item_id of this ItemAutoOrder.
        :type: str
        """

        if not auto_order_cancel_item_id:
            raise ValueError("Invalid value for `auto_order_cancel_item_id`, must not be `None`")
        if len(auto_order_cancel_item_id) > 20:
            raise ValueError("Invalid value for `auto_order_cancel_item_id`, length must be less than `20`")

        self._auto_order_cancel_item_id = auto_order_cancel_item_id

    @property
    def auto_order_cancel_item_oid(self):
        """
        Gets the auto_order_cancel_item_oid of this ItemAutoOrder.
        Item object identifier to attempt charging the customer for if they cancel

        :return: The auto_order_cancel_item_oid of this ItemAutoOrder.
        :rtype: int
        """
        return self._auto_order_cancel_item_oid

    @auto_order_cancel_item_oid.setter
    def auto_order_cancel_item_oid(self, auto_order_cancel_item_oid):
        """
        Sets the auto_order_cancel_item_oid of this ItemAutoOrder.
        Item object identifier to attempt charging the customer for if they cancel

        :param auto_order_cancel_item_oid: The auto_order_cancel_item_oid of this ItemAutoOrder.
        :type: int
        """

        self._auto_order_cancel_item_oid = auto_order_cancel_item_oid

    @property
    def auto_order_downgrade_items(self):
        """
        Gets the auto_order_downgrade_items of this ItemAutoOrder.
        List of downgrade items presented to customer service representatives

        :return: The auto_order_downgrade_items of this ItemAutoOrder.
        :rtype: list[str]
        """
        return self._auto_order_downgrade_items

    @auto_order_downgrade_items.setter
    def auto_order_downgrade_items(self, auto_order_downgrade_items):
        """
        Sets the auto_order_downgrade_items of this ItemAutoOrder.
        List of downgrade items presented to customer service representatives

        :param auto_order_downgrade_items: The auto_order_downgrade_items of this ItemAutoOrder.
        :type: list[str]
        """

        self._auto_order_downgrade_items = auto_order_downgrade_items

    @property
    def auto_order_paused(self):
        """
        Gets the auto_order_paused of this ItemAutoOrder.
        True if the rebill processing of this item is paused

        :return: The auto_order_paused of this ItemAutoOrder.
        :rtype: bool
        """
        return self._auto_order_paused

    @auto_order_paused.setter
    def auto_order_paused(self, auto_order_paused):
        """
        Sets the auto_order_paused of this ItemAutoOrder.
        True if the rebill processing of this item is paused

        :param auto_order_paused: The auto_order_paused of this ItemAutoOrder.
        :type: bool
        """

        self._auto_order_paused = auto_order_paused

    @property
    def auto_order_schedules(self):
        """
        Gets the auto_order_schedules of this ItemAutoOrder.
        The user selectable schedules that are available

        :return: The auto_order_schedules of this ItemAutoOrder.
        :rtype: list[str]
        """
        return self._auto_order_schedules

    @auto_order_schedules.setter
    def auto_order_schedules(self, auto_order_schedules):
        """
        Sets the auto_order_schedules of this ItemAutoOrder.
        The user selectable schedules that are available

        :param auto_order_schedules: The auto_order_schedules of this ItemAutoOrder.
        :type: list[str]
        """

        self._auto_order_schedules = auto_order_schedules

    @property
    def auto_order_upgrade_items(self):
        """
        Gets the auto_order_upgrade_items of this ItemAutoOrder.
        List of upgrade items presented to customer service representatives

        :return: The auto_order_upgrade_items of this ItemAutoOrder.
        :rtype: list[str]
        """
        return self._auto_order_upgrade_items

    @auto_order_upgrade_items.setter
    def auto_order_upgrade_items(self, auto_order_upgrade_items):
        """
        Sets the auto_order_upgrade_items of this ItemAutoOrder.
        List of upgrade items presented to customer service representatives

        :param auto_order_upgrade_items: The auto_order_upgrade_items of this ItemAutoOrder.
        :type: list[str]
        """

        self._auto_order_upgrade_items = auto_order_upgrade_items

    @property
    def auto_order_upsell(self):
        """
        Gets the auto_order_upsell of this ItemAutoOrder.
        True if this item uses a fixed upsell step schedule

        :return: The auto_order_upsell of this ItemAutoOrder.
        :rtype: bool
        """
        return self._auto_order_upsell

    @auto_order_upsell.setter
    def auto_order_upsell(self, auto_order_upsell):
        """
        Sets the auto_order_upsell of this ItemAutoOrder.
        True if this item uses a fixed upsell step schedule

        :param auto_order_upsell: The auto_order_upsell of this ItemAutoOrder.
        :type: bool
        """

        self._auto_order_upsell = auto_order_upsell

    @property
    def auto_order_upsell_no_easy_cancel(self):
        """
        Gets the auto_order_upsell_no_easy_cancel of this ItemAutoOrder.
        Do not send the easy cancel email to the customer

        :return: The auto_order_upsell_no_easy_cancel of this ItemAutoOrder.
        :rtype: bool
        """
        return self._auto_order_upsell_no_easy_cancel

    @auto_order_upsell_no_easy_cancel.setter
    def auto_order_upsell_no_easy_cancel(self, auto_order_upsell_no_easy_cancel):
        """
        Sets the auto_order_upsell_no_easy_cancel of this ItemAutoOrder.
        Do not send the easy cancel email to the customer

        :param auto_order_upsell_no_easy_cancel: The auto_order_upsell_no_easy_cancel of this ItemAutoOrder.
        :type: bool
        """

        self._auto_order_upsell_no_easy_cancel = auto_order_upsell_no_easy_cancel

    @property
    def auto_order_upsell_one_per_customer(self):
        """
        Gets the auto_order_upsell_one_per_customer of this ItemAutoOrder.
        Limit the purchase of this item to one per customer

        :return: The auto_order_upsell_one_per_customer of this ItemAutoOrder.
        :rtype: bool
        """
        return self._auto_order_upsell_one_per_customer

    @auto_order_upsell_one_per_customer.setter
    def auto_order_upsell_one_per_customer(self, auto_order_upsell_one_per_customer):
        """
        Sets the auto_order_upsell_one_per_customer of this ItemAutoOrder.
        Limit the purchase of this item to one per customer

        :param auto_order_upsell_one_per_customer: The auto_order_upsell_one_per_customer of this ItemAutoOrder.
        :type: bool
        """

        self._auto_order_upsell_one_per_customer = auto_order_upsell_one_per_customer

    @property
    def auto_orderable(self):
        """
        Gets the auto_orderable of this ItemAutoOrder.
        True if this item can be automatically ordered by the customer

        :return: The auto_orderable of this ItemAutoOrder.
        :rtype: bool
        """
        return self._auto_orderable

    @auto_orderable.setter
    def auto_orderable(self, auto_orderable):
        """
        Sets the auto_orderable of this ItemAutoOrder.
        True if this item can be automatically ordered by the customer

        :param auto_orderable: The auto_orderable of this ItemAutoOrder.
        :type: bool
        """

        self._auto_orderable = auto_orderable

    @property
    def cancel_other_auto_orders(self):
        """
        Gets the cancel_other_auto_orders of this ItemAutoOrder.
        True if other auto orders for this customer should be canceled when this item is ordered

        :return: The cancel_other_auto_orders of this ItemAutoOrder.
        :rtype: bool
        """
        return self._cancel_other_auto_orders

    @cancel_other_auto_orders.setter
    def cancel_other_auto_orders(self, cancel_other_auto_orders):
        """
        Sets the cancel_other_auto_orders of this ItemAutoOrder.
        True if other auto orders for this customer should be canceled when this item is ordered

        :param cancel_other_auto_orders: The cancel_other_auto_orders of this ItemAutoOrder.
        :type: bool
        """

        self._cancel_other_auto_orders = cancel_other_auto_orders

    @property
    def free_shipping_auto_order(self):
        """
        Gets the free_shipping_auto_order of this ItemAutoOrder.
        True if the customer should be given free shipping

        :return: The free_shipping_auto_order of this ItemAutoOrder.
        :rtype: bool
        """
        return self._free_shipping_auto_order

    @free_shipping_auto_order.setter
    def free_shipping_auto_order(self, free_shipping_auto_order):
        """
        Sets the free_shipping_auto_order of this ItemAutoOrder.
        True if the customer should be given free shipping

        :param free_shipping_auto_order: The free_shipping_auto_order of this ItemAutoOrder.
        :type: bool
        """

        self._free_shipping_auto_order = free_shipping_auto_order

    @property
    def steps(self):
        """
        Gets the steps of this ItemAutoOrder.
        The rebill steps if this auto order is an upsell

        :return: The steps of this ItemAutoOrder.
        :rtype: list[ItemAutoOrderStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this ItemAutoOrder.
        The rebill steps if this auto order is an upsell

        :param steps: The steps of this ItemAutoOrder.
        :type: list[ItemAutoOrderStep]
        """

        self._steps = steps

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
