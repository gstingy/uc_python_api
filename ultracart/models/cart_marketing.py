# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartMarketing(object):
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
        'advertising_source': 'str',
        'mailing_list_opt_in': 'bool'
    }

    attribute_map = {
        'advertising_source': 'advertising_source',
        'mailing_list_opt_in': 'mailing_list_opt_in'
    }

    def __init__(self, advertising_source=None, mailing_list_opt_in=None):
        """
        CartMarketing - a model defined in Swagger
        """

        self._advertising_source = None
        self._mailing_list_opt_in = None
        self.discriminator = None

        if advertising_source is not None:
          self.advertising_source = advertising_source
        if mailing_list_opt_in is not None:
          self.mailing_list_opt_in = mailing_list_opt_in

    @property
    def advertising_source(self):
        """
        Gets the advertising_source of this CartMarketing.
        The advertising source the customer indicated

        :return: The advertising_source of this CartMarketing.
        :rtype: str
        """
        return self._advertising_source

    @advertising_source.setter
    def advertising_source(self, advertising_source):
        """
        Sets the advertising_source of this CartMarketing.
        The advertising source the customer indicated

        :param advertising_source: The advertising_source of this CartMarketing.
        :type: str
        """

        self._advertising_source = advertising_source

    @property
    def mailing_list_opt_in(self):
        """
        Gets the mailing_list_opt_in of this CartMarketing.
        True if the customer agrees to receiving marketing emails

        :return: The mailing_list_opt_in of this CartMarketing.
        :rtype: bool
        """
        return self._mailing_list_opt_in

    @mailing_list_opt_in.setter
    def mailing_list_opt_in(self, mailing_list_opt_in):
        """
        Sets the mailing_list_opt_in of this CartMarketing.
        True if the customer agrees to receiving marketing emails

        :param mailing_list_opt_in: The mailing_list_opt_in of this CartMarketing.
        :type: bool
        """

        self._mailing_list_opt_in = mailing_list_opt_in

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
        if not isinstance(other, CartMarketing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
