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


class ItemEmailNotifications(object):
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
        'skip_receipt': 'bool',
        'skip_shipment_notification': 'bool'
    }

    attribute_map = {
        'skip_receipt': 'skip_receipt',
        'skip_shipment_notification': 'skip_shipment_notification'
    }

    def __init__(self, skip_receipt=None, skip_shipment_notification=None):
        """
        ItemEmailNotifications - a model defined in Swagger
        """

        self._skip_receipt = None
        self._skip_shipment_notification = None
        self.discriminator = None

        if skip_receipt is not None:
          self.skip_receipt = skip_receipt
        if skip_shipment_notification is not None:
          self.skip_shipment_notification = skip_shipment_notification

    @property
    def skip_receipt(self):
        """
        Gets the skip_receipt of this ItemEmailNotifications.
        Skip receipt email to customer

        :return: The skip_receipt of this ItemEmailNotifications.
        :rtype: bool
        """
        return self._skip_receipt

    @skip_receipt.setter
    def skip_receipt(self, skip_receipt):
        """
        Sets the skip_receipt of this ItemEmailNotifications.
        Skip receipt email to customer

        :param skip_receipt: The skip_receipt of this ItemEmailNotifications.
        :type: bool
        """

        self._skip_receipt = skip_receipt

    @property
    def skip_shipment_notification(self):
        """
        Gets the skip_shipment_notification of this ItemEmailNotifications.
        Skip shipment notification to customer

        :return: The skip_shipment_notification of this ItemEmailNotifications.
        :rtype: bool
        """
        return self._skip_shipment_notification

    @skip_shipment_notification.setter
    def skip_shipment_notification(self, skip_shipment_notification):
        """
        Sets the skip_shipment_notification of this ItemEmailNotifications.
        Skip shipment notification to customer

        :param skip_shipment_notification: The skip_shipment_notification of this ItemEmailNotifications.
        :type: bool
        """

        self._skip_shipment_notification = skip_shipment_notification

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
        if not isinstance(other, ItemEmailNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
