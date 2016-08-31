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


class ItemShippingDistributionCenter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allocated_to_placed_orders=None, allocated_to_shopping_carts=None, available_to_allocate=None, desired_inventory_level=None, distribution_center_code=None, distribution_center_oid=None, eta=None, handles=None, inventory_level=None, maximum_backorder=None, reorder_inventory_level=None, sku=None, stock_picking_location=None):
        """
        ItemShippingDistributionCenter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allocated_to_placed_orders': 'float',
            'allocated_to_shopping_carts': 'float',
            'available_to_allocate': 'float',
            'desired_inventory_level': 'float',
            'distribution_center_code': 'str',
            'distribution_center_oid': 'int',
            'eta': 'str',
            'handles': 'bool',
            'inventory_level': 'float',
            'maximum_backorder': 'int',
            'reorder_inventory_level': 'float',
            'sku': 'str',
            'stock_picking_location': 'str'
        }

        self.attribute_map = {
            'allocated_to_placed_orders': 'allocated_to_placed_orders',
            'allocated_to_shopping_carts': 'allocated_to_shopping_carts',
            'available_to_allocate': 'available_to_allocate',
            'desired_inventory_level': 'desired_inventory_level',
            'distribution_center_code': 'distribution_center_code',
            'distribution_center_oid': 'distribution_center_oid',
            'eta': 'eta',
            'handles': 'handles',
            'inventory_level': 'inventory_level',
            'maximum_backorder': 'maximum_backorder',
            'reorder_inventory_level': 'reorder_inventory_level',
            'sku': 'sku',
            'stock_picking_location': 'stock_picking_location'
        }

        self._allocated_to_placed_orders = allocated_to_placed_orders
        self._allocated_to_shopping_carts = allocated_to_shopping_carts
        self._available_to_allocate = available_to_allocate
        self._desired_inventory_level = desired_inventory_level
        self._distribution_center_code = distribution_center_code
        self._distribution_center_oid = distribution_center_oid
        self._eta = eta
        self._handles = handles
        self._inventory_level = inventory_level
        self._maximum_backorder = maximum_backorder
        self._reorder_inventory_level = reorder_inventory_level
        self._sku = sku
        self._stock_picking_location = stock_picking_location

    @property
    def allocated_to_placed_orders(self):
        """
        Gets the allocated_to_placed_orders of this ItemShippingDistributionCenter.


        :return: The allocated_to_placed_orders of this ItemShippingDistributionCenter.
        :rtype: float
        """
        return self._allocated_to_placed_orders

    @allocated_to_placed_orders.setter
    def allocated_to_placed_orders(self, allocated_to_placed_orders):
        """
        Sets the allocated_to_placed_orders of this ItemShippingDistributionCenter.


        :param allocated_to_placed_orders: The allocated_to_placed_orders of this ItemShippingDistributionCenter.
        :type: float
        """

        self._allocated_to_placed_orders = allocated_to_placed_orders

    @property
    def allocated_to_shopping_carts(self):
        """
        Gets the allocated_to_shopping_carts of this ItemShippingDistributionCenter.


        :return: The allocated_to_shopping_carts of this ItemShippingDistributionCenter.
        :rtype: float
        """
        return self._allocated_to_shopping_carts

    @allocated_to_shopping_carts.setter
    def allocated_to_shopping_carts(self, allocated_to_shopping_carts):
        """
        Sets the allocated_to_shopping_carts of this ItemShippingDistributionCenter.


        :param allocated_to_shopping_carts: The allocated_to_shopping_carts of this ItemShippingDistributionCenter.
        :type: float
        """

        self._allocated_to_shopping_carts = allocated_to_shopping_carts

    @property
    def available_to_allocate(self):
        """
        Gets the available_to_allocate of this ItemShippingDistributionCenter.


        :return: The available_to_allocate of this ItemShippingDistributionCenter.
        :rtype: float
        """
        return self._available_to_allocate

    @available_to_allocate.setter
    def available_to_allocate(self, available_to_allocate):
        """
        Sets the available_to_allocate of this ItemShippingDistributionCenter.


        :param available_to_allocate: The available_to_allocate of this ItemShippingDistributionCenter.
        :type: float
        """

        self._available_to_allocate = available_to_allocate

    @property
    def desired_inventory_level(self):
        """
        Gets the desired_inventory_level of this ItemShippingDistributionCenter.


        :return: The desired_inventory_level of this ItemShippingDistributionCenter.
        :rtype: float
        """
        return self._desired_inventory_level

    @desired_inventory_level.setter
    def desired_inventory_level(self, desired_inventory_level):
        """
        Sets the desired_inventory_level of this ItemShippingDistributionCenter.


        :param desired_inventory_level: The desired_inventory_level of this ItemShippingDistributionCenter.
        :type: float
        """

        self._desired_inventory_level = desired_inventory_level

    @property
    def distribution_center_code(self):
        """
        Gets the distribution_center_code of this ItemShippingDistributionCenter.


        :return: The distribution_center_code of this ItemShippingDistributionCenter.
        :rtype: str
        """
        return self._distribution_center_code

    @distribution_center_code.setter
    def distribution_center_code(self, distribution_center_code):
        """
        Sets the distribution_center_code of this ItemShippingDistributionCenter.


        :param distribution_center_code: The distribution_center_code of this ItemShippingDistributionCenter.
        :type: str
        """

        self._distribution_center_code = distribution_center_code

    @property
    def distribution_center_oid(self):
        """
        Gets the distribution_center_oid of this ItemShippingDistributionCenter.


        :return: The distribution_center_oid of this ItemShippingDistributionCenter.
        :rtype: int
        """
        return self._distribution_center_oid

    @distribution_center_oid.setter
    def distribution_center_oid(self, distribution_center_oid):
        """
        Sets the distribution_center_oid of this ItemShippingDistributionCenter.


        :param distribution_center_oid: The distribution_center_oid of this ItemShippingDistributionCenter.
        :type: int
        """

        self._distribution_center_oid = distribution_center_oid

    @property
    def eta(self):
        """
        Gets the eta of this ItemShippingDistributionCenter.


        :return: The eta of this ItemShippingDistributionCenter.
        :rtype: str
        """
        return self._eta

    @eta.setter
    def eta(self, eta):
        """
        Sets the eta of this ItemShippingDistributionCenter.


        :param eta: The eta of this ItemShippingDistributionCenter.
        :type: str
        """

        self._eta = eta

    @property
    def handles(self):
        """
        Gets the handles of this ItemShippingDistributionCenter.


        :return: The handles of this ItemShippingDistributionCenter.
        :rtype: bool
        """
        return self._handles

    @handles.setter
    def handles(self, handles):
        """
        Sets the handles of this ItemShippingDistributionCenter.


        :param handles: The handles of this ItemShippingDistributionCenter.
        :type: bool
        """

        self._handles = handles

    @property
    def inventory_level(self):
        """
        Gets the inventory_level of this ItemShippingDistributionCenter.


        :return: The inventory_level of this ItemShippingDistributionCenter.
        :rtype: float
        """
        return self._inventory_level

    @inventory_level.setter
    def inventory_level(self, inventory_level):
        """
        Sets the inventory_level of this ItemShippingDistributionCenter.


        :param inventory_level: The inventory_level of this ItemShippingDistributionCenter.
        :type: float
        """

        self._inventory_level = inventory_level

    @property
    def maximum_backorder(self):
        """
        Gets the maximum_backorder of this ItemShippingDistributionCenter.


        :return: The maximum_backorder of this ItemShippingDistributionCenter.
        :rtype: int
        """
        return self._maximum_backorder

    @maximum_backorder.setter
    def maximum_backorder(self, maximum_backorder):
        """
        Sets the maximum_backorder of this ItemShippingDistributionCenter.


        :param maximum_backorder: The maximum_backorder of this ItemShippingDistributionCenter.
        :type: int
        """

        self._maximum_backorder = maximum_backorder

    @property
    def reorder_inventory_level(self):
        """
        Gets the reorder_inventory_level of this ItemShippingDistributionCenter.


        :return: The reorder_inventory_level of this ItemShippingDistributionCenter.
        :rtype: float
        """
        return self._reorder_inventory_level

    @reorder_inventory_level.setter
    def reorder_inventory_level(self, reorder_inventory_level):
        """
        Sets the reorder_inventory_level of this ItemShippingDistributionCenter.


        :param reorder_inventory_level: The reorder_inventory_level of this ItemShippingDistributionCenter.
        :type: float
        """

        self._reorder_inventory_level = reorder_inventory_level

    @property
    def sku(self):
        """
        Gets the sku of this ItemShippingDistributionCenter.


        :return: The sku of this ItemShippingDistributionCenter.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this ItemShippingDistributionCenter.


        :param sku: The sku of this ItemShippingDistributionCenter.
        :type: str
        """

        self._sku = sku

    @property
    def stock_picking_location(self):
        """
        Gets the stock_picking_location of this ItemShippingDistributionCenter.


        :return: The stock_picking_location of this ItemShippingDistributionCenter.
        :rtype: str
        """
        return self._stock_picking_location

    @stock_picking_location.setter
    def stock_picking_location(self, stock_picking_location):
        """
        Sets the stock_picking_location of this ItemShippingDistributionCenter.


        :param stock_picking_location: The stock_picking_location of this ItemShippingDistributionCenter.
        :type: str
        """

        self._stock_picking_location = stock_picking_location

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