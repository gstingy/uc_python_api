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


class ItemPricingTierDiscount(object):
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
        'cost': 'float',
        'quantity': 'int'
    }

    attribute_map = {
        'cost': 'cost',
        'quantity': 'quantity'
    }

    def __init__(self, cost=None, quantity=None):
        """
        ItemPricingTierDiscount - a model defined in Swagger
        """

        self._cost = None
        self._quantity = None
        self.discriminator = None

        if cost is not None:
          self.cost = cost
        if quantity is not None:
          self.quantity = quantity

    @property
    def cost(self):
        """
        Gets the cost of this ItemPricingTierDiscount.
        Cost

        :return: The cost of this ItemPricingTierDiscount.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this ItemPricingTierDiscount.
        Cost

        :param cost: The cost of this ItemPricingTierDiscount.
        :type: float
        """

        self._cost = cost

    @property
    def quantity(self):
        """
        Gets the quantity of this ItemPricingTierDiscount.
        Quantity

        :return: The quantity of this ItemPricingTierDiscount.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ItemPricingTierDiscount.
        Quantity

        :param quantity: The quantity of this ItemPricingTierDiscount.
        :type: int
        """

        self._quantity = quantity

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
        if not isinstance(other, ItemPricingTierDiscount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
