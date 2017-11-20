# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrderItemOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'additional_dimension_application': 'str',
        'cost_change': 'Currency',
        'file_attachment': 'OrderItemOptionFileAttachment',
        'height': 'Distance',
        'hidden': 'bool',
        'label': 'str',
        'length': 'Distance',
        'one_time_fee': 'bool',
        'value': 'str',
        'weight_change': 'Weight',
        'width': 'Distance'
    }

    attribute_map = {
        'additional_dimension_application': 'additional_dimension_application',
        'cost_change': 'cost_change',
        'file_attachment': 'file_attachment',
        'height': 'height',
        'hidden': 'hidden',
        'label': 'label',
        'length': 'length',
        'one_time_fee': 'one_time_fee',
        'value': 'value',
        'weight_change': 'weight_change',
        'width': 'width'
    }

    def __init__(self, additional_dimension_application=None, cost_change=None, file_attachment=None, height=None, hidden=None, label=None, length=None, one_time_fee=None, value=None, weight_change=None, width=None):
        """
        OrderItemOption - a model defined in Swagger
        """

        self._additional_dimension_application = None
        self._cost_change = None
        self._file_attachment = None
        self._height = None
        self._hidden = None
        self._label = None
        self._length = None
        self._one_time_fee = None
        self._value = None
        self._weight_change = None
        self._width = None
        self.discriminator = None

        if additional_dimension_application is not None:
          self.additional_dimension_application = additional_dimension_application
        if cost_change is not None:
          self.cost_change = cost_change
        if file_attachment is not None:
          self.file_attachment = file_attachment
        if height is not None:
          self.height = height
        if hidden is not None:
          self.hidden = hidden
        if label is not None:
          self.label = label
        if length is not None:
          self.length = length
        if one_time_fee is not None:
          self.one_time_fee = one_time_fee
        if value is not None:
          self.value = value
        if weight_change is not None:
          self.weight_change = weight_change
        if width is not None:
          self.width = width

    @property
    def additional_dimension_application(self):
        """
        Gets the additional_dimension_application of this OrderItemOption.
        How the additional dimensions are applied to the item.

        :return: The additional_dimension_application of this OrderItemOption.
        :rtype: str
        """
        return self._additional_dimension_application

    @additional_dimension_application.setter
    def additional_dimension_application(self, additional_dimension_application):
        """
        Sets the additional_dimension_application of this OrderItemOption.
        How the additional dimensions are applied to the item.

        :param additional_dimension_application: The additional_dimension_application of this OrderItemOption.
        :type: str
        """
        allowed_values = ["none", "set item to", "add item"]
        if additional_dimension_application not in allowed_values:
            raise ValueError(
                "Invalid value for `additional_dimension_application` ({0}), must be one of {1}"
                .format(additional_dimension_application, allowed_values)
            )

        self._additional_dimension_application = additional_dimension_application

    @property
    def cost_change(self):
        """
        Gets the cost_change of this OrderItemOption.

        :return: The cost_change of this OrderItemOption.
        :rtype: Currency
        """
        return self._cost_change

    @cost_change.setter
    def cost_change(self, cost_change):
        """
        Sets the cost_change of this OrderItemOption.

        :param cost_change: The cost_change of this OrderItemOption.
        :type: Currency
        """

        self._cost_change = cost_change

    @property
    def file_attachment(self):
        """
        Gets the file_attachment of this OrderItemOption.

        :return: The file_attachment of this OrderItemOption.
        :rtype: OrderItemOptionFileAttachment
        """
        return self._file_attachment

    @file_attachment.setter
    def file_attachment(self, file_attachment):
        """
        Sets the file_attachment of this OrderItemOption.

        :param file_attachment: The file_attachment of this OrderItemOption.
        :type: OrderItemOptionFileAttachment
        """

        self._file_attachment = file_attachment

    @property
    def height(self):
        """
        Gets the height of this OrderItemOption.

        :return: The height of this OrderItemOption.
        :rtype: Distance
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this OrderItemOption.

        :param height: The height of this OrderItemOption.
        :type: Distance
        """

        self._height = height

    @property
    def hidden(self):
        """
        Gets the hidden of this OrderItemOption.
        True if this option is hidden from display on the order

        :return: The hidden of this OrderItemOption.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """
        Sets the hidden of this OrderItemOption.
        True if this option is hidden from display on the order

        :param hidden: The hidden of this OrderItemOption.
        :type: bool
        """

        self._hidden = hidden

    @property
    def label(self):
        """
        Gets the label of this OrderItemOption.
        Label

        :return: The label of this OrderItemOption.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this OrderItemOption.
        Label

        :param label: The label of this OrderItemOption.
        :type: str
        """
        if label is not None and len(label) > 50:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `50`")

        self._label = label

    @property
    def length(self):
        """
        Gets the length of this OrderItemOption.

        :return: The length of this OrderItemOption.
        :rtype: Distance
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this OrderItemOption.

        :param length: The length of this OrderItemOption.
        :type: Distance
        """

        self._length = length

    @property
    def one_time_fee(self):
        """
        Gets the one_time_fee of this OrderItemOption.
        True if the cost associated with this option is a one time fee or multiplied by the quantity of the item

        :return: The one_time_fee of this OrderItemOption.
        :rtype: bool
        """
        return self._one_time_fee

    @one_time_fee.setter
    def one_time_fee(self, one_time_fee):
        """
        Sets the one_time_fee of this OrderItemOption.
        True if the cost associated with this option is a one time fee or multiplied by the quantity of the item

        :param one_time_fee: The one_time_fee of this OrderItemOption.
        :type: bool
        """

        self._one_time_fee = one_time_fee

    @property
    def value(self):
        """
        Gets the value of this OrderItemOption.
        Value

        :return: The value of this OrderItemOption.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this OrderItemOption.
        Value

        :param value: The value of this OrderItemOption.
        :type: str
        """
        if value is not None and len(value) > 1024:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `1024`")

        self._value = value

    @property
    def weight_change(self):
        """
        Gets the weight_change of this OrderItemOption.

        :return: The weight_change of this OrderItemOption.
        :rtype: Weight
        """
        return self._weight_change

    @weight_change.setter
    def weight_change(self, weight_change):
        """
        Sets the weight_change of this OrderItemOption.

        :param weight_change: The weight_change of this OrderItemOption.
        :type: Weight
        """

        self._weight_change = weight_change

    @property
    def width(self):
        """
        Gets the width of this OrderItemOption.

        :return: The width of this OrderItemOption.
        :rtype: Distance
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this OrderItemOption.

        :param width: The width of this OrderItemOption.
        :type: Distance
        """

        self._width = width

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
        if not isinstance(other, OrderItemOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
