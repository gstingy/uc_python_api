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


class ItemRelatedItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, related_merchant_item_id=None, related_merchant_item_oid=None, type=None):
        """
        ItemRelatedItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'related_merchant_item_id': 'str',
            'related_merchant_item_oid': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'related_merchant_item_id': 'related_merchant_item_id',
            'related_merchant_item_oid': 'related_merchant_item_oid',
            'type': 'type'
        }

        self._related_merchant_item_id = related_merchant_item_id
        self._related_merchant_item_oid = related_merchant_item_oid
        self._type = type

    @property
    def related_merchant_item_id(self):
        """
        Gets the related_merchant_item_id of this ItemRelatedItem.


        :return: The related_merchant_item_id of this ItemRelatedItem.
        :rtype: str
        """
        return self._related_merchant_item_id

    @related_merchant_item_id.setter
    def related_merchant_item_id(self, related_merchant_item_id):
        """
        Sets the related_merchant_item_id of this ItemRelatedItem.


        :param related_merchant_item_id: The related_merchant_item_id of this ItemRelatedItem.
        :type: str
        """

        self._related_merchant_item_id = related_merchant_item_id

    @property
    def related_merchant_item_oid(self):
        """
        Gets the related_merchant_item_oid of this ItemRelatedItem.


        :return: The related_merchant_item_oid of this ItemRelatedItem.
        :rtype: int
        """
        return self._related_merchant_item_oid

    @related_merchant_item_oid.setter
    def related_merchant_item_oid(self, related_merchant_item_oid):
        """
        Sets the related_merchant_item_oid of this ItemRelatedItem.


        :param related_merchant_item_oid: The related_merchant_item_oid of this ItemRelatedItem.
        :type: int
        """

        self._related_merchant_item_oid = related_merchant_item_oid

    @property
    def type(self):
        """
        Gets the type of this ItemRelatedItem.


        :return: The type of this ItemRelatedItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemRelatedItem.


        :param type: The type of this ItemRelatedItem.
        :type: str
        """

        self._type = type

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
