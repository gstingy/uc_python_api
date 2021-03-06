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


class ItemEbayMarketListing(object):
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
        'auction_id': 'str',
        'price': 'float',
        'seller': 'str',
        'shipping': 'float',
        'total': 'float'
    }

    attribute_map = {
        'auction_id': 'auction_id',
        'price': 'price',
        'seller': 'seller',
        'shipping': 'shipping',
        'total': 'total'
    }

    def __init__(self, auction_id=None, price=None, seller=None, shipping=None, total=None):
        """
        ItemEbayMarketListing - a model defined in Swagger
        """

        self._auction_id = None
        self._price = None
        self._seller = None
        self._shipping = None
        self._total = None
        self.discriminator = None

        if auction_id is not None:
          self.auction_id = auction_id
        if price is not None:
          self.price = price
        if seller is not None:
          self.seller = seller
        if shipping is not None:
          self.shipping = shipping
        if total is not None:
          self.total = total

    @property
    def auction_id(self):
        """
        Gets the auction_id of this ItemEbayMarketListing.
        Auction ID

        :return: The auction_id of this ItemEbayMarketListing.
        :rtype: str
        """
        return self._auction_id

    @auction_id.setter
    def auction_id(self, auction_id):
        """
        Sets the auction_id of this ItemEbayMarketListing.
        Auction ID

        :param auction_id: The auction_id of this ItemEbayMarketListing.
        :type: str
        """

        self._auction_id = auction_id

    @property
    def price(self):
        """
        Gets the price of this ItemEbayMarketListing.
        Price

        :return: The price of this ItemEbayMarketListing.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ItemEbayMarketListing.
        Price

        :param price: The price of this ItemEbayMarketListing.
        :type: float
        """

        self._price = price

    @property
    def seller(self):
        """
        Gets the seller of this ItemEbayMarketListing.
        Seller

        :return: The seller of this ItemEbayMarketListing.
        :rtype: str
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """
        Sets the seller of this ItemEbayMarketListing.
        Seller

        :param seller: The seller of this ItemEbayMarketListing.
        :type: str
        """

        self._seller = seller

    @property
    def shipping(self):
        """
        Gets the shipping of this ItemEbayMarketListing.
        Shipping

        :return: The shipping of this ItemEbayMarketListing.
        :rtype: float
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """
        Sets the shipping of this ItemEbayMarketListing.
        Shipping

        :param shipping: The shipping of this ItemEbayMarketListing.
        :type: float
        """

        self._shipping = shipping

    @property
    def total(self):
        """
        Gets the total of this ItemEbayMarketListing.
        Total

        :return: The total of this ItemEbayMarketListing.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ItemEbayMarketListing.
        Total

        :param total: The total of this ItemEbayMarketListing.
        :type: float
        """

        self._total = total

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
        if not isinstance(other, ItemEbayMarketListing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
