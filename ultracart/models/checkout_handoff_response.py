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


class CheckoutHandoffResponse(object):
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
        'cart': 'Cart',
        'errors': 'list[str]',
        'redirect_to_url': 'str'
    }

    attribute_map = {
        'cart': 'cart',
        'errors': 'errors',
        'redirect_to_url': 'redirect_to_url'
    }

    def __init__(self, cart=None, errors=None, redirect_to_url=None):
        """
        CheckoutHandoffResponse - a model defined in Swagger
        """

        self._cart = None
        self._errors = None
        self._redirect_to_url = None
        self.discriminator = None

        if cart is not None:
          self.cart = cart
        if errors is not None:
          self.errors = errors
        if redirect_to_url is not None:
          self.redirect_to_url = redirect_to_url

    @property
    def cart(self):
        """
        Gets the cart of this CheckoutHandoffResponse.

        :return: The cart of this CheckoutHandoffResponse.
        :rtype: Cart
        """
        return self._cart

    @cart.setter
    def cart(self, cart):
        """
        Sets the cart of this CheckoutHandoffResponse.

        :param cart: The cart of this CheckoutHandoffResponse.
        :type: Cart
        """

        self._cart = cart

    @property
    def errors(self):
        """
        Gets the errors of this CheckoutHandoffResponse.
        Errors that occurred which are preventing the handoff operation.  Display these to the customer.

        :return: The errors of this CheckoutHandoffResponse.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this CheckoutHandoffResponse.
        Errors that occurred which are preventing the handoff operation.  Display these to the customer.

        :param errors: The errors of this CheckoutHandoffResponse.
        :type: list[str]
        """

        self._errors = errors

    @property
    def redirect_to_url(self):
        """
        Gets the redirect_to_url of this CheckoutHandoffResponse.
        The URL that you should redirect the customers browser to

        :return: The redirect_to_url of this CheckoutHandoffResponse.
        :rtype: str
        """
        return self._redirect_to_url

    @redirect_to_url.setter
    def redirect_to_url(self, redirect_to_url):
        """
        Sets the redirect_to_url of this CheckoutHandoffResponse.
        The URL that you should redirect the customers browser to

        :param redirect_to_url: The redirect_to_url of this CheckoutHandoffResponse.
        :type: str
        """

        self._redirect_to_url = redirect_to_url

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
        if not isinstance(other, CheckoutHandoffResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
