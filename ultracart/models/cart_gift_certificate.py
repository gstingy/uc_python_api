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


class CartGiftCertificate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, gift_certificate_amount=None, gift_certificate_code=None, gift_certificate_remaining_balance_after_order=None):
        """
        CartGiftCertificate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'gift_certificate_amount': 'Currency',
            'gift_certificate_code': 'str',
            'gift_certificate_remaining_balance_after_order': 'Currency'
        }

        self.attribute_map = {
            'gift_certificate_amount': 'gift_certificate_amount',
            'gift_certificate_code': 'gift_certificate_code',
            'gift_certificate_remaining_balance_after_order': 'gift_certificate_remaining_balance_after_order'
        }

        self._gift_certificate_amount = gift_certificate_amount
        self._gift_certificate_code = gift_certificate_code
        self._gift_certificate_remaining_balance_after_order = gift_certificate_remaining_balance_after_order

    @property
    def gift_certificate_amount(self):
        """
        Gets the gift_certificate_amount of this CartGiftCertificate.


        :return: The gift_certificate_amount of this CartGiftCertificate.
        :rtype: Currency
        """
        return self._gift_certificate_amount

    @gift_certificate_amount.setter
    def gift_certificate_amount(self, gift_certificate_amount):
        """
        Sets the gift_certificate_amount of this CartGiftCertificate.


        :param gift_certificate_amount: The gift_certificate_amount of this CartGiftCertificate.
        :type: Currency
        """

        self._gift_certificate_amount = gift_certificate_amount

    @property
    def gift_certificate_code(self):
        """
        Gets the gift_certificate_code of this CartGiftCertificate.
        Gift certificate code

        :return: The gift_certificate_code of this CartGiftCertificate.
        :rtype: str
        """
        return self._gift_certificate_code

    @gift_certificate_code.setter
    def gift_certificate_code(self, gift_certificate_code):
        """
        Sets the gift_certificate_code of this CartGiftCertificate.
        Gift certificate code

        :param gift_certificate_code: The gift_certificate_code of this CartGiftCertificate.
        :type: str
        """

        self._gift_certificate_code = gift_certificate_code

    @property
    def gift_certificate_remaining_balance_after_order(self):
        """
        Gets the gift_certificate_remaining_balance_after_order of this CartGiftCertificate.


        :return: The gift_certificate_remaining_balance_after_order of this CartGiftCertificate.
        :rtype: Currency
        """
        return self._gift_certificate_remaining_balance_after_order

    @gift_certificate_remaining_balance_after_order.setter
    def gift_certificate_remaining_balance_after_order(self, gift_certificate_remaining_balance_after_order):
        """
        Sets the gift_certificate_remaining_balance_after_order of this CartGiftCertificate.


        :param gift_certificate_remaining_balance_after_order: The gift_certificate_remaining_balance_after_order of this CartGiftCertificate.
        :type: Currency
        """

        self._gift_certificate_remaining_balance_after_order = gift_certificate_remaining_balance_after_order

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