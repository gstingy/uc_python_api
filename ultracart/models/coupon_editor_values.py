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


class CouponEditorValues(object):
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
        'coupon_types': 'list[str]'
    }

    attribute_map = {
        'coupon_types': 'coupon_types'
    }

    def __init__(self, coupon_types=None):
        """
        CouponEditorValues - a model defined in Swagger
        """

        self._coupon_types = None
        self.discriminator = None

        if coupon_types is not None:
          self.coupon_types = coupon_types

    @property
    def coupon_types(self):
        """
        Gets the coupon_types of this CouponEditorValues.
        coupon_types

        :return: The coupon_types of this CouponEditorValues.
        :rtype: list[str]
        """
        return self._coupon_types

    @coupon_types.setter
    def coupon_types(self, coupon_types):
        """
        Sets the coupon_types of this CouponEditorValues.
        coupon_types

        :param coupon_types: The coupon_types of this CouponEditorValues.
        :type: list[str]
        """

        self._coupon_types = coupon_types

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
        if not isinstance(other, CouponEditorValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
