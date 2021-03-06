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


class ItemReviews(object):
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
        'has_approved_review': 'bool',
        'has_review': 'bool',
        'review_count': 'int',
        'review_overall': 'float',
        'review_template_name': 'str',
        'review_template_oid': 'int',
        'reviewable': 'bool'
    }

    attribute_map = {
        'has_approved_review': 'has_approved_review',
        'has_review': 'has_review',
        'review_count': 'review_count',
        'review_overall': 'review_overall',
        'review_template_name': 'review_template_name',
        'review_template_oid': 'review_template_oid',
        'reviewable': 'reviewable'
    }

    def __init__(self, has_approved_review=None, has_review=None, review_count=None, review_overall=None, review_template_name=None, review_template_oid=None, reviewable=None):
        """
        ItemReviews - a model defined in Swagger
        """

        self._has_approved_review = None
        self._has_review = None
        self._review_count = None
        self._review_overall = None
        self._review_template_name = None
        self._review_template_oid = None
        self._reviewable = None
        self.discriminator = None

        if has_approved_review is not None:
          self.has_approved_review = has_approved_review
        if has_review is not None:
          self.has_review = has_review
        if review_count is not None:
          self.review_count = review_count
        if review_overall is not None:
          self.review_overall = review_overall
        if review_template_name is not None:
          self.review_template_name = review_template_name
        if review_template_oid is not None:
          self.review_template_oid = review_template_oid
        if reviewable is not None:
          self.reviewable = reviewable

    @property
    def has_approved_review(self):
        """
        Gets the has_approved_review of this ItemReviews.
        True if the item has an approved review

        :return: The has_approved_review of this ItemReviews.
        :rtype: bool
        """
        return self._has_approved_review

    @has_approved_review.setter
    def has_approved_review(self, has_approved_review):
        """
        Sets the has_approved_review of this ItemReviews.
        True if the item has an approved review

        :param has_approved_review: The has_approved_review of this ItemReviews.
        :type: bool
        """

        self._has_approved_review = has_approved_review

    @property
    def has_review(self):
        """
        Gets the has_review of this ItemReviews.
        True if the item has a review

        :return: The has_review of this ItemReviews.
        :rtype: bool
        """
        return self._has_review

    @has_review.setter
    def has_review(self, has_review):
        """
        Sets the has_review of this ItemReviews.
        True if the item has a review

        :param has_review: The has_review of this ItemReviews.
        :type: bool
        """

        self._has_review = has_review

    @property
    def review_count(self):
        """
        Gets the review_count of this ItemReviews.
        Number of approved reviews

        :return: The review_count of this ItemReviews.
        :rtype: int
        """
        return self._review_count

    @review_count.setter
    def review_count(self, review_count):
        """
        Sets the review_count of this ItemReviews.
        Number of approved reviews

        :param review_count: The review_count of this ItemReviews.
        :type: int
        """

        self._review_count = review_count

    @property
    def review_overall(self):
        """
        Gets the review_overall of this ItemReviews.
        Overall score of reviews

        :return: The review_overall of this ItemReviews.
        :rtype: float
        """
        return self._review_overall

    @review_overall.setter
    def review_overall(self, review_overall):
        """
        Sets the review_overall of this ItemReviews.
        Overall score of reviews

        :param review_overall: The review_overall of this ItemReviews.
        :type: float
        """

        self._review_overall = review_overall

    @property
    def review_template_name(self):
        """
        Gets the review_template_name of this ItemReviews.
        Review template name

        :return: The review_template_name of this ItemReviews.
        :rtype: str
        """
        return self._review_template_name

    @review_template_name.setter
    def review_template_name(self, review_template_name):
        """
        Sets the review_template_name of this ItemReviews.
        Review template name

        :param review_template_name: The review_template_name of this ItemReviews.
        :type: str
        """

        self._review_template_name = review_template_name

    @property
    def review_template_oid(self):
        """
        Gets the review_template_oid of this ItemReviews.
        Review template object identifier

        :return: The review_template_oid of this ItemReviews.
        :rtype: int
        """
        return self._review_template_oid

    @review_template_oid.setter
    def review_template_oid(self, review_template_oid):
        """
        Sets the review_template_oid of this ItemReviews.
        Review template object identifier

        :param review_template_oid: The review_template_oid of this ItemReviews.
        :type: int
        """

        self._review_template_oid = review_template_oid

    @property
    def reviewable(self):
        """
        Gets the reviewable of this ItemReviews.
        True if the item is reviewable

        :return: The reviewable of this ItemReviews.
        :rtype: bool
        """
        return self._reviewable

    @reviewable.setter
    def reviewable(self, reviewable):
        """
        Sets the reviewable of this ItemReviews.
        True if the item is reviewable

        :param reviewable: The reviewable of this ItemReviews.
        :type: bool
        """

        self._reviewable = reviewable

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
        if not isinstance(other, ItemReviews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
