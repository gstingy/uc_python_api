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


class AffiliateClicksResponse(object):
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
        'clicks': 'list[AffiliateClick]',
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'success': 'bool'
    }

    attribute_map = {
        'clicks': 'clicks',
        'error': 'error',
        'metadata': 'metadata',
        'success': 'success'
    }

    def __init__(self, clicks=None, error=None, metadata=None, success=None):
        """
        AffiliateClicksResponse - a model defined in Swagger
        """

        self._clicks = None
        self._error = None
        self._metadata = None
        self._success = None
        self.discriminator = None

        if clicks is not None:
          self.clicks = clicks
        if error is not None:
          self.error = error
        if metadata is not None:
          self.metadata = metadata
        if success is not None:
          self.success = success

    @property
    def clicks(self):
        """
        Gets the clicks of this AffiliateClicksResponse.
        clicks

        :return: The clicks of this AffiliateClicksResponse.
        :rtype: list[AffiliateClick]
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """
        Sets the clicks of this AffiliateClicksResponse.
        clicks

        :param clicks: The clicks of this AffiliateClicksResponse.
        :type: list[AffiliateClick]
        """

        self._clicks = clicks

    @property
    def error(self):
        """
        Gets the error of this AffiliateClicksResponse.

        :return: The error of this AffiliateClicksResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this AffiliateClicksResponse.

        :param error: The error of this AffiliateClicksResponse.
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """
        Gets the metadata of this AffiliateClicksResponse.

        :return: The metadata of this AffiliateClicksResponse.
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this AffiliateClicksResponse.

        :param metadata: The metadata of this AffiliateClicksResponse.
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """
        Gets the success of this AffiliateClicksResponse.
        Indicates if API call was successful

        :return: The success of this AffiliateClicksResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this AffiliateClicksResponse.
        Indicates if API call was successful

        :param success: The success of this AffiliateClicksResponse.
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
        if not isinstance(other, AffiliateClicksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other