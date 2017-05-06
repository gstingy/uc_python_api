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


class ItemContentMultimedia(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cloud_url=None, cloud_url_expiration=None, code=None, description=None, exclude_from_gallery=None, file_name=None, height=None, merchant_item_multimedia_oid=None, orphan=None, placeholder=None, temp_multimedia_oid=None, thumbnails=None, type=None, url=None, width=None):
        """
        ItemContentMultimedia - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cloud_url': 'str',
            'cloud_url_expiration': 'str',
            'code': 'str',
            'description': 'str',
            'exclude_from_gallery': 'bool',
            'file_name': 'str',
            'height': 'int',
            'merchant_item_multimedia_oid': 'int',
            'orphan': 'bool',
            'placeholder': 'bool',
            'temp_multimedia_oid': 'int',
            'thumbnails': 'list[ItemContentMultimediaThumbnail]',
            'type': 'str',
            'url': 'str',
            'width': 'int'
        }

        self.attribute_map = {
            'cloud_url': 'cloud_url',
            'cloud_url_expiration': 'cloud_url_expiration',
            'code': 'code',
            'description': 'description',
            'exclude_from_gallery': 'exclude_from_gallery',
            'file_name': 'file_name',
            'height': 'height',
            'merchant_item_multimedia_oid': 'merchant_item_multimedia_oid',
            'orphan': 'orphan',
            'placeholder': 'placeholder',
            'temp_multimedia_oid': 'temp_multimedia_oid',
            'thumbnails': 'thumbnails',
            'type': 'type',
            'url': 'url',
            'width': 'width'
        }

        self._cloud_url = cloud_url
        self._cloud_url_expiration = cloud_url_expiration
        self._code = code
        self._description = description
        self._exclude_from_gallery = exclude_from_gallery
        self._file_name = file_name
        self._height = height
        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid
        self._orphan = orphan
        self._placeholder = placeholder
        self._temp_multimedia_oid = temp_multimedia_oid
        self._thumbnails = thumbnails
        self._type = type
        self._url = url
        self._width = width

    @property
    def cloud_url(self):
        """
        Gets the cloud_url of this ItemContentMultimedia.
        URL where the image can be downloaded from the cloud

        :return: The cloud_url of this ItemContentMultimedia.
        :rtype: str
        """
        return self._cloud_url

    @cloud_url.setter
    def cloud_url(self, cloud_url):
        """
        Sets the cloud_url of this ItemContentMultimedia.
        URL where the image can be downloaded from the cloud

        :param cloud_url: The cloud_url of this ItemContentMultimedia.
        :type: str
        """

        self._cloud_url = cloud_url

    @property
    def cloud_url_expiration(self):
        """
        Gets the cloud_url_expiration of this ItemContentMultimedia.
        Expiration date of the cloud URL

        :return: The cloud_url_expiration of this ItemContentMultimedia.
        :rtype: str
        """
        return self._cloud_url_expiration

    @cloud_url_expiration.setter
    def cloud_url_expiration(self, cloud_url_expiration):
        """
        Sets the cloud_url_expiration of this ItemContentMultimedia.
        Expiration date of the cloud URL

        :param cloud_url_expiration: The cloud_url_expiration of this ItemContentMultimedia.
        :type: str
        """

        self._cloud_url_expiration = cloud_url_expiration

    @property
    def code(self):
        """
        Gets the code of this ItemContentMultimedia.
        Code assigned to the file

        :return: The code of this ItemContentMultimedia.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ItemContentMultimedia.
        Code assigned to the file

        :param code: The code of this ItemContentMultimedia.
        :type: str
        """

        if not code:
            raise ValueError("Invalid value for `code`, must not be `None`")
        if len(code) > 20:
            raise ValueError("Invalid value for `code`, length must be less than `20`")

        self._code = code

    @property
    def description(self):
        """
        Gets the description of this ItemContentMultimedia.
        Description

        :return: The description of this ItemContentMultimedia.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ItemContentMultimedia.
        Description

        :param description: The description of this ItemContentMultimedia.
        :type: str
        """

        if not description:
            raise ValueError("Invalid value for `description`, must not be `None`")
        if len(description) > 50000:
            raise ValueError("Invalid value for `description`, length must be less than `50000`")

        self._description = description

    @property
    def exclude_from_gallery(self):
        """
        Gets the exclude_from_gallery of this ItemContentMultimedia.
        True to exclude from multimedia gallery

        :return: The exclude_from_gallery of this ItemContentMultimedia.
        :rtype: bool
        """
        return self._exclude_from_gallery

    @exclude_from_gallery.setter
    def exclude_from_gallery(self, exclude_from_gallery):
        """
        Sets the exclude_from_gallery of this ItemContentMultimedia.
        True to exclude from multimedia gallery

        :param exclude_from_gallery: The exclude_from_gallery of this ItemContentMultimedia.
        :type: bool
        """

        self._exclude_from_gallery = exclude_from_gallery

    @property
    def file_name(self):
        """
        Gets the file_name of this ItemContentMultimedia.
        File name

        :return: The file_name of this ItemContentMultimedia.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this ItemContentMultimedia.
        File name

        :param file_name: The file_name of this ItemContentMultimedia.
        :type: str
        """

        if not file_name:
            raise ValueError("Invalid value for `file_name`, must not be `None`")
        if len(file_name) > 75:
            raise ValueError("Invalid value for `file_name`, length must be less than `75`")

        self._file_name = file_name

    @property
    def height(self):
        """
        Gets the height of this ItemContentMultimedia.
        Height of the image

        :return: The height of this ItemContentMultimedia.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ItemContentMultimedia.
        Height of the image

        :param height: The height of this ItemContentMultimedia.
        :type: int
        """

        self._height = height

    @property
    def merchant_item_multimedia_oid(self):
        """
        Gets the merchant_item_multimedia_oid of this ItemContentMultimedia.
        Item multimedia object identifier

        :return: The merchant_item_multimedia_oid of this ItemContentMultimedia.
        :rtype: int
        """
        return self._merchant_item_multimedia_oid

    @merchant_item_multimedia_oid.setter
    def merchant_item_multimedia_oid(self, merchant_item_multimedia_oid):
        """
        Sets the merchant_item_multimedia_oid of this ItemContentMultimedia.
        Item multimedia object identifier

        :param merchant_item_multimedia_oid: The merchant_item_multimedia_oid of this ItemContentMultimedia.
        :type: int
        """

        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid

    @property
    def orphan(self):
        """
        Gets the orphan of this ItemContentMultimedia.
        True if the multimedia is an orphan of the active StoreFront themes

        :return: The orphan of this ItemContentMultimedia.
        :rtype: bool
        """
        return self._orphan

    @orphan.setter
    def orphan(self, orphan):
        """
        Sets the orphan of this ItemContentMultimedia.
        True if the multimedia is an orphan of the active StoreFront themes

        :param orphan: The orphan of this ItemContentMultimedia.
        :type: bool
        """

        self._orphan = orphan

    @property
    def placeholder(self):
        """
        Gets the placeholder of this ItemContentMultimedia.
        True if the object is a place holder that can be populated

        :return: The placeholder of this ItemContentMultimedia.
        :rtype: bool
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """
        Sets the placeholder of this ItemContentMultimedia.
        True if the object is a place holder that can be populated

        :param placeholder: The placeholder of this ItemContentMultimedia.
        :type: bool
        """

        self._placeholder = placeholder

    @property
    def temp_multimedia_oid(self):
        """
        Gets the temp_multimedia_oid of this ItemContentMultimedia.
        Temporary multimedia object identifier assigned if uploading new multimedia

        :return: The temp_multimedia_oid of this ItemContentMultimedia.
        :rtype: int
        """
        return self._temp_multimedia_oid

    @temp_multimedia_oid.setter
    def temp_multimedia_oid(self, temp_multimedia_oid):
        """
        Sets the temp_multimedia_oid of this ItemContentMultimedia.
        Temporary multimedia object identifier assigned if uploading new multimedia

        :param temp_multimedia_oid: The temp_multimedia_oid of this ItemContentMultimedia.
        :type: int
        """

        self._temp_multimedia_oid = temp_multimedia_oid

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this ItemContentMultimedia.
        Thumbnails of this image

        :return: The thumbnails of this ItemContentMultimedia.
        :rtype: list[ItemContentMultimediaThumbnail]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this ItemContentMultimedia.
        Thumbnails of this image

        :param thumbnails: The thumbnails of this ItemContentMultimedia.
        :type: list[ItemContentMultimediaThumbnail]
        """

        self._thumbnails = thumbnails

    @property
    def type(self):
        """
        Gets the type of this ItemContentMultimedia.
        Type of file

        :return: The type of this ItemContentMultimedia.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemContentMultimedia.
        Type of file

        :param type: The type of this ItemContentMultimedia.
        :type: str
        """
        allowed_values = ["Image", "PDF", "Text", "Unknown", "Video"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def url(self):
        """
        Gets the url of this ItemContentMultimedia.
        URL to download file

        :return: The url of this ItemContentMultimedia.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ItemContentMultimedia.
        URL to download file

        :param url: The url of this ItemContentMultimedia.
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """
        Gets the width of this ItemContentMultimedia.
        Width of the image

        :return: The width of this ItemContentMultimedia.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ItemContentMultimedia.
        Width of the image

        :param width: The width of this ItemContentMultimedia.
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