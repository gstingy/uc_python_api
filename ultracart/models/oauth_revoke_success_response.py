# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class OauthRevokeSuccessResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message=None, successful=None):
        """
        OauthRevokeSuccessResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'successful': 'bool'
        }

        self.attribute_map = {
            'message': 'message',
            'successful': 'successful'
        }

        self._message = message
        self._successful = successful

    @property
    def message(self):
        """
        Gets the message of this OauthRevokeSuccessResponse.
        Message confirming revocation of credentials

        :return: The message of this OauthRevokeSuccessResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this OauthRevokeSuccessResponse.
        Message confirming revocation of credentials

        :param message: The message of this OauthRevokeSuccessResponse.
        :type: str
        """

        self._message = message

    @property
    def successful(self):
        """
        Gets the successful of this OauthRevokeSuccessResponse.
        True if revoke was successful

        :return: The successful of this OauthRevokeSuccessResponse.
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this OauthRevokeSuccessResponse.
        True if revoke was successful

        :param successful: The successful of this OauthRevokeSuccessResponse.
        :type: bool
        """

        self._successful = successful

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
