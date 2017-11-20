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


class CustomerAffiliate(object):
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
        'affiliate_oid': 'int',
        'email': 'str'
    }

    attribute_map = {
        'affiliate_oid': 'affiliate_oid',
        'email': 'email'
    }

    def __init__(self, affiliate_oid=None, email=None):
        """
        CustomerAffiliate - a model defined in Swagger
        """

        self._affiliate_oid = None
        self._email = None
        self.discriminator = None

        if affiliate_oid is not None:
          self.affiliate_oid = affiliate_oid
        if email is not None:
          self.email = email

    @property
    def affiliate_oid(self):
        """
        Gets the affiliate_oid of this CustomerAffiliate.
        Affiliate object identifier

        :return: The affiliate_oid of this CustomerAffiliate.
        :rtype: int
        """
        return self._affiliate_oid

    @affiliate_oid.setter
    def affiliate_oid(self, affiliate_oid):
        """
        Sets the affiliate_oid of this CustomerAffiliate.
        Affiliate object identifier

        :param affiliate_oid: The affiliate_oid of this CustomerAffiliate.
        :type: int
        """

        self._affiliate_oid = affiliate_oid

    @property
    def email(self):
        """
        Gets the email of this CustomerAffiliate.
        email

        :return: The email of this CustomerAffiliate.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerAffiliate.
        email

        :param email: The email of this CustomerAffiliate.
        :type: str
        """

        self._email = email

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
        if not isinstance(other, CustomerAffiliate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
