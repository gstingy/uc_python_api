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


class ItemPricing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allow_arbitrary_cost=None, arbitrary_cost_velocity_code=None, automatic_pricing_tier_name=None, automatic_pricing_tier_oid=None, cogs=None, cost=None, currency_code=None, manufacturer_suggested_retail_price=None, maximum_arbitrary_cost=None, minimum_advertised_price=None, minimum_arbitrary_cost=None, mix_and_match_group=None, mix_and_match_group_oid=None, sale_cost=None, sale_end=None, sale_start=None, tiers=None):
        """
        ItemPricing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_arbitrary_cost': 'bool',
            'arbitrary_cost_velocity_code': 'str',
            'automatic_pricing_tier_name': 'str',
            'automatic_pricing_tier_oid': 'int',
            'cogs': 'float',
            'cost': 'float',
            'currency_code': 'str',
            'manufacturer_suggested_retail_price': 'float',
            'maximum_arbitrary_cost': 'float',
            'minimum_advertised_price': 'float',
            'minimum_arbitrary_cost': 'float',
            'mix_and_match_group': 'str',
            'mix_and_match_group_oid': 'int',
            'sale_cost': 'float',
            'sale_end': 'str',
            'sale_start': 'str',
            'tiers': 'list[ItemPricingTier]'
        }

        self.attribute_map = {
            'allow_arbitrary_cost': 'allow_arbitrary_cost',
            'arbitrary_cost_velocity_code': 'arbitrary_cost_velocity_code',
            'automatic_pricing_tier_name': 'automatic_pricing_tier_name',
            'automatic_pricing_tier_oid': 'automatic_pricing_tier_oid',
            'cogs': 'cogs',
            'cost': 'cost',
            'currency_code': 'currency_code',
            'manufacturer_suggested_retail_price': 'manufacturer_suggested_retail_price',
            'maximum_arbitrary_cost': 'maximum_arbitrary_cost',
            'minimum_advertised_price': 'minimum_advertised_price',
            'minimum_arbitrary_cost': 'minimum_arbitrary_cost',
            'mix_and_match_group': 'mix_and_match_group',
            'mix_and_match_group_oid': 'mix_and_match_group_oid',
            'sale_cost': 'sale_cost',
            'sale_end': 'sale_end',
            'sale_start': 'sale_start',
            'tiers': 'tiers'
        }

        self._allow_arbitrary_cost = allow_arbitrary_cost
        self._arbitrary_cost_velocity_code = arbitrary_cost_velocity_code
        self._automatic_pricing_tier_name = automatic_pricing_tier_name
        self._automatic_pricing_tier_oid = automatic_pricing_tier_oid
        self._cogs = cogs
        self._cost = cost
        self._currency_code = currency_code
        self._manufacturer_suggested_retail_price = manufacturer_suggested_retail_price
        self._maximum_arbitrary_cost = maximum_arbitrary_cost
        self._minimum_advertised_price = minimum_advertised_price
        self._minimum_arbitrary_cost = minimum_arbitrary_cost
        self._mix_and_match_group = mix_and_match_group
        self._mix_and_match_group_oid = mix_and_match_group_oid
        self._sale_cost = sale_cost
        self._sale_end = sale_end
        self._sale_start = sale_start
        self._tiers = tiers

    @property
    def allow_arbitrary_cost(self):
        """
        Gets the allow_arbitrary_cost of this ItemPricing.
        Allow arbitrary cost

        :return: The allow_arbitrary_cost of this ItemPricing.
        :rtype: bool
        """
        return self._allow_arbitrary_cost

    @allow_arbitrary_cost.setter
    def allow_arbitrary_cost(self, allow_arbitrary_cost):
        """
        Sets the allow_arbitrary_cost of this ItemPricing.
        Allow arbitrary cost

        :param allow_arbitrary_cost: The allow_arbitrary_cost of this ItemPricing.
        :type: bool
        """

        self._allow_arbitrary_cost = allow_arbitrary_cost

    @property
    def arbitrary_cost_velocity_code(self):
        """
        Gets the arbitrary_cost_velocity_code of this ItemPricing.
        Arbitrary cost velocity code

        :return: The arbitrary_cost_velocity_code of this ItemPricing.
        :rtype: str
        """
        return self._arbitrary_cost_velocity_code

    @arbitrary_cost_velocity_code.setter
    def arbitrary_cost_velocity_code(self, arbitrary_cost_velocity_code):
        """
        Sets the arbitrary_cost_velocity_code of this ItemPricing.
        Arbitrary cost velocity code

        :param arbitrary_cost_velocity_code: The arbitrary_cost_velocity_code of this ItemPricing.
        :type: str
        """

        if not arbitrary_cost_velocity_code:
            raise ValueError("Invalid value for `arbitrary_cost_velocity_code`, must not be `None`")
        if len(arbitrary_cost_velocity_code) > 10000:
            raise ValueError("Invalid value for `arbitrary_cost_velocity_code`, length must be less than `10000`")

        self._arbitrary_cost_velocity_code = arbitrary_cost_velocity_code

    @property
    def automatic_pricing_tier_name(self):
        """
        Gets the automatic_pricing_tier_name of this ItemPricing.
        Automatic pricing tier name

        :return: The automatic_pricing_tier_name of this ItemPricing.
        :rtype: str
        """
        return self._automatic_pricing_tier_name

    @automatic_pricing_tier_name.setter
    def automatic_pricing_tier_name(self, automatic_pricing_tier_name):
        """
        Sets the automatic_pricing_tier_name of this ItemPricing.
        Automatic pricing tier name

        :param automatic_pricing_tier_name: The automatic_pricing_tier_name of this ItemPricing.
        :type: str
        """

        self._automatic_pricing_tier_name = automatic_pricing_tier_name

    @property
    def automatic_pricing_tier_oid(self):
        """
        Gets the automatic_pricing_tier_oid of this ItemPricing.
        Automatic pricing tier object identifier

        :return: The automatic_pricing_tier_oid of this ItemPricing.
        :rtype: int
        """
        return self._automatic_pricing_tier_oid

    @automatic_pricing_tier_oid.setter
    def automatic_pricing_tier_oid(self, automatic_pricing_tier_oid):
        """
        Sets the automatic_pricing_tier_oid of this ItemPricing.
        Automatic pricing tier object identifier

        :param automatic_pricing_tier_oid: The automatic_pricing_tier_oid of this ItemPricing.
        :type: int
        """

        self._automatic_pricing_tier_oid = automatic_pricing_tier_oid

    @property
    def cogs(self):
        """
        Gets the cogs of this ItemPricing.
        Cost of goods sold

        :return: The cogs of this ItemPricing.
        :rtype: float
        """
        return self._cogs

    @cogs.setter
    def cogs(self, cogs):
        """
        Sets the cogs of this ItemPricing.
        Cost of goods sold

        :param cogs: The cogs of this ItemPricing.
        :type: float
        """

        self._cogs = cogs

    @property
    def cost(self):
        """
        Gets the cost of this ItemPricing.
        Cost

        :return: The cost of this ItemPricing.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this ItemPricing.
        Cost

        :param cost: The cost of this ItemPricing.
        :type: float
        """

        self._cost = cost

    @property
    def currency_code(self):
        """
        Gets the currency_code of this ItemPricing.
        Currency code

        :return: The currency_code of this ItemPricing.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this ItemPricing.
        Currency code

        :param currency_code: The currency_code of this ItemPricing.
        :type: str
        """

        if not currency_code:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")
        if len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than `3`")

        self._currency_code = currency_code

    @property
    def manufacturer_suggested_retail_price(self):
        """
        Gets the manufacturer_suggested_retail_price of this ItemPricing.
        Manufacturer suggested retail price

        :return: The manufacturer_suggested_retail_price of this ItemPricing.
        :rtype: float
        """
        return self._manufacturer_suggested_retail_price

    @manufacturer_suggested_retail_price.setter
    def manufacturer_suggested_retail_price(self, manufacturer_suggested_retail_price):
        """
        Sets the manufacturer_suggested_retail_price of this ItemPricing.
        Manufacturer suggested retail price

        :param manufacturer_suggested_retail_price: The manufacturer_suggested_retail_price of this ItemPricing.
        :type: float
        """

        self._manufacturer_suggested_retail_price = manufacturer_suggested_retail_price

    @property
    def maximum_arbitrary_cost(self):
        """
        Gets the maximum_arbitrary_cost of this ItemPricing.
        Maximum arbitrary cost

        :return: The maximum_arbitrary_cost of this ItemPricing.
        :rtype: float
        """
        return self._maximum_arbitrary_cost

    @maximum_arbitrary_cost.setter
    def maximum_arbitrary_cost(self, maximum_arbitrary_cost):
        """
        Sets the maximum_arbitrary_cost of this ItemPricing.
        Maximum arbitrary cost

        :param maximum_arbitrary_cost: The maximum_arbitrary_cost of this ItemPricing.
        :type: float
        """

        self._maximum_arbitrary_cost = maximum_arbitrary_cost

    @property
    def minimum_advertised_price(self):
        """
        Gets the minimum_advertised_price of this ItemPricing.
        Minimum advertised price

        :return: The minimum_advertised_price of this ItemPricing.
        :rtype: float
        """
        return self._minimum_advertised_price

    @minimum_advertised_price.setter
    def minimum_advertised_price(self, minimum_advertised_price):
        """
        Sets the minimum_advertised_price of this ItemPricing.
        Minimum advertised price

        :param minimum_advertised_price: The minimum_advertised_price of this ItemPricing.
        :type: float
        """

        self._minimum_advertised_price = minimum_advertised_price

    @property
    def minimum_arbitrary_cost(self):
        """
        Gets the minimum_arbitrary_cost of this ItemPricing.
        Minimum arbitrary cost

        :return: The minimum_arbitrary_cost of this ItemPricing.
        :rtype: float
        """
        return self._minimum_arbitrary_cost

    @minimum_arbitrary_cost.setter
    def minimum_arbitrary_cost(self, minimum_arbitrary_cost):
        """
        Sets the minimum_arbitrary_cost of this ItemPricing.
        Minimum arbitrary cost

        :param minimum_arbitrary_cost: The minimum_arbitrary_cost of this ItemPricing.
        :type: float
        """

        self._minimum_arbitrary_cost = minimum_arbitrary_cost

    @property
    def mix_and_match_group(self):
        """
        Gets the mix_and_match_group of this ItemPricing.
        Mix and match group

        :return: The mix_and_match_group of this ItemPricing.
        :rtype: str
        """
        return self._mix_and_match_group

    @mix_and_match_group.setter
    def mix_and_match_group(self, mix_and_match_group):
        """
        Sets the mix_and_match_group of this ItemPricing.
        Mix and match group

        :param mix_and_match_group: The mix_and_match_group of this ItemPricing.
        :type: str
        """

        self._mix_and_match_group = mix_and_match_group

    @property
    def mix_and_match_group_oid(self):
        """
        Gets the mix_and_match_group_oid of this ItemPricing.
        Mix and match group object identifier

        :return: The mix_and_match_group_oid of this ItemPricing.
        :rtype: int
        """
        return self._mix_and_match_group_oid

    @mix_and_match_group_oid.setter
    def mix_and_match_group_oid(self, mix_and_match_group_oid):
        """
        Sets the mix_and_match_group_oid of this ItemPricing.
        Mix and match group object identifier

        :param mix_and_match_group_oid: The mix_and_match_group_oid of this ItemPricing.
        :type: int
        """

        self._mix_and_match_group_oid = mix_and_match_group_oid

    @property
    def sale_cost(self):
        """
        Gets the sale_cost of this ItemPricing.
        Sale cost

        :return: The sale_cost of this ItemPricing.
        :rtype: float
        """
        return self._sale_cost

    @sale_cost.setter
    def sale_cost(self, sale_cost):
        """
        Sets the sale_cost of this ItemPricing.
        Sale cost

        :param sale_cost: The sale_cost of this ItemPricing.
        :type: float
        """

        self._sale_cost = sale_cost

    @property
    def sale_end(self):
        """
        Gets the sale_end of this ItemPricing.
        Sale end

        :return: The sale_end of this ItemPricing.
        :rtype: str
        """
        return self._sale_end

    @sale_end.setter
    def sale_end(self, sale_end):
        """
        Sets the sale_end of this ItemPricing.
        Sale end

        :param sale_end: The sale_end of this ItemPricing.
        :type: str
        """

        self._sale_end = sale_end

    @property
    def sale_start(self):
        """
        Gets the sale_start of this ItemPricing.
        Sale start

        :return: The sale_start of this ItemPricing.
        :rtype: str
        """
        return self._sale_start

    @sale_start.setter
    def sale_start(self, sale_start):
        """
        Sets the sale_start of this ItemPricing.
        Sale start

        :param sale_start: The sale_start of this ItemPricing.
        :type: str
        """

        self._sale_start = sale_start

    @property
    def tiers(self):
        """
        Gets the tiers of this ItemPricing.
        Tiers

        :return: The tiers of this ItemPricing.
        :rtype: list[ItemPricingTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """
        Sets the tiers of this ItemPricing.
        Tiers

        :param tiers: The tiers of this ItemPricing.
        :type: list[ItemPricingTier]
        """

        self._tiers = tiers

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