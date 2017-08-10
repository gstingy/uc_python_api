# ultracart
This is the next generation UltraCart REST API...

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build date: 2017-08-10T12:10:25.024-04:00
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
import ultracart 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ultracart
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ultraCartOauth
ultracart.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: ultraCartSimpleApiKey
ultracart.configuration.api_key['x-ultracart-simple-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# ultracart.configuration.api_key_prefix['x-ultracart-simple-key'] = 'Bearer'
# create an instance of the API class
api_instance = ultracart.AutoorderApi
auto_order_oid = 56 # int | The auto order oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve an auto order
    api_response = api_instance.get_auto_order(auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->get_auto_order: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutoorderApi* | [**get_auto_order**](docs/AutoorderApi.md#get_auto_order) | **GET** /auto_order/auto_orders/{auto_order_oid} | Retrieve an auto order
*AutoorderApi* | [**get_auto_orders**](docs/AutoorderApi.md#get_auto_orders) | **GET** /auto_order/auto_orders | Retrieve auto orders
*AutoorderApi* | [**update_auto_order**](docs/AutoorderApi.md#update_auto_order) | **PUT** /auto_order/auto_orders/{auto_order_oid} | Update an auto order
*ChargebackApi* | [**delete_chargeback**](docs/ChargebackApi.md#delete_chargeback) | **DELETE** /chargeback/chargebacks/{chargeback_dispute_oid} | Delete a chargeback
*ChargebackApi* | [**get_chargeback_dispute**](docs/ChargebackApi.md#get_chargeback_dispute) | **GET** /chargeback/chargebacks/{chargeback_dispute_oid} | Retrieve a chargeback
*ChargebackApi* | [**get_chargeback_disputes**](docs/ChargebackApi.md#get_chargeback_disputes) | **GET** /chargeback/chargebacks | Retrieve chargebacks
*ChargebackApi* | [**insert_chargeback**](docs/ChargebackApi.md#insert_chargeback) | **POST** /chargeback/chargebacks | Insert a chargeback
*ChargebackApi* | [**update_chargeback**](docs/ChargebackApi.md#update_chargeback) | **PUT** /chargeback/chargebacks/{chargeback_dispute_oid} | Update a chargeback
*CheckoutApi* | [**city_state**](docs/CheckoutApi.md#city_state) | **POST** /checkout/city_state | City/State for Zip
*CheckoutApi* | [**finalize_order**](docs/CheckoutApi.md#finalize_order) | **POST** /checkout/cart/finalizeOrder | Finalize Order
*CheckoutApi* | [**get_cart**](docs/CheckoutApi.md#get_cart) | **GET** /checkout/cart | Get cart
*CheckoutApi* | [**get_cart_by_cart_id**](docs/CheckoutApi.md#get_cart_by_cart_id) | **GET** /checkout/cart/{cart_id} | Get cart (by cart id)
*CheckoutApi* | [**get_cart_by_return_code**](docs/CheckoutApi.md#get_cart_by_return_code) | **GET** /checkout/return/{return_code} | Get cart (by return code)
*CheckoutApi* | [**handoff_cart**](docs/CheckoutApi.md#handoff_cart) | **POST** /checkout/cart/handoff | Handoff cart
*CheckoutApi* | [**login**](docs/CheckoutApi.md#login) | **POST** /checkout/cart/profile/login | Profile login
*CheckoutApi* | [**logout**](docs/CheckoutApi.md#logout) | **POST** /checkout/cart/profile/logout | Profile logout
*CheckoutApi* | [**register**](docs/CheckoutApi.md#register) | **POST** /checkout/cart/profile/register | Profile registration
*CheckoutApi* | [**related_items_for_cart**](docs/CheckoutApi.md#related_items_for_cart) | **POST** /checkout/related_items | Related items
*CheckoutApi* | [**related_items_for_item**](docs/CheckoutApi.md#related_items_for_item) | **POST** /checkout/relatedItems/{item_id} | Related items (specific item)
*CheckoutApi* | [**setup_browser_key**](docs/CheckoutApi.md#setup_browser_key) | **PUT** /checkout/browser_key | Setup Browser Application
*CheckoutApi* | [**update_cart**](docs/CheckoutApi.md#update_cart) | **PUT** /checkout/cart | Update cart
*CheckoutApi* | [**validate_cart**](docs/CheckoutApi.md#validate_cart) | **POST** /checkout/cart/validate | Validate
*CustomerApi* | [**delete_customer**](docs/CustomerApi.md#delete_customer) | **DELETE** /customer/customers/{customer_profile_oid} | Delete a customer
*CustomerApi* | [**get_customer**](docs/CustomerApi.md#get_customer) | **GET** /customer/customers/{customer_profile_oid} | Retrieve a customer
*CustomerApi* | [**get_customers**](docs/CustomerApi.md#get_customers) | **GET** /customer/customers | Retrieve customers
*CustomerApi* | [**insert_customer**](docs/CustomerApi.md#insert_customer) | **POST** /customer/customers | Insert a customer
*CustomerApi* | [**update_customer**](docs/CustomerApi.md#update_customer) | **PUT** /customer/customers/{customer_profile_oid} | Update a customer
*FulfillmentApi* | [**acknowledge_orders**](docs/FulfillmentApi.md#acknowledge_orders) | **PUT** /fulfillment/distribution_centers/{distribution_center_code}/acknowledgements | Acknowledge receipt of orders.
*FulfillmentApi* | [**get_distribution_center_orders**](docs/FulfillmentApi.md#get_distribution_center_orders) | **GET** /fulfillment/distribution_centers/{distribution_center_code}/orders | Retrieve orders queued up for this distribution center.
*FulfillmentApi* | [**get_distribution_centers**](docs/FulfillmentApi.md#get_distribution_centers) | **GET** /fulfillment/distribution_centers | Retrieve distribution centers
*FulfillmentApi* | [**ship_orders**](docs/FulfillmentApi.md#ship_orders) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/shipments | Mark orders as shipped
*FulfillmentApi* | [**update_inventory**](docs/FulfillmentApi.md#update_inventory) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/inventory | Update inventory
*ItemApi* | [**delete_item**](docs/ItemApi.md#delete_item) | **DELETE** /item/items/{merchant_item_oid} | Delete an item
*ItemApi* | [**get_item**](docs/ItemApi.md#get_item) | **GET** /item/items/{merchant_item_oid} | Retrieve an item
*ItemApi* | [**get_items**](docs/ItemApi.md#get_items) | **GET** /item/items | Retrieve items
*ItemApi* | [**insert_item**](docs/ItemApi.md#insert_item) | **POST** /item/items | Create an item
*ItemApi* | [**update_item**](docs/ItemApi.md#update_item) | **PUT** /item/items/{merchant_item_oid} | Update an item
*ItemApi* | [**upload_temporary_multimedia**](docs/ItemApi.md#upload_temporary_multimedia) | **POST** /item/temp_multimedia | Upload an image to the temporary multimedia.
*OauthApi* | [**oauth_access_token**](docs/OauthApi.md#oauth_access_token) | **POST** /oauth/token | Exchange authorization code for access token.
*OauthApi* | [**oauth_revoke**](docs/OauthApi.md#oauth_revoke) | **POST** /oauth/revoke | Revoke this OAuth application.
*OrderApi* | [**cancel_order**](docs/OrderApi.md#cancel_order) | **POST** /order/orders/{order_id}/cancel | Cancel an order
*OrderApi* | [**delete_order**](docs/OrderApi.md#delete_order) | **DELETE** /order/orders/{order_id} | Delete an order
*OrderApi* | [**get_order**](docs/OrderApi.md#get_order) | **GET** /order/orders/{order_id} | Retrieve an order
*OrderApi* | [**get_orders**](docs/OrderApi.md#get_orders) | **GET** /order/orders | Retrieve orders
*OrderApi* | [**resend_receipt**](docs/OrderApi.md#resend_receipt) | **POST** /order/orders/{order_id}/resend_receipt | Resend receipt
*OrderApi* | [**resend_shipment_confirmation**](docs/OrderApi.md#resend_shipment_confirmation) | **POST** /order/orders/{order_id}/resend_shipment_confirmation | Resend shipment confirmation
*OrderApi* | [**update_order**](docs/OrderApi.md#update_order) | **PUT** /order/orders/{order_id} | Update an order
*WebhookApi* | [**delete_webhook**](docs/WebhookApi.md#delete_webhook) | **DELETE** /webhook/webhooks/{webhookOid} | Delete a webhook
*WebhookApi* | [**get_webhook_log**](docs/WebhookApi.md#get_webhook_log) | **GET** /webhook/webhooks/{webhookOid}/logs/{requestId} | Retrieve an individual log
*WebhookApi* | [**get_webhook_log_summaries**](docs/WebhookApi.md#get_webhook_log_summaries) | **GET** /webhook/webhooks/{webhookOid}/logs | Retrieve the log summaries
*WebhookApi* | [**get_webhooks**](docs/WebhookApi.md#get_webhooks) | **GET** /webhook/webhooks | Retrieve webhooks
*WebhookApi* | [**insert_webhook**](docs/WebhookApi.md#insert_webhook) | **POST** /webhook/webhooks | Add a webhook
*WebhookApi* | [**resend_event**](docs/WebhookApi.md#resend_event) | **POST** /webhook/webhooks/{webhookOid}/reflow/{eventName} | Resend events to the webhook endpoint.
*WebhookApi* | [**update_webhook**](docs/WebhookApi.md#update_webhook) | **PUT** /webhook/webhooks/{webhookOid} | Update a webhook


## Documentation For Models

 - [ApiUserApplicationProfile](docs/ApiUserApplicationProfile.md)
 - [AutoOrder](docs/AutoOrder.md)
 - [AutoOrderItem](docs/AutoOrderItem.md)
 - [AutoOrderItemOption](docs/AutoOrderItemOption.md)
 - [AutoOrderResponse](docs/AutoOrderResponse.md)
 - [AutoOrdersResponse](docs/AutoOrdersResponse.md)
 - [BaseResponse](docs/BaseResponse.md)
 - [Cart](docs/Cart.md)
 - [CartAffiliate](docs/CartAffiliate.md)
 - [CartBilling](docs/CartBilling.md)
 - [CartBuysafe](docs/CartBuysafe.md)
 - [CartCheckout](docs/CartCheckout.md)
 - [CartCoupon](docs/CartCoupon.md)
 - [CartCustomerProfile](docs/CartCustomerProfile.md)
 - [CartCustomerProfileAddress](docs/CartCustomerProfileAddress.md)
 - [CartCustomerProfileCreditCard](docs/CartCustomerProfileCreditCard.md)
 - [CartFinalizeOrderRequest](docs/CartFinalizeOrderRequest.md)
 - [CartFinalizeOrderRequestOptions](docs/CartFinalizeOrderRequestOptions.md)
 - [CartFinalizeOrderResponse](docs/CartFinalizeOrderResponse.md)
 - [CartGift](docs/CartGift.md)
 - [CartGiftCertificate](docs/CartGiftCertificate.md)
 - [CartItem](docs/CartItem.md)
 - [CartItemAttribute](docs/CartItemAttribute.md)
 - [CartItemMultimedia](docs/CartItemMultimedia.md)
 - [CartItemMultimediaThumbnail](docs/CartItemMultimediaThumbnail.md)
 - [CartItemOption](docs/CartItemOption.md)
 - [CartItemOptionValue](docs/CartItemOptionValue.md)
 - [CartItemPhysical](docs/CartItemPhysical.md)
 - [CartItemVariationSelection](docs/CartItemVariationSelection.md)
 - [CartKitComponentOption](docs/CartKitComponentOption.md)
 - [CartMarketing](docs/CartMarketing.md)
 - [CartPayment](docs/CartPayment.md)
 - [CartPaymentAmazon](docs/CartPaymentAmazon.md)
 - [CartPaymentCheck](docs/CartPaymentCheck.md)
 - [CartPaymentCreditCard](docs/CartPaymentCreditCard.md)
 - [CartPaymentPurchaseOrder](docs/CartPaymentPurchaseOrder.md)
 - [CartProfileLoginRequest](docs/CartProfileLoginRequest.md)
 - [CartProfileLoginResponse](docs/CartProfileLoginResponse.md)
 - [CartProfileRegisterRequest](docs/CartProfileRegisterRequest.md)
 - [CartProfileRegisterResponse](docs/CartProfileRegisterResponse.md)
 - [CartResponse](docs/CartResponse.md)
 - [CartSettings](docs/CartSettings.md)
 - [CartSettingsBilling](docs/CartSettingsBilling.md)
 - [CartSettingsGift](docs/CartSettingsGift.md)
 - [CartSettingsGiftWrap](docs/CartSettingsGiftWrap.md)
 - [CartSettingsPayment](docs/CartSettingsPayment.md)
 - [CartSettingsPaymentAmazon](docs/CartSettingsPaymentAmazon.md)
 - [CartSettingsPaymentCreditCard](docs/CartSettingsPaymentCreditCard.md)
 - [CartSettingsPaymentPayPal](docs/CartSettingsPaymentPayPal.md)
 - [CartSettingsProvince](docs/CartSettingsProvince.md)
 - [CartSettingsShipping](docs/CartSettingsShipping.md)
 - [CartSettingsShippingCalendar](docs/CartSettingsShippingCalendar.md)
 - [CartSettingsShippingEstimate](docs/CartSettingsShippingEstimate.md)
 - [CartSettingsTaxes](docs/CartSettingsTaxes.md)
 - [CartSettingsTerms](docs/CartSettingsTerms.md)
 - [CartShipping](docs/CartShipping.md)
 - [CartSummary](docs/CartSummary.md)
 - [CartTaxes](docs/CartTaxes.md)
 - [CartUpsellAfter](docs/CartUpsellAfter.md)
 - [CartValidationRequest](docs/CartValidationRequest.md)
 - [CartValidationResponse](docs/CartValidationResponse.md)
 - [ChargebackDispute](docs/ChargebackDispute.md)
 - [ChargebackDisputeResponse](docs/ChargebackDisputeResponse.md)
 - [ChargebackDisputesResponse](docs/ChargebackDisputesResponse.md)
 - [CheckoutHandoffRequest](docs/CheckoutHandoffRequest.md)
 - [CheckoutHandoffResponse](docs/CheckoutHandoffResponse.md)
 - [CheckoutSetupBrowserKeyRequest](docs/CheckoutSetupBrowserKeyRequest.md)
 - [CheckoutSetupBrowserKeyResponse](docs/CheckoutSetupBrowserKeyResponse.md)
 - [Currency](docs/Currency.md)
 - [Customer](docs/Customer.md)
 - [CustomerBilling](docs/CustomerBilling.md)
 - [CustomerCard](docs/CustomerCard.md)
 - [CustomerPricingTier](docs/CustomerPricingTier.md)
 - [CustomerResponse](docs/CustomerResponse.md)
 - [CustomerShipping](docs/CustomerShipping.md)
 - [CustomersResponse](docs/CustomersResponse.md)
 - [Distance](docs/Distance.md)
 - [DistributionCenter](docs/DistributionCenter.md)
 - [DistributionCentersResponse](docs/DistributionCentersResponse.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FulfillmentInventory](docs/FulfillmentInventory.md)
 - [FulfillmentShipment](docs/FulfillmentShipment.md)
 - [HTTPHeader](docs/HTTPHeader.md)
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
 - [OauthRevokeSuccessResponse](docs/OauthRevokeSuccessResponse.md)
 - [OauthTokenResponse](docs/OauthTokenResponse.md)
 - [Order](docs/Order.md)
 - [OrderAffiliate](docs/OrderAffiliate.md)
 - [OrderAffiliateLedger](docs/OrderAffiliateLedger.md)
 - [OrderAutoOrder](docs/OrderAutoOrder.md)
 - [OrderBilling](docs/OrderBilling.md)
 - [OrderBuysafe](docs/OrderBuysafe.md)
 - [OrderChannelPartner](docs/OrderChannelPartner.md)
 - [OrderCheckout](docs/OrderCheckout.md)
 - [OrderCoupon](docs/OrderCoupon.md)
 - [OrderDigitalItem](docs/OrderDigitalItem.md)
 - [OrderDigitalOrder](docs/OrderDigitalOrder.md)
 - [OrderEdi](docs/OrderEdi.md)
 - [OrderFraudScore](docs/OrderFraudScore.md)
 - [OrderGift](docs/OrderGift.md)
 - [OrderGiftCertificate](docs/OrderGiftCertificate.md)
 - [OrderInternal](docs/OrderInternal.md)
 - [OrderItem](docs/OrderItem.md)
 - [OrderItemEdi](docs/OrderItemEdi.md)
 - [OrderItemEdiIdentification](docs/OrderItemEdiIdentification.md)
 - [OrderItemEdiLot](docs/OrderItemEdiLot.md)
 - [OrderItemOption](docs/OrderItemOption.md)
 - [OrderItemOptionFileAttachment](docs/OrderItemOptionFileAttachment.md)
 - [OrderLinkedShipment](docs/OrderLinkedShipment.md)
 - [OrderMarketing](docs/OrderMarketing.md)
 - [OrderPayment](docs/OrderPayment.md)
 - [OrderPaymentCheck](docs/OrderPaymentCheck.md)
 - [OrderPaymentCreditCard](docs/OrderPaymentCreditCard.md)
 - [OrderPaymentECheck](docs/OrderPaymentECheck.md)
 - [OrderPaymentPurchaseOrder](docs/OrderPaymentPurchaseOrder.md)
 - [OrderPaymentTransaction](docs/OrderPaymentTransaction.md)
 - [OrderPaymentTransactionDetail](docs/OrderPaymentTransactionDetail.md)
 - [OrderQuote](docs/OrderQuote.md)
 - [OrderResponse](docs/OrderResponse.md)
 - [OrderSalesforce](docs/OrderSalesforce.md)
 - [OrderShipping](docs/OrderShipping.md)
 - [OrderSummary](docs/OrderSummary.md)
 - [OrderTaxes](docs/OrderTaxes.md)
 - [OrdersResponse](docs/OrdersResponse.md)
 - [ResponseMetadata](docs/ResponseMetadata.md)
 - [ResultSet](docs/ResultSet.md)
 - [TempMultimedia](docs/TempMultimedia.md)
 - [TempMultimediaResponse](docs/TempMultimediaResponse.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookEventCategory](docs/WebhookEventCategory.md)
 - [WebhookEventSubscription](docs/WebhookEventSubscription.md)
 - [WebhookLog](docs/WebhookLog.md)
 - [WebhookLogResponse](docs/WebhookLogResponse.md)
 - [WebhookLogSummariesResponse](docs/WebhookLogSummariesResponse.md)
 - [WebhookLogSummary](docs/WebhookLogSummary.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookSampleRequest](docs/WebhookSampleRequest.md)
 - [WebhookSampleRequestResponse](docs/WebhookSampleRequestResponse.md)
 - [WebhooksResponse](docs/WebhooksResponse.md)
 - [Weight](docs/Weight.md)


## Documentation For Authorization


## ultraCartBrowserApiKey

- **Type**: API key
- **API key parameter name**: x-ultracart-browser-key
- **Location**: HTTP header

## ultraCartOauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://secure.ultracart.com/rest/v2/oauth/authorize
- **Scopes**: 
 - **auto_order_read**: Allows you to read auto order information.
 - **auto_order_write**: Allows you to write auto order information.
 - **chargeback_read**: Allows you to read chargeback information.
 - **chargeback_write**: Allows you to write chargeback information.
 - **checkout_read**: Allows you to read checkout information.
 - **checkout_write**: Allows you to write checkout information.
 - **customer_read**: Allows you to read customer information.
 - **customer_write**: Allows you to write customer information.
 - **fulfillment_read**: Allows you to read fulfillment information.
 - **fulfillment_write**: Allows you to write fulfillment information.
 - **order_read**: Allows you to read order information.
 - **order_write**: Allows you to write order information.
 - **item_read**: Allows you to read item information.
 - **item_write**: Allows you to write item information.
 - **webhook_read**: Allows you to read webhook information.
 - **webhook_write**: Allows you to write webhook information.
 - **ultrabooks_read**: 1 of 2 required to use UltraBooks
 - **ultrabooks_write**: 2 of 2 required to use UltraBooks

## ultraCartSimpleApiKey

- **Type**: API key
- **API key parameter name**: x-ultracart-simple-key
- **Location**: HTTP header


## Author

support@ultracart.com

