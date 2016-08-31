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


class ItemInstantPaymentNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, post_operation=None, successful_response_text=None, url=None):
        """
        ItemInstantPaymentNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'post_operation': 'bool',
            'successful_response_text': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'post_operation': 'post_operation',
            'successful_response_text': 'successful_response_text',
            'url': 'url'
        }

        self._post_operation = post_operation
        self._successful_response_text = successful_response_text
        self._url = url

    @property
    def post_operation(self):
        """
        Gets the post_operation of this ItemInstantPaymentNotification.


        :return: The post_operation of this ItemInstantPaymentNotification.
        :rtype: bool
        """
        return self._post_operation

    @post_operation.setter
    def post_operation(self, post_operation):
        """
        Sets the post_operation of this ItemInstantPaymentNotification.


        :param post_operation: The post_operation of this ItemInstantPaymentNotification.
        :type: bool
        """

        self._post_operation = post_operation

    @property
    def successful_response_text(self):
        """
        Gets the successful_response_text of this ItemInstantPaymentNotification.


        :return: The successful_response_text of this ItemInstantPaymentNotification.
        :rtype: str
        """
        return self._successful_response_text

    @successful_response_text.setter
    def successful_response_text(self, successful_response_text):
        """
        Sets the successful_response_text of this ItemInstantPaymentNotification.


        :param successful_response_text: The successful_response_text of this ItemInstantPaymentNotification.
        :type: str
        """

        self._successful_response_text = successful_response_text

    @property
    def url(self):
        """
        Gets the url of this ItemInstantPaymentNotification.


        :return: The url of this ItemInstantPaymentNotification.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ItemInstantPaymentNotification.


        :param url: The url of this ItemInstantPaymentNotification.
        :type: str
        """

        self._url = url

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