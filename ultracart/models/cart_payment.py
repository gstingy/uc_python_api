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


class CartPayment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, amazon=None, check=None, credit_card=None, payment_method=None, purchase_order=None):
        """
        CartPayment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'amazon': 'CartPaymentAmazon',
            'check': 'CartPaymentCheck',
            'credit_card': 'CartPaymentCreditCard',
            'payment_method': 'str',
            'purchase_order': 'CartPaymentPurchaseOrder'
        }

        self.attribute_map = {
            'amazon': 'amazon',
            'check': 'check',
            'credit_card': 'credit_card',
            'payment_method': 'payment_method',
            'purchase_order': 'purchase_order'
        }

        self._amazon = amazon
        self._check = check
        self._credit_card = credit_card
        self._payment_method = payment_method
        self._purchase_order = purchase_order

    @property
    def amazon(self):
        """
        Gets the amazon of this CartPayment.


        :return: The amazon of this CartPayment.
        :rtype: CartPaymentAmazon
        """
        return self._amazon

    @amazon.setter
    def amazon(self, amazon):
        """
        Sets the amazon of this CartPayment.


        :param amazon: The amazon of this CartPayment.
        :type: CartPaymentAmazon
        """

        self._amazon = amazon

    @property
    def check(self):
        """
        Gets the check of this CartPayment.


        :return: The check of this CartPayment.
        :rtype: CartPaymentCheck
        """
        return self._check

    @check.setter
    def check(self, check):
        """
        Sets the check of this CartPayment.


        :param check: The check of this CartPayment.
        :type: CartPaymentCheck
        """

        self._check = check

    @property
    def credit_card(self):
        """
        Gets the credit_card of this CartPayment.


        :return: The credit_card of this CartPayment.
        :rtype: CartPaymentCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """
        Sets the credit_card of this CartPayment.


        :param credit_card: The credit_card of this CartPayment.
        :type: CartPaymentCreditCard
        """

        self._credit_card = credit_card

    @property
    def payment_method(self):
        """
        Gets the payment_method of this CartPayment.
        Payment method

        :return: The payment_method of this CartPayment.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this CartPayment.
        Payment method

        :param payment_method: The payment_method of this CartPayment.
        :type: str
        """

        self._payment_method = payment_method

    @property
    def purchase_order(self):
        """
        Gets the purchase_order of this CartPayment.


        :return: The purchase_order of this CartPayment.
        :rtype: CartPaymentPurchaseOrder
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """
        Sets the purchase_order of this CartPayment.


        :param purchase_order: The purchase_order of this CartPayment.
        :type: CartPaymentPurchaseOrder
        """

        self._purchase_order = purchase_order

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