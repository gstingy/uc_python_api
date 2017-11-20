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


class ItemShippingCase(object):
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
        'case_label': 'str',
        'case_merchant_item_id': 'str',
        'case_merchant_item_oid': 'int',
        'quantity': 'int'
    }

    attribute_map = {
        'case_label': 'case_label',
        'case_merchant_item_id': 'case_merchant_item_id',
        'case_merchant_item_oid': 'case_merchant_item_oid',
        'quantity': 'quantity'
    }

    def __init__(self, case_label=None, case_merchant_item_id=None, case_merchant_item_oid=None, quantity=None):
        """
        ItemShippingCase - a model defined in Swagger
        """

        self._case_label = None
        self._case_merchant_item_id = None
        self._case_merchant_item_oid = None
        self._quantity = None
        self.discriminator = None

        if case_label is not None:
          self.case_label = case_label
        if case_merchant_item_id is not None:
          self.case_merchant_item_id = case_merchant_item_id
        if case_merchant_item_oid is not None:
          self.case_merchant_item_oid = case_merchant_item_oid
        if quantity is not None:
          self.quantity = quantity

    @property
    def case_label(self):
        """
        Gets the case_label of this ItemShippingCase.
        Case label

        :return: The case_label of this ItemShippingCase.
        :rtype: str
        """
        return self._case_label

    @case_label.setter
    def case_label(self, case_label):
        """
        Sets the case_label of this ItemShippingCase.
        Case label

        :param case_label: The case_label of this ItemShippingCase.
        :type: str
        """
        if case_label is not None and len(case_label) > 20:
            raise ValueError("Invalid value for `case_label`, length must be less than or equal to `20`")

        self._case_label = case_label

    @property
    def case_merchant_item_id(self):
        """
        Gets the case_merchant_item_id of this ItemShippingCase.
        Case item id

        :return: The case_merchant_item_id of this ItemShippingCase.
        :rtype: str
        """
        return self._case_merchant_item_id

    @case_merchant_item_id.setter
    def case_merchant_item_id(self, case_merchant_item_id):
        """
        Sets the case_merchant_item_id of this ItemShippingCase.
        Case item id

        :param case_merchant_item_id: The case_merchant_item_id of this ItemShippingCase.
        :type: str
        """

        self._case_merchant_item_id = case_merchant_item_id

    @property
    def case_merchant_item_oid(self):
        """
        Gets the case_merchant_item_oid of this ItemShippingCase.
        Case item object identifier

        :return: The case_merchant_item_oid of this ItemShippingCase.
        :rtype: int
        """
        return self._case_merchant_item_oid

    @case_merchant_item_oid.setter
    def case_merchant_item_oid(self, case_merchant_item_oid):
        """
        Sets the case_merchant_item_oid of this ItemShippingCase.
        Case item object identifier

        :param case_merchant_item_oid: The case_merchant_item_oid of this ItemShippingCase.
        :type: int
        """

        self._case_merchant_item_oid = case_merchant_item_oid

    @property
    def quantity(self):
        """
        Gets the quantity of this ItemShippingCase.
        Case quantity

        :return: The quantity of this ItemShippingCase.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ItemShippingCase.
        Case quantity

        :param quantity: The quantity of this ItemShippingCase.
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
        if not isinstance(other, ItemShippingCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
