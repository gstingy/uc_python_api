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


class CartItemVariationSelection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, variation_name=None, variation_value=None):
        """
        CartItemVariationSelection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'variation_name': 'str',
            'variation_value': 'str'
        }

        self.attribute_map = {
            'variation_name': 'variation_name',
            'variation_value': 'variation_value'
        }

        self._variation_name = variation_name
        self._variation_value = variation_value

    @property
    def variation_name(self):
        """
        Gets the variation_name of this CartItemVariationSelection.
        Variation name

        :return: The variation_name of this CartItemVariationSelection.
        :rtype: str
        """
        return self._variation_name

    @variation_name.setter
    def variation_name(self, variation_name):
        """
        Sets the variation_name of this CartItemVariationSelection.
        Variation name

        :param variation_name: The variation_name of this CartItemVariationSelection.
        :type: str
        """

        self._variation_name = variation_name

    @property
    def variation_value(self):
        """
        Gets the variation_value of this CartItemVariationSelection.
        Variation value

        :return: The variation_value of this CartItemVariationSelection.
        :rtype: str
        """
        return self._variation_value

    @variation_value.setter
    def variation_value(self, variation_value):
        """
        Sets the variation_value of this CartItemVariationSelection.
        Variation value

        :param variation_value: The variation_value of this CartItemVariationSelection.
        :type: str
        """

        self._variation_value = variation_value

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