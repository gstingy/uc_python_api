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


class ItemChannelPartnerMapping(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, barcode_ua=None, barcode_uc=None, barcode_ui=None, barcode_uk=None, buyer_dpci=None, buyer_item_number=None, channel_partner_code=None, channel_partner_oid=None, from_item_id=None, from_sku=None, mutually_defined_number=None, quantity_ratio_cp=None, quantity_ratio_uc=None, sku=None, unit_of_measure=None, vendor_number=None, vendor_style_number=None):
        """
        ItemChannelPartnerMapping - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'barcode_ua': 'str',
            'barcode_uc': 'str',
            'barcode_ui': 'str',
            'barcode_uk': 'str',
            'buyer_dpci': 'str',
            'buyer_item_number': 'str',
            'channel_partner_code': 'str',
            'channel_partner_oid': 'int',
            'from_item_id': 'str',
            'from_sku': 'str',
            'mutually_defined_number': 'str',
            'quantity_ratio_cp': 'int',
            'quantity_ratio_uc': 'int',
            'sku': 'str',
            'unit_of_measure': 'str',
            'vendor_number': 'str',
            'vendor_style_number': 'str'
        }

        self.attribute_map = {
            'barcode_ua': 'barcode_ua',
            'barcode_uc': 'barcode_uc',
            'barcode_ui': 'barcode_ui',
            'barcode_uk': 'barcode_uk',
            'buyer_dpci': 'buyer_dpci',
            'buyer_item_number': 'buyer_item_number',
            'channel_partner_code': 'channel_partner_code',
            'channel_partner_oid': 'channel_partner_oid',
            'from_item_id': 'from_item_id',
            'from_sku': 'from_sku',
            'mutually_defined_number': 'mutually_defined_number',
            'quantity_ratio_cp': 'quantity_ratio_cp',
            'quantity_ratio_uc': 'quantity_ratio_uc',
            'sku': 'sku',
            'unit_of_measure': 'unit_of_measure',
            'vendor_number': 'vendor_number',
            'vendor_style_number': 'vendor_style_number'
        }

        self._barcode_ua = barcode_ua
        self._barcode_uc = barcode_uc
        self._barcode_ui = barcode_ui
        self._barcode_uk = barcode_uk
        self._buyer_dpci = buyer_dpci
        self._buyer_item_number = buyer_item_number
        self._channel_partner_code = channel_partner_code
        self._channel_partner_oid = channel_partner_oid
        self._from_item_id = from_item_id
        self._from_sku = from_sku
        self._mutually_defined_number = mutually_defined_number
        self._quantity_ratio_cp = quantity_ratio_cp
        self._quantity_ratio_uc = quantity_ratio_uc
        self._sku = sku
        self._unit_of_measure = unit_of_measure
        self._vendor_number = vendor_number
        self._vendor_style_number = vendor_style_number

    @property
    def barcode_ua(self):
        """
        Gets the barcode_ua of this ItemChannelPartnerMapping.
        Barcode UA (EDI only)

        :return: The barcode_ua of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._barcode_ua

    @barcode_ua.setter
    def barcode_ua(self, barcode_ua):
        """
        Sets the barcode_ua of this ItemChannelPartnerMapping.
        Barcode UA (EDI only)

        :param barcode_ua: The barcode_ua of this ItemChannelPartnerMapping.
        :type: str
        """

        self._barcode_ua = barcode_ua

    @property
    def barcode_uc(self):
        """
        Gets the barcode_uc of this ItemChannelPartnerMapping.
        Barcode UC (EDI only)

        :return: The barcode_uc of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._barcode_uc

    @barcode_uc.setter
    def barcode_uc(self, barcode_uc):
        """
        Sets the barcode_uc of this ItemChannelPartnerMapping.
        Barcode UC (EDI only)

        :param barcode_uc: The barcode_uc of this ItemChannelPartnerMapping.
        :type: str
        """

        self._barcode_uc = barcode_uc

    @property
    def barcode_ui(self):
        """
        Gets the barcode_ui of this ItemChannelPartnerMapping.
        Barcode UI (EDI only)

        :return: The barcode_ui of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._barcode_ui

    @barcode_ui.setter
    def barcode_ui(self, barcode_ui):
        """
        Sets the barcode_ui of this ItemChannelPartnerMapping.
        Barcode UI (EDI only)

        :param barcode_ui: The barcode_ui of this ItemChannelPartnerMapping.
        :type: str
        """

        self._barcode_ui = barcode_ui

    @property
    def barcode_uk(self):
        """
        Gets the barcode_uk of this ItemChannelPartnerMapping.
        Barcode UK (EDI only)

        :return: The barcode_uk of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._barcode_uk

    @barcode_uk.setter
    def barcode_uk(self, barcode_uk):
        """
        Sets the barcode_uk of this ItemChannelPartnerMapping.
        Barcode UK (EDI only)

        :param barcode_uk: The barcode_uk of this ItemChannelPartnerMapping.
        :type: str
        """

        self._barcode_uk = barcode_uk

    @property
    def buyer_dpci(self):
        """
        Gets the buyer_dpci of this ItemChannelPartnerMapping.
        Buyer DPCI (EDI only)

        :return: The buyer_dpci of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._buyer_dpci

    @buyer_dpci.setter
    def buyer_dpci(self, buyer_dpci):
        """
        Sets the buyer_dpci of this ItemChannelPartnerMapping.
        Buyer DPCI (EDI only)

        :param buyer_dpci: The buyer_dpci of this ItemChannelPartnerMapping.
        :type: str
        """

        self._buyer_dpci = buyer_dpci

    @property
    def buyer_item_number(self):
        """
        Gets the buyer_item_number of this ItemChannelPartnerMapping.
        Buyer item number (EDI only)

        :return: The buyer_item_number of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._buyer_item_number

    @buyer_item_number.setter
    def buyer_item_number(self, buyer_item_number):
        """
        Sets the buyer_item_number of this ItemChannelPartnerMapping.
        Buyer item number (EDI only)

        :param buyer_item_number: The buyer_item_number of this ItemChannelPartnerMapping.
        :type: str
        """

        self._buyer_item_number = buyer_item_number

    @property
    def channel_partner_code(self):
        """
        Gets the channel_partner_code of this ItemChannelPartnerMapping.
        Channel partner code

        :return: The channel_partner_code of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._channel_partner_code

    @channel_partner_code.setter
    def channel_partner_code(self, channel_partner_code):
        """
        Sets the channel_partner_code of this ItemChannelPartnerMapping.
        Channel partner code

        :param channel_partner_code: The channel_partner_code of this ItemChannelPartnerMapping.
        :type: str
        """

        self._channel_partner_code = channel_partner_code

    @property
    def channel_partner_oid(self):
        """
        Gets the channel_partner_oid of this ItemChannelPartnerMapping.
        Channel partner object identifier

        :return: The channel_partner_oid of this ItemChannelPartnerMapping.
        :rtype: int
        """
        return self._channel_partner_oid

    @channel_partner_oid.setter
    def channel_partner_oid(self, channel_partner_oid):
        """
        Sets the channel_partner_oid of this ItemChannelPartnerMapping.
        Channel partner object identifier

        :param channel_partner_oid: The channel_partner_oid of this ItemChannelPartnerMapping.
        :type: int
        """

        self._channel_partner_oid = channel_partner_oid

    @property
    def from_item_id(self):
        """
        Gets the from_item_id of this ItemChannelPartnerMapping.
        From Item ID

        :return: The from_item_id of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._from_item_id

    @from_item_id.setter
    def from_item_id(self, from_item_id):
        """
        Sets the from_item_id of this ItemChannelPartnerMapping.
        From Item ID

        :param from_item_id: The from_item_id of this ItemChannelPartnerMapping.
        :type: str
        """

        if not from_item_id:
            raise ValueError("Invalid value for `from_item_id`, must not be `None`")
        if len(from_item_id) > 30:
            raise ValueError("Invalid value for `from_item_id`, length must be less than `30`")

        self._from_item_id = from_item_id

    @property
    def from_sku(self):
        """
        Gets the from_sku of this ItemChannelPartnerMapping.
        From SKU

        :return: The from_sku of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._from_sku

    @from_sku.setter
    def from_sku(self, from_sku):
        """
        Sets the from_sku of this ItemChannelPartnerMapping.
        From SKU

        :param from_sku: The from_sku of this ItemChannelPartnerMapping.
        :type: str
        """

        if not from_sku:
            raise ValueError("Invalid value for `from_sku`, must not be `None`")
        if len(from_sku) > 50:
            raise ValueError("Invalid value for `from_sku`, length must be less than `50`")

        self._from_sku = from_sku

    @property
    def mutually_defined_number(self):
        """
        Gets the mutually_defined_number of this ItemChannelPartnerMapping.
        Mutually defined number (EDI only)

        :return: The mutually_defined_number of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._mutually_defined_number

    @mutually_defined_number.setter
    def mutually_defined_number(self, mutually_defined_number):
        """
        Sets the mutually_defined_number of this ItemChannelPartnerMapping.
        Mutually defined number (EDI only)

        :param mutually_defined_number: The mutually_defined_number of this ItemChannelPartnerMapping.
        :type: str
        """

        self._mutually_defined_number = mutually_defined_number

    @property
    def quantity_ratio_cp(self):
        """
        Gets the quantity_ratio_cp of this ItemChannelPartnerMapping.
        Ratio (Channel Partner)

        :return: The quantity_ratio_cp of this ItemChannelPartnerMapping.
        :rtype: int
        """
        return self._quantity_ratio_cp

    @quantity_ratio_cp.setter
    def quantity_ratio_cp(self, quantity_ratio_cp):
        """
        Sets the quantity_ratio_cp of this ItemChannelPartnerMapping.
        Ratio (Channel Partner)

        :param quantity_ratio_cp: The quantity_ratio_cp of this ItemChannelPartnerMapping.
        :type: int
        """

        self._quantity_ratio_cp = quantity_ratio_cp

    @property
    def quantity_ratio_uc(self):
        """
        Gets the quantity_ratio_uc of this ItemChannelPartnerMapping.
        Ratio (UltraCart)

        :return: The quantity_ratio_uc of this ItemChannelPartnerMapping.
        :rtype: int
        """
        return self._quantity_ratio_uc

    @quantity_ratio_uc.setter
    def quantity_ratio_uc(self, quantity_ratio_uc):
        """
        Sets the quantity_ratio_uc of this ItemChannelPartnerMapping.
        Ratio (UltraCart)

        :param quantity_ratio_uc: The quantity_ratio_uc of this ItemChannelPartnerMapping.
        :type: int
        """

        self._quantity_ratio_uc = quantity_ratio_uc

    @property
    def sku(self):
        """
        Gets the sku of this ItemChannelPartnerMapping.
        SKU

        :return: The sku of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this ItemChannelPartnerMapping.
        SKU

        :param sku: The sku of this ItemChannelPartnerMapping.
        :type: str
        """

        if not sku:
            raise ValueError("Invalid value for `sku`, must not be `None`")
        if len(sku) > 50:
            raise ValueError("Invalid value for `sku`, length must be less than `50`")

        self._sku = sku

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this ItemChannelPartnerMapping.
        Unit of measure

        :return: The unit_of_measure of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this ItemChannelPartnerMapping.
        Unit of measure

        :param unit_of_measure: The unit_of_measure of this ItemChannelPartnerMapping.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def vendor_number(self):
        """
        Gets the vendor_number of this ItemChannelPartnerMapping.
        Vendor number (EDI only)

        :return: The vendor_number of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._vendor_number

    @vendor_number.setter
    def vendor_number(self, vendor_number):
        """
        Sets the vendor_number of this ItemChannelPartnerMapping.
        Vendor number (EDI only)

        :param vendor_number: The vendor_number of this ItemChannelPartnerMapping.
        :type: str
        """

        self._vendor_number = vendor_number

    @property
    def vendor_style_number(self):
        """
        Gets the vendor_style_number of this ItemChannelPartnerMapping.
        Vendor style number (EDI only)

        :return: The vendor_style_number of this ItemChannelPartnerMapping.
        :rtype: str
        """
        return self._vendor_style_number

    @vendor_style_number.setter
    def vendor_style_number(self, vendor_style_number):
        """
        Sets the vendor_style_number of this ItemChannelPartnerMapping.
        Vendor style number (EDI only)

        :param vendor_style_number: The vendor_style_number of this ItemChannelPartnerMapping.
        :type: str
        """

        self._vendor_style_number = vendor_style_number

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