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


class WebhookLogSummary(object):
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
        'delivery_dts': 'str',
        'request_id': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'delivery_dts': 'delivery_dts',
        'request_id': 'request_id',
        'success': 'success'
    }

    def __init__(self, delivery_dts=None, request_id=None, success=None):
        """
        WebhookLogSummary - a model defined in Swagger
        """

        self._delivery_dts = None
        self._request_id = None
        self._success = None
        self.discriminator = None

        if delivery_dts is not None:
          self.delivery_dts = delivery_dts
        if request_id is not None:
          self.request_id = request_id
        if success is not None:
          self.success = success

    @property
    def delivery_dts(self):
        """
        Gets the delivery_dts of this WebhookLogSummary.
        Date/time of the delivery

        :return: The delivery_dts of this WebhookLogSummary.
        :rtype: str
        """
        return self._delivery_dts

    @delivery_dts.setter
    def delivery_dts(self, delivery_dts):
        """
        Sets the delivery_dts of this WebhookLogSummary.
        Date/time of the delivery

        :param delivery_dts: The delivery_dts of this WebhookLogSummary.
        :type: str
        """

        self._delivery_dts = delivery_dts

    @property
    def request_id(self):
        """
        Gets the request_id of this WebhookLogSummary.
        Request id

        :return: The request_id of this WebhookLogSummary.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this WebhookLogSummary.
        Request id

        :param request_id: The request_id of this WebhookLogSummary.
        :type: str
        """

        self._request_id = request_id

    @property
    def success(self):
        """
        Gets the success of this WebhookLogSummary.
        True if the notification was successful

        :return: The success of this WebhookLogSummary.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this WebhookLogSummary.
        True if the notification was successful

        :param success: The success of this WebhookLogSummary.
        :type: bool
        """

        self._success = success

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
        if not isinstance(other, WebhookLogSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
