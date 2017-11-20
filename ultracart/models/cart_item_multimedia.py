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


class CartItemMultimedia(object):
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
        'code': 'str',
        'description': 'str',
        'exclude_from_gallery': 'bool',
        'image_height': 'int',
        'image_width': 'int',
        'is_default': 'bool',
        'thumbnails': 'list[CartItemMultimediaThumbnail]',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'exclude_from_gallery': 'exclude_from_gallery',
        'image_height': 'image_height',
        'image_width': 'image_width',
        'is_default': 'is_default',
        'thumbnails': 'thumbnails',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, code=None, description=None, exclude_from_gallery=None, image_height=None, image_width=None, is_default=None, thumbnails=None, type=None, url=None):
        """
        CartItemMultimedia - a model defined in Swagger
        """

        self._code = None
        self._description = None
        self._exclude_from_gallery = None
        self._image_height = None
        self._image_width = None
        self._is_default = None
        self._thumbnails = None
        self._type = None
        self._url = None
        self.discriminator = None

        if code is not None:
          self.code = code
        if description is not None:
          self.description = description
        if exclude_from_gallery is not None:
          self.exclude_from_gallery = exclude_from_gallery
        if image_height is not None:
          self.image_height = image_height
        if image_width is not None:
          self.image_width = image_width
        if is_default is not None:
          self.is_default = is_default
        if thumbnails is not None:
          self.thumbnails = thumbnails
        if type is not None:
          self.type = type
        if url is not None:
          self.url = url

    @property
    def code(self):
        """
        Gets the code of this CartItemMultimedia.
        Code assigned to the multimedia

        :return: The code of this CartItemMultimedia.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CartItemMultimedia.
        Code assigned to the multimedia

        :param code: The code of this CartItemMultimedia.
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """
        Gets the description of this CartItemMultimedia.
        Description

        :return: The description of this CartItemMultimedia.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CartItemMultimedia.
        Description

        :param description: The description of this CartItemMultimedia.
        :type: str
        """

        self._description = description

    @property
    def exclude_from_gallery(self):
        """
        Gets the exclude_from_gallery of this CartItemMultimedia.
        True if the image should be excluded from galleries

        :return: The exclude_from_gallery of this CartItemMultimedia.
        :rtype: bool
        """
        return self._exclude_from_gallery

    @exclude_from_gallery.setter
    def exclude_from_gallery(self, exclude_from_gallery):
        """
        Sets the exclude_from_gallery of this CartItemMultimedia.
        True if the image should be excluded from galleries

        :param exclude_from_gallery: The exclude_from_gallery of this CartItemMultimedia.
        :type: bool
        """

        self._exclude_from_gallery = exclude_from_gallery

    @property
    def image_height(self):
        """
        Gets the image_height of this CartItemMultimedia.
        Image height

        :return: The image_height of this CartItemMultimedia.
        :rtype: int
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """
        Sets the image_height of this CartItemMultimedia.
        Image height

        :param image_height: The image_height of this CartItemMultimedia.
        :type: int
        """

        self._image_height = image_height

    @property
    def image_width(self):
        """
        Gets the image_width of this CartItemMultimedia.
        Image width

        :return: The image_width of this CartItemMultimedia.
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """
        Sets the image_width of this CartItemMultimedia.
        Image width

        :param image_width: The image_width of this CartItemMultimedia.
        :type: int
        """

        self._image_width = image_width

    @property
    def is_default(self):
        """
        Gets the is_default of this CartItemMultimedia.
        True if the multimedia is the default for this type

        :return: The is_default of this CartItemMultimedia.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this CartItemMultimedia.
        True if the multimedia is the default for this type

        :param is_default: The is_default of this CartItemMultimedia.
        :type: bool
        """

        self._is_default = is_default

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this CartItemMultimedia.
        Thumbnails of the images

        :return: The thumbnails of this CartItemMultimedia.
        :rtype: list[CartItemMultimediaThumbnail]
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this CartItemMultimedia.
        Thumbnails of the images

        :param thumbnails: The thumbnails of this CartItemMultimedia.
        :type: list[CartItemMultimediaThumbnail]
        """

        self._thumbnails = thumbnails

    @property
    def type(self):
        """
        Gets the type of this CartItemMultimedia.
        Type of multimedia

        :return: The type of this CartItemMultimedia.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CartItemMultimedia.
        Type of multimedia

        :param type: The type of this CartItemMultimedia.
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
        Gets the url of this CartItemMultimedia.
        URL to view multimedia at

        :return: The url of this CartItemMultimedia.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CartItemMultimedia.
        URL to view multimedia at

        :param url: The url of this CartItemMultimedia.
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
        if not isinstance(other, CartItemMultimedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
