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


class ItemVariationOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default_option=None, merchant_item_multimedia_oid=None, translated_text_instance_oid=None, value=None):
        """
        ItemVariationOption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_option': 'bool',
            'merchant_item_multimedia_oid': 'int',
            'translated_text_instance_oid': 'int',
            'value': 'str'
        }

        self.attribute_map = {
            'default_option': 'default_option',
            'merchant_item_multimedia_oid': 'merchant_item_multimedia_oid',
            'translated_text_instance_oid': 'translated_text_instance_oid',
            'value': 'value'
        }

        self._default_option = default_option
        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid
        self._translated_text_instance_oid = translated_text_instance_oid
        self._value = value

    @property
    def default_option(self):
        """
        Gets the default_option of this ItemVariationOption.


        :return: The default_option of this ItemVariationOption.
        :rtype: bool
        """
        return self._default_option

    @default_option.setter
    def default_option(self, default_option):
        """
        Sets the default_option of this ItemVariationOption.


        :param default_option: The default_option of this ItemVariationOption.
        :type: bool
        """

        self._default_option = default_option

    @property
    def merchant_item_multimedia_oid(self):
        """
        Gets the merchant_item_multimedia_oid of this ItemVariationOption.


        :return: The merchant_item_multimedia_oid of this ItemVariationOption.
        :rtype: int
        """
        return self._merchant_item_multimedia_oid

    @merchant_item_multimedia_oid.setter
    def merchant_item_multimedia_oid(self, merchant_item_multimedia_oid):
        """
        Sets the merchant_item_multimedia_oid of this ItemVariationOption.


        :param merchant_item_multimedia_oid: The merchant_item_multimedia_oid of this ItemVariationOption.
        :type: int
        """

        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid

    @property
    def translated_text_instance_oid(self):
        """
        Gets the translated_text_instance_oid of this ItemVariationOption.


        :return: The translated_text_instance_oid of this ItemVariationOption.
        :rtype: int
        """
        return self._translated_text_instance_oid

    @translated_text_instance_oid.setter
    def translated_text_instance_oid(self, translated_text_instance_oid):
        """
        Sets the translated_text_instance_oid of this ItemVariationOption.


        :param translated_text_instance_oid: The translated_text_instance_oid of this ItemVariationOption.
        :type: int
        """

        self._translated_text_instance_oid = translated_text_instance_oid

    @property
    def value(self):
        """
        Gets the value of this ItemVariationOption.


        :return: The value of this ItemVariationOption.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ItemVariationOption.


        :param value: The value of this ItemVariationOption.
        :type: str
        """

        self._value = value

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
