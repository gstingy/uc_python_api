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


class WebhookLogSummariesResponse(object):
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
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'success': 'bool',
        'webhook_log_summaries': 'list[WebhookLogSummary]'
    }

    attribute_map = {
        'error': 'error',
        'metadata': 'metadata',
        'success': 'success',
        'webhook_log_summaries': 'webhook_log_summaries'
    }

    def __init__(self, error=None, metadata=None, success=None, webhook_log_summaries=None):
        """
        WebhookLogSummariesResponse - a model defined in Swagger
        """

        self._error = None
        self._metadata = None
        self._success = None
        self._webhook_log_summaries = None
        self.discriminator = None

        if error is not None:
          self.error = error
        if metadata is not None:
          self.metadata = metadata
        if success is not None:
          self.success = success
        if webhook_log_summaries is not None:
          self.webhook_log_summaries = webhook_log_summaries

    @property
    def error(self):
        """
        Gets the error of this WebhookLogSummariesResponse.

        :return: The error of this WebhookLogSummariesResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this WebhookLogSummariesResponse.

        :param error: The error of this WebhookLogSummariesResponse.
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """
        Gets the metadata of this WebhookLogSummariesResponse.

        :return: The metadata of this WebhookLogSummariesResponse.
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this WebhookLogSummariesResponse.

        :param metadata: The metadata of this WebhookLogSummariesResponse.
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """
        Gets the success of this WebhookLogSummariesResponse.
        Indicates if API call was successful

        :return: The success of this WebhookLogSummariesResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this WebhookLogSummariesResponse.
        Indicates if API call was successful

        :param success: The success of this WebhookLogSummariesResponse.
        :type: bool
        """

        self._success = success

    @property
    def webhook_log_summaries(self):
        """
        Gets the webhook_log_summaries of this WebhookLogSummariesResponse.
        Webhook log summaries

        :return: The webhook_log_summaries of this WebhookLogSummariesResponse.
        :rtype: list[WebhookLogSummary]
        """
        return self._webhook_log_summaries

    @webhook_log_summaries.setter
    def webhook_log_summaries(self, webhook_log_summaries):
        """
        Sets the webhook_log_summaries of this WebhookLogSummariesResponse.
        Webhook log summaries

        :param webhook_log_summaries: The webhook_log_summaries of this WebhookLogSummariesResponse.
        :type: list[WebhookLogSummary]
        """

        self._webhook_log_summaries = webhook_log_summaries

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
        if not isinstance(other, WebhookLogSummariesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
