# Coupon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_oid** | **int** | Associates an order with an affiliate when this value is set. | [optional] 
**amount_off_items** | [**CouponAmountOffItems**](CouponAmountOffItems.md) |  | [optional] 
**amount_off_shipping** | [**CouponAmountOffShipping**](CouponAmountOffShipping.md) |  | [optional] 
**amount_off_shipping_with_items_purchase** | [**CouponAmountOffShippingWithItemsPurchase**](CouponAmountOffShippingWithItemsPurchase.md) |  | [optional] 
**amount_off_subtotal** | [**CouponAmountOffSubtotal**](CouponAmountOffSubtotal.md) |  | [optional] 
**amount_off_subtotal_and_free_shipping** | [**CouponAmountOffSubtotalFreeShippingWithPurchase**](CouponAmountOffSubtotalFreeShippingWithPurchase.md) |  | [optional] 
**amount_off_subtotal_and_shipping** | [**CouponAmountOffSubtotalAndShipping**](CouponAmountOffSubtotalAndShipping.md) |  | [optional] 
**amount_off_subtotal_with_block_purchase** | [**CouponAmountOffSubtotalWithBlockPurchase**](CouponAmountOffSubtotalWithBlockPurchase.md) |  | [optional] 
**amount_off_subtotal_with_items_purchase** | [**CouponAmountOffSubtotalWithItemsPurchase**](CouponAmountOffSubtotalWithItemsPurchase.md) |  | [optional] 
**can_be_used_with_other_coupons** | **bool** | True if this coupon can be used with other coupons in a single order. | [optional] 
**coupon_oid** | **int** | Coupon oid. | [optional] 
**coupon_type** | **str** | Coupon type. | [optional] 
**description** | **str** | Description of the coupon up to 50 characters. | [optional] 
**discount_item_with_item_purchase** | [**CouponDiscountItemWithItemPurchase**](CouponDiscountItemWithItemPurchase.md) |  | [optional] 
**discount_items** | [**CouponDiscountItems**](CouponDiscountItems.md) |  | [optional] 
**expiration_dts** | **str** | Date/time when coupon expires | [optional] 
**free_item_and_shipping_with_subtotal** | [**CouponFreeItemAndShippingWithSubtotal**](CouponFreeItemAndShippingWithSubtotal.md) |  | [optional] 
**free_item_with_item_purchase** | [**CouponFreeItemWithItemPurchase**](CouponFreeItemWithItemPurchase.md) |  | [optional] 
**free_item_with_subtotal** | [**CouponFreeItemWithSubtotal**](CouponFreeItemWithSubtotal.md) |  | [optional] 
**free_items_with_item_purchase** | [**CouponFreeItemsWithItemPurchase**](CouponFreeItemsWithItemPurchase.md) |  | [optional] 
**free_items_with_mixmatch_purchase** | [**CouponFreeItemsWithMixMatchPurchase**](CouponFreeItemsWithMixMatchPurchase.md) |  | [optional] 
**free_shipping** | [**CouponFreeShipping**](CouponFreeShipping.md) |  | [optional] 
**free_shipping_specific_items** | [**CouponFreeShippingSpecificItems**](CouponFreeShippingSpecificItems.md) |  | [optional] 
**free_shipping_with_items_purchase** | [**CouponFreeShippingWithItemsPurchase**](CouponFreeShippingWithItemsPurchase.md) |  | [optional] 
**free_shipping_with_subtotal** | [**CouponFreeShippingWithSubtotal**](CouponFreeShippingWithSubtotal.md) |  | [optional] 
**merchant_code** | **str** | Merchant code of coupon up to 20 characters. | [optional] 
**multiple_amounts_off_items** | [**CouponMultipleAmountsOffItems**](CouponMultipleAmountsOffItems.md) |  | [optional] 
**no_discount** | [**CouponNoDiscount**](CouponNoDiscount.md) |  | [optional] 
**percent_off_item_with_items_quantity_purchase** | [**CouponPercentOffItemWithItemsQuantityPurchase**](CouponPercentOffItemWithItemsQuantityPurchase.md) |  | [optional] 
**percent_off_items** | [**CouponPercentOffItems**](CouponPercentOffItems.md) |  | [optional] 
**percent_off_items_and_free_shipping** | [**CouponPercentOffItemsAndFreeShipping**](CouponPercentOffItemsAndFreeShipping.md) |  | [optional] 
**percent_off_items_with_items_purchase** | [**CouponPercentOffItemsWithItemsPurchase**](CouponPercentOffItemsWithItemsPurchase.md) |  | [optional] 
**percent_off_retail_price_items** | [**CouponPercentOffRetailPriceItems**](CouponPercentOffRetailPriceItems.md) |  | [optional] 
**percent_off_shipping** | [**CouponPercentOffShipping**](CouponPercentOffShipping.md) |  | [optional] 
**percent_off_subtotal** | [**CouponPercentOffSubtotal**](CouponPercentOffSubtotal.md) |  | [optional] 
**percent_off_subtotal_and_free_shipping** | [**CouponPercentOffSubtotalAndFreeShipping**](CouponPercentOffSubtotalAndFreeShipping.md) |  | [optional] 
**percent_off_subtotal_limit** | [**CouponPercentOffSubtotalLimit**](CouponPercentOffSubtotalLimit.md) |  | [optional] 
**percent_off_subtotal_with_items_purchase** | [**CouponPercentOffSubtotalWithItemsPurchase**](CouponPercentOffSubtotalWithItemsPurchase.md) |  | [optional] 
**percent_off_subtotal_with_subtotal** | [**CouponPercentOffSubtotalWithSubtotal**](CouponPercentOffSubtotalWithSubtotal.md) |  | [optional] 
**quickbooks_code** | **str** | Quickbooks accounting code. | [optional] 
**start_dts** | **str** | Date/time when coupon is valid | [optional] 
**tiered_amount_off_item** | [**CouponTieredAmountOffItem**](CouponTieredAmountOffItem.md) |  | [optional] 
**tiered_amount_off_subtotal** | [**CouponTieredAmountOffSubtotal**](CouponTieredAmountOffSubtotal.md) |  | [optional] 
**tiered_percent_off_items** | [**CouponTieredPercentOffItems**](CouponTieredPercentOffItems.md) |  | [optional] 
**tiered_percent_off_shipping** | [**CouponTieredPercentOffShipping**](CouponTieredPercentOffShipping.md) |  | [optional] 
**tiered_percent_off_subtotal** | [**CouponTieredPercentOffSubtotal**](CouponTieredPercentOffSubtotal.md) |  | [optional] 
**usable_by** | **str** | Who may use this coupon. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

