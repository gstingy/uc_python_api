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


class CouponAmountOffShippingWithItemsPurchase(object):
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
        'currency_code': 'str',
        'discount_amount': 'float',
        'items': 'list[str]',
        'shipping_methods': 'list[str]'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'discount_amount': 'discount_amount',
        'items': 'items',
        'shipping_methods': 'shipping_methods'
    }

    def __init__(self, currency_code=None, discount_amount=None, items=None, shipping_methods=None):
        """
        CouponAmountOffShippingWithItemsPurchase - a model defined in Swagger
        """

        self._currency_code = None
        self._discount_amount = None
        self._items = None
        self._shipping_methods = None
        self.discriminator = None

        if currency_code is not None:
          self.currency_code = currency_code
        if discount_amount is not None:
          self.discount_amount = discount_amount
        if items is not None:
          self.items = items
        if shipping_methods is not None:
          self.shipping_methods = shipping_methods

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CouponAmountOffShippingWithItemsPurchase.
        The ISO-4217 three letter currency code the customer is viewing prices in

        :return: The currency_code of this CouponAmountOffShippingWithItemsPurchase.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CouponAmountOffShippingWithItemsPurchase.
        The ISO-4217 three letter currency code the customer is viewing prices in

        :param currency_code: The currency_code of this CouponAmountOffShippingWithItemsPurchase.
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")

        self._currency_code = currency_code

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this CouponAmountOffShippingWithItemsPurchase.
        The amount of shipping discount

        :return: The discount_amount of this CouponAmountOffShippingWithItemsPurchase.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this CouponAmountOffShippingWithItemsPurchase.
        The amount of shipping discount

        :param discount_amount: The discount_amount of this CouponAmountOffShippingWithItemsPurchase.
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def items(self):
        """
        Gets the items of this CouponAmountOffShippingWithItemsPurchase.
        A list of items of which at least one must be purchased for coupon to be valid.

        :return: The items of this CouponAmountOffShippingWithItemsPurchase.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponAmountOffShippingWithItemsPurchase.
        A list of items of which at least one must be purchased for coupon to be valid.

        :param items: The items of this CouponAmountOffShippingWithItemsPurchase.
        :type: list[str]
        """

        self._items = items

    @property
    def shipping_methods(self):
        """
        Gets the shipping_methods of this CouponAmountOffShippingWithItemsPurchase.
        One or more shipping methods that may receive this discount

        :return: The shipping_methods of this CouponAmountOffShippingWithItemsPurchase.
        :rtype: list[str]
        """
        return self._shipping_methods

    @shipping_methods.setter
    def shipping_methods(self, shipping_methods):
        """
        Sets the shipping_methods of this CouponAmountOffShippingWithItemsPurchase.
        One or more shipping methods that may receive this discount

        :param shipping_methods: The shipping_methods of this CouponAmountOffShippingWithItemsPurchase.
        :type: list[str]
        """

        self._shipping_methods = shipping_methods

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
        if not isinstance(other, CouponAmountOffShippingWithItemsPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
