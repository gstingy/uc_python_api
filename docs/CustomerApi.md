# ultracart.CustomerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_customers_customer_profile_oid_get**](CustomerApi.md#customer_customers_customer_profile_oid_get) | **GET** /customer/customers/{customer_profile_oid} | Retrieve a customer
[**customer_customers_customer_profile_oid_put**](CustomerApi.md#customer_customers_customer_profile_oid_put) | **PUT** /customer/customers/{customer_profile_oid} | Update a customer
[**customer_customers_get**](CustomerApi.md#customer_customers_get) | **GET** /customer/customers | Retrieve customers


# **customer_customers_customer_profile_oid_get**
> CustomerResponse customer_customers_customer_profile_oid_get(customer_profile_oid, expand=expand)

Retrieve a customer

Retrieves a single customer using the specified customer profile oid. 

### Example 
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
api_instance = ultracart.CustomerApi()
customer_profile_oid = 56 # int | The customer oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve a customer
    api_response = api_instance.customer_customers_customer_profile_oid_get(customer_profile_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomerApi->customer_customers_customer_profile_oid_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customers_customer_profile_oid_put**
> CustomerResponse customer_customers_customer_profile_oid_put(customer, customer_profile_oid)

Update a customer

Update a customer on the UltraCart account. 

### Example 
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
api_instance = ultracart.CustomerApi()
customer = ultracart.Customer() # Customer | Customer to update
customer_profile_oid = 56 # int | The customer_profile_oid to update.

try: 
    # Update a customer
    api_response = api_instance.customer_customers_customer_profile_oid_put(customer, customer_profile_oid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomerApi->customer_customers_customer_profile_oid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| Customer to update | 
 **customer_profile_oid** | **int**| The customer_profile_oid to update. | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customers_get**
> CustomersResponse customer_customers_get(email=email, qb_class=qb_class, quickbooks_code=quickbooks_code, last_modified_dts_start=last_modified_dts_start, last_modified_dts_end=last_modified_dts_end, signup_dts_start=signup_dts_start, signup_dts_end=signup_dts_end, billing_first_name=billing_first_name, billing_last_name=billing_last_name, billing_company=billing_company, billing_city=billing_city, billing_state=billing_state, billing_postal_code=billing_postal_code, billing_country_code=billing_country_code, billing_day_phone=billing_day_phone, billing_evening_phone=billing_evening_phone, shipping_first_name=shipping_first_name, shipping_last_name=shipping_last_name, shipping_company=shipping_company, shipping_city=shipping_city, shipping_state=shipping_state, shipping_postal_code=shipping_postal_code, shipping_country_code=shipping_country_code, shipping_day_phone=shipping_day_phone, shipping_evening_phone=shipping_evening_phone, pricing_tier_oid=pricing_tier_oid, pricing_tier_name=pricing_tier_name, limit=limit, offset=offset, since=since, sort=sort, expand=expand)

Retrieve customers

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example 
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
api_instance = ultracart.CustomerApi()
email = 'email_example' # str | Email (optional)
qb_class = 'qb_class_example' # str | Quickbooks class (optional)
quickbooks_code = 'quickbooks_code_example' # str | Quickbooks code (optional)
last_modified_dts_start = 'last_modified_dts_start_example' # str | Last modified date start (optional)
last_modified_dts_end = 'last_modified_dts_end_example' # str | Last modified date end (optional)
signup_dts_start = 'signup_dts_start_example' # str | Signup date start (optional)
signup_dts_end = 'signup_dts_end_example' # str | Signup date end (optional)
billing_first_name = 'billing_first_name_example' # str | Billing first name (optional)
billing_last_name = 'billing_last_name_example' # str | Billing last name (optional)
billing_company = 'billing_company_example' # str | Billing company (optional)
billing_city = 'billing_city_example' # str | Billing city (optional)
billing_state = 'billing_state_example' # str | Billing state (optional)
billing_postal_code = 'billing_postal_code_example' # str | Billing postal code (optional)
billing_country_code = 'billing_country_code_example' # str | Billing country code (optional)
billing_day_phone = 'billing_day_phone_example' # str | Billing day phone (optional)
billing_evening_phone = 'billing_evening_phone_example' # str | Billing evening phone (optional)
shipping_first_name = 'shipping_first_name_example' # str | Shipping first name (optional)
shipping_last_name = 'shipping_last_name_example' # str | Shipping last name (optional)
shipping_company = 'shipping_company_example' # str | Shipping company (optional)
shipping_city = 'shipping_city_example' # str | Shipping city (optional)
shipping_state = 'shipping_state_example' # str | Shipping state (optional)
shipping_postal_code = 'shipping_postal_code_example' # str | Shipping postal code (optional)
shipping_country_code = 'shipping_country_code_example' # str | Shipping country code (optional)
shipping_day_phone = 'shipping_day_phone_example' # str | Shipping day phone (optional)
shipping_evening_phone = 'shipping_evening_phone_example' # str | Shipping evening phone (optional)
pricing_tier_oid = 56 # int | Pricing tier oid (optional)
pricing_tier_name = 'pricing_tier_name_example' # str | Pricing tier name (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch customers that have been created/modified since this date/time. (optional)
sort = 'sort_example' # str | The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve customers
    api_response = api_instance.customer_customers_get(email=email, qb_class=qb_class, quickbooks_code=quickbooks_code, last_modified_dts_start=last_modified_dts_start, last_modified_dts_end=last_modified_dts_end, signup_dts_start=signup_dts_start, signup_dts_end=signup_dts_end, billing_first_name=billing_first_name, billing_last_name=billing_last_name, billing_company=billing_company, billing_city=billing_city, billing_state=billing_state, billing_postal_code=billing_postal_code, billing_country_code=billing_country_code, billing_day_phone=billing_day_phone, billing_evening_phone=billing_evening_phone, shipping_first_name=shipping_first_name, shipping_last_name=shipping_last_name, shipping_company=shipping_company, shipping_city=shipping_city, shipping_state=shipping_state, shipping_postal_code=shipping_postal_code, shipping_country_code=shipping_country_code, shipping_day_phone=shipping_day_phone, shipping_evening_phone=shipping_evening_phone, pricing_tier_oid=pricing_tier_oid, pricing_tier_name=pricing_tier_name, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomerApi->customer_customers_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email | [optional] 
 **qb_class** | **str**| Quickbooks class | [optional] 
 **quickbooks_code** | **str**| Quickbooks code | [optional] 
 **last_modified_dts_start** | **str**| Last modified date start | [optional] 
 **last_modified_dts_end** | **str**| Last modified date end | [optional] 
 **signup_dts_start** | **str**| Signup date start | [optional] 
 **signup_dts_end** | **str**| Signup date end | [optional] 
 **billing_first_name** | **str**| Billing first name | [optional] 
 **billing_last_name** | **str**| Billing last name | [optional] 
 **billing_company** | **str**| Billing company | [optional] 
 **billing_city** | **str**| Billing city | [optional] 
 **billing_state** | **str**| Billing state | [optional] 
 **billing_postal_code** | **str**| Billing postal code | [optional] 
 **billing_country_code** | **str**| Billing country code | [optional] 
 **billing_day_phone** | **str**| Billing day phone | [optional] 
 **billing_evening_phone** | **str**| Billing evening phone | [optional] 
 **shipping_first_name** | **str**| Shipping first name | [optional] 
 **shipping_last_name** | **str**| Shipping last name | [optional] 
 **shipping_company** | **str**| Shipping company | [optional] 
 **shipping_city** | **str**| Shipping city | [optional] 
 **shipping_state** | **str**| Shipping state | [optional] 
 **shipping_postal_code** | **str**| Shipping postal code | [optional] 
 **shipping_country_code** | **str**| Shipping country code | [optional] 
 **shipping_day_phone** | **str**| Shipping day phone | [optional] 
 **shipping_evening_phone** | **str**| Shipping evening phone | [optional] 
 **pricing_tier_oid** | **int**| Pricing tier oid | [optional] 
 **pricing_tier_name** | **str**| Pricing tier name | [optional] 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional] 
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomersResponse**](CustomersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
