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


class AutoOrder(object):
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
        'auto_order_code': 'str',
        'auto_order_oid': 'int',
        'cancel_after_next_x_orders': 'int',
        'cancel_downgrade': 'bool',
        'cancel_upgrade': 'bool',
        'canceled_by_user': 'str',
        'canceled_dts': 'str',
        'credit_card_attempt': 'int',
        'disabled_dts': 'str',
        'enabled': 'bool',
        'failure_reason': 'str',
        'items': 'list[AutoOrderItem]',
        'next_attempt': 'str',
        'original_order': 'Order',
        'original_order_id': 'str',
        'override_affiliate_id': 'int',
        'rebill_orders': 'list[Order]',
        'rotating_transaction_gateway_code': 'str'
    }

    attribute_map = {
        'auto_order_code': 'auto_order_code',
        'auto_order_oid': 'auto_order_oid',
        'cancel_after_next_x_orders': 'cancel_after_next_x_orders',
        'cancel_downgrade': 'cancel_downgrade',
        'cancel_upgrade': 'cancel_upgrade',
        'canceled_by_user': 'canceled_by_user',
        'canceled_dts': 'canceled_dts',
        'credit_card_attempt': 'credit_card_attempt',
        'disabled_dts': 'disabled_dts',
        'enabled': 'enabled',
        'failure_reason': 'failure_reason',
        'items': 'items',
        'next_attempt': 'next_attempt',
        'original_order': 'original_order',
        'original_order_id': 'original_order_id',
        'override_affiliate_id': 'override_affiliate_id',
        'rebill_orders': 'rebill_orders',
        'rotating_transaction_gateway_code': 'rotating_transaction_gateway_code'
    }

    def __init__(self, auto_order_code=None, auto_order_oid=None, cancel_after_next_x_orders=None, cancel_downgrade=None, cancel_upgrade=None, canceled_by_user=None, canceled_dts=None, credit_card_attempt=None, disabled_dts=None, enabled=None, failure_reason=None, items=None, next_attempt=None, original_order=None, original_order_id=None, override_affiliate_id=None, rebill_orders=None, rotating_transaction_gateway_code=None):
        """
        AutoOrder - a model defined in Swagger
        """

        self._auto_order_code = None
        self._auto_order_oid = None
        self._cancel_after_next_x_orders = None
        self._cancel_downgrade = None
        self._cancel_upgrade = None
        self._canceled_by_user = None
        self._canceled_dts = None
        self._credit_card_attempt = None
        self._disabled_dts = None
        self._enabled = None
        self._failure_reason = None
        self._items = None
        self._next_attempt = None
        self._original_order = None
        self._original_order_id = None
        self._override_affiliate_id = None
        self._rebill_orders = None
        self._rotating_transaction_gateway_code = None
        self.discriminator = None

        if auto_order_code is not None:
          self.auto_order_code = auto_order_code
        if auto_order_oid is not None:
          self.auto_order_oid = auto_order_oid
        if cancel_after_next_x_orders is not None:
          self.cancel_after_next_x_orders = cancel_after_next_x_orders
        if cancel_downgrade is not None:
          self.cancel_downgrade = cancel_downgrade
        if cancel_upgrade is not None:
          self.cancel_upgrade = cancel_upgrade
        if canceled_by_user is not None:
          self.canceled_by_user = canceled_by_user
        if canceled_dts is not None:
          self.canceled_dts = canceled_dts
        if credit_card_attempt is not None:
          self.credit_card_attempt = credit_card_attempt
        if disabled_dts is not None:
          self.disabled_dts = disabled_dts
        if enabled is not None:
          self.enabled = enabled
        if failure_reason is not None:
          self.failure_reason = failure_reason
        if items is not None:
          self.items = items
        if next_attempt is not None:
          self.next_attempt = next_attempt
        if original_order is not None:
          self.original_order = original_order
        if original_order_id is not None:
          self.original_order_id = original_order_id
        if override_affiliate_id is not None:
          self.override_affiliate_id = override_affiliate_id
        if rebill_orders is not None:
          self.rebill_orders = rebill_orders
        if rotating_transaction_gateway_code is not None:
          self.rotating_transaction_gateway_code = rotating_transaction_gateway_code

    @property
    def auto_order_code(self):
        """
        Gets the auto_order_code of this AutoOrder.
        Unique code assigned to this auto order

        :return: The auto_order_code of this AutoOrder.
        :rtype: str
        """
        return self._auto_order_code

    @auto_order_code.setter
    def auto_order_code(self, auto_order_code):
        """
        Sets the auto_order_code of this AutoOrder.
        Unique code assigned to this auto order

        :param auto_order_code: The auto_order_code of this AutoOrder.
        :type: str
        """

        self._auto_order_code = auto_order_code

    @property
    def auto_order_oid(self):
        """
        Gets the auto_order_oid of this AutoOrder.
        Auto order object identifier

        :return: The auto_order_oid of this AutoOrder.
        :rtype: int
        """
        return self._auto_order_oid

    @auto_order_oid.setter
    def auto_order_oid(self, auto_order_oid):
        """
        Sets the auto_order_oid of this AutoOrder.
        Auto order object identifier

        :param auto_order_oid: The auto_order_oid of this AutoOrder.
        :type: int
        """

        self._auto_order_oid = auto_order_oid

    @property
    def cancel_after_next_x_orders(self):
        """
        Gets the cancel_after_next_x_orders of this AutoOrder.
        Cancel this auto order after X additional rebills

        :return: The cancel_after_next_x_orders of this AutoOrder.
        :rtype: int
        """
        return self._cancel_after_next_x_orders

    @cancel_after_next_x_orders.setter
    def cancel_after_next_x_orders(self, cancel_after_next_x_orders):
        """
        Sets the cancel_after_next_x_orders of this AutoOrder.
        Cancel this auto order after X additional rebills

        :param cancel_after_next_x_orders: The cancel_after_next_x_orders of this AutoOrder.
        :type: int
        """

        self._cancel_after_next_x_orders = cancel_after_next_x_orders

    @property
    def cancel_downgrade(self):
        """
        Gets the cancel_downgrade of this AutoOrder.
        True if the auto order was canceled because the customer purchased a downgrade item

        :return: The cancel_downgrade of this AutoOrder.
        :rtype: bool
        """
        return self._cancel_downgrade

    @cancel_downgrade.setter
    def cancel_downgrade(self, cancel_downgrade):
        """
        Sets the cancel_downgrade of this AutoOrder.
        True if the auto order was canceled because the customer purchased a downgrade item

        :param cancel_downgrade: The cancel_downgrade of this AutoOrder.
        :type: bool
        """

        self._cancel_downgrade = cancel_downgrade

    @property
    def cancel_upgrade(self):
        """
        Gets the cancel_upgrade of this AutoOrder.
        True if the auto order was canceled because the customer purchased an upgrade item

        :return: The cancel_upgrade of this AutoOrder.
        :rtype: bool
        """
        return self._cancel_upgrade

    @cancel_upgrade.setter
    def cancel_upgrade(self, cancel_upgrade):
        """
        Sets the cancel_upgrade of this AutoOrder.
        True if the auto order was canceled because the customer purchased an upgrade item

        :param cancel_upgrade: The cancel_upgrade of this AutoOrder.
        :type: bool
        """

        self._cancel_upgrade = cancel_upgrade

    @property
    def canceled_by_user(self):
        """
        Gets the canceled_by_user of this AutoOrder.
        The user that canceled the auto order

        :return: The canceled_by_user of this AutoOrder.
        :rtype: str
        """
        return self._canceled_by_user

    @canceled_by_user.setter
    def canceled_by_user(self, canceled_by_user):
        """
        Sets the canceled_by_user of this AutoOrder.
        The user that canceled the auto order

        :param canceled_by_user: The canceled_by_user of this AutoOrder.
        :type: str
        """

        self._canceled_by_user = canceled_by_user

    @property
    def canceled_dts(self):
        """
        Gets the canceled_dts of this AutoOrder.
        The date/time that the auto order was canceled

        :return: The canceled_dts of this AutoOrder.
        :rtype: str
        """
        return self._canceled_dts

    @canceled_dts.setter
    def canceled_dts(self, canceled_dts):
        """
        Sets the canceled_dts of this AutoOrder.
        The date/time that the auto order was canceled

        :param canceled_dts: The canceled_dts of this AutoOrder.
        :type: str
        """

        self._canceled_dts = canceled_dts

    @property
    def credit_card_attempt(self):
        """
        Gets the credit_card_attempt of this AutoOrder.
        The number of credit card attempts that have taken place

        :return: The credit_card_attempt of this AutoOrder.
        :rtype: int
        """
        return self._credit_card_attempt

    @credit_card_attempt.setter
    def credit_card_attempt(self, credit_card_attempt):
        """
        Sets the credit_card_attempt of this AutoOrder.
        The number of credit card attempts that have taken place

        :param credit_card_attempt: The credit_card_attempt of this AutoOrder.
        :type: int
        """

        self._credit_card_attempt = credit_card_attempt

    @property
    def disabled_dts(self):
        """
        Gets the disabled_dts of this AutoOrder.
        The date/time the auto order was disabled due to failed rebills

        :return: The disabled_dts of this AutoOrder.
        :rtype: str
        """
        return self._disabled_dts

    @disabled_dts.setter
    def disabled_dts(self, disabled_dts):
        """
        Sets the disabled_dts of this AutoOrder.
        The date/time the auto order was disabled due to failed rebills

        :param disabled_dts: The disabled_dts of this AutoOrder.
        :type: str
        """

        self._disabled_dts = disabled_dts

    @property
    def enabled(self):
        """
        Gets the enabled of this AutoOrder.
        True if this auto order is enabled

        :return: The enabled of this AutoOrder.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AutoOrder.
        True if this auto order is enabled

        :param enabled: The enabled of this AutoOrder.
        :type: bool
        """

        self._enabled = enabled

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this AutoOrder.
        The reason this auto order failed during the last rebill attempt

        :return: The failure_reason of this AutoOrder.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this AutoOrder.
        The reason this auto order failed during the last rebill attempt

        :param failure_reason: The failure_reason of this AutoOrder.
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def items(self):
        """
        Gets the items of this AutoOrder.
        The items that are setup to rebill

        :return: The items of this AutoOrder.
        :rtype: list[AutoOrderItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AutoOrder.
        The items that are setup to rebill

        :param items: The items of this AutoOrder.
        :type: list[AutoOrderItem]
        """

        self._items = items

    @property
    def next_attempt(self):
        """
        Gets the next_attempt of this AutoOrder.
        The next time that the auto order will be attempted for processing

        :return: The next_attempt of this AutoOrder.
        :rtype: str
        """
        return self._next_attempt

    @next_attempt.setter
    def next_attempt(self, next_attempt):
        """
        Sets the next_attempt of this AutoOrder.
        The next time that the auto order will be attempted for processing

        :param next_attempt: The next_attempt of this AutoOrder.
        :type: str
        """

        self._next_attempt = next_attempt

    @property
    def original_order(self):
        """
        Gets the original_order of this AutoOrder.

        :return: The original_order of this AutoOrder.
        :rtype: Order
        """
        return self._original_order

    @original_order.setter
    def original_order(self, original_order):
        """
        Sets the original_order of this AutoOrder.

        :param original_order: The original_order of this AutoOrder.
        :type: Order
        """

        self._original_order = original_order

    @property
    def original_order_id(self):
        """
        Gets the original_order_id of this AutoOrder.
        The original order id that this auto order is associated with.

        :return: The original_order_id of this AutoOrder.
        :rtype: str
        """
        return self._original_order_id

    @original_order_id.setter
    def original_order_id(self, original_order_id):
        """
        Sets the original_order_id of this AutoOrder.
        The original order id that this auto order is associated with.

        :param original_order_id: The original_order_id of this AutoOrder.
        :type: str
        """

        self._original_order_id = original_order_id

    @property
    def override_affiliate_id(self):
        """
        Gets the override_affiliate_id of this AutoOrder.
        Override the affiliate id given credit for rebills of this auto order

        :return: The override_affiliate_id of this AutoOrder.
        :rtype: int
        """
        return self._override_affiliate_id

    @override_affiliate_id.setter
    def override_affiliate_id(self, override_affiliate_id):
        """
        Sets the override_affiliate_id of this AutoOrder.
        Override the affiliate id given credit for rebills of this auto order

        :param override_affiliate_id: The override_affiliate_id of this AutoOrder.
        :type: int
        """

        self._override_affiliate_id = override_affiliate_id

    @property
    def rebill_orders(self):
        """
        Gets the rebill_orders of this AutoOrder.
        Rebill orders that have taken place on this auto order

        :return: The rebill_orders of this AutoOrder.
        :rtype: list[Order]
        """
        return self._rebill_orders

    @rebill_orders.setter
    def rebill_orders(self, rebill_orders):
        """
        Sets the rebill_orders of this AutoOrder.
        Rebill orders that have taken place on this auto order

        :param rebill_orders: The rebill_orders of this AutoOrder.
        :type: list[Order]
        """

        self._rebill_orders = rebill_orders

    @property
    def rotating_transaction_gateway_code(self):
        """
        Gets the rotating_transaction_gateway_code of this AutoOrder.
        The RTG code associated with this order for future rebills

        :return: The rotating_transaction_gateway_code of this AutoOrder.
        :rtype: str
        """
        return self._rotating_transaction_gateway_code

    @rotating_transaction_gateway_code.setter
    def rotating_transaction_gateway_code(self, rotating_transaction_gateway_code):
        """
        Sets the rotating_transaction_gateway_code of this AutoOrder.
        The RTG code associated with this order for future rebills

        :param rotating_transaction_gateway_code: The rotating_transaction_gateway_code of this AutoOrder.
        :type: str
        """

        self._rotating_transaction_gateway_code = rotating_transaction_gateway_code

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
        if not isinstance(other, AutoOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
