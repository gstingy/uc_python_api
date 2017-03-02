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


class CartItemOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cost_if_specified=None, cost_per_letter=None, cost_per_line=None, ignore_if_default=None, label=None, name=None, one_time_fee=None, option_oid=None, required=None, selected_value=None, type=None, values=None):
        """
        CartItemOption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cost_if_specified': 'Currency',
            'cost_per_letter': 'Currency',
            'cost_per_line': 'Currency',
            'ignore_if_default': 'bool',
            'label': 'str',
            'name': 'str',
            'one_time_fee': 'bool',
            'option_oid': 'int',
            'required': 'bool',
            'selected_value': 'str',
            'type': 'str',
            'values': 'list[CartItemOptionValue]'
        }

        self.attribute_map = {
            'cost_if_specified': 'cost_if_specified',
            'cost_per_letter': 'cost_per_letter',
            'cost_per_line': 'cost_per_line',
            'ignore_if_default': 'ignore_if_default',
            'label': 'label',
            'name': 'name',
            'one_time_fee': 'one_time_fee',
            'option_oid': 'option_oid',
            'required': 'required',
            'selected_value': 'selected_value',
            'type': 'type',
            'values': 'values'
        }

        self._cost_if_specified = cost_if_specified
        self._cost_per_letter = cost_per_letter
        self._cost_per_line = cost_per_line
        self._ignore_if_default = ignore_if_default
        self._label = label
        self._name = name
        self._one_time_fee = one_time_fee
        self._option_oid = option_oid
        self._required = required
        self._selected_value = selected_value
        self._type = type
        self._values = values

    @property
    def cost_if_specified(self):
        """
        Gets the cost_if_specified of this CartItemOption.


        :return: The cost_if_specified of this CartItemOption.
        :rtype: Currency
        """
        return self._cost_if_specified

    @cost_if_specified.setter
    def cost_if_specified(self, cost_if_specified):
        """
        Sets the cost_if_specified of this CartItemOption.


        :param cost_if_specified: The cost_if_specified of this CartItemOption.
        :type: Currency
        """

        self._cost_if_specified = cost_if_specified

    @property
    def cost_per_letter(self):
        """
        Gets the cost_per_letter of this CartItemOption.


        :return: The cost_per_letter of this CartItemOption.
        :rtype: Currency
        """
        return self._cost_per_letter

    @cost_per_letter.setter
    def cost_per_letter(self, cost_per_letter):
        """
        Sets the cost_per_letter of this CartItemOption.


        :param cost_per_letter: The cost_per_letter of this CartItemOption.
        :type: Currency
        """

        self._cost_per_letter = cost_per_letter

    @property
    def cost_per_line(self):
        """
        Gets the cost_per_line of this CartItemOption.


        :return: The cost_per_line of this CartItemOption.
        :rtype: Currency
        """
        return self._cost_per_line

    @cost_per_line.setter
    def cost_per_line(self, cost_per_line):
        """
        Sets the cost_per_line of this CartItemOption.


        :param cost_per_line: The cost_per_line of this CartItemOption.
        :type: Currency
        """

        self._cost_per_line = cost_per_line

    @property
    def ignore_if_default(self):
        """
        Gets the ignore_if_default of this CartItemOption.
        True if the default answer is ignored

        :return: The ignore_if_default of this CartItemOption.
        :rtype: bool
        """
        return self._ignore_if_default

    @ignore_if_default.setter
    def ignore_if_default(self, ignore_if_default):
        """
        Sets the ignore_if_default of this CartItemOption.
        True if the default answer is ignored

        :param ignore_if_default: The ignore_if_default of this CartItemOption.
        :type: bool
        """

        self._ignore_if_default = ignore_if_default

    @property
    def label(self):
        """
        Gets the label of this CartItemOption.
        Display label for the option

        :return: The label of this CartItemOption.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this CartItemOption.
        Display label for the option

        :param label: The label of this CartItemOption.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this CartItemOption.
        Name of the option

        :return: The name of this CartItemOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CartItemOption.
        Name of the option

        :param name: The name of this CartItemOption.
        :type: str
        """

        self._name = name

    @property
    def one_time_fee(self):
        """
        Gets the one_time_fee of this CartItemOption.
        Charge the fee a single time instead of multiplying by the quantity

        :return: The one_time_fee of this CartItemOption.
        :rtype: bool
        """
        return self._one_time_fee

    @one_time_fee.setter
    def one_time_fee(self, one_time_fee):
        """
        Sets the one_time_fee of this CartItemOption.
        Charge the fee a single time instead of multiplying by the quantity

        :param one_time_fee: The one_time_fee of this CartItemOption.
        :type: bool
        """

        self._one_time_fee = one_time_fee

    @property
    def option_oid(self):
        """
        Gets the option_oid of this CartItemOption.
        Unique identifier for the option

        :return: The option_oid of this CartItemOption.
        :rtype: int
        """
        return self._option_oid

    @option_oid.setter
    def option_oid(self, option_oid):
        """
        Sets the option_oid of this CartItemOption.
        Unique identifier for the option

        :param option_oid: The option_oid of this CartItemOption.
        :type: int
        """

        self._option_oid = option_oid

    @property
    def required(self):
        """
        Gets the required of this CartItemOption.
        True if the customer is required to select a value

        :return: The required of this CartItemOption.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this CartItemOption.
        True if the customer is required to select a value

        :param required: The required of this CartItemOption.
        :type: bool
        """

        self._required = required

    @property
    def selected_value(self):
        """
        Gets the selected_value of this CartItemOption.
        The value of the option specified by the customer

        :return: The selected_value of this CartItemOption.
        :rtype: str
        """
        return self._selected_value

    @selected_value.setter
    def selected_value(self, selected_value):
        """
        Sets the selected_value of this CartItemOption.
        The value of the option specified by the customer

        :param selected_value: The selected_value of this CartItemOption.
        :type: str
        """

        if not selected_value:
            raise ValueError("Invalid value for `selected_value`, must not be `None`")
        if len(selected_value) > 1024:
            raise ValueError("Invalid value for `selected_value`, length must be less than `1024`")

        self._selected_value = selected_value

    @property
    def type(self):
        """
        Gets the type of this CartItemOption.
        Type of option

        :return: The type of this CartItemOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CartItemOption.
        Type of option

        :param type: The type of this CartItemOption.
        :type: str
        """
        allowed_values = ["single", "multiline", "dropdown", "hidden", "radio", "fixed"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def values(self):
        """
        Gets the values of this CartItemOption.
        Values that the customer can select from for radio or select type options

        :return: The values of this CartItemOption.
        :rtype: list[CartItemOptionValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this CartItemOption.
        Values that the customer can select from for radio or select type options

        :param values: The values of this CartItemOption.
        :type: list[CartItemOptionValue]
        """

        self._values = values

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
