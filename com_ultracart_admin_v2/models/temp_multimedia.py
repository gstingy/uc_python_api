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


class TempMultimedia(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, filename=None, height=None, multimedia_type=None, size=None, temp_multimedia_oid=None, url=None, width=None):
        """
        TempMultimedia - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'filename': 'str',
            'height': 'int',
            'multimedia_type': 'str',
            'size': 'int',
            'temp_multimedia_oid': 'int',
            'url': 'str',
            'width': 'int'
        }

        self.attribute_map = {
            'filename': 'filename',
            'height': 'height',
            'multimedia_type': 'multimedia_type',
            'size': 'size',
            'temp_multimedia_oid': 'temp_multimedia_oid',
            'url': 'url',
            'width': 'width'
        }

        self._filename = filename
        self._height = height
        self._multimedia_type = multimedia_type
        self._size = size
        self._temp_multimedia_oid = temp_multimedia_oid
        self._url = url
        self._width = width

    @property
    def filename(self):
        """
        Gets the filename of this TempMultimedia.


        :return: The filename of this TempMultimedia.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this TempMultimedia.


        :param filename: The filename of this TempMultimedia.
        :type: str
        """

        self._filename = filename

    @property
    def height(self):
        """
        Gets the height of this TempMultimedia.


        :return: The height of this TempMultimedia.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this TempMultimedia.


        :param height: The height of this TempMultimedia.
        :type: int
        """

        self._height = height

    @property
    def multimedia_type(self):
        """
        Gets the multimedia_type of this TempMultimedia.


        :return: The multimedia_type of this TempMultimedia.
        :rtype: str
        """
        return self._multimedia_type

    @multimedia_type.setter
    def multimedia_type(self, multimedia_type):
        """
        Sets the multimedia_type of this TempMultimedia.


        :param multimedia_type: The multimedia_type of this TempMultimedia.
        :type: str
        """

        self._multimedia_type = multimedia_type

    @property
    def size(self):
        """
        Gets the size of this TempMultimedia.


        :return: The size of this TempMultimedia.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this TempMultimedia.


        :param size: The size of this TempMultimedia.
        :type: int
        """

        self._size = size

    @property
    def temp_multimedia_oid(self):
        """
        Gets the temp_multimedia_oid of this TempMultimedia.


        :return: The temp_multimedia_oid of this TempMultimedia.
        :rtype: int
        """
        return self._temp_multimedia_oid

    @temp_multimedia_oid.setter
    def temp_multimedia_oid(self, temp_multimedia_oid):
        """
        Sets the temp_multimedia_oid of this TempMultimedia.


        :param temp_multimedia_oid: The temp_multimedia_oid of this TempMultimedia.
        :type: int
        """

        self._temp_multimedia_oid = temp_multimedia_oid

    @property
    def url(self):
        """
        Gets the url of this TempMultimedia.


        :return: The url of this TempMultimedia.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this TempMultimedia.


        :param url: The url of this TempMultimedia.
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """
        Gets the width of this TempMultimedia.


        :return: The width of this TempMultimedia.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this TempMultimedia.


        :param width: The width of this TempMultimedia.
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