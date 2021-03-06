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


class CouponTierItemDiscount(object):
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
        'discount_amount': 'float',
        'items': 'list[str]'
    }

    attribute_map = {
        'discount_amount': 'discount_amount',
        'items': 'items'
    }

    def __init__(self, discount_amount=None, items=None):
        """
        CouponTierItemDiscount - a model defined in Swagger
        """

        self._discount_amount = None
        self._items = None
        self.discriminator = None

        if discount_amount is not None:
          self.discount_amount = discount_amount
        if items is not None:
          self.items = items

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this CouponTierItemDiscount.
        The amount of subtotal discount

        :return: The discount_amount of this CouponTierItemDiscount.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this CouponTierItemDiscount.
        The amount of subtotal discount

        :param discount_amount: The discount_amount of this CouponTierItemDiscount.
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def items(self):
        """
        Gets the items of this CouponTierItemDiscount.
        A list of items which will receive this discount.

        :return: The items of this CouponTierItemDiscount.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponTierItemDiscount.
        A list of items which will receive this discount.

        :param items: The items of this CouponTierItemDiscount.
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
        if not isinstance(other, CouponTierItemDiscount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
