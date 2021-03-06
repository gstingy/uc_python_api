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


class CartSettingsPayment(object):
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
        'amazon': 'CartSettingsPaymentAmazon',
        'credit_card': 'CartSettingsPaymentCreditCard',
        'need_payment': 'bool',
        'paypal': 'CartSettingsPaymentPayPal',
        'supports_amazon': 'bool',
        'supports_check': 'bool',
        'supports_cod': 'bool',
        'supports_credit_card': 'bool',
        'supports_money_order': 'bool',
        'supports_paypal': 'bool',
        'supports_purchase_order': 'bool',
        'supports_quote_request': 'bool',
        'supports_wire_transfer': 'bool'
    }

    attribute_map = {
        'amazon': 'amazon',
        'credit_card': 'credit_card',
        'need_payment': 'need_payment',
        'paypal': 'paypal',
        'supports_amazon': 'supports_amazon',
        'supports_check': 'supports_check',
        'supports_cod': 'supports_cod',
        'supports_credit_card': 'supports_credit_card',
        'supports_money_order': 'supports_money_order',
        'supports_paypal': 'supports_paypal',
        'supports_purchase_order': 'supports_purchase_order',
        'supports_quote_request': 'supports_quote_request',
        'supports_wire_transfer': 'supports_wire_transfer'
    }

    def __init__(self, amazon=None, credit_card=None, need_payment=None, paypal=None, supports_amazon=None, supports_check=None, supports_cod=None, supports_credit_card=None, supports_money_order=None, supports_paypal=None, supports_purchase_order=None, supports_quote_request=None, supports_wire_transfer=None):
        """
        CartSettingsPayment - a model defined in Swagger
        """

        self._amazon = None
        self._credit_card = None
        self._need_payment = None
        self._paypal = None
        self._supports_amazon = None
        self._supports_check = None
        self._supports_cod = None
        self._supports_credit_card = None
        self._supports_money_order = None
        self._supports_paypal = None
        self._supports_purchase_order = None
        self._supports_quote_request = None
        self._supports_wire_transfer = None
        self.discriminator = None

        if amazon is not None:
          self.amazon = amazon
        if credit_card is not None:
          self.credit_card = credit_card
        if need_payment is not None:
          self.need_payment = need_payment
        if paypal is not None:
          self.paypal = paypal
        if supports_amazon is not None:
          self.supports_amazon = supports_amazon
        if supports_check is not None:
          self.supports_check = supports_check
        if supports_cod is not None:
          self.supports_cod = supports_cod
        if supports_credit_card is not None:
          self.supports_credit_card = supports_credit_card
        if supports_money_order is not None:
          self.supports_money_order = supports_money_order
        if supports_paypal is not None:
          self.supports_paypal = supports_paypal
        if supports_purchase_order is not None:
          self.supports_purchase_order = supports_purchase_order
        if supports_quote_request is not None:
          self.supports_quote_request = supports_quote_request
        if supports_wire_transfer is not None:
          self.supports_wire_transfer = supports_wire_transfer

    @property
    def amazon(self):
        """
        Gets the amazon of this CartSettingsPayment.

        :return: The amazon of this CartSettingsPayment.
        :rtype: CartSettingsPaymentAmazon
        """
        return self._amazon

    @amazon.setter
    def amazon(self, amazon):
        """
        Sets the amazon of this CartSettingsPayment.

        :param amazon: The amazon of this CartSettingsPayment.
        :type: CartSettingsPaymentAmazon
        """

        self._amazon = amazon

    @property
    def credit_card(self):
        """
        Gets the credit_card of this CartSettingsPayment.

        :return: The credit_card of this CartSettingsPayment.
        :rtype: CartSettingsPaymentCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """
        Sets the credit_card of this CartSettingsPayment.

        :param credit_card: The credit_card of this CartSettingsPayment.
        :type: CartSettingsPaymentCreditCard
        """

        self._credit_card = credit_card

    @property
    def need_payment(self):
        """
        Gets the need_payment of this CartSettingsPayment.
        True if this card requires a payment from the customer

        :return: The need_payment of this CartSettingsPayment.
        :rtype: bool
        """
        return self._need_payment

    @need_payment.setter
    def need_payment(self, need_payment):
        """
        Sets the need_payment of this CartSettingsPayment.
        True if this card requires a payment from the customer

        :param need_payment: The need_payment of this CartSettingsPayment.
        :type: bool
        """

        self._need_payment = need_payment

    @property
    def paypal(self):
        """
        Gets the paypal of this CartSettingsPayment.

        :return: The paypal of this CartSettingsPayment.
        :rtype: CartSettingsPaymentPayPal
        """
        return self._paypal

    @paypal.setter
    def paypal(self, paypal):
        """
        Sets the paypal of this CartSettingsPayment.

        :param paypal: The paypal of this CartSettingsPayment.
        :type: CartSettingsPaymentPayPal
        """

        self._paypal = paypal

    @property
    def supports_amazon(self):
        """
        Gets the supports_amazon of this CartSettingsPayment.
        True if Amazon payments are available on this order

        :return: The supports_amazon of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_amazon

    @supports_amazon.setter
    def supports_amazon(self, supports_amazon):
        """
        Sets the supports_amazon of this CartSettingsPayment.
        True if Amazon payments are available on this order

        :param supports_amazon: The supports_amazon of this CartSettingsPayment.
        :type: bool
        """

        self._supports_amazon = supports_amazon

    @property
    def supports_check(self):
        """
        Gets the supports_check of this CartSettingsPayment.
        True if check payments are available on this order

        :return: The supports_check of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_check

    @supports_check.setter
    def supports_check(self, supports_check):
        """
        Sets the supports_check of this CartSettingsPayment.
        True if check payments are available on this order

        :param supports_check: The supports_check of this CartSettingsPayment.
        :type: bool
        """

        self._supports_check = supports_check

    @property
    def supports_cod(self):
        """
        Gets the supports_cod of this CartSettingsPayment.
        True if COD payments are available on this order

        :return: The supports_cod of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_cod

    @supports_cod.setter
    def supports_cod(self, supports_cod):
        """
        Sets the supports_cod of this CartSettingsPayment.
        True if COD payments are available on this order

        :param supports_cod: The supports_cod of this CartSettingsPayment.
        :type: bool
        """

        self._supports_cod = supports_cod

    @property
    def supports_credit_card(self):
        """
        Gets the supports_credit_card of this CartSettingsPayment.
        True if credit card payments are available on this order

        :return: The supports_credit_card of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_credit_card

    @supports_credit_card.setter
    def supports_credit_card(self, supports_credit_card):
        """
        Sets the supports_credit_card of this CartSettingsPayment.
        True if credit card payments are available on this order

        :param supports_credit_card: The supports_credit_card of this CartSettingsPayment.
        :type: bool
        """

        self._supports_credit_card = supports_credit_card

    @property
    def supports_money_order(self):
        """
        Gets the supports_money_order of this CartSettingsPayment.
        True if money order payments are available on this order

        :return: The supports_money_order of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_money_order

    @supports_money_order.setter
    def supports_money_order(self, supports_money_order):
        """
        Sets the supports_money_order of this CartSettingsPayment.
        True if money order payments are available on this order

        :param supports_money_order: The supports_money_order of this CartSettingsPayment.
        :type: bool
        """

        self._supports_money_order = supports_money_order

    @property
    def supports_paypal(self):
        """
        Gets the supports_paypal of this CartSettingsPayment.
        True if PayPal payments are available on this order

        :return: The supports_paypal of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_paypal

    @supports_paypal.setter
    def supports_paypal(self, supports_paypal):
        """
        Sets the supports_paypal of this CartSettingsPayment.
        True if PayPal payments are available on this order

        :param supports_paypal: The supports_paypal of this CartSettingsPayment.
        :type: bool
        """

        self._supports_paypal = supports_paypal

    @property
    def supports_purchase_order(self):
        """
        Gets the supports_purchase_order of this CartSettingsPayment.
        True if purchase order payments are available on this order

        :return: The supports_purchase_order of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_purchase_order

    @supports_purchase_order.setter
    def supports_purchase_order(self, supports_purchase_order):
        """
        Sets the supports_purchase_order of this CartSettingsPayment.
        True if purchase order payments are available on this order

        :param supports_purchase_order: The supports_purchase_order of this CartSettingsPayment.
        :type: bool
        """

        self._supports_purchase_order = supports_purchase_order

    @property
    def supports_quote_request(self):
        """
        Gets the supports_quote_request of this CartSettingsPayment.
        True if quote requests payments are available on this order

        :return: The supports_quote_request of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_quote_request

    @supports_quote_request.setter
    def supports_quote_request(self, supports_quote_request):
        """
        Sets the supports_quote_request of this CartSettingsPayment.
        True if quote requests payments are available on this order

        :param supports_quote_request: The supports_quote_request of this CartSettingsPayment.
        :type: bool
        """

        self._supports_quote_request = supports_quote_request

    @property
    def supports_wire_transfer(self):
        """
        Gets the supports_wire_transfer of this CartSettingsPayment.
        True if wire transfer payments are available on this order

        :return: The supports_wire_transfer of this CartSettingsPayment.
        :rtype: bool
        """
        return self._supports_wire_transfer

    @supports_wire_transfer.setter
    def supports_wire_transfer(self, supports_wire_transfer):
        """
        Sets the supports_wire_transfer of this CartSettingsPayment.
        True if wire transfer payments are available on this order

        :param supports_wire_transfer: The supports_wire_transfer of this CartSettingsPayment.
        :type: bool
        """

        self._supports_wire_transfer = supports_wire_transfer

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
        if not isinstance(other, CartSettingsPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
