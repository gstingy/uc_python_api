# ultracart
This is the next generation UltraCart REST API...

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build date: 2017-05-08T08:16:08.879-04:00
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
    api_response = api_instance.auto_order_auto_orders_auto_order_oid_get(auto_order_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AutoorderApi->auto_order_auto_orders_auto_order_oid_get: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutoorderApi* | [**auto_order_auto_orders_auto_order_oid_get**](docs/AutoorderApi.md#auto_order_auto_orders_auto_order_oid_get) | **GET** /auto_order/auto_orders/{auto_order_oid} | Retrieve an auto order
*AutoorderApi* | [**auto_order_auto_orders_auto_order_oid_put**](docs/AutoorderApi.md#auto_order_auto_orders_auto_order_oid_put) | **PUT** /auto_order/auto_orders/{auto_order_oid} | Update an auto order
*AutoorderApi* | [**auto_order_auto_orders_get**](docs/AutoorderApi.md#auto_order_auto_orders_get) | **GET** /auto_order/auto_orders | Retrieve auto orders
*ChargebackApi* | [**chargeback_chargebacks_chargeback_dispute_oid_delete**](docs/ChargebackApi.md#chargeback_chargebacks_chargeback_dispute_oid_delete) | **DELETE** /chargeback/chargebacks/{chargeback_dispute_oid} | Delete a chargeback
*ChargebackApi* | [**chargeback_chargebacks_chargeback_dispute_oid_get**](docs/ChargebackApi.md#chargeback_chargebacks_chargeback_dispute_oid_get) | **GET** /chargeback/chargebacks/{chargeback_dispute_oid} | Retrieve a chargeback
*ChargebackApi* | [**chargeback_chargebacks_chargeback_dispute_oid_put**](docs/ChargebackApi.md#chargeback_chargebacks_chargeback_dispute_oid_put) | **PUT** /chargeback/chargebacks/{chargeback_dispute_oid} | Update a chargeback
*ChargebackApi* | [**chargeback_chargebacks_get**](docs/ChargebackApi.md#chargeback_chargebacks_get) | **GET** /chargeback/chargebacks | Retrieve chargebacks
*ChargebackApi* | [**chargeback_chargebacks_post**](docs/ChargebackApi.md#chargeback_chargebacks_post) | **POST** /chargeback/chargebacks | Insert a chargeback
*CheckoutApi* | [**checkout_browser_key_put**](docs/CheckoutApi.md#checkout_browser_key_put) | **PUT** /checkout/browser_key | Setup Browser Application
*CheckoutApi* | [**checkout_cart_cart_id_get**](docs/CheckoutApi.md#checkout_cart_cart_id_get) | **GET** /checkout/cart/{cart_id} | Get cart (by cart id)
*CheckoutApi* | [**checkout_cart_finalize_order_post**](docs/CheckoutApi.md#checkout_cart_finalize_order_post) | **POST** /checkout/cart/finalizeOrder | Finalize Order
*CheckoutApi* | [**checkout_cart_get**](docs/CheckoutApi.md#checkout_cart_get) | **GET** /checkout/cart | Get cart
*CheckoutApi* | [**checkout_cart_handoff_post**](docs/CheckoutApi.md#checkout_cart_handoff_post) | **POST** /checkout/cart/handoff | Handoff cart
*CheckoutApi* | [**checkout_cart_profile_login_post**](docs/CheckoutApi.md#checkout_cart_profile_login_post) | **POST** /checkout/cart/profile/login | Profile login
*CheckoutApi* | [**checkout_cart_profile_logout_post**](docs/CheckoutApi.md#checkout_cart_profile_logout_post) | **POST** /checkout/cart/profile/logout | Profile logout
*CheckoutApi* | [**checkout_cart_profile_register_post**](docs/CheckoutApi.md#checkout_cart_profile_register_post) | **POST** /checkout/cart/profile/register | Profile registration
*CheckoutApi* | [**checkout_cart_put**](docs/CheckoutApi.md#checkout_cart_put) | **PUT** /checkout/cart | Update cart
*CheckoutApi* | [**checkout_cart_validate_post**](docs/CheckoutApi.md#checkout_cart_validate_post) | **POST** /checkout/cart/validate | Validate
*CheckoutApi* | [**checkout_city_state_post**](docs/CheckoutApi.md#checkout_city_state_post) | **POST** /checkout/city_state | City/State for Zip
*CheckoutApi* | [**checkout_related_items_item_id_post**](docs/CheckoutApi.md#checkout_related_items_item_id_post) | **POST** /checkout/relatedItems/{item_id} | Related items (specific item)
*CheckoutApi* | [**checkout_related_items_post**](docs/CheckoutApi.md#checkout_related_items_post) | **POST** /checkout/related_items | Related items
*CheckoutApi* | [**checkout_return_return_code_get**](docs/CheckoutApi.md#checkout_return_return_code_get) | **GET** /checkout/return/{return_code} | Get cart (by return code)
*CustomerApi* | [**customer_customers_customer_profile_oid_delete**](docs/CustomerApi.md#customer_customers_customer_profile_oid_delete) | **DELETE** /customer/customers/{customer_profile_oid} | Delete a customer
*CustomerApi* | [**customer_customers_customer_profile_oid_get**](docs/CustomerApi.md#customer_customers_customer_profile_oid_get) | **GET** /customer/customers/{customer_profile_oid} | Retrieve a customer
*CustomerApi* | [**customer_customers_customer_profile_oid_put**](docs/CustomerApi.md#customer_customers_customer_profile_oid_put) | **PUT** /customer/customers/{customer_profile_oid} | Update a customer
*CustomerApi* | [**customer_customers_get**](docs/CustomerApi.md#customer_customers_get) | **GET** /customer/customers | Retrieve customers
*CustomerApi* | [**customer_customers_post**](docs/CustomerApi.md#customer_customers_post) | **POST** /customer/customers | Insert a customer
*FulfillmentApi* | [**fulfillment_distribution_centers_distribution_center_code_acknowledgements_put**](docs/FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_acknowledgements_put) | **PUT** /fulfillment/distribution_centers/{distribution_center_code}/acknowledgements | Acknowledge receipt of orders.
*FulfillmentApi* | [**fulfillment_distribution_centers_distribution_center_code_inventory_post**](docs/FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_inventory_post) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/inventory | Update inventory
*FulfillmentApi* | [**fulfillment_distribution_centers_distribution_center_code_orders_get**](docs/FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_orders_get) | **GET** /fulfillment/distribution_centers/{distribution_center_code}/orders | Retrieve orders queued up for this distribution center.
*FulfillmentApi* | [**fulfillment_distribution_centers_distribution_center_code_shipments_post**](docs/FulfillmentApi.md#fulfillment_distribution_centers_distribution_center_code_shipments_post) | **POST** /fulfillment/distribution_centers/{distribution_center_code}/shipments | Mark orders as shipped
*FulfillmentApi* | [**fulfillment_distribution_centers_get**](docs/FulfillmentApi.md#fulfillment_distribution_centers_get) | **GET** /fulfillment/distribution_centers | Retrieve distribution centers
*ItemApi* | [**item_items_get**](docs/ItemApi.md#item_items_get) | **GET** /item/items | Retrieve items
*ItemApi* | [**item_items_merchant_item_oid_delete**](docs/ItemApi.md#item_items_merchant_item_oid_delete) | **DELETE** /item/items/{merchant_item_oid} | Delete an item
*ItemApi* | [**item_items_merchant_item_oid_get**](docs/ItemApi.md#item_items_merchant_item_oid_get) | **GET** /item/items/{merchant_item_oid} | Retrieve an item
*ItemApi* | [**item_items_merchant_item_oid_put**](docs/ItemApi.md#item_items_merchant_item_oid_put) | **PUT** /item/items/{merchant_item_oid} | Update an item
*ItemApi* | [**item_items_post**](docs/ItemApi.md#item_items_post) | **POST** /item/items | Create an item
*ItemApi* | [**item_temp_multimedia_post**](docs/ItemApi.md#item_temp_multimedia_post) | **POST** /item/temp_multimedia | Upload an image to the temporary multimedia.
*OauthApi* | [**oauth_revoke_post**](docs/OauthApi.md#oauth_revoke_post) | **POST** /oauth/revoke | Revoke this OAuth application.
*OauthApi* | [**oauth_token_post**](docs/OauthApi.md#oauth_token_post) | **POST** /oauth/token | Exchange authorization code for access token.
*OrderApi* | [**order_orders_get**](docs/OrderApi.md#order_orders_get) | **GET** /order/orders | Retrieve orders
*OrderApi* | [**order_orders_order_id_cancel_post**](docs/OrderApi.md#order_orders_order_id_cancel_post) | **POST** /order/orders/{order_id}/cancel | Cancel an order
*OrderApi* | [**order_orders_order_id_delete**](docs/OrderApi.md#order_orders_order_id_delete) | **DELETE** /order/orders/{order_id} | Delete an order
*OrderApi* | [**order_orders_order_id_get**](docs/OrderApi.md#order_orders_order_id_get) | **GET** /order/orders/{order_id} | Retrieve an order
*OrderApi* | [**order_orders_order_id_put**](docs/OrderApi.md#order_orders_order_id_put) | **PUT** /order/orders/{order_id} | Update an order
*OrderApi* | [**order_orders_order_id_resend_receipt_post**](docs/OrderApi.md#order_orders_order_id_resend_receipt_post) | **POST** /order/orders/{order_id}/resend_receipt | Resend receipt
*OrderApi* | [**order_orders_order_id_resend_shipment_confirmation_post**](docs/OrderApi.md#order_orders_order_id_resend_shipment_confirmation_post) | **POST** /order/orders/{order_id}/resend_shipment_confirmation | Resend shipment confirmation
*WebhookApi* | [**webhook_webhooks_get**](docs/WebhookApi.md#webhook_webhooks_get) | **GET** /webhook/webhooks | Retrieve webhooks
*WebhookApi* | [**webhook_webhooks_post**](docs/WebhookApi.md#webhook_webhooks_post) | **POST** /webhook/webhooks | Add a webhook
*WebhookApi* | [**webhook_webhooks_webhook_oid_delete**](docs/WebhookApi.md#webhook_webhooks_webhook_oid_delete) | **DELETE** /webhook/webhooks/{webhookOid} | Delete a webhook
*WebhookApi* | [**webhook_webhooks_webhook_oid_logs_get**](docs/WebhookApi.md#webhook_webhooks_webhook_oid_logs_get) | **GET** /webhook/webhooks/{webhookOid}/logs | Retrieve the log summaries
*WebhookApi* | [**webhook_webhooks_webhook_oid_logs_request_id_get**](docs/WebhookApi.md#webhook_webhooks_webhook_oid_logs_request_id_get) | **GET** /webhook/webhooks/{webhookOid}/logs/{requestId} | Retrieve an individual log
*WebhookApi* | [**webhook_webhooks_webhook_oid_put**](docs/WebhookApi.md#webhook_webhooks_webhook_oid_put) | **PUT** /webhook/webhooks/{webhookOid} | Update a webhook
*WebhookApi* | [**webhook_webhooks_webhook_oid_reflow_event_name_post**](docs/WebhookApi.md#webhook_webhooks_webhook_oid_reflow_event_name_post) | **POST** /webhook/webhooks/{webhookOid}/reflow/{eventName} | Resend events to the webhook endpoint.


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

