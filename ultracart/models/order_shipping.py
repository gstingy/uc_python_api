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


class OrderShipping(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address1=None, address2=None, city=None, company=None, country_code=None, day_phone=None, delivery_date=None, evening_phone=None, first_name=None, last_name=None, lift_gate=None, postal_code=None, rma=None, ship_on_date=None, ship_to_residential=None, shipping_3rd_party_account_number=None, shipping_date=None, shipping_department_status=None, shipping_method=None, shipping_method_accounting_code=None, special_instructions=None, state_region=None, title=None, tracking_numbers=None, weight=None):
        """
        OrderShipping - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address1': 'str',
            'address2': 'str',
            'city': 'str',
            'company': 'str',
            'country_code': 'str',
            'day_phone': 'str',
            'delivery_date': 'str',
            'evening_phone': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'lift_gate': 'bool',
            'postal_code': 'str',
            'rma': 'str',
            'ship_on_date': 'str',
            'ship_to_residential': 'bool',
            'shipping_3rd_party_account_number': 'str',
            'shipping_date': 'str',
            'shipping_department_status': 'str',
            'shipping_method': 'str',
            'shipping_method_accounting_code': 'str',
            'special_instructions': 'str',
            'state_region': 'str',
            'title': 'str',
            'tracking_numbers': 'list[str]',
            'weight': 'Weight'
        }

        self.attribute_map = {
            'address1': 'address1',
            'address2': 'address2',
            'city': 'city',
            'company': 'company',
            'country_code': 'country_code',
            'day_phone': 'day_phone',
            'delivery_date': 'delivery_date',
            'evening_phone': 'evening_phone',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'lift_gate': 'lift_gate',
            'postal_code': 'postal_code',
            'rma': 'rma',
            'ship_on_date': 'ship_on_date',
            'ship_to_residential': 'ship_to_residential',
            'shipping_3rd_party_account_number': 'shipping_3rd_party_account_number',
            'shipping_date': 'shipping_date',
            'shipping_department_status': 'shipping_department_status',
            'shipping_method': 'shipping_method',
            'shipping_method_accounting_code': 'shipping_method_accounting_code',
            'special_instructions': 'special_instructions',
            'state_region': 'state_region',
            'title': 'title',
            'tracking_numbers': 'tracking_numbers',
            'weight': 'weight'
        }

        self._address1 = address1
        self._address2 = address2
        self._city = city
        self._company = company
        self._country_code = country_code
        self._day_phone = day_phone
        self._delivery_date = delivery_date
        self._evening_phone = evening_phone
        self._first_name = first_name
        self._last_name = last_name
        self._lift_gate = lift_gate
        self._postal_code = postal_code
        self._rma = rma
        self._ship_on_date = ship_on_date
        self._ship_to_residential = ship_to_residential
        self._shipping_3rd_party_account_number = shipping_3rd_party_account_number
        self._shipping_date = shipping_date
        self._shipping_department_status = shipping_department_status
        self._shipping_method = shipping_method
        self._shipping_method_accounting_code = shipping_method_accounting_code
        self._special_instructions = special_instructions
        self._state_region = state_region
        self._title = title
        self._tracking_numbers = tracking_numbers
        self._weight = weight

    @property
    def address1(self):
        """
        Gets the address1 of this OrderShipping.
        Address line 1

        :return: The address1 of this OrderShipping.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this OrderShipping.
        Address line 1

        :param address1: The address1 of this OrderShipping.
        :type: str
        """

        if not address1:
            raise ValueError("Invalid value for `address1`, must not be `None`")
        if len(address1) > 50:
            raise ValueError("Invalid value for `address1`, length must be less than `50`")

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this OrderShipping.
        Address line 2

        :return: The address2 of this OrderShipping.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this OrderShipping.
        Address line 2

        :param address2: The address2 of this OrderShipping.
        :type: str
        """

        if not address2:
            raise ValueError("Invalid value for `address2`, must not be `None`")
        if len(address2) > 50:
            raise ValueError("Invalid value for `address2`, length must be less than `50`")

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this OrderShipping.
        City

        :return: The city of this OrderShipping.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this OrderShipping.
        City

        :param city: The city of this OrderShipping.
        :type: str
        """

        if not city:
            raise ValueError("Invalid value for `city`, must not be `None`")
        if len(city) > 32:
            raise ValueError("Invalid value for `city`, length must be less than `32`")

        self._city = city

    @property
    def company(self):
        """
        Gets the company of this OrderShipping.
        Company

        :return: The company of this OrderShipping.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this OrderShipping.
        Company

        :param company: The company of this OrderShipping.
        :type: str
        """

        if not company:
            raise ValueError("Invalid value for `company`, must not be `None`")
        if len(company) > 50:
            raise ValueError("Invalid value for `company`, length must be less than `50`")

        self._company = company

    @property
    def country_code(self):
        """
        Gets the country_code of this OrderShipping.
        ISO-3166 two letter country code

        :return: The country_code of this OrderShipping.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this OrderShipping.
        ISO-3166 two letter country code

        :param country_code: The country_code of this OrderShipping.
        :type: str
        """

        if not country_code:
            raise ValueError("Invalid value for `country_code`, must not be `None`")
        if len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than `2`")

        self._country_code = country_code

    @property
    def day_phone(self):
        """
        Gets the day_phone of this OrderShipping.
        Day time phone

        :return: The day_phone of this OrderShipping.
        :rtype: str
        """
        return self._day_phone

    @day_phone.setter
    def day_phone(self, day_phone):
        """
        Sets the day_phone of this OrderShipping.
        Day time phone

        :param day_phone: The day_phone of this OrderShipping.
        :type: str
        """

        if not day_phone:
            raise ValueError("Invalid value for `day_phone`, must not be `None`")
        if len(day_phone) > 25:
            raise ValueError("Invalid value for `day_phone`, length must be less than `25`")

        self._day_phone = day_phone

    @property
    def delivery_date(self):
        """
        Gets the delivery_date of this OrderShipping.
        Date the customer is requesting delivery on.  Typically used for perishable product delivery.

        :return: The delivery_date of this OrderShipping.
        :rtype: str
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """
        Sets the delivery_date of this OrderShipping.
        Date the customer is requesting delivery on.  Typically used for perishable product delivery.

        :param delivery_date: The delivery_date of this OrderShipping.
        :type: str
        """

        self._delivery_date = delivery_date

    @property
    def evening_phone(self):
        """
        Gets the evening_phone of this OrderShipping.
        Evening phone

        :return: The evening_phone of this OrderShipping.
        :rtype: str
        """
        return self._evening_phone

    @evening_phone.setter
    def evening_phone(self, evening_phone):
        """
        Sets the evening_phone of this OrderShipping.
        Evening phone

        :param evening_phone: The evening_phone of this OrderShipping.
        :type: str
        """

        if not evening_phone:
            raise ValueError("Invalid value for `evening_phone`, must not be `None`")
        if len(evening_phone) > 25:
            raise ValueError("Invalid value for `evening_phone`, length must be less than `25`")

        self._evening_phone = evening_phone

    @property
    def first_name(self):
        """
        Gets the first_name of this OrderShipping.
        First name

        :return: The first_name of this OrderShipping.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this OrderShipping.
        First name

        :param first_name: The first_name of this OrderShipping.
        :type: str
        """

        if not first_name:
            raise ValueError("Invalid value for `first_name`, must not be `None`")
        if len(first_name) > 30:
            raise ValueError("Invalid value for `first_name`, length must be less than `30`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this OrderShipping.
        Last name

        :return: The last_name of this OrderShipping.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this OrderShipping.
        Last name

        :param last_name: The last_name of this OrderShipping.
        :type: str
        """

        if not last_name:
            raise ValueError("Invalid value for `last_name`, must not be `None`")
        if len(last_name) > 30:
            raise ValueError("Invalid value for `last_name`, length must be less than `30`")

        self._last_name = last_name

    @property
    def lift_gate(self):
        """
        Gets the lift_gate of this OrderShipping.
        Lift gate requested (LTL shipping methods only)

        :return: The lift_gate of this OrderShipping.
        :rtype: bool
        """
        return self._lift_gate

    @lift_gate.setter
    def lift_gate(self, lift_gate):
        """
        Sets the lift_gate of this OrderShipping.
        Lift gate requested (LTL shipping methods only)

        :param lift_gate: The lift_gate of this OrderShipping.
        :type: bool
        """

        self._lift_gate = lift_gate

    @property
    def postal_code(self):
        """
        Gets the postal_code of this OrderShipping.
        Postal code

        :return: The postal_code of this OrderShipping.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this OrderShipping.
        Postal code

        :param postal_code: The postal_code of this OrderShipping.
        :type: str
        """

        if not postal_code:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")
        if len(postal_code) > 20:
            raise ValueError("Invalid value for `postal_code`, length must be less than `20`")

        self._postal_code = postal_code

    @property
    def rma(self):
        """
        Gets the rma of this OrderShipping.
        RMA number

        :return: The rma of this OrderShipping.
        :rtype: str
        """
        return self._rma

    @rma.setter
    def rma(self, rma):
        """
        Sets the rma of this OrderShipping.
        RMA number

        :param rma: The rma of this OrderShipping.
        :type: str
        """

        if not rma:
            raise ValueError("Invalid value for `rma`, must not be `None`")
        if len(rma) > 30:
            raise ValueError("Invalid value for `rma`, length must be less than `30`")

        self._rma = rma

    @property
    def ship_on_date(self):
        """
        Gets the ship_on_date of this OrderShipping.
        Date the customer is requesting that the order ship on.  Typically used for perishable product delivery.

        :return: The ship_on_date of this OrderShipping.
        :rtype: str
        """
        return self._ship_on_date

    @ship_on_date.setter
    def ship_on_date(self, ship_on_date):
        """
        Sets the ship_on_date of this OrderShipping.
        Date the customer is requesting that the order ship on.  Typically used for perishable product delivery.

        :param ship_on_date: The ship_on_date of this OrderShipping.
        :type: str
        """

        self._ship_on_date = ship_on_date

    @property
    def ship_to_residential(self):
        """
        Gets the ship_to_residential of this OrderShipping.
        True if the shipping address is residential.  Effects the methods that are available to the customer as well as the price of the shipping method.

        :return: The ship_to_residential of this OrderShipping.
        :rtype: bool
        """
        return self._ship_to_residential

    @ship_to_residential.setter
    def ship_to_residential(self, ship_to_residential):
        """
        Sets the ship_to_residential of this OrderShipping.
        True if the shipping address is residential.  Effects the methods that are available to the customer as well as the price of the shipping method.

        :param ship_to_residential: The ship_to_residential of this OrderShipping.
        :type: bool
        """

        self._ship_to_residential = ship_to_residential

    @property
    def shipping_3rd_party_account_number(self):
        """
        Gets the shipping_3rd_party_account_number of this OrderShipping.
        Shipping 3rd party account number

        :return: The shipping_3rd_party_account_number of this OrderShipping.
        :rtype: str
        """
        return self._shipping_3rd_party_account_number

    @shipping_3rd_party_account_number.setter
    def shipping_3rd_party_account_number(self, shipping_3rd_party_account_number):
        """
        Sets the shipping_3rd_party_account_number of this OrderShipping.
        Shipping 3rd party account number

        :param shipping_3rd_party_account_number: The shipping_3rd_party_account_number of this OrderShipping.
        :type: str
        """

        if not shipping_3rd_party_account_number:
            raise ValueError("Invalid value for `shipping_3rd_party_account_number`, must not be `None`")
        if len(shipping_3rd_party_account_number) > 20:
            raise ValueError("Invalid value for `shipping_3rd_party_account_number`, length must be less than `20`")

        self._shipping_3rd_party_account_number = shipping_3rd_party_account_number

    @property
    def shipping_date(self):
        """
        Gets the shipping_date of this OrderShipping.
        Date/time the order shipped on.  This date is set once the first shipment is sent to the customer.

        :return: The shipping_date of this OrderShipping.
        :rtype: str
        """
        return self._shipping_date

    @shipping_date.setter
    def shipping_date(self, shipping_date):
        """
        Sets the shipping_date of this OrderShipping.
        Date/time the order shipped on.  This date is set once the first shipment is sent to the customer.

        :param shipping_date: The shipping_date of this OrderShipping.
        :type: str
        """

        self._shipping_date = shipping_date

    @property
    def shipping_department_status(self):
        """
        Gets the shipping_department_status of this OrderShipping.
        Shipping department status

        :return: The shipping_department_status of this OrderShipping.
        :rtype: str
        """
        return self._shipping_department_status

    @shipping_department_status.setter
    def shipping_department_status(self, shipping_department_status):
        """
        Sets the shipping_department_status of this OrderShipping.
        Shipping department status

        :param shipping_department_status: The shipping_department_status of this OrderShipping.
        :type: str
        """

        if not shipping_department_status:
            raise ValueError("Invalid value for `shipping_department_status`, must not be `None`")
        if len(shipping_department_status) > 30:
            raise ValueError("Invalid value for `shipping_department_status`, length must be less than `30`")

        self._shipping_department_status = shipping_department_status

    @property
    def shipping_method(self):
        """
        Gets the shipping_method of this OrderShipping.
        Shipping method

        :return: The shipping_method of this OrderShipping.
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """
        Sets the shipping_method of this OrderShipping.
        Shipping method

        :param shipping_method: The shipping_method of this OrderShipping.
        :type: str
        """

        self._shipping_method = shipping_method

    @property
    def shipping_method_accounting_code(self):
        """
        Gets the shipping_method_accounting_code of this OrderShipping.
        Shipping method accounting code

        :return: The shipping_method_accounting_code of this OrderShipping.
        :rtype: str
        """
        return self._shipping_method_accounting_code

    @shipping_method_accounting_code.setter
    def shipping_method_accounting_code(self, shipping_method_accounting_code):
        """
        Sets the shipping_method_accounting_code of this OrderShipping.
        Shipping method accounting code

        :param shipping_method_accounting_code: The shipping_method_accounting_code of this OrderShipping.
        :type: str
        """

        self._shipping_method_accounting_code = shipping_method_accounting_code

    @property
    def special_instructions(self):
        """
        Gets the special_instructions of this OrderShipping.
        Special instructions from the customer regarding shipping

        :return: The special_instructions of this OrderShipping.
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """
        Sets the special_instructions of this OrderShipping.
        Special instructions from the customer regarding shipping

        :param special_instructions: The special_instructions of this OrderShipping.
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def state_region(self):
        """
        Gets the state_region of this OrderShipping.
        State

        :return: The state_region of this OrderShipping.
        :rtype: str
        """
        return self._state_region

    @state_region.setter
    def state_region(self, state_region):
        """
        Sets the state_region of this OrderShipping.
        State

        :param state_region: The state_region of this OrderShipping.
        :type: str
        """

        if not state_region:
            raise ValueError("Invalid value for `state_region`, must not be `None`")
        if len(state_region) > 32:
            raise ValueError("Invalid value for `state_region`, length must be less than `32`")

        self._state_region = state_region

    @property
    def title(self):
        """
        Gets the title of this OrderShipping.
        Title

        :return: The title of this OrderShipping.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this OrderShipping.
        Title

        :param title: The title of this OrderShipping.
        :type: str
        """

        if not title:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if len(title) > 50:
            raise ValueError("Invalid value for `title`, length must be less than `50`")

        self._title = title

    @property
    def tracking_numbers(self):
        """
        Gets the tracking_numbers of this OrderShipping.
        Tracking numbers

        :return: The tracking_numbers of this OrderShipping.
        :rtype: list[str]
        """
        return self._tracking_numbers

    @tracking_numbers.setter
    def tracking_numbers(self, tracking_numbers):
        """
        Sets the tracking_numbers of this OrderShipping.
        Tracking numbers

        :param tracking_numbers: The tracking_numbers of this OrderShipping.
        :type: list[str]
        """

        self._tracking_numbers = tracking_numbers

    @property
    def weight(self):
        """
        Gets the weight of this OrderShipping.


        :return: The weight of this OrderShipping.
        :rtype: Weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this OrderShipping.


        :param weight: The weight of this OrderShipping.
        :type: Weight
        """

        self._weight = weight

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