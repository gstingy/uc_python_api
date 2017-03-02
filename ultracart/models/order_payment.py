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


class OrderPayment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, check=None, credit_card=None, echeck=None, hold_for_fraud_review=None, payment_dts=None, payment_method=None, payment_method_accounting_code=None, payment_method_deposit_to_account=None, payment_status=None, purchase_order=None, rotating_transaction_gateway_code=None, surcharge=None, surcharge_accounting_code=None, surcharge_transaction_fee=None, surcharge_transaction_percentage=None, test_order=None, transactions=None):
        """
        OrderPayment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'check': 'OrderPaymentCheck',
            'credit_card': 'OrderPaymentCreditCard',
            'echeck': 'OrderPaymentECheck',
            'hold_for_fraud_review': 'bool',
            'payment_dts': 'str',
            'payment_method': 'str',
            'payment_method_accounting_code': 'str',
            'payment_method_deposit_to_account': 'str',
            'payment_status': 'str',
            'purchase_order': 'OrderPaymentPurchaseOrder',
            'rotating_transaction_gateway_code': 'str',
            'surcharge': 'Currency',
            'surcharge_accounting_code': 'str',
            'surcharge_transaction_fee': 'float',
            'surcharge_transaction_percentage': 'float',
            'test_order': 'bool',
            'transactions': 'list[OrderPaymentTransaction]'
        }

        self.attribute_map = {
            'check': 'check',
            'credit_card': 'credit_card',
            'echeck': 'echeck',
            'hold_for_fraud_review': 'hold_for_fraud_review',
            'payment_dts': 'payment_dts',
            'payment_method': 'payment_method',
            'payment_method_accounting_code': 'payment_method_accounting_code',
            'payment_method_deposit_to_account': 'payment_method_deposit_to_account',
            'payment_status': 'payment_status',
            'purchase_order': 'purchase_order',
            'rotating_transaction_gateway_code': 'rotating_transaction_gateway_code',
            'surcharge': 'surcharge',
            'surcharge_accounting_code': 'surcharge_accounting_code',
            'surcharge_transaction_fee': 'surcharge_transaction_fee',
            'surcharge_transaction_percentage': 'surcharge_transaction_percentage',
            'test_order': 'test_order',
            'transactions': 'transactions'
        }

        self._check = check
        self._credit_card = credit_card
        self._echeck = echeck
        self._hold_for_fraud_review = hold_for_fraud_review
        self._payment_dts = payment_dts
        self._payment_method = payment_method
        self._payment_method_accounting_code = payment_method_accounting_code
        self._payment_method_deposit_to_account = payment_method_deposit_to_account
        self._payment_status = payment_status
        self._purchase_order = purchase_order
        self._rotating_transaction_gateway_code = rotating_transaction_gateway_code
        self._surcharge = surcharge
        self._surcharge_accounting_code = surcharge_accounting_code
        self._surcharge_transaction_fee = surcharge_transaction_fee
        self._surcharge_transaction_percentage = surcharge_transaction_percentage
        self._test_order = test_order
        self._transactions = transactions

    @property
    def check(self):
        """
        Gets the check of this OrderPayment.


        :return: The check of this OrderPayment.
        :rtype: OrderPaymentCheck
        """
        return self._check

    @check.setter
    def check(self, check):
        """
        Sets the check of this OrderPayment.


        :param check: The check of this OrderPayment.
        :type: OrderPaymentCheck
        """

        self._check = check

    @property
    def credit_card(self):
        """
        Gets the credit_card of this OrderPayment.


        :return: The credit_card of this OrderPayment.
        :rtype: OrderPaymentCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """
        Sets the credit_card of this OrderPayment.


        :param credit_card: The credit_card of this OrderPayment.
        :type: OrderPaymentCreditCard
        """

        self._credit_card = credit_card

    @property
    def echeck(self):
        """
        Gets the echeck of this OrderPayment.


        :return: The echeck of this OrderPayment.
        :rtype: OrderPaymentECheck
        """
        return self._echeck

    @echeck.setter
    def echeck(self, echeck):
        """
        Sets the echeck of this OrderPayment.


        :param echeck: The echeck of this OrderPayment.
        :type: OrderPaymentECheck
        """

        self._echeck = echeck

    @property
    def hold_for_fraud_review(self):
        """
        Gets the hold_for_fraud_review of this OrderPayment.
        True if order has been held for fraud review

        :return: The hold_for_fraud_review of this OrderPayment.
        :rtype: bool
        """
        return self._hold_for_fraud_review

    @hold_for_fraud_review.setter
    def hold_for_fraud_review(self, hold_for_fraud_review):
        """
        Sets the hold_for_fraud_review of this OrderPayment.
        True if order has been held for fraud review

        :param hold_for_fraud_review: The hold_for_fraud_review of this OrderPayment.
        :type: bool
        """

        self._hold_for_fraud_review = hold_for_fraud_review

    @property
    def payment_dts(self):
        """
        Gets the payment_dts of this OrderPayment.
        Date/time that the payment was successfully processed

        :return: The payment_dts of this OrderPayment.
        :rtype: str
        """
        return self._payment_dts

    @payment_dts.setter
    def payment_dts(self, payment_dts):
        """
        Sets the payment_dts of this OrderPayment.
        Date/time that the payment was successfully processed

        :param payment_dts: The payment_dts of this OrderPayment.
        :type: str
        """

        self._payment_dts = payment_dts

    @property
    def payment_method(self):
        """
        Gets the payment_method of this OrderPayment.
        Payment method

        :return: The payment_method of this OrderPayment.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this OrderPayment.
        Payment method

        :param payment_method: The payment_method of this OrderPayment.
        :type: str
        """
        allowed_values = ["Affirm", "Amazon", "Amazon SC", "Cash", "Check", "COD", "Coinbase", "Credit Card", "eCheck", "Money Order", "PayPal", "Purchase Order", "Quote Request", "Unknown", "Wire Transfer"]
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def payment_method_accounting_code(self):
        """
        Gets the payment_method_accounting_code of this OrderPayment.
        Payment method QuickBooks code

        :return: The payment_method_accounting_code of this OrderPayment.
        :rtype: str
        """
        return self._payment_method_accounting_code

    @payment_method_accounting_code.setter
    def payment_method_accounting_code(self, payment_method_accounting_code):
        """
        Sets the payment_method_accounting_code of this OrderPayment.
        Payment method QuickBooks code

        :param payment_method_accounting_code: The payment_method_accounting_code of this OrderPayment.
        :type: str
        """

        self._payment_method_accounting_code = payment_method_accounting_code

    @property
    def payment_method_deposit_to_account(self):
        """
        Gets the payment_method_deposit_to_account of this OrderPayment.
        Payment method QuickBooks deposit account

        :return: The payment_method_deposit_to_account of this OrderPayment.
        :rtype: str
        """
        return self._payment_method_deposit_to_account

    @payment_method_deposit_to_account.setter
    def payment_method_deposit_to_account(self, payment_method_deposit_to_account):
        """
        Sets the payment_method_deposit_to_account of this OrderPayment.
        Payment method QuickBooks deposit account

        :param payment_method_deposit_to_account: The payment_method_deposit_to_account of this OrderPayment.
        :type: str
        """

        self._payment_method_deposit_to_account = payment_method_deposit_to_account

    @property
    def payment_status(self):
        """
        Gets the payment_status of this OrderPayment.
        Payment status

        :return: The payment_status of this OrderPayment.
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """
        Sets the payment_status of this OrderPayment.
        Payment status

        :param payment_status: The payment_status of this OrderPayment.
        :type: str
        """
        allowed_values = ["Unprocessed", "Authorized", "Capture Failed", "Processed", "Declined", "Voided", "Refunded", "Skipped"]
        if payment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_status` ({0}), must be one of {1}"
                .format(payment_status, allowed_values)
            )

        self._payment_status = payment_status

    @property
    def purchase_order(self):
        """
        Gets the purchase_order of this OrderPayment.


        :return: The purchase_order of this OrderPayment.
        :rtype: OrderPaymentPurchaseOrder
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """
        Sets the purchase_order of this OrderPayment.


        :param purchase_order: The purchase_order of this OrderPayment.
        :type: OrderPaymentPurchaseOrder
        """

        self._purchase_order = purchase_order

    @property
    def rotating_transaction_gateway_code(self):
        """
        Gets the rotating_transaction_gateway_code of this OrderPayment.
        Rotating transaction gateway code used to process this order

        :return: The rotating_transaction_gateway_code of this OrderPayment.
        :rtype: str
        """
        return self._rotating_transaction_gateway_code

    @rotating_transaction_gateway_code.setter
    def rotating_transaction_gateway_code(self, rotating_transaction_gateway_code):
        """
        Sets the rotating_transaction_gateway_code of this OrderPayment.
        Rotating transaction gateway code used to process this order

        :param rotating_transaction_gateway_code: The rotating_transaction_gateway_code of this OrderPayment.
        :type: str
        """

        self._rotating_transaction_gateway_code = rotating_transaction_gateway_code

    @property
    def surcharge(self):
        """
        Gets the surcharge of this OrderPayment.


        :return: The surcharge of this OrderPayment.
        :rtype: Currency
        """
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        """
        Sets the surcharge of this OrderPayment.


        :param surcharge: The surcharge of this OrderPayment.
        :type: Currency
        """

        self._surcharge = surcharge

    @property
    def surcharge_accounting_code(self):
        """
        Gets the surcharge_accounting_code of this OrderPayment.
        Surcharge accounting code

        :return: The surcharge_accounting_code of this OrderPayment.
        :rtype: str
        """
        return self._surcharge_accounting_code

    @surcharge_accounting_code.setter
    def surcharge_accounting_code(self, surcharge_accounting_code):
        """
        Sets the surcharge_accounting_code of this OrderPayment.
        Surcharge accounting code

        :param surcharge_accounting_code: The surcharge_accounting_code of this OrderPayment.
        :type: str
        """

        self._surcharge_accounting_code = surcharge_accounting_code

    @property
    def surcharge_transaction_fee(self):
        """
        Gets the surcharge_transaction_fee of this OrderPayment.
        Surcharge transaction fee

        :return: The surcharge_transaction_fee of this OrderPayment.
        :rtype: float
        """
        return self._surcharge_transaction_fee

    @surcharge_transaction_fee.setter
    def surcharge_transaction_fee(self, surcharge_transaction_fee):
        """
        Sets the surcharge_transaction_fee of this OrderPayment.
        Surcharge transaction fee

        :param surcharge_transaction_fee: The surcharge_transaction_fee of this OrderPayment.
        :type: float
        """

        self._surcharge_transaction_fee = surcharge_transaction_fee

    @property
    def surcharge_transaction_percentage(self):
        """
        Gets the surcharge_transaction_percentage of this OrderPayment.
        Surcharge transaction percentage

        :return: The surcharge_transaction_percentage of this OrderPayment.
        :rtype: float
        """
        return self._surcharge_transaction_percentage

    @surcharge_transaction_percentage.setter
    def surcharge_transaction_percentage(self, surcharge_transaction_percentage):
        """
        Sets the surcharge_transaction_percentage of this OrderPayment.
        Surcharge transaction percentage

        :param surcharge_transaction_percentage: The surcharge_transaction_percentage of this OrderPayment.
        :type: float
        """

        self._surcharge_transaction_percentage = surcharge_transaction_percentage

    @property
    def test_order(self):
        """
        Gets the test_order of this OrderPayment.
        True if this is a test order

        :return: The test_order of this OrderPayment.
        :rtype: bool
        """
        return self._test_order

    @test_order.setter
    def test_order(self, test_order):
        """
        Sets the test_order of this OrderPayment.
        True if this is a test order

        :param test_order: The test_order of this OrderPayment.
        :type: bool
        """

        self._test_order = test_order

    @property
    def transactions(self):
        """
        Gets the transactions of this OrderPayment.
        Transactions associated with processing this payment

        :return: The transactions of this OrderPayment.
        :rtype: list[OrderPaymentTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """
        Sets the transactions of this OrderPayment.
        Transactions associated with processing this payment

        :param transactions: The transactions of this OrderPayment.
        :type: list[OrderPaymentTransaction]
        """

        self._transactions = transactions

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
