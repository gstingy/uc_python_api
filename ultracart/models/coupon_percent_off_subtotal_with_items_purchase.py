# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CouponPercentOffSubtotalWithItemsPurchase(object):
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
        'items': 'list[str]'
    }

    attribute_map = {
        'discount_percent': 'discount_percent',
        'items': 'items'
    }

    def __init__(self, discount_percent=None, items=None):
        """
        CouponPercentOffSubtotalWithItemsPurchase - a model defined in Swagger
        """

        self._discount_percent = None
        self._items = None
        self.discriminator = None

        if discount_percent is not None:
          self.discount_percent = discount_percent
        if items is not None:
          self.items = items

    @property
    def discount_percent(self):
        """
        Gets the discount_percent of this CouponPercentOffSubtotalWithItemsPurchase.
        The percentage of subtotal discount

        :return: The discount_percent of this CouponPercentOffSubtotalWithItemsPurchase.
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """
        Sets the discount_percent of this CouponPercentOffSubtotalWithItemsPurchase.
        The percentage of subtotal discount

        :param discount_percent: The discount_percent of this CouponPercentOffSubtotalWithItemsPurchase.
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def items(self):
        """
        Gets the items of this CouponPercentOffSubtotalWithItemsPurchase.
        A list of items of which at least one must be purchased for coupon to be valid.

        :return: The items of this CouponPercentOffSubtotalWithItemsPurchase.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponPercentOffSubtotalWithItemsPurchase.
        A list of items of which at least one must be purchased for coupon to be valid.

        :param items: The items of this CouponPercentOffSubtotalWithItemsPurchase.
        :type: list[str]
        """

        self._items = items

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
        if not isinstance(other, CouponPercentOffSubtotalWithItemsPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
