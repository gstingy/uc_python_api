# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class AutoOrderApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_auto_order(self, auto_order_oid, **kwargs):
        """
        Retrieve an auto order
        Retrieves a single auto order using the specified auto order oid. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_order(auto_order_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param int auto_order_oid: The auto order oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_auto_order_with_http_info(auto_order_oid, **kwargs)
        else:
            (data) = self.get_auto_order_with_http_info(auto_order_oid, **kwargs)
            return data

    def get_auto_order_with_http_info(self, auto_order_oid, **kwargs):
        """
        Retrieve an auto order
        Retrieves a single auto order using the specified auto order oid. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_order_with_http_info(auto_order_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param int auto_order_oid: The auto order oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auto_order_oid', 'expand']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auto_order_oid' is set
        if ('auto_order_oid' not in params) or (params['auto_order_oid'] is None):
            raise ValueError("Missing the required parameter `auto_order_oid` when calling `get_auto_order`")


        collection_formats = {}

        path_params = {}
        if 'auto_order_oid' in params:
            path_params['auto_order_oid'] = params['auto_order_oid']

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/auto_order/auto_orders/{auto_order_oid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AutoOrderResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_auto_order_by_code(self, auto_order_code, **kwargs):
        """
        Retrieve an auto order
        Retrieves a single auto order using the specified reference (original) order id. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_order_by_code(auto_order_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auto_order_code: The auto order oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_auto_order_by_code_with_http_info(auto_order_code, **kwargs)
        else:
            (data) = self.get_auto_order_by_code_with_http_info(auto_order_code, **kwargs)
            return data

    def get_auto_order_by_code_with_http_info(self, auto_order_code, **kwargs):
        """
        Retrieve an auto order
        Retrieves a single auto order using the specified reference (original) order id. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_order_by_code_with_http_info(auto_order_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auto_order_code: The auto order oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auto_order_code', 'expand']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_order_by_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auto_order_code' is set
        if ('auto_order_code' not in params) or (params['auto_order_code'] is None):
            raise ValueError("Missing the required parameter `auto_order_code` when calling `get_auto_order_by_code`")


        collection_formats = {}

        path_params = {}
        if 'auto_order_code' in params:
            path_params['auto_order_code'] = params['auto_order_code']

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/auto_order/auto_orders/code/{auto_order_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AutoOrderResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_auto_order_by_reference_order_id(self, reference_order_id, **kwargs):
        """
        Retrieve an auto order
        Retrieves a single auto order using the specified reference (original) order id. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_order_by_reference_order_id(reference_order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reference_order_id: The auto order oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_auto_order_by_reference_order_id_with_http_info(reference_order_id, **kwargs)
        else:
            (data) = self.get_auto_order_by_reference_order_id_with_http_info(reference_order_id, **kwargs)
            return data

    def get_auto_order_by_reference_order_id_with_http_info(self, reference_order_id, **kwargs):
        """
        Retrieve an auto order
        Retrieves a single auto order using the specified reference (original) order id. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_order_by_reference_order_id_with_http_info(reference_order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reference_order_id: The auto order oid to retrieve. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reference_order_id', 'expand']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_order_by_reference_order_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reference_order_id' is set
        if ('reference_order_id' not in params) or (params['reference_order_id'] is None):
            raise ValueError("Missing the required parameter `reference_order_id` when calling `get_auto_order_by_reference_order_id`")


        collection_formats = {}

        path_params = {}
        if 'reference_order_id' in params:
            path_params['reference_order_id'] = params['reference_order_id']

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/auto_order/auto_orders/reference_order_id/{reference_order_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AutoOrderResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_auto_orders(self, **kwargs):
        """
        Retrieve auto orders
        Retrieves auto orders from the account.  If no parameters are specified, all auto orders will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_orders(async=True)
        >>> result = thread.get()

        :param async bool
        :param str auto_order_code: Auto order code
        :param str original_order_id: Original order id
        :param str first_name: First name
        :param str last_name: Last name
        :param str company: Company
        :param str city: City
        :param str state: State
        :param str postal_code: Postal code
        :param str country_code: Country code (ISO-3166 two letter)
        :param str phone: Phone
        :param str email: Email
        :param str original_order_date_begin: Original order date begin
        :param str original_order_date_end: Original order date end
        :param str next_shipment_date_begin: Next shipment date begin
        :param str next_shipment_date_end: Next shipment date end
        :param str card_type: Card type
        :param str item_id: Item ID
        :param str status: Status
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch auto orders that have been created/modified since this date/time.
        :param str sort: The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_auto_orders_with_http_info(**kwargs)
        else:
            (data) = self.get_auto_orders_with_http_info(**kwargs)
            return data

    def get_auto_orders_with_http_info(self, **kwargs):
        """
        Retrieve auto orders
        Retrieves auto orders from the account.  If no parameters are specified, all auto orders will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_auto_orders_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str auto_order_code: Auto order code
        :param str original_order_id: Original order id
        :param str first_name: First name
        :param str last_name: Last name
        :param str company: Company
        :param str city: City
        :param str state: State
        :param str postal_code: Postal code
        :param str country_code: Country code (ISO-3166 two letter)
        :param str phone: Phone
        :param str email: Email
        :param str original_order_date_begin: Original order date begin
        :param str original_order_date_end: Original order date end
        :param str next_shipment_date_begin: Next shipment date begin
        :param str next_shipment_date_end: Next shipment date end
        :param str card_type: Card type
        :param str item_id: Item ID
        :param str status: Status
        :param int limit: The maximum number of records to return on this one API call. (Max 200)
        :param int offset: Pagination of the record set.  Offset is a zero based index.
        :param str since: Fetch auto orders that have been created/modified since this date/time.
        :param str sort: The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending.
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auto_order_code', 'original_order_id', 'first_name', 'last_name', 'company', 'city', 'state', 'postal_code', 'country_code', 'phone', 'email', 'original_order_date_begin', 'original_order_date_end', 'next_shipment_date_begin', 'next_shipment_date_end', 'card_type', 'item_id', 'status', 'limit', 'offset', 'since', 'sort', 'expand']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_orders" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'auto_order_code' in params:
            query_params.append(('auto_order_code', params['auto_order_code']))
        if 'original_order_id' in params:
            query_params.append(('original_order_id', params['original_order_id']))
        if 'first_name' in params:
            query_params.append(('first_name', params['first_name']))
        if 'last_name' in params:
            query_params.append(('last_name', params['last_name']))
        if 'company' in params:
            query_params.append(('company', params['company']))
        if 'city' in params:
            query_params.append(('city', params['city']))
        if 'state' in params:
            query_params.append(('state', params['state']))
        if 'postal_code' in params:
            query_params.append(('postal_code', params['postal_code']))
        if 'country_code' in params:
            query_params.append(('country_code', params['country_code']))
        if 'phone' in params:
            query_params.append(('phone', params['phone']))
        if 'email' in params:
            query_params.append(('email', params['email']))
        if 'original_order_date_begin' in params:
            query_params.append(('original_order_date_begin', params['original_order_date_begin']))
        if 'original_order_date_end' in params:
            query_params.append(('original_order_date_end', params['original_order_date_end']))
        if 'next_shipment_date_begin' in params:
            query_params.append(('next_shipment_date_begin', params['next_shipment_date_begin']))
        if 'next_shipment_date_end' in params:
            query_params.append(('next_shipment_date_end', params['next_shipment_date_end']))
        if 'card_type' in params:
            query_params.append(('card_type', params['card_type']))
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))
        if 'status' in params:
            query_params.append(('status', params['status']))
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))
        if 'since' in params:
            query_params.append(('_since', params['since']))
        if 'sort' in params:
            query_params.append(('_sort', params['sort']))
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/auto_order/auto_orders', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AutoOrdersResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_auto_order(self, auto_order, auto_order_oid, **kwargs):
        """
        Update an auto order
        Update an auto order on the UltraCart account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_auto_order(auto_order, auto_order_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param AutoOrder auto_order: Auto order to update (required)
        :param int auto_order_oid: The auto order oid to update. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_auto_order_with_http_info(auto_order, auto_order_oid, **kwargs)
        else:
            (data) = self.update_auto_order_with_http_info(auto_order, auto_order_oid, **kwargs)
            return data

    def update_auto_order_with_http_info(self, auto_order, auto_order_oid, **kwargs):
        """
        Update an auto order
        Update an auto order on the UltraCart account. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_auto_order_with_http_info(auto_order, auto_order_oid, async=True)
        >>> result = thread.get()

        :param async bool
        :param AutoOrder auto_order: Auto order to update (required)
        :param int auto_order_oid: The auto order oid to update. (required)
        :param str expand: The object expansion to perform on the result.  See documentation for examples
        :return: AutoOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auto_order', 'auto_order_oid', 'expand']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_auto_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auto_order' is set
        if ('auto_order' not in params) or (params['auto_order'] is None):
            raise ValueError("Missing the required parameter `auto_order` when calling `update_auto_order`")
        # verify the required parameter 'auto_order_oid' is set
        if ('auto_order_oid' not in params) or (params['auto_order_oid'] is None):
            raise ValueError("Missing the required parameter `auto_order_oid` when calling `update_auto_order`")


        collection_formats = {}

        path_params = {}
        if 'auto_order_oid' in params:
            path_params['auto_order_oid'] = params['auto_order_oid']

        query_params = []
        if 'expand' in params:
            query_params.append(('_expand', params['expand']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'auto_order' in params:
            body_params = params['auto_order']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json; charset=UTF-8'])

        # Authentication setting
        auth_settings = ['ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/auto_order/auto_orders/{auto_order_oid}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AutoOrderResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
