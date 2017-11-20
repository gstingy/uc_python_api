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


class CartBilling(object):
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
        'cc_emails': 'list[str]',
        'city': 'str',
        'company': 'str',
        'country_code': 'str',
        'day_phone': 'str',
        'email': 'str',
        'email_confirm': 'str',
        'evening_phone': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'postal_code': 'str',
        'state_region': 'str',
        'title': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'cc_emails': 'cc_emails',
        'city': 'city',
        'company': 'company',
        'country_code': 'country_code',
        'day_phone': 'day_phone',
        'email': 'email',
        'email_confirm': 'email_confirm',
        'evening_phone': 'evening_phone',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'postal_code': 'postal_code',
        'state_region': 'state_region',
        'title': 'title'
    }

    def __init__(self, address1=None, address2=None, cc_emails=None, city=None, company=None, country_code=None, day_phone=None, email=None, email_confirm=None, evening_phone=None, first_name=None, last_name=None, postal_code=None, state_region=None, title=None):
        """
        CartBilling - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._cc_emails = None
        self._city = None
        self._company = None
        self._country_code = None
        self._day_phone = None
        self._email = None
        self._email_confirm = None
        self._evening_phone = None
        self._first_name = None
        self._last_name = None
        self._postal_code = None
        self._state_region = None
        self._title = None
        self.discriminator = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if cc_emails is not None:
          self.cc_emails = cc_emails
        if city is not None:
          self.city = city
        if company is not None:
          self.company = company
        if country_code is not None:
          self.country_code = country_code
        if day_phone is not None:
          self.day_phone = day_phone
        if email is not None:
          self.email = email
        if email_confirm is not None:
          self.email_confirm = email_confirm
        if evening_phone is not None:
          self.evening_phone = evening_phone
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if postal_code is not None:
          self.postal_code = postal_code
        if state_region is not None:
          self.state_region = state_region
        if title is not None:
          self.title = title

    @property
    def address1(self):
        """
        Gets the address1 of this CartBilling.
        Address line 1

        :return: The address1 of this CartBilling.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this CartBilling.
        Address line 1

        :param address1: The address1 of this CartBilling.
        :type: str
        """
        if address1 is not None and len(address1) > 50:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `50`")

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this CartBilling.
        Address line 2

        :return: The address2 of this CartBilling.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this CartBilling.
        Address line 2

        :param address2: The address2 of this CartBilling.
        :type: str
        """
        if address2 is not None and len(address2) > 50:
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `50`")

        self._address2 = address2

    @property
    def cc_emails(self):
        """
        Gets the cc_emails of this CartBilling.
        CC emails.  Multiple allowed, but total length of all emails can not exceed 100 characters.

        :return: The cc_emails of this CartBilling.
        :rtype: list[str]
        """
        return self._cc_emails

    @cc_emails.setter
    def cc_emails(self, cc_emails):
        """
        Sets the cc_emails of this CartBilling.
        CC emails.  Multiple allowed, but total length of all emails can not exceed 100 characters.

        :param cc_emails: The cc_emails of this CartBilling.
        :type: list[str]
        """

        self._cc_emails = cc_emails

    @property
    def city(self):
        """
        Gets the city of this CartBilling.
        City

        :return: The city of this CartBilling.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this CartBilling.
        City

        :param city: The city of this CartBilling.
        :type: str
        """
        if city is not None and len(city) > 32:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `32`")

        self._city = city

    @property
    def company(self):
        """
        Gets the company of this CartBilling.
        Company

        :return: The company of this CartBilling.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this CartBilling.
        Company

        :param company: The company of this CartBilling.
        :type: str
        """
        if company is not None and len(company) > 50:
            raise ValueError("Invalid value for `company`, length must be less than or equal to `50`")

        self._company = company

    @property
    def country_code(self):
        """
        Gets the country_code of this CartBilling.
        ISO-3166 two letter country code

        :return: The country_code of this CartBilling.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this CartBilling.
        ISO-3166 two letter country code

        :param country_code: The country_code of this CartBilling.
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")

        self._country_code = country_code

    @property
    def day_phone(self):
        """
        Gets the day_phone of this CartBilling.
        Day phone

        :return: The day_phone of this CartBilling.
        :rtype: str
        """
        return self._day_phone

    @day_phone.setter
    def day_phone(self, day_phone):
        """
        Sets the day_phone of this CartBilling.
        Day phone

        :param day_phone: The day_phone of this CartBilling.
        :type: str
        """
        if day_phone is not None and len(day_phone) > 25:
            raise ValueError("Invalid value for `day_phone`, length must be less than or equal to `25`")

        self._day_phone = day_phone

    @property
    def email(self):
        """
        Gets the email of this CartBilling.
        Email

        :return: The email of this CartBilling.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CartBilling.
        Email

        :param email: The email of this CartBilling.
        :type: str
        """
        if email is not None and len(email) > 100:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")

        self._email = email

    @property
    def email_confirm(self):
        """
        Gets the email_confirm of this CartBilling.
        Email entered for confirmation

        :return: The email_confirm of this CartBilling.
        :rtype: str
        """
        return self._email_confirm

    @email_confirm.setter
    def email_confirm(self, email_confirm):
        """
        Sets the email_confirm of this CartBilling.
        Email entered for confirmation

        :param email_confirm: The email_confirm of this CartBilling.
        :type: str
        """
        if email_confirm is not None and len(email_confirm) > 100:
            raise ValueError("Invalid value for `email_confirm`, length must be less than or equal to `100`")

        self._email_confirm = email_confirm

    @property
    def evening_phone(self):
        """
        Gets the evening_phone of this CartBilling.
        Evening phone

        :return: The evening_phone of this CartBilling.
        :rtype: str
        """
        return self._evening_phone

    @evening_phone.setter
    def evening_phone(self, evening_phone):
        """
        Sets the evening_phone of this CartBilling.
        Evening phone

        :param evening_phone: The evening_phone of this CartBilling.
        :type: str
        """
        if evening_phone is not None and len(evening_phone) > 25:
            raise ValueError("Invalid value for `evening_phone`, length must be less than or equal to `25`")

        self._evening_phone = evening_phone

    @property
    def first_name(self):
        """
        Gets the first_name of this CartBilling.
        First name

        :return: The first_name of this CartBilling.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CartBilling.
        First name

        :param first_name: The first_name of this CartBilling.
        :type: str
        """
        if first_name is not None and len(first_name) > 30:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this CartBilling.
        Last name

        :return: The last_name of this CartBilling.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CartBilling.
        Last name

        :param last_name: The last_name of this CartBilling.
        :type: str
        """
        if last_name is not None and len(last_name) > 30:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `30`")

        self._last_name = last_name

    @property
    def postal_code(self):
        """
        Gets the postal_code of this CartBilling.
        Postal code

        :return: The postal_code of this CartBilling.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this CartBilling.
        Postal code

        :param postal_code: The postal_code of this CartBilling.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 20:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `20`")

        self._postal_code = postal_code

    @property
    def state_region(self):
        """
        Gets the state_region of this CartBilling.
        State for United States otherwise region or province for other countries

        :return: The state_region of this CartBilling.
        :rtype: str
        """
        return self._state_region

    @state_region.setter
    def state_region(self, state_region):
        """
        Sets the state_region of this CartBilling.
        State for United States otherwise region or province for other countries

        :param state_region: The state_region of this CartBilling.
        :type: str
        """
        if state_region is not None and len(state_region) > 32:
            raise ValueError("Invalid value for `state_region`, length must be less than or equal to `32`")

        self._state_region = state_region

    @property
    def title(self):
        """
        Gets the title of this CartBilling.
        Title

        :return: The title of this CartBilling.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CartBilling.
        Title

        :param title: The title of this CartBilling.
        :type: str
        """
        if title is not None and len(title) > 50:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `50`")

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
        if not isinstance(other, CartBilling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
