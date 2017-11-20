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


class CouponTieredPercentOffItems(object):
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
        'items': 'list[str]',
        'limit': 'float',
        'tiers': 'list[CouponTierQuantityPercent]'
    }

    attribute_map = {
        'items': 'items',
        'limit': 'limit',
        'tiers': 'tiers'
    }

    def __init__(self, items=None, limit=None, tiers=None):
        """
        CouponTieredPercentOffItems - a model defined in Swagger
        """

        self._items = None
        self._limit = None
        self._tiers = None
        self.discriminator = None

        if items is not None:
          self.items = items
        if limit is not None:
          self.limit = limit
        if tiers is not None:
          self.tiers = tiers

    @property
    def items(self):
        """
        Gets the items of this CouponTieredPercentOffItems.
        A list of items of which at least one must be purchased for coupon to be valid.

        :return: The items of this CouponTieredPercentOffItems.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponTieredPercentOffItems.
        A list of items of which at least one must be purchased for coupon to be valid.

        :param items: The items of this CouponTieredPercentOffItems.
        :type: list[str]
        """

        self._items = items

    @property
    def limit(self):
        """
        Gets the limit of this CouponTieredPercentOffItems.
        The maximum amount of total discount by this coupon.

        :return: The limit of this CouponTieredPercentOffItems.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CouponTieredPercentOffItems.
        The maximum amount of total discount by this coupon.

        :param limit: The limit of this CouponTieredPercentOffItems.
        :type: float
        """

        self._limit = limit

    @property
    def tiers(self):
        """
        Gets the tiers of this CouponTieredPercentOffItems.
        A list of discount tiers.

        :return: The tiers of this CouponTieredPercentOffItems.
        :rtype: list[CouponTierQuantityPercent]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """
        Sets the tiers of this CouponTieredPercentOffItems.
        A list of discount tiers.

        :param tiers: The tiers of this CouponTieredPercentOffItems.
        :type: list[CouponTierQuantityPercent]
        """

        self._tiers = tiers

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
        if not isinstance(other, CouponTieredPercentOffItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
