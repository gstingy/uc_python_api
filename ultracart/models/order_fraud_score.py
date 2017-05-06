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


class OrderFraudScore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anonymous_proxy=None, bin_match=None, carder_email=None, country_code=None, country_match=None, customer_phone_in_billing_location=None, distance_km=None, free_email=None, high_risk_country=None, ip_city=None, ip_isp=None, ip_latitude=None, ip_longitude=None, ip_org=None, ip_region=None, proxy_score=None, score=None, ship_forwarder=None, spam_score=None, transparent_proxy=None):
        """
        OrderFraudScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'anonymous_proxy': 'bool',
            'bin_match': 'str',
            'carder_email': 'bool',
            'country_code': 'str',
            'country_match': 'bool',
            'customer_phone_in_billing_location': 'str',
            'distance_km': 'int',
            'free_email': 'bool',
            'high_risk_country': 'bool',
            'ip_city': 'str',
            'ip_isp': 'str',
            'ip_latitude': 'str',
            'ip_longitude': 'str',
            'ip_org': 'str',
            'ip_region': 'str',
            'proxy_score': 'float',
            'score': 'float',
            'ship_forwarder': 'bool',
            'spam_score': 'float',
            'transparent_proxy': 'bool'
        }

        self.attribute_map = {
            'anonymous_proxy': 'anonymous_proxy',
            'bin_match': 'bin_match',
            'carder_email': 'carder_email',
            'country_code': 'country_code',
            'country_match': 'country_match',
            'customer_phone_in_billing_location': 'customer_phone_in_billing_location',
            'distance_km': 'distance_km',
            'free_email': 'free_email',
            'high_risk_country': 'high_risk_country',
            'ip_city': 'ip_city',
            'ip_isp': 'ip_isp',
            'ip_latitude': 'ip_latitude',
            'ip_longitude': 'ip_longitude',
            'ip_org': 'ip_org',
            'ip_region': 'ip_region',
            'proxy_score': 'proxy_score',
            'score': 'score',
            'ship_forwarder': 'ship_forwarder',
            'spam_score': 'spam_score',
            'transparent_proxy': 'transparent_proxy'
        }

        self._anonymous_proxy = anonymous_proxy
        self._bin_match = bin_match
        self._carder_email = carder_email
        self._country_code = country_code
        self._country_match = country_match
        self._customer_phone_in_billing_location = customer_phone_in_billing_location
        self._distance_km = distance_km
        self._free_email = free_email
        self._high_risk_country = high_risk_country
        self._ip_city = ip_city
        self._ip_isp = ip_isp
        self._ip_latitude = ip_latitude
        self._ip_longitude = ip_longitude
        self._ip_org = ip_org
        self._ip_region = ip_region
        self._proxy_score = proxy_score
        self._score = score
        self._ship_forwarder = ship_forwarder
        self._spam_score = spam_score
        self._transparent_proxy = transparent_proxy

    @property
    def anonymous_proxy(self):
        """
        Gets the anonymous_proxy of this OrderFraudScore.
        True if the IP address is a known anonymous proxy server

        :return: The anonymous_proxy of this OrderFraudScore.
        :rtype: bool
        """
        return self._anonymous_proxy

    @anonymous_proxy.setter
    def anonymous_proxy(self, anonymous_proxy):
        """
        Sets the anonymous_proxy of this OrderFraudScore.
        True if the IP address is a known anonymous proxy server

        :param anonymous_proxy: The anonymous_proxy of this OrderFraudScore.
        :type: bool
        """

        self._anonymous_proxy = anonymous_proxy

    @property
    def bin_match(self):
        """
        Gets the bin_match of this OrderFraudScore.
        Whether the BIN (first six digits) matched the country

        :return: The bin_match of this OrderFraudScore.
        :rtype: str
        """
        return self._bin_match

    @bin_match.setter
    def bin_match(self, bin_match):
        """
        Sets the bin_match of this OrderFraudScore.
        Whether the BIN (first six digits) matched the country

        :param bin_match: The bin_match of this OrderFraudScore.
        :type: str
        """
        allowed_values = ["NA", "No", "NotFound", "Yes"]
        if bin_match not in allowed_values:
            raise ValueError(
                "Invalid value for `bin_match` ({0}), must be one of {1}"
                .format(bin_match, allowed_values)
            )

        self._bin_match = bin_match

    @property
    def carder_email(self):
        """
        Gets the carder_email of this OrderFraudScore.
        True if the email address belongs to a known credit card fraudster

        :return: The carder_email of this OrderFraudScore.
        :rtype: bool
        """
        return self._carder_email

    @carder_email.setter
    def carder_email(self, carder_email):
        """
        Sets the carder_email of this OrderFraudScore.
        True if the email address belongs to a known credit card fraudster

        :param carder_email: The carder_email of this OrderFraudScore.
        :type: bool
        """

        self._carder_email = carder_email

    @property
    def country_code(self):
        """
        Gets the country_code of this OrderFraudScore.
        Country code

        :return: The country_code of this OrderFraudScore.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this OrderFraudScore.
        Country code

        :param country_code: The country_code of this OrderFraudScore.
        :type: str
        """

        self._country_code = country_code

    @property
    def country_match(self):
        """
        Gets the country_match of this OrderFraudScore.
        Country code matches BIN country

        :return: The country_match of this OrderFraudScore.
        :rtype: bool
        """
        return self._country_match

    @country_match.setter
    def country_match(self, country_match):
        """
        Sets the country_match of this OrderFraudScore.
        Country code matches BIN country

        :param country_match: The country_match of this OrderFraudScore.
        :type: bool
        """

        self._country_match = country_match

    @property
    def customer_phone_in_billing_location(self):
        """
        Gets the customer_phone_in_billing_location of this OrderFraudScore.
        Whether the customer's phone number is located in the area of the billing address

        :return: The customer_phone_in_billing_location of this OrderFraudScore.
        :rtype: str
        """
        return self._customer_phone_in_billing_location

    @customer_phone_in_billing_location.setter
    def customer_phone_in_billing_location(self, customer_phone_in_billing_location):
        """
        Sets the customer_phone_in_billing_location of this OrderFraudScore.
        Whether the customer's phone number is located in the area of the billing address

        :param customer_phone_in_billing_location: The customer_phone_in_billing_location of this OrderFraudScore.
        :type: str
        """
        allowed_values = ["", "No", "NotFound", "Yes"]
        if customer_phone_in_billing_location not in allowed_values:
            raise ValueError(
                "Invalid value for `customer_phone_in_billing_location` ({0}), must be one of {1}"
                .format(customer_phone_in_billing_location, allowed_values)
            )

        self._customer_phone_in_billing_location = customer_phone_in_billing_location

    @property
    def distance_km(self):
        """
        Gets the distance_km of this OrderFraudScore.
        Distance in kilometers between the IP address and the BIN

        :return: The distance_km of this OrderFraudScore.
        :rtype: int
        """
        return self._distance_km

    @distance_km.setter
    def distance_km(self, distance_km):
        """
        Sets the distance_km of this OrderFraudScore.
        Distance in kilometers between the IP address and the BIN

        :param distance_km: The distance_km of this OrderFraudScore.
        :type: int
        """

        self._distance_km = distance_km

    @property
    def free_email(self):
        """
        Gets the free_email of this OrderFraudScore.
        True if the email address is for a free service like gmail.com

        :return: The free_email of this OrderFraudScore.
        :rtype: bool
        """
        return self._free_email

    @free_email.setter
    def free_email(self, free_email):
        """
        Sets the free_email of this OrderFraudScore.
        True if the email address is for a free service like gmail.com

        :param free_email: The free_email of this OrderFraudScore.
        :type: bool
        """

        self._free_email = free_email

    @property
    def high_risk_country(self):
        """
        Gets the high_risk_country of this OrderFraudScore.
        True if the customer is in a high risk country known for internet fraud

        :return: The high_risk_country of this OrderFraudScore.
        :rtype: bool
        """
        return self._high_risk_country

    @high_risk_country.setter
    def high_risk_country(self, high_risk_country):
        """
        Sets the high_risk_country of this OrderFraudScore.
        True if the customer is in a high risk country known for internet fraud

        :param high_risk_country: The high_risk_country of this OrderFraudScore.
        :type: bool
        """

        self._high_risk_country = high_risk_country

    @property
    def ip_city(self):
        """
        Gets the ip_city of this OrderFraudScore.
        City associated with the IP address

        :return: The ip_city of this OrderFraudScore.
        :rtype: str
        """
        return self._ip_city

    @ip_city.setter
    def ip_city(self, ip_city):
        """
        Sets the ip_city of this OrderFraudScore.
        City associated with the IP address

        :param ip_city: The ip_city of this OrderFraudScore.
        :type: str
        """

        self._ip_city = ip_city

    @property
    def ip_isp(self):
        """
        Gets the ip_isp of this OrderFraudScore.
        ISP that owns the IP address

        :return: The ip_isp of this OrderFraudScore.
        :rtype: str
        """
        return self._ip_isp

    @ip_isp.setter
    def ip_isp(self, ip_isp):
        """
        Sets the ip_isp of this OrderFraudScore.
        ISP that owns the IP address

        :param ip_isp: The ip_isp of this OrderFraudScore.
        :type: str
        """

        self._ip_isp = ip_isp

    @property
    def ip_latitude(self):
        """
        Gets the ip_latitude of this OrderFraudScore.
        Approximate latitude associated with the IP address

        :return: The ip_latitude of this OrderFraudScore.
        :rtype: str
        """
        return self._ip_latitude

    @ip_latitude.setter
    def ip_latitude(self, ip_latitude):
        """
        Sets the ip_latitude of this OrderFraudScore.
        Approximate latitude associated with the IP address

        :param ip_latitude: The ip_latitude of this OrderFraudScore.
        :type: str
        """

        self._ip_latitude = ip_latitude

    @property
    def ip_longitude(self):
        """
        Gets the ip_longitude of this OrderFraudScore.
        Approximate longitude associated with the IP address

        :return: The ip_longitude of this OrderFraudScore.
        :rtype: str
        """
        return self._ip_longitude

    @ip_longitude.setter
    def ip_longitude(self, ip_longitude):
        """
        Sets the ip_longitude of this OrderFraudScore.
        Approximate longitude associated with the IP address

        :param ip_longitude: The ip_longitude of this OrderFraudScore.
        :type: str
        """

        self._ip_longitude = ip_longitude

    @property
    def ip_org(self):
        """
        Gets the ip_org of this OrderFraudScore.
        Organization that owns the IP address

        :return: The ip_org of this OrderFraudScore.
        :rtype: str
        """
        return self._ip_org

    @ip_org.setter
    def ip_org(self, ip_org):
        """
        Sets the ip_org of this OrderFraudScore.
        Organization that owns the IP address

        :param ip_org: The ip_org of this OrderFraudScore.
        :type: str
        """

        self._ip_org = ip_org

    @property
    def ip_region(self):
        """
        Gets the ip_region of this OrderFraudScore.
        State/region associated with the IP address

        :return: The ip_region of this OrderFraudScore.
        :rtype: str
        """
        return self._ip_region

    @ip_region.setter
    def ip_region(self, ip_region):
        """
        Sets the ip_region of this OrderFraudScore.
        State/region associated with the IP address

        :param ip_region: The ip_region of this OrderFraudScore.
        :type: str
        """

        self._ip_region = ip_region

    @property
    def proxy_score(self):
        """
        Gets the proxy_score of this OrderFraudScore.
        Likelihood of the IP address being a proxy server

        :return: The proxy_score of this OrderFraudScore.
        :rtype: float
        """
        return self._proxy_score

    @proxy_score.setter
    def proxy_score(self, proxy_score):
        """
        Sets the proxy_score of this OrderFraudScore.
        Likelihood of the IP address being a proxy server

        :param proxy_score: The proxy_score of this OrderFraudScore.
        :type: float
        """

        self._proxy_score = proxy_score

    @property
    def score(self):
        """
        Gets the score of this OrderFraudScore.
        Overall score.  This is the score that is compared to see if the order is rejected or held for review by the fraud filter rules.

        :return: The score of this OrderFraudScore.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this OrderFraudScore.
        Overall score.  This is the score that is compared to see if the order is rejected or held for review by the fraud filter rules.

        :param score: The score of this OrderFraudScore.
        :type: float
        """

        self._score = score

    @property
    def ship_forwarder(self):
        """
        Gets the ship_forwarder of this OrderFraudScore.
        True if the address is a known ship forwarding company

        :return: The ship_forwarder of this OrderFraudScore.
        :rtype: bool
        """
        return self._ship_forwarder

    @ship_forwarder.setter
    def ship_forwarder(self, ship_forwarder):
        """
        Sets the ship_forwarder of this OrderFraudScore.
        True if the address is a known ship forwarding company

        :param ship_forwarder: The ship_forwarder of this OrderFraudScore.
        :type: bool
        """

        self._ship_forwarder = ship_forwarder

    @property
    def spam_score(self):
        """
        Gets the spam_score of this OrderFraudScore.
        Likelihood of the email address being associated with a spammer

        :return: The spam_score of this OrderFraudScore.
        :rtype: float
        """
        return self._spam_score

    @spam_score.setter
    def spam_score(self, spam_score):
        """
        Sets the spam_score of this OrderFraudScore.
        Likelihood of the email address being associated with a spammer

        :param spam_score: The spam_score of this OrderFraudScore.
        :type: float
        """

        self._spam_score = spam_score

    @property
    def transparent_proxy(self):
        """
        Gets the transparent_proxy of this OrderFraudScore.
        True if the IP address that placed the order is a transparent proxy server

        :return: The transparent_proxy of this OrderFraudScore.
        :rtype: bool
        """
        return self._transparent_proxy

    @transparent_proxy.setter
    def transparent_proxy(self, transparent_proxy):
        """
        Sets the transparent_proxy of this OrderFraudScore.
        True if the IP address that placed the order is a transparent proxy server

        :param transparent_proxy: The transparent_proxy of this OrderFraudScore.
        :type: bool
        """

        self._transparent_proxy = transparent_proxy

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