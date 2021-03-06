# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ItemContentAssignment(object):
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
        'group_oid': 'int',
        'group_path': 'str',
        'host': 'str',
        'sort_order': 'int',
        'url_part': 'str'
    }

    attribute_map = {
        'group_oid': 'group_oid',
        'group_path': 'group_path',
        'host': 'host',
        'sort_order': 'sort_order',
        'url_part': 'url_part'
    }

    def __init__(self, group_oid=None, group_path=None, host=None, sort_order=None, url_part=None):
        """
        ItemContentAssignment - a model defined in Swagger
        """

        self._group_oid = None
        self._group_path = None
        self._host = None
        self._sort_order = None
        self._url_part = None
        self.discriminator = None

        if group_oid is not None:
          self.group_oid = group_oid
        if group_path is not None:
          self.group_path = group_path
        if host is not None:
          self.host = host
        if sort_order is not None:
          self.sort_order = sort_order
        if url_part is not None:
          self.url_part = url_part

    @property
    def group_oid(self):
        """
        Gets the group_oid of this ItemContentAssignment.
        Page (group) object identifier

        :return: The group_oid of this ItemContentAssignment.
        :rtype: int
        """
        return self._group_oid

    @group_oid.setter
    def group_oid(self, group_oid):
        """
        Sets the group_oid of this ItemContentAssignment.
        Page (group) object identifier

        :param group_oid: The group_oid of this ItemContentAssignment.
        :type: int
        """

        self._group_oid = group_oid

    @property
    def group_path(self):
        """
        Gets the group_path of this ItemContentAssignment.
        Page (group) path

        :return: The group_path of this ItemContentAssignment.
        :rtype: str
        """
        return self._group_path

    @group_path.setter
    def group_path(self, group_path):
        """
        Sets the group_path of this ItemContentAssignment.
        Page (group) path

        :param group_path: The group_path of this ItemContentAssignment.
        :type: str
        """

        self._group_path = group_path

    @property
    def host(self):
        """
        Gets the host of this ItemContentAssignment.
        StoreFront host name

        :return: The host of this ItemContentAssignment.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ItemContentAssignment.
        StoreFront host name

        :param host: The host of this ItemContentAssignment.
        :type: str
        """

        self._host = host

    @property
    def sort_order(self):
        """
        Gets the sort_order of this ItemContentAssignment.
        Sort order (optional)

        :return: The sort_order of this ItemContentAssignment.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this ItemContentAssignment.
        Sort order (optional)

        :param sort_order: The sort_order of this ItemContentAssignment.
        :type: int
        """

        self._sort_order = sort_order

    @property
    def url_part(self):
        """
        Gets the url_part of this ItemContentAssignment.
        URL part if the item id is not used

        :return: The url_part of this ItemContentAssignment.
        :rtype: str
        """
        return self._url_part

    @url_part.setter
    def url_part(self, url_part):
        """
        Sets the url_part of this ItemContentAssignment.
        URL part if the item id is not used

        :param url_part: The url_part of this ItemContentAssignment.
        :type: str
        """
        if url_part is not None and len(url_part) > 150:
            raise ValueError("Invalid value for `url_part`, length must be less than or equal to `150`")

        self._url_part = url_part

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
        if not isinstance(other, ItemContentAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
