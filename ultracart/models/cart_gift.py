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


class CartGift(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, gift=None, gift_charge=None, gift_email=None, gift_message=None, gift_wrap_cost=None, gift_wrap_title=None):
        """
        CartGift - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'gift': 'bool',
            'gift_charge': 'Currency',
            'gift_email': 'str',
            'gift_message': 'str',
            'gift_wrap_cost': 'Currency',
            'gift_wrap_title': 'str'
        }

        self.attribute_map = {
            'gift': 'gift',
            'gift_charge': 'gift_charge',
            'gift_email': 'gift_email',
            'gift_message': 'gift_message',
            'gift_wrap_cost': 'gift_wrap_cost',
            'gift_wrap_title': 'gift_wrap_title'
        }

        self._gift = gift
        self._gift_charge = gift_charge
        self._gift_email = gift_email
        self._gift_message = gift_message
        self._gift_wrap_cost = gift_wrap_cost
        self._gift_wrap_title = gift_wrap_title

    @property
    def gift(self):
        """
        Gets the gift of this CartGift.
        True if this order is a gift

        :return: The gift of this CartGift.
        :rtype: bool
        """
        return self._gift

    @gift.setter
    def gift(self, gift):
        """
        Sets the gift of this CartGift.
        True if this order is a gift

        :param gift: The gift of this CartGift.
        :type: bool
        """

        self._gift = gift

    @property
    def gift_charge(self):
        """
        Gets the gift_charge of this CartGift.


        :return: The gift_charge of this CartGift.
        :rtype: Currency
        """
        return self._gift_charge

    @gift_charge.setter
    def gift_charge(self, gift_charge):
        """
        Sets the gift_charge of this CartGift.


        :param gift_charge: The gift_charge of this CartGift.
        :type: Currency
        """

        self._gift_charge = gift_charge

    @property
    def gift_email(self):
        """
        Gets the gift_email of this CartGift.
        Email address of the gift recipient

        :return: The gift_email of this CartGift.
        :rtype: str
        """
        return self._gift_email

    @gift_email.setter
    def gift_email(self, gift_email):
        """
        Sets the gift_email of this CartGift.
        Email address of the gift recipient

        :param gift_email: The gift_email of this CartGift.
        :type: str
        """

        if not gift_email:
            raise ValueError("Invalid value for `gift_email`, must not be `None`")
        if len(gift_email) > 100:
            raise ValueError("Invalid value for `gift_email`, length must be less than `100`")

        self._gift_email = gift_email

    @property
    def gift_message(self):
        """
        Gets the gift_message of this CartGift.
        Message to the gift recipient

        :return: The gift_message of this CartGift.
        :rtype: str
        """
        return self._gift_message

    @gift_message.setter
    def gift_message(self, gift_message):
        """
        Sets the gift_message of this CartGift.
        Message to the gift recipient

        :param gift_message: The gift_message of this CartGift.
        :type: str
        """

        if not gift_message:
            raise ValueError("Invalid value for `gift_message`, must not be `None`")
        if len(gift_message) > 10000:
            raise ValueError("Invalid value for `gift_message`, length must be less than `10000`")

        self._gift_message = gift_message

    @property
    def gift_wrap_cost(self):
        """
        Gets the gift_wrap_cost of this CartGift.


        :return: The gift_wrap_cost of this CartGift.
        :rtype: Currency
        """
        return self._gift_wrap_cost

    @gift_wrap_cost.setter
    def gift_wrap_cost(self, gift_wrap_cost):
        """
        Sets the gift_wrap_cost of this CartGift.


        :param gift_wrap_cost: The gift_wrap_cost of this CartGift.
        :type: Currency
        """

        self._gift_wrap_cost = gift_wrap_cost

    @property
    def gift_wrap_title(self):
        """
        Gets the gift_wrap_title of this CartGift.
        Title of the selected gift wrap

        :return: The gift_wrap_title of this CartGift.
        :rtype: str
        """
        return self._gift_wrap_title

    @gift_wrap_title.setter
    def gift_wrap_title(self, gift_wrap_title):
        """
        Sets the gift_wrap_title of this CartGift.
        Title of the selected gift wrap

        :param gift_wrap_title: The gift_wrap_title of this CartGift.
        :type: str
        """

        if not gift_wrap_title:
            raise ValueError("Invalid value for `gift_wrap_title`, must not be `None`")
        if len(gift_wrap_title) > 30:
            raise ValueError("Invalid value for `gift_wrap_title`, length must be less than `30`")

        self._gift_wrap_title = gift_wrap_title

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