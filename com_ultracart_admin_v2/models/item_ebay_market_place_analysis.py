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


class ItemEbayMarketPlaceAnalysis(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, adjusted_price=None, adjusted_shipping=None, adjusted_total=None, cogs=None, final_value_fee=None, minimum_advertised_price=None, other_listings=None, our_listing=None, overhead=None, profit_potential=None):
        """
        ItemEbayMarketPlaceAnalysis - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'adjusted_price': 'float',
            'adjusted_shipping': 'float',
            'adjusted_total': 'float',
            'cogs': 'float',
            'final_value_fee': 'float',
            'minimum_advertised_price': 'float',
            'other_listings': 'list[ItemEbayMarketListing]',
            'our_listing': 'ItemEbayMarketListing',
            'overhead': 'float',
            'profit_potential': 'float'
        }

        self.attribute_map = {
            'adjusted_price': 'adjusted_price',
            'adjusted_shipping': 'adjusted_shipping',
            'adjusted_total': 'adjusted_total',
            'cogs': 'cogs',
            'final_value_fee': 'final_value_fee',
            'minimum_advertised_price': 'minimum_advertised_price',
            'other_listings': 'other_listings',
            'our_listing': 'our_listing',
            'overhead': 'overhead',
            'profit_potential': 'profit_potential'
        }

        self._adjusted_price = adjusted_price
        self._adjusted_shipping = adjusted_shipping
        self._adjusted_total = adjusted_total
        self._cogs = cogs
        self._final_value_fee = final_value_fee
        self._minimum_advertised_price = minimum_advertised_price
        self._other_listings = other_listings
        self._our_listing = our_listing
        self._overhead = overhead
        self._profit_potential = profit_potential

    @property
    def adjusted_price(self):
        """
        Gets the adjusted_price of this ItemEbayMarketPlaceAnalysis.


        :return: The adjusted_price of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._adjusted_price

    @adjusted_price.setter
    def adjusted_price(self, adjusted_price):
        """
        Sets the adjusted_price of this ItemEbayMarketPlaceAnalysis.


        :param adjusted_price: The adjusted_price of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._adjusted_price = adjusted_price

    @property
    def adjusted_shipping(self):
        """
        Gets the adjusted_shipping of this ItemEbayMarketPlaceAnalysis.


        :return: The adjusted_shipping of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._adjusted_shipping

    @adjusted_shipping.setter
    def adjusted_shipping(self, adjusted_shipping):
        """
        Sets the adjusted_shipping of this ItemEbayMarketPlaceAnalysis.


        :param adjusted_shipping: The adjusted_shipping of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._adjusted_shipping = adjusted_shipping

    @property
    def adjusted_total(self):
        """
        Gets the adjusted_total of this ItemEbayMarketPlaceAnalysis.


        :return: The adjusted_total of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._adjusted_total

    @adjusted_total.setter
    def adjusted_total(self, adjusted_total):
        """
        Sets the adjusted_total of this ItemEbayMarketPlaceAnalysis.


        :param adjusted_total: The adjusted_total of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._adjusted_total = adjusted_total

    @property
    def cogs(self):
        """
        Gets the cogs of this ItemEbayMarketPlaceAnalysis.


        :return: The cogs of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._cogs

    @cogs.setter
    def cogs(self, cogs):
        """
        Sets the cogs of this ItemEbayMarketPlaceAnalysis.


        :param cogs: The cogs of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._cogs = cogs

    @property
    def final_value_fee(self):
        """
        Gets the final_value_fee of this ItemEbayMarketPlaceAnalysis.


        :return: The final_value_fee of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._final_value_fee

    @final_value_fee.setter
    def final_value_fee(self, final_value_fee):
        """
        Sets the final_value_fee of this ItemEbayMarketPlaceAnalysis.


        :param final_value_fee: The final_value_fee of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._final_value_fee = final_value_fee

    @property
    def minimum_advertised_price(self):
        """
        Gets the minimum_advertised_price of this ItemEbayMarketPlaceAnalysis.


        :return: The minimum_advertised_price of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._minimum_advertised_price

    @minimum_advertised_price.setter
    def minimum_advertised_price(self, minimum_advertised_price):
        """
        Sets the minimum_advertised_price of this ItemEbayMarketPlaceAnalysis.


        :param minimum_advertised_price: The minimum_advertised_price of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._minimum_advertised_price = minimum_advertised_price

    @property
    def other_listings(self):
        """
        Gets the other_listings of this ItemEbayMarketPlaceAnalysis.


        :return: The other_listings of this ItemEbayMarketPlaceAnalysis.
        :rtype: list[ItemEbayMarketListing]
        """
        return self._other_listings

    @other_listings.setter
    def other_listings(self, other_listings):
        """
        Sets the other_listings of this ItemEbayMarketPlaceAnalysis.


        :param other_listings: The other_listings of this ItemEbayMarketPlaceAnalysis.
        :type: list[ItemEbayMarketListing]
        """

        self._other_listings = other_listings

    @property
    def our_listing(self):
        """
        Gets the our_listing of this ItemEbayMarketPlaceAnalysis.


        :return: The our_listing of this ItemEbayMarketPlaceAnalysis.
        :rtype: ItemEbayMarketListing
        """
        return self._our_listing

    @our_listing.setter
    def our_listing(self, our_listing):
        """
        Sets the our_listing of this ItemEbayMarketPlaceAnalysis.


        :param our_listing: The our_listing of this ItemEbayMarketPlaceAnalysis.
        :type: ItemEbayMarketListing
        """

        self._our_listing = our_listing

    @property
    def overhead(self):
        """
        Gets the overhead of this ItemEbayMarketPlaceAnalysis.


        :return: The overhead of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._overhead

    @overhead.setter
    def overhead(self, overhead):
        """
        Sets the overhead of this ItemEbayMarketPlaceAnalysis.


        :param overhead: The overhead of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._overhead = overhead

    @property
    def profit_potential(self):
        """
        Gets the profit_potential of this ItemEbayMarketPlaceAnalysis.


        :return: The profit_potential of this ItemEbayMarketPlaceAnalysis.
        :rtype: float
        """
        return self._profit_potential

    @profit_potential.setter
    def profit_potential(self, profit_potential):
        """
        Sets the profit_potential of this ItemEbayMarketPlaceAnalysis.


        :param profit_potential: The profit_potential of this ItemEbayMarketPlaceAnalysis.
        :type: float
        """

        self._profit_potential = profit_potential

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
