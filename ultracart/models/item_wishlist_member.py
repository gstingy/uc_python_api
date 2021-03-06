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


class ItemWishlistMember(object):
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
        'wishlist_member_instance_description': 'str',
        'wishlist_member_instance_oid': 'int',
        'wishlist_member_sku': 'str'
    }

    attribute_map = {
        'wishlist_member_instance_description': 'wishlist_member_instance_description',
        'wishlist_member_instance_oid': 'wishlist_member_instance_oid',
        'wishlist_member_sku': 'wishlist_member_sku'
    }

    def __init__(self, wishlist_member_instance_description=None, wishlist_member_instance_oid=None, wishlist_member_sku=None):
        """
        ItemWishlistMember - a model defined in Swagger
        """

        self._wishlist_member_instance_description = None
        self._wishlist_member_instance_oid = None
        self._wishlist_member_sku = None
        self.discriminator = None

        if wishlist_member_instance_description is not None:
          self.wishlist_member_instance_description = wishlist_member_instance_description
        if wishlist_member_instance_oid is not None:
          self.wishlist_member_instance_oid = wishlist_member_instance_oid
        if wishlist_member_sku is not None:
          self.wishlist_member_sku = wishlist_member_sku

    @property
    def wishlist_member_instance_description(self):
        """
        Gets the wishlist_member_instance_description of this ItemWishlistMember.
        WishList Member instance description

        :return: The wishlist_member_instance_description of this ItemWishlistMember.
        :rtype: str
        """
        return self._wishlist_member_instance_description

    @wishlist_member_instance_description.setter
    def wishlist_member_instance_description(self, wishlist_member_instance_description):
        """
        Sets the wishlist_member_instance_description of this ItemWishlistMember.
        WishList Member instance description

        :param wishlist_member_instance_description: The wishlist_member_instance_description of this ItemWishlistMember.
        :type: str
        """

        self._wishlist_member_instance_description = wishlist_member_instance_description

    @property
    def wishlist_member_instance_oid(self):
        """
        Gets the wishlist_member_instance_oid of this ItemWishlistMember.
        WishList Member instance object identifier

        :return: The wishlist_member_instance_oid of this ItemWishlistMember.
        :rtype: int
        """
        return self._wishlist_member_instance_oid

    @wishlist_member_instance_oid.setter
    def wishlist_member_instance_oid(self, wishlist_member_instance_oid):
        """
        Sets the wishlist_member_instance_oid of this ItemWishlistMember.
        WishList Member instance object identifier

        :param wishlist_member_instance_oid: The wishlist_member_instance_oid of this ItemWishlistMember.
        :type: int
        """

        self._wishlist_member_instance_oid = wishlist_member_instance_oid

    @property
    def wishlist_member_sku(self):
        """
        Gets the wishlist_member_sku of this ItemWishlistMember.
        WishList Member SKU

        :return: The wishlist_member_sku of this ItemWishlistMember.
        :rtype: str
        """
        return self._wishlist_member_sku

    @wishlist_member_sku.setter
    def wishlist_member_sku(self, wishlist_member_sku):
        """
        Sets the wishlist_member_sku of this ItemWishlistMember.
        WishList Member SKU

        :param wishlist_member_sku: The wishlist_member_sku of this ItemWishlistMember.
        :type: str
        """
        if wishlist_member_sku is not None and len(wishlist_member_sku) > 25:
            raise ValueError("Invalid value for `wishlist_member_sku`, length must be less than or equal to `25`")

        self._wishlist_member_sku = wishlist_member_sku

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
        if not isinstance(other, ItemWishlistMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
