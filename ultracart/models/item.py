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


class Item(object):
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
        'accounting': 'ItemAccounting',
        'amember': 'ItemAmember',
        'auto_order': 'ItemAutoOrder',
        'ccbill': 'ItemCCBill',
        'channel_partner_mappings': 'list[ItemChannelPartnerMapping]',
        'chargeback': 'ItemChargeback',
        'checkout': 'ItemCheckout',
        'content': 'ItemContent',
        'creation_dts': 'str',
        'description': 'str',
        'description_translated_text_instance_oid': 'int',
        'digital_delivery': 'ItemDigitalDelivery',
        'ebay': 'ItemEbay',
        'email_notifications': 'ItemEmailNotifications',
        'enrollment123': 'ItemEnrollment123',
        'gift_certificate': 'ItemGiftCertificate',
        'google_product_search': 'ItemGoogleProductSearch',
        'identifiers': 'ItemIdentifiers',
        'inactive': 'bool',
        'instant_payment_notifications': 'ItemInstantPaymentNotifications',
        'internal': 'ItemInternal',
        'kit': 'bool',
        'kit_definition': 'ItemKitDefinition',
        'last_modified_dts': 'str',
        'merchant_id': 'str',
        'merchant_item_id': 'str',
        'merchant_item_oid': 'int',
        'options': 'list[ItemOption]',
        'parent_category_id': 'int',
        'payment_processing': 'ItemPaymentProcessing',
        'physical': 'ItemPhysical',
        'pricing': 'ItemPricing',
        'realtime_pricing': 'ItemRealtimePricing',
        'related': 'ItemRelated',
        'reporting': 'ItemReporting',
        'restriction': 'ItemRestriction',
        'revguard': 'ItemRevguard',
        'reviews': 'ItemReviews',
        'salesforce': 'ItemSalesforce',
        'shipping': 'ItemShipping',
        'tax': 'ItemTax',
        'third_party_email_marketing': 'list[ItemThirdPartyEmailMarketing]',
        'variant_items': 'list[ItemVariantItem]',
        'variations': 'list[ItemVariation]',
        'wishlist_member': 'ItemWishlistMember'
    }

    attribute_map = {
        'accounting': 'accounting',
        'amember': 'amember',
        'auto_order': 'auto_order',
        'ccbill': 'ccbill',
        'channel_partner_mappings': 'channelPartnerMappings',
        'chargeback': 'chargeback',
        'checkout': 'checkout',
        'content': 'content',
        'creation_dts': 'creation_dts',
        'description': 'description',
        'description_translated_text_instance_oid': 'description_translated_text_instance_oid',
        'digital_delivery': 'digital_delivery',
        'ebay': 'ebay',
        'email_notifications': 'email_notifications',
        'enrollment123': 'enrollment123',
        'gift_certificate': 'gift_certificate',
        'google_product_search': 'google_product_search',
        'identifiers': 'identifiers',
        'inactive': 'inactive',
        'instant_payment_notifications': 'instant_payment_notifications',
        'internal': 'internal',
        'kit': 'kit',
        'kit_definition': 'kit_definition',
        'last_modified_dts': 'last_modified_dts',
        'merchant_id': 'merchant_id',
        'merchant_item_id': 'merchant_item_id',
        'merchant_item_oid': 'merchant_item_oid',
        'options': 'options',
        'parent_category_id': 'parent_category_id',
        'payment_processing': 'payment_processing',
        'physical': 'physical',
        'pricing': 'pricing',
        'realtime_pricing': 'realtime_pricing',
        'related': 'related',
        'reporting': 'reporting',
        'restriction': 'restriction',
        'revguard': 'revguard',
        'reviews': 'reviews',
        'salesforce': 'salesforce',
        'shipping': 'shipping',
        'tax': 'tax',
        'third_party_email_marketing': 'third_party_email_marketing',
        'variant_items': 'variant_items',
        'variations': 'variations',
        'wishlist_member': 'wishlist_member'
    }

    def __init__(self, accounting=None, amember=None, auto_order=None, ccbill=None, channel_partner_mappings=None, chargeback=None, checkout=None, content=None, creation_dts=None, description=None, description_translated_text_instance_oid=None, digital_delivery=None, ebay=None, email_notifications=None, enrollment123=None, gift_certificate=None, google_product_search=None, identifiers=None, inactive=None, instant_payment_notifications=None, internal=None, kit=None, kit_definition=None, last_modified_dts=None, merchant_id=None, merchant_item_id=None, merchant_item_oid=None, options=None, parent_category_id=None, payment_processing=None, physical=None, pricing=None, realtime_pricing=None, related=None, reporting=None, restriction=None, revguard=None, reviews=None, salesforce=None, shipping=None, tax=None, third_party_email_marketing=None, variant_items=None, variations=None, wishlist_member=None):
        """
        Item - a model defined in Swagger
        """

        self._accounting = None
        self._amember = None
        self._auto_order = None
        self._ccbill = None
        self._channel_partner_mappings = None
        self._chargeback = None
        self._checkout = None
        self._content = None
        self._creation_dts = None
        self._description = None
        self._description_translated_text_instance_oid = None
        self._digital_delivery = None
        self._ebay = None
        self._email_notifications = None
        self._enrollment123 = None
        self._gift_certificate = None
        self._google_product_search = None
        self._identifiers = None
        self._inactive = None
        self._instant_payment_notifications = None
        self._internal = None
        self._kit = None
        self._kit_definition = None
        self._last_modified_dts = None
        self._merchant_id = None
        self._merchant_item_id = None
        self._merchant_item_oid = None
        self._options = None
        self._parent_category_id = None
        self._payment_processing = None
        self._physical = None
        self._pricing = None
        self._realtime_pricing = None
        self._related = None
        self._reporting = None
        self._restriction = None
        self._revguard = None
        self._reviews = None
        self._salesforce = None
        self._shipping = None
        self._tax = None
        self._third_party_email_marketing = None
        self._variant_items = None
        self._variations = None
        self._wishlist_member = None
        self.discriminator = None

        if accounting is not None:
          self.accounting = accounting
        if amember is not None:
          self.amember = amember
        if auto_order is not None:
          self.auto_order = auto_order
        if ccbill is not None:
          self.ccbill = ccbill
        if channel_partner_mappings is not None:
          self.channel_partner_mappings = channel_partner_mappings
        if chargeback is not None:
          self.chargeback = chargeback
        if checkout is not None:
          self.checkout = checkout
        if content is not None:
          self.content = content
        if creation_dts is not None:
          self.creation_dts = creation_dts
        if description is not None:
          self.description = description
        if description_translated_text_instance_oid is not None:
          self.description_translated_text_instance_oid = description_translated_text_instance_oid
        if digital_delivery is not None:
          self.digital_delivery = digital_delivery
        if ebay is not None:
          self.ebay = ebay
        if email_notifications is not None:
          self.email_notifications = email_notifications
        if enrollment123 is not None:
          self.enrollment123 = enrollment123
        if gift_certificate is not None:
          self.gift_certificate = gift_certificate
        if google_product_search is not None:
          self.google_product_search = google_product_search
        if identifiers is not None:
          self.identifiers = identifiers
        if inactive is not None:
          self.inactive = inactive
        if instant_payment_notifications is not None:
          self.instant_payment_notifications = instant_payment_notifications
        if internal is not None:
          self.internal = internal
        if kit is not None:
          self.kit = kit
        if kit_definition is not None:
          self.kit_definition = kit_definition
        if last_modified_dts is not None:
          self.last_modified_dts = last_modified_dts
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if merchant_item_id is not None:
          self.merchant_item_id = merchant_item_id
        if merchant_item_oid is not None:
          self.merchant_item_oid = merchant_item_oid
        if options is not None:
          self.options = options
        if parent_category_id is not None:
          self.parent_category_id = parent_category_id
        if payment_processing is not None:
          self.payment_processing = payment_processing
        if physical is not None:
          self.physical = physical
        if pricing is not None:
          self.pricing = pricing
        if realtime_pricing is not None:
          self.realtime_pricing = realtime_pricing
        if related is not None:
          self.related = related
        if reporting is not None:
          self.reporting = reporting
        if restriction is not None:
          self.restriction = restriction
        if revguard is not None:
          self.revguard = revguard
        if reviews is not None:
          self.reviews = reviews
        if salesforce is not None:
          self.salesforce = salesforce
        if shipping is not None:
          self.shipping = shipping
        if tax is not None:
          self.tax = tax
        if third_party_email_marketing is not None:
          self.third_party_email_marketing = third_party_email_marketing
        if variant_items is not None:
          self.variant_items = variant_items
        if variations is not None:
          self.variations = variations
        if wishlist_member is not None:
          self.wishlist_member = wishlist_member

    @property
    def accounting(self):
        """
        Gets the accounting of this Item.

        :return: The accounting of this Item.
        :rtype: ItemAccounting
        """
        return self._accounting

    @accounting.setter
    def accounting(self, accounting):
        """
        Sets the accounting of this Item.

        :param accounting: The accounting of this Item.
        :type: ItemAccounting
        """

        self._accounting = accounting

    @property
    def amember(self):
        """
        Gets the amember of this Item.

        :return: The amember of this Item.
        :rtype: ItemAmember
        """
        return self._amember

    @amember.setter
    def amember(self, amember):
        """
        Sets the amember of this Item.

        :param amember: The amember of this Item.
        :type: ItemAmember
        """

        self._amember = amember

    @property
    def auto_order(self):
        """
        Gets the auto_order of this Item.

        :return: The auto_order of this Item.
        :rtype: ItemAutoOrder
        """
        return self._auto_order

    @auto_order.setter
    def auto_order(self, auto_order):
        """
        Sets the auto_order of this Item.

        :param auto_order: The auto_order of this Item.
        :type: ItemAutoOrder
        """

        self._auto_order = auto_order

    @property
    def ccbill(self):
        """
        Gets the ccbill of this Item.

        :return: The ccbill of this Item.
        :rtype: ItemCCBill
        """
        return self._ccbill

    @ccbill.setter
    def ccbill(self, ccbill):
        """
        Sets the ccbill of this Item.

        :param ccbill: The ccbill of this Item.
        :type: ItemCCBill
        """

        self._ccbill = ccbill

    @property
    def channel_partner_mappings(self):
        """
        Gets the channel_partner_mappings of this Item.
        Channel Partner Item Mapping

        :return: The channel_partner_mappings of this Item.
        :rtype: list[ItemChannelPartnerMapping]
        """
        return self._channel_partner_mappings

    @channel_partner_mappings.setter
    def channel_partner_mappings(self, channel_partner_mappings):
        """
        Sets the channel_partner_mappings of this Item.
        Channel Partner Item Mapping

        :param channel_partner_mappings: The channel_partner_mappings of this Item.
        :type: list[ItemChannelPartnerMapping]
        """

        self._channel_partner_mappings = channel_partner_mappings

    @property
    def chargeback(self):
        """
        Gets the chargeback of this Item.

        :return: The chargeback of this Item.
        :rtype: ItemChargeback
        """
        return self._chargeback

    @chargeback.setter
    def chargeback(self, chargeback):
        """
        Sets the chargeback of this Item.

        :param chargeback: The chargeback of this Item.
        :type: ItemChargeback
        """

        self._chargeback = chargeback

    @property
    def checkout(self):
        """
        Gets the checkout of this Item.

        :return: The checkout of this Item.
        :rtype: ItemCheckout
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """
        Sets the checkout of this Item.

        :param checkout: The checkout of this Item.
        :type: ItemCheckout
        """

        self._checkout = checkout

    @property
    def content(self):
        """
        Gets the content of this Item.

        :return: The content of this Item.
        :rtype: ItemContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Item.

        :param content: The content of this Item.
        :type: ItemContent
        """

        self._content = content

    @property
    def creation_dts(self):
        """
        Gets the creation_dts of this Item.
        Date/time of creation

        :return: The creation_dts of this Item.
        :rtype: str
        """
        return self._creation_dts

    @creation_dts.setter
    def creation_dts(self, creation_dts):
        """
        Sets the creation_dts of this Item.
        Date/time of creation

        :param creation_dts: The creation_dts of this Item.
        :type: str
        """

        self._creation_dts = creation_dts

    @property
    def description(self):
        """
        Gets the description of this Item.
        Description of the item up to 500 characters.

        :return: The description of this Item.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Item.
        Description of the item up to 500 characters.

        :param description: The description of this Item.
        :type: str
        """
        if description is not None and len(description) > 512:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")

        self._description = description

    @property
    def description_translated_text_instance_oid(self):
        """
        Gets the description_translated_text_instance_oid of this Item.
        Description translated text instance id

        :return: The description_translated_text_instance_oid of this Item.
        :rtype: int
        """
        return self._description_translated_text_instance_oid

    @description_translated_text_instance_oid.setter
    def description_translated_text_instance_oid(self, description_translated_text_instance_oid):
        """
        Sets the description_translated_text_instance_oid of this Item.
        Description translated text instance id

        :param description_translated_text_instance_oid: The description_translated_text_instance_oid of this Item.
        :type: int
        """

        self._description_translated_text_instance_oid = description_translated_text_instance_oid

    @property
    def digital_delivery(self):
        """
        Gets the digital_delivery of this Item.

        :return: The digital_delivery of this Item.
        :rtype: ItemDigitalDelivery
        """
        return self._digital_delivery

    @digital_delivery.setter
    def digital_delivery(self, digital_delivery):
        """
        Sets the digital_delivery of this Item.

        :param digital_delivery: The digital_delivery of this Item.
        :type: ItemDigitalDelivery
        """

        self._digital_delivery = digital_delivery

    @property
    def ebay(self):
        """
        Gets the ebay of this Item.

        :return: The ebay of this Item.
        :rtype: ItemEbay
        """
        return self._ebay

    @ebay.setter
    def ebay(self, ebay):
        """
        Sets the ebay of this Item.

        :param ebay: The ebay of this Item.
        :type: ItemEbay
        """

        self._ebay = ebay

    @property
    def email_notifications(self):
        """
        Gets the email_notifications of this Item.

        :return: The email_notifications of this Item.
        :rtype: ItemEmailNotifications
        """
        return self._email_notifications

    @email_notifications.setter
    def email_notifications(self, email_notifications):
        """
        Sets the email_notifications of this Item.

        :param email_notifications: The email_notifications of this Item.
        :type: ItemEmailNotifications
        """

        self._email_notifications = email_notifications

    @property
    def enrollment123(self):
        """
        Gets the enrollment123 of this Item.

        :return: The enrollment123 of this Item.
        :rtype: ItemEnrollment123
        """
        return self._enrollment123

    @enrollment123.setter
    def enrollment123(self, enrollment123):
        """
        Sets the enrollment123 of this Item.

        :param enrollment123: The enrollment123 of this Item.
        :type: ItemEnrollment123
        """

        self._enrollment123 = enrollment123

    @property
    def gift_certificate(self):
        """
        Gets the gift_certificate of this Item.

        :return: The gift_certificate of this Item.
        :rtype: ItemGiftCertificate
        """
        return self._gift_certificate

    @gift_certificate.setter
    def gift_certificate(self, gift_certificate):
        """
        Sets the gift_certificate of this Item.

        :param gift_certificate: The gift_certificate of this Item.
        :type: ItemGiftCertificate
        """

        self._gift_certificate = gift_certificate

    @property
    def google_product_search(self):
        """
        Gets the google_product_search of this Item.

        :return: The google_product_search of this Item.
        :rtype: ItemGoogleProductSearch
        """
        return self._google_product_search

    @google_product_search.setter
    def google_product_search(self, google_product_search):
        """
        Sets the google_product_search of this Item.

        :param google_product_search: The google_product_search of this Item.
        :type: ItemGoogleProductSearch
        """

        self._google_product_search = google_product_search

    @property
    def identifiers(self):
        """
        Gets the identifiers of this Item.

        :return: The identifiers of this Item.
        :rtype: ItemIdentifiers
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """
        Sets the identifiers of this Item.

        :param identifiers: The identifiers of this Item.
        :type: ItemIdentifiers
        """

        self._identifiers = identifiers

    @property
    def inactive(self):
        """
        Gets the inactive of this Item.
        True if this item is inactive and can not be purchased

        :return: The inactive of this Item.
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive):
        """
        Sets the inactive of this Item.
        True if this item is inactive and can not be purchased

        :param inactive: The inactive of this Item.
        :type: bool
        """

        self._inactive = inactive

    @property
    def instant_payment_notifications(self):
        """
        Gets the instant_payment_notifications of this Item.

        :return: The instant_payment_notifications of this Item.
        :rtype: ItemInstantPaymentNotifications
        """
        return self._instant_payment_notifications

    @instant_payment_notifications.setter
    def instant_payment_notifications(self, instant_payment_notifications):
        """
        Sets the instant_payment_notifications of this Item.

        :param instant_payment_notifications: The instant_payment_notifications of this Item.
        :type: ItemInstantPaymentNotifications
        """

        self._instant_payment_notifications = instant_payment_notifications

    @property
    def internal(self):
        """
        Gets the internal of this Item.

        :return: The internal of this Item.
        :rtype: ItemInternal
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """
        Sets the internal of this Item.

        :param internal: The internal of this Item.
        :type: ItemInternal
        """

        self._internal = internal

    @property
    def kit(self):
        """
        Gets the kit of this Item.
        True if this item is a kit

        :return: The kit of this Item.
        :rtype: bool
        """
        return self._kit

    @kit.setter
    def kit(self, kit):
        """
        Sets the kit of this Item.
        True if this item is a kit

        :param kit: The kit of this Item.
        :type: bool
        """

        self._kit = kit

    @property
    def kit_definition(self):
        """
        Gets the kit_definition of this Item.

        :return: The kit_definition of this Item.
        :rtype: ItemKitDefinition
        """
        return self._kit_definition

    @kit_definition.setter
    def kit_definition(self, kit_definition):
        """
        Sets the kit_definition of this Item.

        :param kit_definition: The kit_definition of this Item.
        :type: ItemKitDefinition
        """

        self._kit_definition = kit_definition

    @property
    def last_modified_dts(self):
        """
        Gets the last_modified_dts of this Item.
        Date/time of last modification

        :return: The last_modified_dts of this Item.
        :rtype: str
        """
        return self._last_modified_dts

    @last_modified_dts.setter
    def last_modified_dts(self, last_modified_dts):
        """
        Sets the last_modified_dts of this Item.
        Date/time of last modification

        :param last_modified_dts: The last_modified_dts of this Item.
        :type: str
        """

        self._last_modified_dts = last_modified_dts

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this Item.
        UltraCart merchant ID owning item

        :return: The merchant_id of this Item.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this Item.
        UltraCart merchant ID owning item

        :param merchant_id: The merchant_id of this Item.
        :type: str
        """
        if merchant_id is not None and len(merchant_id) > 5:
            raise ValueError("Invalid value for `merchant_id`, length must be less than or equal to `5`")

        self._merchant_id = merchant_id

    @property
    def merchant_item_id(self):
        """
        Gets the merchant_item_id of this Item.
        Unique item id assigned to this item

        :return: The merchant_item_id of this Item.
        :rtype: str
        """
        return self._merchant_item_id

    @merchant_item_id.setter
    def merchant_item_id(self, merchant_item_id):
        """
        Sets the merchant_item_id of this Item.
        Unique item id assigned to this item

        :param merchant_item_id: The merchant_item_id of this Item.
        :type: str
        """
        if merchant_item_id is not None and len(merchant_item_id) > 20:
            raise ValueError("Invalid value for `merchant_item_id`, length must be less than or equal to `20`")

        self._merchant_item_id = merchant_item_id

    @property
    def merchant_item_oid(self):
        """
        Gets the merchant_item_oid of this Item.
        Unique object identifier for this item

        :return: The merchant_item_oid of this Item.
        :rtype: int
        """
        return self._merchant_item_oid

    @merchant_item_oid.setter
    def merchant_item_oid(self, merchant_item_oid):
        """
        Sets the merchant_item_oid of this Item.
        Unique object identifier for this item

        :param merchant_item_oid: The merchant_item_oid of this Item.
        :type: int
        """

        self._merchant_item_oid = merchant_item_oid

    @property
    def options(self):
        """
        Gets the options of this Item.
        Options

        :return: The options of this Item.
        :rtype: list[ItemOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this Item.
        Options

        :param options: The options of this Item.
        :type: list[ItemOption]
        """

        self._options = options

    @property
    def parent_category_id(self):
        """
        Gets the parent_category_id of this Item.
        Parent category of the item.  Zero indicates the root folder.

        :return: The parent_category_id of this Item.
        :rtype: int
        """
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, parent_category_id):
        """
        Sets the parent_category_id of this Item.
        Parent category of the item.  Zero indicates the root folder.

        :param parent_category_id: The parent_category_id of this Item.
        :type: int
        """

        self._parent_category_id = parent_category_id

    @property
    def payment_processing(self):
        """
        Gets the payment_processing of this Item.

        :return: The payment_processing of this Item.
        :rtype: ItemPaymentProcessing
        """
        return self._payment_processing

    @payment_processing.setter
    def payment_processing(self, payment_processing):
        """
        Sets the payment_processing of this Item.

        :param payment_processing: The payment_processing of this Item.
        :type: ItemPaymentProcessing
        """

        self._payment_processing = payment_processing

    @property
    def physical(self):
        """
        Gets the physical of this Item.

        :return: The physical of this Item.
        :rtype: ItemPhysical
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """
        Sets the physical of this Item.

        :param physical: The physical of this Item.
        :type: ItemPhysical
        """

        self._physical = physical

    @property
    def pricing(self):
        """
        Gets the pricing of this Item.

        :return: The pricing of this Item.
        :rtype: ItemPricing
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """
        Sets the pricing of this Item.

        :param pricing: The pricing of this Item.
        :type: ItemPricing
        """

        self._pricing = pricing

    @property
    def realtime_pricing(self):
        """
        Gets the realtime_pricing of this Item.

        :return: The realtime_pricing of this Item.
        :rtype: ItemRealtimePricing
        """
        return self._realtime_pricing

    @realtime_pricing.setter
    def realtime_pricing(self, realtime_pricing):
        """
        Sets the realtime_pricing of this Item.

        :param realtime_pricing: The realtime_pricing of this Item.
        :type: ItemRealtimePricing
        """

        self._realtime_pricing = realtime_pricing

    @property
    def related(self):
        """
        Gets the related of this Item.

        :return: The related of this Item.
        :rtype: ItemRelated
        """
        return self._related

    @related.setter
    def related(self, related):
        """
        Sets the related of this Item.

        :param related: The related of this Item.
        :type: ItemRelated
        """

        self._related = related

    @property
    def reporting(self):
        """
        Gets the reporting of this Item.

        :return: The reporting of this Item.
        :rtype: ItemReporting
        """
        return self._reporting

    @reporting.setter
    def reporting(self, reporting):
        """
        Sets the reporting of this Item.

        :param reporting: The reporting of this Item.
        :type: ItemReporting
        """

        self._reporting = reporting

    @property
    def restriction(self):
        """
        Gets the restriction of this Item.

        :return: The restriction of this Item.
        :rtype: ItemRestriction
        """
        return self._restriction

    @restriction.setter
    def restriction(self, restriction):
        """
        Sets the restriction of this Item.

        :param restriction: The restriction of this Item.
        :type: ItemRestriction
        """

        self._restriction = restriction

    @property
    def revguard(self):
        """
        Gets the revguard of this Item.

        :return: The revguard of this Item.
        :rtype: ItemRevguard
        """
        return self._revguard

    @revguard.setter
    def revguard(self, revguard):
        """
        Sets the revguard of this Item.

        :param revguard: The revguard of this Item.
        :type: ItemRevguard
        """

        self._revguard = revguard

    @property
    def reviews(self):
        """
        Gets the reviews of this Item.

        :return: The reviews of this Item.
        :rtype: ItemReviews
        """
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        """
        Sets the reviews of this Item.

        :param reviews: The reviews of this Item.
        :type: ItemReviews
        """

        self._reviews = reviews

    @property
    def salesforce(self):
        """
        Gets the salesforce of this Item.

        :return: The salesforce of this Item.
        :rtype: ItemSalesforce
        """
        return self._salesforce

    @salesforce.setter
    def salesforce(self, salesforce):
        """
        Sets the salesforce of this Item.

        :param salesforce: The salesforce of this Item.
        :type: ItemSalesforce
        """

        self._salesforce = salesforce

    @property
    def shipping(self):
        """
        Gets the shipping of this Item.

        :return: The shipping of this Item.
        :rtype: ItemShipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """
        Sets the shipping of this Item.

        :param shipping: The shipping of this Item.
        :type: ItemShipping
        """

        self._shipping = shipping

    @property
    def tax(self):
        """
        Gets the tax of this Item.

        :return: The tax of this Item.
        :rtype: ItemTax
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this Item.

        :param tax: The tax of this Item.
        :type: ItemTax
        """

        self._tax = tax

    @property
    def third_party_email_marketing(self):
        """
        Gets the third_party_email_marketing of this Item.
        3rd Party Email Marketing

        :return: The third_party_email_marketing of this Item.
        :rtype: list[ItemThirdPartyEmailMarketing]
        """
        return self._third_party_email_marketing

    @third_party_email_marketing.setter
    def third_party_email_marketing(self, third_party_email_marketing):
        """
        Sets the third_party_email_marketing of this Item.
        3rd Party Email Marketing

        :param third_party_email_marketing: The third_party_email_marketing of this Item.
        :type: list[ItemThirdPartyEmailMarketing]
        """

        self._third_party_email_marketing = third_party_email_marketing

    @property
    def variant_items(self):
        """
        Gets the variant_items of this Item.
        Variant Items

        :return: The variant_items of this Item.
        :rtype: list[ItemVariantItem]
        """
        return self._variant_items

    @variant_items.setter
    def variant_items(self, variant_items):
        """
        Sets the variant_items of this Item.
        Variant Items

        :param variant_items: The variant_items of this Item.
        :type: list[ItemVariantItem]
        """

        self._variant_items = variant_items

    @property
    def variations(self):
        """
        Gets the variations of this Item.
        Variations

        :return: The variations of this Item.
        :rtype: list[ItemVariation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """
        Sets the variations of this Item.
        Variations

        :param variations: The variations of this Item.
        :type: list[ItemVariation]
        """

        self._variations = variations

    @property
    def wishlist_member(self):
        """
        Gets the wishlist_member of this Item.

        :return: The wishlist_member of this Item.
        :rtype: ItemWishlistMember
        """
        return self._wishlist_member

    @wishlist_member.setter
    def wishlist_member(self, wishlist_member):
        """
        Sets the wishlist_member of this Item.

        :param wishlist_member: The wishlist_member of this Item.
        :type: ItemWishlistMember
        """

        self._wishlist_member = wishlist_member

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
        if not isinstance(other, Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
