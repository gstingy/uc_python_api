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


class ItemOptionValueDigitalItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, digital_item_oid=None, original_filename=None):
        """
        ItemOptionValueDigitalItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'digital_item_oid': 'int',
            'original_filename': 'str'
        }

        self.attribute_map = {
            'digital_item_oid': 'digital_item_oid',
            'original_filename': 'original_filename'
        }

        self._digital_item_oid = digital_item_oid
        self._original_filename = original_filename

    @property
    def digital_item_oid(self):
        """
        Gets the digital_item_oid of this ItemOptionValueDigitalItem.


        :return: The digital_item_oid of this ItemOptionValueDigitalItem.
        :rtype: int
        """
        return self._digital_item_oid

    @digital_item_oid.setter
    def digital_item_oid(self, digital_item_oid):
        """
        Sets the digital_item_oid of this ItemOptionValueDigitalItem.


        :param digital_item_oid: The digital_item_oid of this ItemOptionValueDigitalItem.
        :type: int
        """

        self._digital_item_oid = digital_item_oid

    @property
    def original_filename(self):
        """
        Gets the original_filename of this ItemOptionValueDigitalItem.


        :return: The original_filename of this ItemOptionValueDigitalItem.
        :rtype: str
        """
        return self._original_filename

    @original_filename.setter
    def original_filename(self, original_filename):
        """
        Sets the original_filename of this ItemOptionValueDigitalItem.


        :param original_filename: The original_filename of this ItemOptionValueDigitalItem.
        :type: str
        """

        self._original_filename = original_filename

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
