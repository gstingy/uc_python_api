# com_ultracart_admin_v2
This is the next generation UltraCart REST API...

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build date: 2016-08-31T10:55:52.438-04:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://www.ultracart.com](http://www.ultracart.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/UltraCart/rest_api_v2_sdk_python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/UltraCart/rest_api_v2_sdk_python.git`)

Then import the package:
```python
import com_ultracart_admin_v2 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import com_ultracart_admin_v2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import com_ultracart_admin_v2
from com_ultracart_admin_v2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
com_ultracart_admin_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
com_ultracart_admin_v2.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# com_ultracart_admin_v2.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'
# create an instance of the API class
api_instance = com_ultracart_admin_v2.ItemApi
parent_category_id = 56 # int | The parent category to retrieve items for.  Unspecified means all items on the account.  0 = root (optional)

try:
    # Retrieve items
    api_response = api_instance.item_items_get(parent_category_id=parent_category_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ItemApi->item_items_get: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/rest/admin/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ItemApi* | [**item_items_get**](docs/ItemApi.md#item_items_get) | **GET** /item/items | Retrieve items
*ItemApi* | [**item_items_merchant_item_oid_delete**](docs/ItemApi.md#item_items_merchant_item_oid_delete) | **DELETE** /item/items/{merchant_item_oid} | Delete an item
*ItemApi* | [**item_items_merchant_item_oid_get**](docs/ItemApi.md#item_items_merchant_item_oid_get) | **GET** /item/items/{merchant_item_oid} | Retrieve an item
*ItemApi* | [**item_items_merchant_item_oid_put**](docs/ItemApi.md#item_items_merchant_item_oid_put) | **PUT** /item/items/{merchant_item_oid} | Update an item
*ItemApi* | [**item_items_post**](docs/ItemApi.md#item_items_post) | **POST** /item/items | Create an item
*ItemApi* | [**item_temp_multimedia_post**](docs/ItemApi.md#item_temp_multimedia_post) | **POST** /item/temp_multimedia | Upload an image to the temporary multimedia.


## Documentation For Models

 - [Distance](docs/Distance.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Item](docs/Item.md)
 - [ItemAccounting](docs/ItemAccounting.md)
 - [ItemAmember](docs/ItemAmember.md)
 - [ItemAutoOrder](docs/ItemAutoOrder.md)
 - [ItemAutoOrderStep](docs/ItemAutoOrderStep.md)
 - [ItemAutoOrderStepArbitraryUnitCostSchedule](docs/ItemAutoOrderStepArbitraryUnitCostSchedule.md)
 - [ItemAutoOrderStepGrandfatherPricing](docs/ItemAutoOrderStepGrandfatherPricing.md)
 - [ItemCCBill](docs/ItemCCBill.md)
 - [ItemChannelPartnerMapping](docs/ItemChannelPartnerMapping.md)
 - [ItemChargeback](docs/ItemChargeback.md)
 - [ItemChargebackAddendum](docs/ItemChargebackAddendum.md)
 - [ItemChargebackAdjustmentRequest](docs/ItemChargebackAdjustmentRequest.md)
 - [ItemCheckout](docs/ItemCheckout.md)
 - [ItemContent](docs/ItemContent.md)
 - [ItemContentAssignment](docs/ItemContentAssignment.md)
 - [ItemContentAttribute](docs/ItemContentAttribute.md)
 - [ItemContentMultimedia](docs/ItemContentMultimedia.md)
 - [ItemContentMultimediaThumbnail](docs/ItemContentMultimediaThumbnail.md)
 - [ItemDigitalDelivery](docs/ItemDigitalDelivery.md)
 - [ItemDigitalItem](docs/ItemDigitalItem.md)
 - [ItemEbay](docs/ItemEbay.md)
 - [ItemEbayCategorySpecific](docs/ItemEbayCategorySpecific.md)
 - [ItemEbayMarketListing](docs/ItemEbayMarketListing.md)
 - [ItemEbayMarketPlaceAnalysis](docs/ItemEbayMarketPlaceAnalysis.md)
 - [ItemEmailNotifications](docs/ItemEmailNotifications.md)
 - [ItemEnrollment123](docs/ItemEnrollment123.md)
 - [ItemGiftCertificate](docs/ItemGiftCertificate.md)
 - [ItemGoogleProductSearch](docs/ItemGoogleProductSearch.md)
 - [ItemIdentifiers](docs/ItemIdentifiers.md)
 - [ItemInstantPaymentNotification](docs/ItemInstantPaymentNotification.md)
 - [ItemInstantPaymentNotifications](docs/ItemInstantPaymentNotifications.md)
 - [ItemInternal](docs/ItemInternal.md)
 - [ItemKitComponent](docs/ItemKitComponent.md)
 - [ItemKitDefinition](docs/ItemKitDefinition.md)
 - [ItemOption](docs/ItemOption.md)
 - [ItemOptionValue](docs/ItemOptionValue.md)
 - [ItemOptionValueAdditionalItem](docs/ItemOptionValueAdditionalItem.md)
 - [ItemOptionValueDigitalItem](docs/ItemOptionValueDigitalItem.md)
 - [ItemPaymentProcessing](docs/ItemPaymentProcessing.md)
 - [ItemPhysical](docs/ItemPhysical.md)
 - [ItemPricing](docs/ItemPricing.md)
 - [ItemPricingTier](docs/ItemPricingTier.md)
 - [ItemPricingTierDiscount](docs/ItemPricingTierDiscount.md)
 - [ItemPricingTierLimit](docs/ItemPricingTierLimit.md)
 - [ItemRealtimePricing](docs/ItemRealtimePricing.md)
 - [ItemRelated](docs/ItemRelated.md)
 - [ItemRelatedItem](docs/ItemRelatedItem.md)
 - [ItemReporting](docs/ItemReporting.md)
 - [ItemResponse](docs/ItemResponse.md)
 - [ItemRestriction](docs/ItemRestriction.md)
 - [ItemRestrictionItem](docs/ItemRestrictionItem.md)
 - [ItemRevguard](docs/ItemRevguard.md)
 - [ItemReviews](docs/ItemReviews.md)
 - [ItemSalesforce](docs/ItemSalesforce.md)
 - [ItemShipping](docs/ItemShipping.md)
 - [ItemShippingCase](docs/ItemShippingCase.md)
 - [ItemShippingDestinationMarkup](docs/ItemShippingDestinationMarkup.md)
 - [ItemShippingDestinationRestriction](docs/ItemShippingDestinationRestriction.md)
 - [ItemShippingDistributionCenter](docs/ItemShippingDistributionCenter.md)
 - [ItemShippingMethod](docs/ItemShippingMethod.md)
 - [ItemShippingPackageRequirement](docs/ItemShippingPackageRequirement.md)
 - [ItemTax](docs/ItemTax.md)
 - [ItemTaxExemption](docs/ItemTaxExemption.md)
 - [ItemThirdPartyEmailMarketing](docs/ItemThirdPartyEmailMarketing.md)
 - [ItemVariantItem](docs/ItemVariantItem.md)
 - [ItemVariation](docs/ItemVariation.md)
 - [ItemVariationOption](docs/ItemVariationOption.md)
 - [ItemWishlistMember](docs/ItemWishlistMember.md)
 - [ItemsResponse](docs/ItemsResponse.md)
 - [ResponseMetadata](docs/ResponseMetadata.md)
 - [ResultSet](docs/ResultSet.md)
 - [TempMultimedia](docs/TempMultimedia.md)
 - [TempMultimediaResponse](docs/TempMultimediaResponse.md)
 - [Weight](docs/Weight.md)


## Documentation For Authorization


## ultraCartOauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://secure.ultracart.com/rest/oauth/authorize
- **Scopes**: 
 - **item_read**: Allows you to read item information.
 - **item_write**: Allows you to write item information.

## ultraCartSimpleApiKey

- **Type**: API key
- **API key parameter name**: x-ultracart-simple-key
- **Location**: HTTP header


## Author

support@ultracart.com

