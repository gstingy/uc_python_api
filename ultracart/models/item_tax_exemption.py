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


class ItemTaxExemption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, city=None, country_code=None, county=None, postal_code=None, state_code=None):
        """
        ItemTaxExemption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'city': 'str',
            'country_code': 'str',
            'county': 'str',
            'postal_code': 'str',
            'state_code': 'str'
        }

        self.attribute_map = {
            'city': 'city',
            'country_code': 'country_code',
            'county': 'county',
            'postal_code': 'postal_code',
            'state_code': 'state_code'
        }

        self._city = city
        self._country_code = country_code
        self._county = county
        self._postal_code = postal_code
        self._state_code = state_code

    @property
    def city(self):
        """
        Gets the city of this ItemTaxExemption.
        City

        :return: The city of this ItemTaxExemption.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this ItemTaxExemption.
        City

        :param city: The city of this ItemTaxExemption.
        :type: str
        """

        if not city:
            raise ValueError("Invalid value for `city`, must not be `None`")
        if len(city) > 32:
            raise ValueError("Invalid value for `city`, length must be less than `32`")

        self._city = city

    @property
    def country_code(self):
        """
        Gets the country_code of this ItemTaxExemption.
        Country code (ISO-3166 two letter)

        :return: The country_code of this ItemTaxExemption.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this ItemTaxExemption.
        Country code (ISO-3166 two letter)

        :param country_code: The country_code of this ItemTaxExemption.
        :type: str
        """

        if not country_code:
            raise ValueError("Invalid value for `country_code`, must not be `None`")
        if len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than `2`")

        self._country_code = country_code

    @property
    def county(self):
        """
        Gets the county of this ItemTaxExemption.
        County

        :return: The county of this ItemTaxExemption.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this ItemTaxExemption.
        County

        :param county: The county of this ItemTaxExemption.
        :type: str
        """

        if not county:
            raise ValueError("Invalid value for `county`, must not be `None`")
        if len(county) > 32:
            raise ValueError("Invalid value for `county`, length must be less than `32`")

        self._county = county

    @property
    def postal_code(self):
        """
        Gets the postal_code of this ItemTaxExemption.
        Postal code

        :return: The postal_code of this ItemTaxExemption.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this ItemTaxExemption.
        Postal code

        :param postal_code: The postal_code of this ItemTaxExemption.
        :type: str
        """

        if not postal_code:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")
        if len(postal_code) > 20:
            raise ValueError("Invalid value for `postal_code`, length must be less than `20`")

        self._postal_code = postal_code

    @property
    def state_code(self):
        """
        Gets the state_code of this ItemTaxExemption.
        State code

        :return: The state_code of this ItemTaxExemption.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """
        Sets the state_code of this ItemTaxExemption.
        State code

        :param state_code: The state_code of this ItemTaxExemption.
        :type: str
        """

        if not state_code:
            raise ValueError("Invalid value for `state_code`, must not be `None`")
        if len(state_code) > 32:
            raise ValueError("Invalid value for `state_code`, length must be less than `32`")

        self._state_code = state_code

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
