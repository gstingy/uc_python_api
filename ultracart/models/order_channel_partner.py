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


class OrderChannelPartner(object):
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
        'channel_partner_code': 'str',
        'channel_partner_data': 'str',
        'channel_partner_oid': 'int',
        'channel_partner_order_id': 'str'
    }

    attribute_map = {
        'channel_partner_code': 'channel_partner_code',
        'channel_partner_data': 'channel_partner_data',
        'channel_partner_oid': 'channel_partner_oid',
        'channel_partner_order_id': 'channel_partner_order_id'
    }

    def __init__(self, channel_partner_code=None, channel_partner_data=None, channel_partner_oid=None, channel_partner_order_id=None):
        """
        OrderChannelPartner - a model defined in Swagger
        """

        self._channel_partner_code = None
        self._channel_partner_data = None
        self._channel_partner_oid = None
        self._channel_partner_order_id = None
        self.discriminator = None

        if channel_partner_code is not None:
          self.channel_partner_code = channel_partner_code
        if channel_partner_data is not None:
          self.channel_partner_data = channel_partner_data
        if channel_partner_oid is not None:
          self.channel_partner_oid = channel_partner_oid
        if channel_partner_order_id is not None:
          self.channel_partner_order_id = channel_partner_order_id

    @property
    def channel_partner_code(self):
        """
        Gets the channel_partner_code of this OrderChannelPartner.
        The code of the channel partner

        :return: The channel_partner_code of this OrderChannelPartner.
        :rtype: str
        """
        return self._channel_partner_code

    @channel_partner_code.setter
    def channel_partner_code(self, channel_partner_code):
        """
        Sets the channel_partner_code of this OrderChannelPartner.
        The code of the channel partner

        :param channel_partner_code: The channel_partner_code of this OrderChannelPartner.
        :type: str
        """

        self._channel_partner_code = channel_partner_code

    @property
    def channel_partner_data(self):
        """
        Gets the channel_partner_data of this OrderChannelPartner.
        Additional data provided by the channel partner

        :return: The channel_partner_data of this OrderChannelPartner.
        :rtype: str
        """
        return self._channel_partner_data

    @channel_partner_data.setter
    def channel_partner_data(self, channel_partner_data):
        """
        Sets the channel_partner_data of this OrderChannelPartner.
        Additional data provided by the channel partner

        :param channel_partner_data: The channel_partner_data of this OrderChannelPartner.
        :type: str
        """

        self._channel_partner_data = channel_partner_data

    @property
    def channel_partner_oid(self):
        """
        Gets the channel_partner_oid of this OrderChannelPartner.
        Channel partner object identifier

        :return: The channel_partner_oid of this OrderChannelPartner.
        :rtype: int
        """
        return self._channel_partner_oid

    @channel_partner_oid.setter
    def channel_partner_oid(self, channel_partner_oid):
        """
        Sets the channel_partner_oid of this OrderChannelPartner.
        Channel partner object identifier

        :param channel_partner_oid: The channel_partner_oid of this OrderChannelPartner.
        :type: int
        """

        self._channel_partner_oid = channel_partner_oid

    @property
    def channel_partner_order_id(self):
        """
        Gets the channel_partner_order_id of this OrderChannelPartner.
        The order ID assigned by the channel partner for this order

        :return: The channel_partner_order_id of this OrderChannelPartner.
        :rtype: str
        """
        return self._channel_partner_order_id

    @channel_partner_order_id.setter
    def channel_partner_order_id(self, channel_partner_order_id):
        """
        Sets the channel_partner_order_id of this OrderChannelPartner.
        The order ID assigned by the channel partner for this order

        :param channel_partner_order_id: The channel_partner_order_id of this OrderChannelPartner.
        :type: str
        """

        self._channel_partner_order_id = channel_partner_order_id

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
        if not isinstance(other, OrderChannelPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
