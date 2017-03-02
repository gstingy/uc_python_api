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


class ItemKitComponent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, component_cost=None, component_description=None, component_merchant_item_id=None, component_merchant_item_oid=None, quantity=None):
        """
        ItemKitComponent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'component_cost': 'float',
            'component_description': 'str',
            'component_merchant_item_id': 'str',
            'component_merchant_item_oid': 'int',
            'quantity': 'int'
        }

        self.attribute_map = {
            'component_cost': 'component_cost',
            'component_description': 'component_description',
            'component_merchant_item_id': 'component_merchant_item_id',
            'component_merchant_item_oid': 'component_merchant_item_oid',
            'quantity': 'quantity'
        }

        self._component_cost = component_cost
        self._component_description = component_description
        self._component_merchant_item_id = component_merchant_item_id
        self._component_merchant_item_oid = component_merchant_item_oid
        self._quantity = quantity

    @property
    def component_cost(self):
        """
        Gets the component_cost of this ItemKitComponent.
        Component item cost

        :return: The component_cost of this ItemKitComponent.
        :rtype: float
        """
        return self._component_cost

    @component_cost.setter
    def component_cost(self, component_cost):
        """
        Sets the component_cost of this ItemKitComponent.
        Component item cost

        :param component_cost: The component_cost of this ItemKitComponent.
        :type: float
        """

        self._component_cost = component_cost

    @property
    def component_description(self):
        """
        Gets the component_description of this ItemKitComponent.
        Component item description

        :return: The component_description of this ItemKitComponent.
        :rtype: str
        """
        return self._component_description

    @component_description.setter
    def component_description(self, component_description):
        """
        Sets the component_description of this ItemKitComponent.
        Component item description

        :param component_description: The component_description of this ItemKitComponent.
        :type: str
        """

        self._component_description = component_description

    @property
    def component_merchant_item_id(self):
        """
        Gets the component_merchant_item_id of this ItemKitComponent.
        Component item ID

        :return: The component_merchant_item_id of this ItemKitComponent.
        :rtype: str
        """
        return self._component_merchant_item_id

    @component_merchant_item_id.setter
    def component_merchant_item_id(self, component_merchant_item_id):
        """
        Sets the component_merchant_item_id of this ItemKitComponent.
        Component item ID

        :param component_merchant_item_id: The component_merchant_item_id of this ItemKitComponent.
        :type: str
        """

        self._component_merchant_item_id = component_merchant_item_id

    @property
    def component_merchant_item_oid(self):
        """
        Gets the component_merchant_item_oid of this ItemKitComponent.
        Component item object identifier

        :return: The component_merchant_item_oid of this ItemKitComponent.
        :rtype: int
        """
        return self._component_merchant_item_oid

    @component_merchant_item_oid.setter
    def component_merchant_item_oid(self, component_merchant_item_oid):
        """
        Sets the component_merchant_item_oid of this ItemKitComponent.
        Component item object identifier

        :param component_merchant_item_oid: The component_merchant_item_oid of this ItemKitComponent.
        :type: int
        """

        self._component_merchant_item_oid = component_merchant_item_oid

    @property
    def quantity(self):
        """
        Gets the quantity of this ItemKitComponent.
        Quantity

        :return: The quantity of this ItemKitComponent.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ItemKitComponent.
        Quantity

        :param quantity: The quantity of this ItemKitComponent.
        :type: int
        """

        self._quantity = quantity

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
