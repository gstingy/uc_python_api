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


class ItemAutoOrderStep(object):
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
        'arbitrary_schedule_days': 'int',
        'arbitrary_unit_cost': 'float',
        'arbitrary_unit_cost_schedules': 'list[ItemAutoOrderStepArbitraryUnitCostSchedule]',
        'grandfather_pricing': 'list[ItemAutoOrderStepGrandfatherPricing]',
        'managed_by': 'str',
        'pause_days': 'int',
        'pause_until_date': 'str',
        'preshipment_notice_days': 'int',
        'recurring_merchant_item_id': 'str',
        'recurring_merchant_item_oid': 'int',
        'repeat_count': 'int',
        'schedule': 'str',
        'subscribe_email_list_name': 'str',
        'subscribe_email_list_oid': 'int',
        'type': 'str'
    }

    attribute_map = {
        'arbitrary_schedule_days': 'arbitrary_schedule_days',
        'arbitrary_unit_cost': 'arbitrary_unit_cost',
        'arbitrary_unit_cost_schedules': 'arbitrary_unit_cost_schedules',
        'grandfather_pricing': 'grandfather_pricing',
        'managed_by': 'managed_by',
        'pause_days': 'pause_days',
        'pause_until_date': 'pause_until_date',
        'preshipment_notice_days': 'preshipment_notice_days',
        'recurring_merchant_item_id': 'recurring_merchant_item_id',
        'recurring_merchant_item_oid': 'recurring_merchant_item_oid',
        'repeat_count': 'repeat_count',
        'schedule': 'schedule',
        'subscribe_email_list_name': 'subscribe_email_list_name',
        'subscribe_email_list_oid': 'subscribe_email_list_oid',
        'type': 'type'
    }

    def __init__(self, arbitrary_schedule_days=None, arbitrary_unit_cost=None, arbitrary_unit_cost_schedules=None, grandfather_pricing=None, managed_by=None, pause_days=None, pause_until_date=None, preshipment_notice_days=None, recurring_merchant_item_id=None, recurring_merchant_item_oid=None, repeat_count=None, schedule=None, subscribe_email_list_name=None, subscribe_email_list_oid=None, type=None):
        """
        ItemAutoOrderStep - a model defined in Swagger
        """

        self._arbitrary_schedule_days = None
        self._arbitrary_unit_cost = None
        self._arbitrary_unit_cost_schedules = None
        self._grandfather_pricing = None
        self._managed_by = None
        self._pause_days = None
        self._pause_until_date = None
        self._preshipment_notice_days = None
        self._recurring_merchant_item_id = None
        self._recurring_merchant_item_oid = None
        self._repeat_count = None
        self._schedule = None
        self._subscribe_email_list_name = None
        self._subscribe_email_list_oid = None
        self._type = None
        self.discriminator = None

        if arbitrary_schedule_days is not None:
          self.arbitrary_schedule_days = arbitrary_schedule_days
        if arbitrary_unit_cost is not None:
          self.arbitrary_unit_cost = arbitrary_unit_cost
        if arbitrary_unit_cost_schedules is not None:
          self.arbitrary_unit_cost_schedules = arbitrary_unit_cost_schedules
        if grandfather_pricing is not None:
          self.grandfather_pricing = grandfather_pricing
        if managed_by is not None:
          self.managed_by = managed_by
        if pause_days is not None:
          self.pause_days = pause_days
        if pause_until_date is not None:
          self.pause_until_date = pause_until_date
        if preshipment_notice_days is not None:
          self.preshipment_notice_days = preshipment_notice_days
        if recurring_merchant_item_id is not None:
          self.recurring_merchant_item_id = recurring_merchant_item_id
        if recurring_merchant_item_oid is not None:
          self.recurring_merchant_item_oid = recurring_merchant_item_oid
        if repeat_count is not None:
          self.repeat_count = repeat_count
        if schedule is not None:
          self.schedule = schedule
        if subscribe_email_list_name is not None:
          self.subscribe_email_list_name = subscribe_email_list_name
        if subscribe_email_list_oid is not None:
          self.subscribe_email_list_oid = subscribe_email_list_oid
        if type is not None:
          self.type = type

    @property
    def arbitrary_schedule_days(self):
        """
        Gets the arbitrary_schedule_days of this ItemAutoOrderStep.
        If the schedule is arbitrary, then this is the number of days

        :return: The arbitrary_schedule_days of this ItemAutoOrderStep.
        :rtype: int
        """
        return self._arbitrary_schedule_days

    @arbitrary_schedule_days.setter
    def arbitrary_schedule_days(self, arbitrary_schedule_days):
        """
        Sets the arbitrary_schedule_days of this ItemAutoOrderStep.
        If the schedule is arbitrary, then this is the number of days

        :param arbitrary_schedule_days: The arbitrary_schedule_days of this ItemAutoOrderStep.
        :type: int
        """

        self._arbitrary_schedule_days = arbitrary_schedule_days

    @property
    def arbitrary_unit_cost(self):
        """
        Gets the arbitrary_unit_cost of this ItemAutoOrderStep.
        Arbitrary unit cost used to override the regular item cost

        :return: The arbitrary_unit_cost of this ItemAutoOrderStep.
        :rtype: float
        """
        return self._arbitrary_unit_cost

    @arbitrary_unit_cost.setter
    def arbitrary_unit_cost(self, arbitrary_unit_cost):
        """
        Sets the arbitrary_unit_cost of this ItemAutoOrderStep.
        Arbitrary unit cost used to override the regular item cost

        :param arbitrary_unit_cost: The arbitrary_unit_cost of this ItemAutoOrderStep.
        :type: float
        """

        self._arbitrary_unit_cost = arbitrary_unit_cost

    @property
    def arbitrary_unit_cost_schedules(self):
        """
        Gets the arbitrary_unit_cost_schedules of this ItemAutoOrderStep.
        Arbitrary unit costs schedules for more advanced discounting by rebill attempt

        :return: The arbitrary_unit_cost_schedules of this ItemAutoOrderStep.
        :rtype: list[ItemAutoOrderStepArbitraryUnitCostSchedule]
        """
        return self._arbitrary_unit_cost_schedules

    @arbitrary_unit_cost_schedules.setter
    def arbitrary_unit_cost_schedules(self, arbitrary_unit_cost_schedules):
        """
        Sets the arbitrary_unit_cost_schedules of this ItemAutoOrderStep.
        Arbitrary unit costs schedules for more advanced discounting by rebill attempt

        :param arbitrary_unit_cost_schedules: The arbitrary_unit_cost_schedules of this ItemAutoOrderStep.
        :type: list[ItemAutoOrderStepArbitraryUnitCostSchedule]
        """

        self._arbitrary_unit_cost_schedules = arbitrary_unit_cost_schedules

    @property
    def grandfather_pricing(self):
        """
        Gets the grandfather_pricing of this ItemAutoOrderStep.
        Grand-father pricing configuration if the rebill schedule has changed over time

        :return: The grandfather_pricing of this ItemAutoOrderStep.
        :rtype: list[ItemAutoOrderStepGrandfatherPricing]
        """
        return self._grandfather_pricing

    @grandfather_pricing.setter
    def grandfather_pricing(self, grandfather_pricing):
        """
        Sets the grandfather_pricing of this ItemAutoOrderStep.
        Grand-father pricing configuration if the rebill schedule has changed over time

        :param grandfather_pricing: The grandfather_pricing of this ItemAutoOrderStep.
        :type: list[ItemAutoOrderStepGrandfatherPricing]
        """

        self._grandfather_pricing = grandfather_pricing

    @property
    def managed_by(self):
        """
        Gets the managed_by of this ItemAutoOrderStep.
        Managed by (defaults to UltraCart)

        :return: The managed_by of this ItemAutoOrderStep.
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """
        Sets the managed_by of this ItemAutoOrderStep.
        Managed by (defaults to UltraCart)

        :param managed_by: The managed_by of this ItemAutoOrderStep.
        :type: str
        """

        self._managed_by = managed_by

    @property
    def pause_days(self):
        """
        Gets the pause_days of this ItemAutoOrderStep.
        Number of days to pause

        :return: The pause_days of this ItemAutoOrderStep.
        :rtype: int
        """
        return self._pause_days

    @pause_days.setter
    def pause_days(self, pause_days):
        """
        Sets the pause_days of this ItemAutoOrderStep.
        Number of days to pause

        :param pause_days: The pause_days of this ItemAutoOrderStep.
        :type: int
        """

        self._pause_days = pause_days

    @property
    def pause_until_date(self):
        """
        Gets the pause_until_date of this ItemAutoOrderStep.
        Wait for this step to happen until the specified date

        :return: The pause_until_date of this ItemAutoOrderStep.
        :rtype: str
        """
        return self._pause_until_date

    @pause_until_date.setter
    def pause_until_date(self, pause_until_date):
        """
        Sets the pause_until_date of this ItemAutoOrderStep.
        Wait for this step to happen until the specified date

        :param pause_until_date: The pause_until_date of this ItemAutoOrderStep.
        :type: str
        """

        self._pause_until_date = pause_until_date

    @property
    def preshipment_notice_days(self):
        """
        Gets the preshipment_notice_days of this ItemAutoOrderStep.
        If set, a pre-shipment notice is sent to the customer this many days in advance

        :return: The preshipment_notice_days of this ItemAutoOrderStep.
        :rtype: int
        """
        return self._preshipment_notice_days

    @preshipment_notice_days.setter
    def preshipment_notice_days(self, preshipment_notice_days):
        """
        Sets the preshipment_notice_days of this ItemAutoOrderStep.
        If set, a pre-shipment notice is sent to the customer this many days in advance

        :param preshipment_notice_days: The preshipment_notice_days of this ItemAutoOrderStep.
        :type: int
        """

        self._preshipment_notice_days = preshipment_notice_days

    @property
    def recurring_merchant_item_id(self):
        """
        Gets the recurring_merchant_item_id of this ItemAutoOrderStep.
        Item id to rebill

        :return: The recurring_merchant_item_id of this ItemAutoOrderStep.
        :rtype: str
        """
        return self._recurring_merchant_item_id

    @recurring_merchant_item_id.setter
    def recurring_merchant_item_id(self, recurring_merchant_item_id):
        """
        Sets the recurring_merchant_item_id of this ItemAutoOrderStep.
        Item id to rebill

        :param recurring_merchant_item_id: The recurring_merchant_item_id of this ItemAutoOrderStep.
        :type: str
        """
        if recurring_merchant_item_id is not None and len(recurring_merchant_item_id) > 20:
            raise ValueError("Invalid value for `recurring_merchant_item_id`, length must be less than or equal to `20`")

        self._recurring_merchant_item_id = recurring_merchant_item_id

    @property
    def recurring_merchant_item_oid(self):
        """
        Gets the recurring_merchant_item_oid of this ItemAutoOrderStep.
        Item object identifier to rebill

        :return: The recurring_merchant_item_oid of this ItemAutoOrderStep.
        :rtype: int
        """
        return self._recurring_merchant_item_oid

    @recurring_merchant_item_oid.setter
    def recurring_merchant_item_oid(self, recurring_merchant_item_oid):
        """
        Sets the recurring_merchant_item_oid of this ItemAutoOrderStep.
        Item object identifier to rebill

        :param recurring_merchant_item_oid: The recurring_merchant_item_oid of this ItemAutoOrderStep.
        :type: int
        """

        self._recurring_merchant_item_oid = recurring_merchant_item_oid

    @property
    def repeat_count(self):
        """
        Gets the repeat_count of this ItemAutoOrderStep.
        Number of times to rebill.  Last step can be null for infinite

        :return: The repeat_count of this ItemAutoOrderStep.
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """
        Sets the repeat_count of this ItemAutoOrderStep.
        Number of times to rebill.  Last step can be null for infinite

        :param repeat_count: The repeat_count of this ItemAutoOrderStep.
        :type: int
        """

        self._repeat_count = repeat_count

    @property
    def schedule(self):
        """
        Gets the schedule of this ItemAutoOrderStep.
        Frequency of the rebill

        :return: The schedule of this ItemAutoOrderStep.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this ItemAutoOrderStep.
        Frequency of the rebill

        :param schedule: The schedule of this ItemAutoOrderStep.
        :type: str
        """

        self._schedule = schedule

    @property
    def subscribe_email_list_name(self):
        """
        Gets the subscribe_email_list_name of this ItemAutoOrderStep.
        Email list name to subscribe the customer to when the rebill occurs

        :return: The subscribe_email_list_name of this ItemAutoOrderStep.
        :rtype: str
        """
        return self._subscribe_email_list_name

    @subscribe_email_list_name.setter
    def subscribe_email_list_name(self, subscribe_email_list_name):
        """
        Sets the subscribe_email_list_name of this ItemAutoOrderStep.
        Email list name to subscribe the customer to when the rebill occurs

        :param subscribe_email_list_name: The subscribe_email_list_name of this ItemAutoOrderStep.
        :type: str
        """

        self._subscribe_email_list_name = subscribe_email_list_name

    @property
    def subscribe_email_list_oid(self):
        """
        Gets the subscribe_email_list_oid of this ItemAutoOrderStep.
        Email list identifier to subscribe the customer to when this rebill occurs

        :return: The subscribe_email_list_oid of this ItemAutoOrderStep.
        :rtype: int
        """
        return self._subscribe_email_list_oid

    @subscribe_email_list_oid.setter
    def subscribe_email_list_oid(self, subscribe_email_list_oid):
        """
        Sets the subscribe_email_list_oid of this ItemAutoOrderStep.
        Email list identifier to subscribe the customer to when this rebill occurs

        :param subscribe_email_list_oid: The subscribe_email_list_oid of this ItemAutoOrderStep.
        :type: int
        """

        self._subscribe_email_list_oid = subscribe_email_list_oid

    @property
    def type(self):
        """
        Gets the type of this ItemAutoOrderStep.
        Type of step (item or pause)

        :return: The type of this ItemAutoOrderStep.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemAutoOrderStep.
        Type of step (item or pause)

        :param type: The type of this ItemAutoOrderStep.
        :type: str
        """
        allowed_values = ["item", "pause"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, ItemAutoOrderStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
