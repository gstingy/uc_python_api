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


class WebhookEventSubscription(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, comments=None, deprecated_flag=None, discontinued_flag=None, event_description=None, event_name=None, expansion=None, subscribed=None, webhook_event_oid=None):
        """
        WebhookEventSubscription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'comments': 'str',
            'deprecated_flag': 'bool',
            'discontinued_flag': 'bool',
            'event_description': 'str',
            'event_name': 'str',
            'expansion': 'str',
            'subscribed': 'bool',
            'webhook_event_oid': 'int'
        }

        self.attribute_map = {
            'comments': 'comments',
            'deprecated_flag': 'deprecated_flag',
            'discontinued_flag': 'discontinued_flag',
            'event_description': 'event_description',
            'event_name': 'event_name',
            'expansion': 'expansion',
            'subscribed': 'subscribed',
            'webhook_event_oid': 'webhook_event_oid'
        }

        self._comments = comments
        self._deprecated_flag = deprecated_flag
        self._discontinued_flag = discontinued_flag
        self._event_description = event_description
        self._event_name = event_name
        self._expansion = expansion
        self._subscribed = subscribed
        self._webhook_event_oid = webhook_event_oid

    @property
    def comments(self):
        """
        Gets the comments of this WebhookEventSubscription.
        Comment about the event to provide further clarification to the end user

        :return: The comments of this WebhookEventSubscription.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this WebhookEventSubscription.
        Comment about the event to provide further clarification to the end user

        :param comments: The comments of this WebhookEventSubscription.
        :type: str
        """

        self._comments = comments

    @property
    def deprecated_flag(self):
        """
        Gets the deprecated_flag of this WebhookEventSubscription.
        True if the event is deprecated.  See the API change log for details on when it will be discontinued.

        :return: The deprecated_flag of this WebhookEventSubscription.
        :rtype: bool
        """
        return self._deprecated_flag

    @deprecated_flag.setter
    def deprecated_flag(self, deprecated_flag):
        """
        Sets the deprecated_flag of this WebhookEventSubscription.
        True if the event is deprecated.  See the API change log for details on when it will be discontinued.

        :param deprecated_flag: The deprecated_flag of this WebhookEventSubscription.
        :type: bool
        """

        self._deprecated_flag = deprecated_flag

    @property
    def discontinued_flag(self):
        """
        Gets the discontinued_flag of this WebhookEventSubscription.
        True if the event is discontinued.  See the API change log for details on migration details.

        :return: The discontinued_flag of this WebhookEventSubscription.
        :rtype: bool
        """
        return self._discontinued_flag

    @discontinued_flag.setter
    def discontinued_flag(self, discontinued_flag):
        """
        Sets the discontinued_flag of this WebhookEventSubscription.
        True if the event is discontinued.  See the API change log for details on migration details.

        :param discontinued_flag: The discontinued_flag of this WebhookEventSubscription.
        :type: bool
        """

        self._discontinued_flag = discontinued_flag

    @property
    def event_description(self):
        """
        Gets the event_description of this WebhookEventSubscription.
        Description of the event

        :return: The event_description of this WebhookEventSubscription.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """
        Sets the event_description of this WebhookEventSubscription.
        Description of the event

        :param event_description: The event_description of this WebhookEventSubscription.
        :type: str
        """

        self._event_description = event_description

    @property
    def event_name(self):
        """
        Gets the event_name of this WebhookEventSubscription.
        Event name

        :return: The event_name of this WebhookEventSubscription.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this WebhookEventSubscription.
        Event name

        :param event_name: The event_name of this WebhookEventSubscription.
        :type: str
        """

        self._event_name = event_name

    @property
    def expansion(self):
        """
        Gets the expansion of this WebhookEventSubscription.
        The expand string for the notification object.  See the individual resource _expand documentation for valid values.

        :return: The expansion of this WebhookEventSubscription.
        :rtype: str
        """
        return self._expansion

    @expansion.setter
    def expansion(self, expansion):
        """
        Sets the expansion of this WebhookEventSubscription.
        The expand string for the notification object.  See the individual resource _expand documentation for valid values.

        :param expansion: The expansion of this WebhookEventSubscription.
        :type: str
        """

        self._expansion = expansion

    @property
    def subscribed(self):
        """
        Gets the subscribed of this WebhookEventSubscription.
        True if this is event is subscribed to

        :return: The subscribed of this WebhookEventSubscription.
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """
        Sets the subscribed of this WebhookEventSubscription.
        True if this is event is subscribed to

        :param subscribed: The subscribed of this WebhookEventSubscription.
        :type: bool
        """

        self._subscribed = subscribed

    @property
    def webhook_event_oid(self):
        """
        Gets the webhook_event_oid of this WebhookEventSubscription.
        The webhook event object identifier

        :return: The webhook_event_oid of this WebhookEventSubscription.
        :rtype: int
        """
        return self._webhook_event_oid

    @webhook_event_oid.setter
    def webhook_event_oid(self, webhook_event_oid):
        """
        Sets the webhook_event_oid of this WebhookEventSubscription.
        The webhook event object identifier

        :param webhook_event_oid: The webhook_event_oid of this WebhookEventSubscription.
        :type: int
        """

        self._webhook_event_oid = webhook_event_oid

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