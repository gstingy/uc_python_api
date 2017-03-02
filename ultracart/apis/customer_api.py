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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def customer_customers_customer_profile_oid_get(self, customer_profile_oid, **kwargs):
        """
        Retrieve a customer
        Retrieves a single customer using the specified customer profile oid. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customers_customer_profile_oid_get(customer_profile_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_profile_oid: The customer oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: CustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customers_customer_profile_oid_get_with_http_info(customer_profile_oid, **kwargs)
        else:
            (data) = self.customer_customers_customer_profile_oid_get_with_http_info(customer_profile_oid, **kwargs)
            return data

    def customer_customers_customer_profile_oid_get_with_http_info(self, customer_profile_oid, **kwargs):
        """
        Retrieve a customer
        Retrieves a single customer using the specified customer profile oid. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customers_customer_profile_oid_get_with_http_info(customer_profile_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_profile_oid: The customer oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: CustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_profile_oid', 'expand']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customers_customer_profile_oid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_profile_oid' is set
        if ('customer_profile_oid' not in params) or (params['customer_profile_oid'] is None):
            raise ValueError("Missing the required parameter `customer_profile_oid` when calling `customer_customers_customer_profile_oid_get`")

        resource_path = '/customer/customers/{customer_profile_oid}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_profile_oid' in params:
            path_params['customer_profile_oid'] = params['customer_profile_oid']

        query_params = {}
        if 'expand' in params:
            query_params['_expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def customer_customers_customer_profile_oid_put(self, customer, customer_profile_oid, **kwargs):
        """
        Update a customer
        Update a customer on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customers_customer_profile_oid_put(customer, customer_profile_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Customer customer: Customer to update (required)
        :param int customer_profile_oid: The customer_profile_oid to update. (required)
        :return: CustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customers_customer_profile_oid_put_with_http_info(customer, customer_profile_oid, **kwargs)
        else:
            (data) = self.customer_customers_customer_profile_oid_put_with_http_info(customer, customer_profile_oid, **kwargs)
            return data

    def customer_customers_customer_profile_oid_put_with_http_info(self, customer, customer_profile_oid, **kwargs):
        """
        Update a customer
        Update a customer on the UltraCart account. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customers_customer_profile_oid_put_with_http_info(customer, customer_profile_oid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Customer customer: Customer to update (required)
        :param int customer_profile_oid: The customer_profile_oid to update. (required)
        :return: CustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer', 'customer_profile_oid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customers_customer_profile_oid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer' is set
        if ('customer' not in params) or (params['customer'] is None):
            raise ValueError("Missing the required parameter `customer` when calling `customer_customers_customer_profile_oid_put`")
        # verify the required parameter 'customer_profile_oid' is set
        if ('customer_profile_oid' not in params) or (params['customer_profile_oid'] is None):
            raise ValueError("Missing the required parameter `customer_profile_oid` when calling `customer_customers_customer_profile_oid_put`")

        resource_path = '/customer/customers/{customer_profile_oid}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_profile_oid' in params:
            path_params['customer_profile_oid'] = params['customer_profile_oid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer' in params:
            body_params = params['customer']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json; charset=UTF-8'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CustomerResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def customer_customers_get(self, **kwargs):
        """
        Retrieve customers
        Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customers_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email: Email
        :param str qb_class: Quickbooks class
        :param str quickbooks_code: Quickbooks code
        :param str last_modified_dts_start: Last modified date start
        :param str last_modified_dts_end: Last modified date end
        :param str signup_dts_start: Signup date start
        :param str signup_dts_end: Signup date end
        :param str billing_first_name: Billing first name
        :param str billing_last_name: Billing last name
        :param str billing_company: Billing company
        :param str billing_city: Billing city
        :param str billing_state: Billing state
        :param str billing_postal_code: Billing postal code
        :param str billing_country_code: Billing country code
        :param str billing_day_phone: Billing day phone
        :param str billing_evening_phone: Billing evening phone
        :param str shipping_first_name: Shipping first name
        :param str shipping_last_name: Shipping last name
        :param str shipping_company: Shipping company
        :param str shipping_city: Shipping city
        :param str shipping_state: Shipping state
        :param str shipping_postal_code: Shipping postal code
        :param str shipping_country_code: Shipping country code
        :param str shipping_day_phone: Shipping day phone
        :param str shipping_evening_phone: Shipping evening phone
        :param int pricing_tier_oid: Pricing tier oid
        :param str pricing_tier_name: Pricing tier name
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch customers that have been created/modified since this date/time.
        :param str sort: The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: CustomersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customers_get_with_http_info(**kwargs)
        else:
            (data) = self.customer_customers_get_with_http_info(**kwargs)
            return data

    def customer_customers_get_with_http_info(self, **kwargs):
        """
        Retrieve customers
        Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customers_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str email: Email
        :param str qb_class: Quickbooks class
        :param str quickbooks_code: Quickbooks code
        :param str last_modified_dts_start: Last modified date start
        :param str last_modified_dts_end: Last modified date end
        :param str signup_dts_start: Signup date start
        :param str signup_dts_end: Signup date end
        :param str billing_first_name: Billing first name
        :param str billing_last_name: Billing last name
        :param str billing_company: Billing company
        :param str billing_city: Billing city
        :param str billing_state: Billing state
        :param str billing_postal_code: Billing postal code
        :param str billing_country_code: Billing country code
        :param str billing_day_phone: Billing day phone
        :param str billing_evening_phone: Billing evening phone
        :param str shipping_first_name: Shipping first name
        :param str shipping_last_name: Shipping last name
        :param str shipping_company: Shipping company
        :param str shipping_city: Shipping city
        :param str shipping_state: Shipping state
        :param str shipping_postal_code: Shipping postal code
        :param str shipping_country_code: Shipping country code
        :param str shipping_day_phone: Shipping day phone
        :param str shipping_evening_phone: Shipping evening phone
        :param int pricing_tier_oid: Pricing tier oid
        :param str pricing_tier_name: Pricing tier name
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch customers that have been created/modified since this date/time.
        :param str sort: The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: CustomersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'qb_class', 'quickbooks_code', 'last_modified_dts_start', 'last_modified_dts_end', 'signup_dts_start', 'signup_dts_end', 'billing_first_name', 'billing_last_name', 'billing_company', 'billing_city', 'billing_state', 'billing_postal_code', 'billing_country_code', 'billing_day_phone', 'billing_evening_phone', 'shipping_first_name', 'shipping_last_name', 'shipping_company', 'shipping_city', 'shipping_state', 'shipping_postal_code', 'shipping_country_code', 'shipping_day_phone', 'shipping_evening_phone', 'pricing_tier_oid', 'pricing_tier_name', 'limit', 'offset', 'since', 'sort', 'expand']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customers_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/customer/customers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'email' in params:
            query_params['email'] = params['email']
        if 'qb_class' in params:
            query_params['qb_class'] = params['qb_class']
        if 'quickbooks_code' in params:
            query_params['quickbooks_code'] = params['quickbooks_code']
        if 'last_modified_dts_start' in params:
            query_params['last_modified_dts_start'] = params['last_modified_dts_start']
        if 'last_modified_dts_end' in params:
            query_params['last_modified_dts_end'] = params['last_modified_dts_end']
        if 'signup_dts_start' in params:
            query_params['signup_dts_start'] = params['signup_dts_start']
        if 'signup_dts_end' in params:
            query_params['signup_dts_end'] = params['signup_dts_end']
        if 'billing_first_name' in params:
            query_params['billing_first_name'] = params['billing_first_name']
        if 'billing_last_name' in params:
            query_params['billing_last_name'] = params['billing_last_name']
        if 'billing_company' in params:
            query_params['billing_company'] = params['billing_company']
        if 'billing_city' in params:
            query_params['billing_city'] = params['billing_city']
        if 'billing_state' in params:
            query_params['billing_state'] = params['billing_state']
        if 'billing_postal_code' in params:
            query_params['billing_postal_code'] = params['billing_postal_code']
        if 'billing_country_code' in params:
            query_params['billing_country_code'] = params['billing_country_code']
        if 'billing_day_phone' in params:
            query_params['billing_day_phone'] = params['billing_day_phone']
        if 'billing_evening_phone' in params:
            query_params['billing_evening_phone'] = params['billing_evening_phone']
        if 'shipping_first_name' in params:
            query_params['shipping_first_name'] = params['shipping_first_name']
        if 'shipping_last_name' in params:
            query_params['shipping_last_name'] = params['shipping_last_name']
        if 'shipping_company' in params:
            query_params['shipping_company'] = params['shipping_company']
        if 'shipping_city' in params:
            query_params['shipping_city'] = params['shipping_city']
        if 'shipping_state' in params:
            query_params['shipping_state'] = params['shipping_state']
        if 'shipping_postal_code' in params:
            query_params['shipping_postal_code'] = params['shipping_postal_code']
        if 'shipping_country_code' in params:
            query_params['shipping_country_code'] = params['shipping_country_code']
        if 'shipping_day_phone' in params:
            query_params['shipping_day_phone'] = params['shipping_day_phone']
        if 'shipping_evening_phone' in params:
            query_params['shipping_evening_phone'] = params['shipping_evening_phone']
        if 'pricing_tier_oid' in params:
            query_params['pricing_tier_oid'] = params['pricing_tier_oid']
        if 'pricing_tier_name' in params:
            query_params['pricing_tier_name'] = params['pricing_tier_name']
        if 'limit' in params:
            query_params['_limit'] = params['limit']
        if 'offset' in params:
            query_params['_offset'] = params['offset']
        if 'since' in params:
            query_params['_since'] = params['since']
        if 'sort' in params:
            query_params['_sort'] = params['sort']
        if 'expand' in params:
            query_params['_expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CustomersResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
