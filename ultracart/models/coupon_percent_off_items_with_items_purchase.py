# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CouponPercentOffItemsWithItemsPurchase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'discount_percent': 'float',
        'items': 'list[str]',
        'limit': 'int',
        'required_purchase_items': 'list[str]'
    }

    attribute_map = {
        'discount_percent': 'discount_percent',
        'items': 'items',
        'limit': 'limit',
        'required_purchase_items': 'required_purchase_items'
    }

    def __init__(self, discount_percent=None, items=None, limit=None, required_purchase_items=None):
        """
        CouponPercentOffItemsWithItemsPurchase - a model defined in Swagger
        """

        self._discount_percent = None
        self._items = None
        self._limit = None
        self._required_purchase_items = None
        self.discriminator = None

        if discount_percent is not None:
          self.discount_percent = discount_percent
        if items is not None:
          self.items = items
        if limit is not None:
          self.limit = limit
        if required_purchase_items is not None:
          self.required_purchase_items = required_purchase_items

    @property
    def discount_percent(self):
        """
        Gets the discount_percent of this CouponPercentOffItemsWithItemsPurchase.
        The percentage of subtotal discount

        :return: The discount_percent of this CouponPercentOffItemsWithItemsPurchase.
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """
        Sets the discount_percent of this CouponPercentOffItemsWithItemsPurchase.
        The percentage of subtotal discount

        :param discount_percent: The discount_percent of this CouponPercentOffItemsWithItemsPurchase.
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def items(self):
        """
        Gets the items of this CouponPercentOffItemsWithItemsPurchase.
        A list of items which will receive a discount if one of the required purchase items is purchased.

        :return: The items of this CouponPercentOffItemsWithItemsPurchase.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponPercentOffItemsWithItemsPurchase.
        A list of items which will receive a discount if one of the required purchase items is purchased.

        :param items: The items of this CouponPercentOffItemsWithItemsPurchase.
        :type: list[str]
        """

        self._items = items

    @property
    def limit(self):
        """
        Gets the limit of this CouponPercentOffItemsWithItemsPurchase.
        The (optional) maximum quantity of discounted items.

        :return: The limit of this CouponPercentOffItemsWithItemsPurchase.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CouponPercentOffItemsWithItemsPurchase.
        The (optional) maximum quantity of discounted items.

        :param limit: The limit of this CouponPercentOffItemsWithItemsPurchase.
        :type: int
        """

        self._limit = limit

    @property
    def required_purchase_items(self):
        """
        Gets the required_purchase_items of this CouponPercentOffItemsWithItemsPurchase.
        Required items (at least one from the list) that must be purchased for coupon to be valid

        :return: The required_purchase_items of this CouponPercentOffItemsWithItemsPurchase.
        :rtype: list[str]
        """
        return self._required_purchase_items

    @required_purchase_items.setter
    def required_purchase_items(self, required_purchase_items):
        """
        Sets the required_purchase_items of this CouponPercentOffItemsWithItemsPurchase.
        Required items (at least one from the list) that must be purchased for coupon to be valid

        :param required_purchase_items: The required_purchase_items of this CouponPercentOffItemsWithItemsPurchase.
        :type: list[str]
        """

        self._required_purchase_items = required_purchase_items

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
        if not isinstance(other, CouponPercentOffItemsWithItemsPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other