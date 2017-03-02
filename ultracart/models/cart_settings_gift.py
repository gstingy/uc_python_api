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


class CartSettingsGift(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allow_gifts=None, gift_charge=None, gift_wraps=None, max_message_length=None):
        """
        CartSettingsGift - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_gifts': 'bool',
            'gift_charge': 'Currency',
            'gift_wraps': 'list[CartSettingsGiftWrap]',
            'max_message_length': 'int'
        }

        self.attribute_map = {
            'allow_gifts': 'allow_gifts',
            'gift_charge': 'gift_charge',
            'gift_wraps': 'gift_wraps',
            'max_message_length': 'max_message_length'
        }

        self._allow_gifts = allow_gifts
        self._gift_charge = gift_charge
        self._gift_wraps = gift_wraps
        self._max_message_length = max_message_length

    @property
    def allow_gifts(self):
        """
        Gets the allow_gifts of this CartSettingsGift.
        True if this checkout supports gift giving

        :return: The allow_gifts of this CartSettingsGift.
        :rtype: bool
        """
        return self._allow_gifts

    @allow_gifts.setter
    def allow_gifts(self, allow_gifts):
        """
        Sets the allow_gifts of this CartSettingsGift.
        True if this checkout supports gift giving

        :param allow_gifts: The allow_gifts of this CartSettingsGift.
        :type: bool
        """

        self._allow_gifts = allow_gifts

    @property
    def gift_charge(self):
        """
        Gets the gift_charge of this CartSettingsGift.


        :return: The gift_charge of this CartSettingsGift.
        :rtype: Currency
        """
        return self._gift_charge

    @gift_charge.setter
    def gift_charge(self, gift_charge):
        """
        Sets the gift_charge of this CartSettingsGift.


        :param gift_charge: The gift_charge of this CartSettingsGift.
        :type: Currency
        """

        self._gift_charge = gift_charge

    @property
    def gift_wraps(self):
        """
        Gets the gift_wraps of this CartSettingsGift.
        The gift wraps available for the customer to select from

        :return: The gift_wraps of this CartSettingsGift.
        :rtype: list[CartSettingsGiftWrap]
        """
        return self._gift_wraps

    @gift_wraps.setter
    def gift_wraps(self, gift_wraps):
        """
        Sets the gift_wraps of this CartSettingsGift.
        The gift wraps available for the customer to select from

        :param gift_wraps: The gift_wraps of this CartSettingsGift.
        :type: list[CartSettingsGiftWrap]
        """

        self._gift_wraps = gift_wraps

    @property
    def max_message_length(self):
        """
        Gets the max_message_length of this CartSettingsGift.
        The maximum length of the gift message the giver can enter

        :return: The max_message_length of this CartSettingsGift.
        :rtype: int
        """
        return self._max_message_length

    @max_message_length.setter
    def max_message_length(self, max_message_length):
        """
        Sets the max_message_length of this CartSettingsGift.
        The maximum length of the gift message the giver can enter

        :param max_message_length: The max_message_length of this CartSettingsGift.
        :type: int
        """

        self._max_message_length = max_message_length

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
