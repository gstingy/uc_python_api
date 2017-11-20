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


class CartCustomerProfileAddress(object):
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
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'company': 'str',
        'country_code': 'str',
        'day_phone': 'str',
        'evening_phone': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'oid': 'int',
        'postal_code': 'str',
        'state_region': 'str',
        'tax_county': 'str',
        'title': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'company': 'company',
        'country_code': 'country_code',
        'day_phone': 'day_phone',
        'evening_phone': 'evening_phone',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'oid': 'oid',
        'postal_code': 'postal_code',
        'state_region': 'state_region',
        'tax_county': 'tax_county',
        'title': 'title'
    }

    def __init__(self, address1=None, address2=None, city=None, company=None, country_code=None, day_phone=None, evening_phone=None, first_name=None, last_name=None, oid=None, postal_code=None, state_region=None, tax_county=None, title=None):
        """
        CartCustomerProfileAddress - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._city = None
        self._company = None
        self._country_code = None
        self._day_phone = None
        self._evening_phone = None
        self._first_name = None
        self._last_name = None
        self._oid = None
        self._postal_code = None
        self._state_region = None
        self._tax_county = None
        self._title = None
        self.discriminator = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if city is not None:
          self.city = city
        if company is not None:
          self.company = company
        if country_code is not None:
          self.country_code = country_code
        if day_phone is not None:
          self.day_phone = day_phone
        if evening_phone is not None:
          self.evening_phone = evening_phone
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if oid is not None:
          self.oid = oid
        if postal_code is not None:
          self.postal_code = postal_code
        if state_region is not None:
          self.state_region = state_region
        if tax_county is not None:
          self.tax_county = tax_county
        if title is not None:
          self.title = title

    @property
    def address1(self):
        """
        Gets the address1 of this CartCustomerProfileAddress.
        Address 1

        :return: The address1 of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this CartCustomerProfileAddress.
        Address 1

        :param address1: The address1 of this CartCustomerProfileAddress.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this CartCustomerProfileAddress.
        Address 2

        :return: The address2 of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this CartCustomerProfileAddress.
        Address 2

        :param address2: The address2 of this CartCustomerProfileAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this CartCustomerProfileAddress.
        City

        :return: The city of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this CartCustomerProfileAddress.
        City

        :param city: The city of this CartCustomerProfileAddress.
        :type: str
        """

        self._city = city

    @property
    def company(self):
        """
        Gets the company of this CartCustomerProfileAddress.
        Company

        :return: The company of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this CartCustomerProfileAddress.
        Company

        :param company: The company of this CartCustomerProfileAddress.
        :type: str
        """

        self._company = company

    @property
    def country_code(self):
        """
        Gets the country_code of this CartCustomerProfileAddress.
        ISO-3166 Country code

        :return: The country_code of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this CartCustomerProfileAddress.
        ISO-3166 Country code

        :param country_code: The country_code of this CartCustomerProfileAddress.
        :type: str
        """

        self._country_code = country_code

    @property
    def day_phone(self):
        """
        Gets the day_phone of this CartCustomerProfileAddress.
        Day phone

        :return: The day_phone of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._day_phone

    @day_phone.setter
    def day_phone(self, day_phone):
        """
        Sets the day_phone of this CartCustomerProfileAddress.
        Day phone

        :param day_phone: The day_phone of this CartCustomerProfileAddress.
        :type: str
        """

        self._day_phone = day_phone

    @property
    def evening_phone(self):
        """
        Gets the evening_phone of this CartCustomerProfileAddress.
        Evening phone

        :return: The evening_phone of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._evening_phone

    @evening_phone.setter
    def evening_phone(self, evening_phone):
        """
        Sets the evening_phone of this CartCustomerProfileAddress.
        Evening phone

        :param evening_phone: The evening_phone of this CartCustomerProfileAddress.
        :type: str
        """

        self._evening_phone = evening_phone

    @property
    def first_name(self):
        """
        Gets the first_name of this CartCustomerProfileAddress.
        First name

        :return: The first_name of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CartCustomerProfileAddress.
        First name

        :param first_name: The first_name of this CartCustomerProfileAddress.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this CartCustomerProfileAddress.
        Last name

        :return: The last_name of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CartCustomerProfileAddress.
        Last name

        :param last_name: The last_name of this CartCustomerProfileAddress.
        :type: str
        """

        self._last_name = last_name

    @property
    def oid(self):
        """
        Gets the oid of this CartCustomerProfileAddress.
        Unique identifier for this address

        :return: The oid of this CartCustomerProfileAddress.
        :rtype: int
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """
        Sets the oid of this CartCustomerProfileAddress.
        Unique identifier for this address

        :param oid: The oid of this CartCustomerProfileAddress.
        :type: int
        """

        self._oid = oid

    @property
    def postal_code(self):
        """
        Gets the postal_code of this CartCustomerProfileAddress.
        Postal code

        :return: The postal_code of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this CartCustomerProfileAddress.
        Postal code

        :param postal_code: The postal_code of this CartCustomerProfileAddress.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_region(self):
        """
        Gets the state_region of this CartCustomerProfileAddress.
        State for United States otherwise region or province for other countries

        :return: The state_region of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._state_region

    @state_region.setter
    def state_region(self, state_region):
        """
        Sets the state_region of this CartCustomerProfileAddress.
        State for United States otherwise region or province for other countries

        :param state_region: The state_region of this CartCustomerProfileAddress.
        :type: str
        """

        self._state_region = state_region

    @property
    def tax_county(self):
        """
        Gets the tax_county of this CartCustomerProfileAddress.
        Tax county if a billing address

        :return: The tax_county of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._tax_county

    @tax_county.setter
    def tax_county(self, tax_county):
        """
        Sets the tax_county of this CartCustomerProfileAddress.
        Tax county if a billing address

        :param tax_county: The tax_county of this CartCustomerProfileAddress.
        :type: str
        """

        self._tax_county = tax_county

    @property
    def title(self):
        """
        Gets the title of this CartCustomerProfileAddress.
        Title

        :return: The title of this CartCustomerProfileAddress.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CartCustomerProfileAddress.
        Title

        :param title: The title of this CartCustomerProfileAddress.
        :type: str
        """

        self._title = title

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
        if not isinstance(other, CartCustomerProfileAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
