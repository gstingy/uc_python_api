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


class OrderAffiliate(object):
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
        'ledger_entries': 'list[OrderAffiliateLedger]',
        'sub_id': 'str'
    }

    attribute_map = {
        'affiliate_oid': 'affiliate_oid',
        'ledger_entries': 'ledger_entries',
        'sub_id': 'sub_id'
    }

    def __init__(self, affiliate_oid=None, ledger_entries=None, sub_id=None):
        """
        OrderAffiliate - a model defined in Swagger
        """

        self._affiliate_oid = None
        self._ledger_entries = None
        self._sub_id = None
        self.discriminator = None

        if affiliate_oid is not None:
          self.affiliate_oid = affiliate_oid
        if ledger_entries is not None:
          self.ledger_entries = ledger_entries
        if sub_id is not None:
          self.sub_id = sub_id

    @property
    def affiliate_oid(self):
        """
        Gets the affiliate_oid of this OrderAffiliate.
        Affiliate ID

        :return: The affiliate_oid of this OrderAffiliate.
        :rtype: int
        """
        return self._affiliate_oid

    @affiliate_oid.setter
    def affiliate_oid(self, affiliate_oid):
        """
        Sets the affiliate_oid of this OrderAffiliate.
        Affiliate ID

        :param affiliate_oid: The affiliate_oid of this OrderAffiliate.
        :type: int
        """

        self._affiliate_oid = affiliate_oid

    @property
    def ledger_entries(self):
        """
        Gets the ledger_entries of this OrderAffiliate.
        Ledger entries associated with all the commissions earned on this order

        :return: The ledger_entries of this OrderAffiliate.
        :rtype: list[OrderAffiliateLedger]
        """
        return self._ledger_entries

    @ledger_entries.setter
    def ledger_entries(self, ledger_entries):
        """
        Sets the ledger_entries of this OrderAffiliate.
        Ledger entries associated with all the commissions earned on this order

        :param ledger_entries: The ledger_entries of this OrderAffiliate.
        :type: list[OrderAffiliateLedger]
        """

        self._ledger_entries = ledger_entries

    @property
    def sub_id(self):
        """
        Gets the sub_id of this OrderAffiliate.
        Sub identifier provided by the affiliate on the click that generated this order

        :return: The sub_id of this OrderAffiliate.
        :rtype: str
        """
        return self._sub_id

    @sub_id.setter
    def sub_id(self, sub_id):
        """
        Sets the sub_id of this OrderAffiliate.
        Sub identifier provided by the affiliate on the click that generated this order

        :param sub_id: The sub_id of this OrderAffiliate.
        :type: str
        """

        self._sub_id = sub_id

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
        if not isinstance(other, OrderAffiliate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
