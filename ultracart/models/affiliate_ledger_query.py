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


class AffiliateLedgerQuery(object):
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
        'item_id': 'str',
        'order_id': 'str',
        'sub_id': 'str',
        'transaction_dts_begin': 'str',
        'transaction_dts_end': 'str'
    }

    attribute_map = {
        'affiliate_oid': 'affiliate_oid',
        'item_id': 'item_id',
        'order_id': 'order_id',
        'sub_id': 'sub_id',
        'transaction_dts_begin': 'transaction_dts_begin',
        'transaction_dts_end': 'transaction_dts_end'
    }

    def __init__(self, affiliate_oid=None, item_id=None, order_id=None, sub_id=None, transaction_dts_begin=None, transaction_dts_end=None):
        """
        AffiliateLedgerQuery - a model defined in Swagger
        """

        self._affiliate_oid = None
        self._item_id = None
        self._order_id = None
        self._sub_id = None
        self._transaction_dts_begin = None
        self._transaction_dts_end = None
        self.discriminator = None

        if affiliate_oid is not None:
          self.affiliate_oid = affiliate_oid
        if item_id is not None:
          self.item_id = item_id
        if order_id is not None:
          self.order_id = order_id
        if sub_id is not None:
          self.sub_id = sub_id
        if transaction_dts_begin is not None:
          self.transaction_dts_begin = transaction_dts_begin
        if transaction_dts_end is not None:
          self.transaction_dts_end = transaction_dts_end

    @property
    def affiliate_oid(self):
        """
        Gets the affiliate_oid of this AffiliateLedgerQuery.
        Affiliate ID associated with the ledger

        :return: The affiliate_oid of this AffiliateLedgerQuery.
        :rtype: int
        """
        return self._affiliate_oid

    @affiliate_oid.setter
    def affiliate_oid(self, affiliate_oid):
        """
        Sets the affiliate_oid of this AffiliateLedgerQuery.
        Affiliate ID associated with the ledger

        :param affiliate_oid: The affiliate_oid of this AffiliateLedgerQuery.
        :type: int
        """

        self._affiliate_oid = affiliate_oid

    @property
    def item_id(self):
        """
        Gets the item_id of this AffiliateLedgerQuery.
        Item id associated with the ledger entry

        :return: The item_id of this AffiliateLedgerQuery.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this AffiliateLedgerQuery.
        Item id associated with the ledger entry

        :param item_id: The item_id of this AffiliateLedgerQuery.
        :type: str
        """

        self._item_id = item_id

    @property
    def order_id(self):
        """
        Gets the order_id of this AffiliateLedgerQuery.
        Order ID associated with the ledger entries

        :return: The order_id of this AffiliateLedgerQuery.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this AffiliateLedgerQuery.
        Order ID associated with the ledger entries

        :param order_id: The order_id of this AffiliateLedgerQuery.
        :type: str
        """

        self._order_id = order_id

    @property
    def sub_id(self):
        """
        Gets the sub_id of this AffiliateLedgerQuery.
        Sub ID value passed on the click that generated the ledger

        :return: The sub_id of this AffiliateLedgerQuery.
        :rtype: str
        """
        return self._sub_id

    @sub_id.setter
    def sub_id(self, sub_id):
        """
        Sets the sub_id of this AffiliateLedgerQuery.
        Sub ID value passed on the click that generated the ledger

        :param sub_id: The sub_id of this AffiliateLedgerQuery.
        :type: str
        """

        self._sub_id = sub_id

    @property
    def transaction_dts_begin(self):
        """
        Gets the transaction_dts_begin of this AffiliateLedgerQuery.
        Minimum transaction date/time to return

        :return: The transaction_dts_begin of this AffiliateLedgerQuery.
        :rtype: str
        """
        return self._transaction_dts_begin

    @transaction_dts_begin.setter
    def transaction_dts_begin(self, transaction_dts_begin):
        """
        Sets the transaction_dts_begin of this AffiliateLedgerQuery.
        Minimum transaction date/time to return

        :param transaction_dts_begin: The transaction_dts_begin of this AffiliateLedgerQuery.
        :type: str
        """

        self._transaction_dts_begin = transaction_dts_begin

    @property
    def transaction_dts_end(self):
        """
        Gets the transaction_dts_end of this AffiliateLedgerQuery.
        Maximum transaction date/time to return

        :return: The transaction_dts_end of this AffiliateLedgerQuery.
        :rtype: str
        """
        return self._transaction_dts_end

    @transaction_dts_end.setter
    def transaction_dts_end(self, transaction_dts_end):
        """
        Sets the transaction_dts_end of this AffiliateLedgerQuery.
        Maximum transaction date/time to return

        :param transaction_dts_end: The transaction_dts_end of this AffiliateLedgerQuery.
        :type: str
        """

        self._transaction_dts_end = transaction_dts_end

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
        if not isinstance(other, AffiliateLedgerQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
