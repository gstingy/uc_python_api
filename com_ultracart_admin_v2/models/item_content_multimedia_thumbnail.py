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


class ItemContentMultimediaThumbnail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, height=None, http_url=None, https_url=None, png_format=None, square=None, width=None):
        """
        ItemContentMultimediaThumbnail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'height': 'int',
            'http_url': 'str',
            'https_url': 'str',
            'png_format': 'bool',
            'square': 'bool',
            'width': 'int'
        }

        self.attribute_map = {
            'height': 'height',
            'http_url': 'http_url',
            'https_url': 'https_url',
            'png_format': 'png_format',
            'square': 'square',
            'width': 'width'
        }

        self._height = height
        self._http_url = http_url
        self._https_url = https_url
        self._png_format = png_format
        self._square = square
        self._width = width

    @property
    def height(self):
        """
        Gets the height of this ItemContentMultimediaThumbnail.


        :return: The height of this ItemContentMultimediaThumbnail.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ItemContentMultimediaThumbnail.


        :param height: The height of this ItemContentMultimediaThumbnail.
        :type: int
        """

        self._height = height

    @property
    def http_url(self):
        """
        Gets the http_url of this ItemContentMultimediaThumbnail.


        :return: The http_url of this ItemContentMultimediaThumbnail.
        :rtype: str
        """
        return self._http_url

    @http_url.setter
    def http_url(self, http_url):
        """
        Sets the http_url of this ItemContentMultimediaThumbnail.


        :param http_url: The http_url of this ItemContentMultimediaThumbnail.
        :type: str
        """

        self._http_url = http_url

    @property
    def https_url(self):
        """
        Gets the https_url of this ItemContentMultimediaThumbnail.


        :return: The https_url of this ItemContentMultimediaThumbnail.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        """
        Sets the https_url of this ItemContentMultimediaThumbnail.


        :param https_url: The https_url of this ItemContentMultimediaThumbnail.
        :type: str
        """

        self._https_url = https_url

    @property
    def png_format(self):
        """
        Gets the png_format of this ItemContentMultimediaThumbnail.


        :return: The png_format of this ItemContentMultimediaThumbnail.
        :rtype: bool
        """
        return self._png_format

    @png_format.setter
    def png_format(self, png_format):
        """
        Sets the png_format of this ItemContentMultimediaThumbnail.


        :param png_format: The png_format of this ItemContentMultimediaThumbnail.
        :type: bool
        """

        self._png_format = png_format

    @property
    def square(self):
        """
        Gets the square of this ItemContentMultimediaThumbnail.


        :return: The square of this ItemContentMultimediaThumbnail.
        :rtype: bool
        """
        return self._square

    @square.setter
    def square(self, square):
        """
        Sets the square of this ItemContentMultimediaThumbnail.


        :param square: The square of this ItemContentMultimediaThumbnail.
        :type: bool
        """

        self._square = square

    @property
    def width(self):
        """
        Gets the width of this ItemContentMultimediaThumbnail.


        :return: The width of this ItemContentMultimediaThumbnail.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ItemContentMultimediaThumbnail.


        :param width: The width of this ItemContentMultimediaThumbnail.
        :type: int
        """

        self._width = width

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
