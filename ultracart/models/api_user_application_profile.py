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


class ApiUserApplicationProfile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_application_logo_url=None, application_description=None, application_name=None, developer_name=None, developer_website=None):
        """
        ApiUserApplicationProfile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_application_logo_url': 'str',
            'application_description': 'str',
            'application_name': 'str',
            'developer_name': 'str',
            'developer_website': 'str'
        }

        self.attribute_map = {
            'api_application_logo_url': 'api_application_logo_url',
            'application_description': 'application_description',
            'application_name': 'application_name',
            'developer_name': 'developer_name',
            'developer_website': 'developer_website'
        }

        self._api_application_logo_url = api_application_logo_url
        self._application_description = application_description
        self._application_name = application_name
        self._developer_name = developer_name
        self._developer_website = developer_website

    @property
    def api_application_logo_url(self):
        """
        Gets the api_application_logo_url of this ApiUserApplicationProfile.
        Application logo URL

        :return: The api_application_logo_url of this ApiUserApplicationProfile.
        :rtype: str
        """
        return self._api_application_logo_url

    @api_application_logo_url.setter
    def api_application_logo_url(self, api_application_logo_url):
        """
        Sets the api_application_logo_url of this ApiUserApplicationProfile.
        Application logo URL

        :param api_application_logo_url: The api_application_logo_url of this ApiUserApplicationProfile.
        :type: str
        """

        self._api_application_logo_url = api_application_logo_url

    @property
    def application_description(self):
        """
        Gets the application_description of this ApiUserApplicationProfile.
        Application description

        :return: The application_description of this ApiUserApplicationProfile.
        :rtype: str
        """
        return self._application_description

    @application_description.setter
    def application_description(self, application_description):
        """
        Sets the application_description of this ApiUserApplicationProfile.
        Application description

        :param application_description: The application_description of this ApiUserApplicationProfile.
        :type: str
        """

        self._application_description = application_description

    @property
    def application_name(self):
        """
        Gets the application_name of this ApiUserApplicationProfile.
        Application name

        :return: The application_name of this ApiUserApplicationProfile.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this ApiUserApplicationProfile.
        Application name

        :param application_name: The application_name of this ApiUserApplicationProfile.
        :type: str
        """

        self._application_name = application_name

    @property
    def developer_name(self):
        """
        Gets the developer_name of this ApiUserApplicationProfile.
        Developer name

        :return: The developer_name of this ApiUserApplicationProfile.
        :rtype: str
        """
        return self._developer_name

    @developer_name.setter
    def developer_name(self, developer_name):
        """
        Sets the developer_name of this ApiUserApplicationProfile.
        Developer name

        :param developer_name: The developer_name of this ApiUserApplicationProfile.
        :type: str
        """

        self._developer_name = developer_name

    @property
    def developer_website(self):
        """
        Gets the developer_website of this ApiUserApplicationProfile.
        Developer website

        :return: The developer_website of this ApiUserApplicationProfile.
        :rtype: str
        """
        return self._developer_website

    @developer_website.setter
    def developer_website(self, developer_website):
        """
        Sets the developer_website of this ApiUserApplicationProfile.
        Developer website

        :param developer_website: The developer_website of this ApiUserApplicationProfile.
        :type: str
        """

        self._developer_website = developer_website

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
