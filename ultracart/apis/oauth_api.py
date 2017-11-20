# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

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


class OauthApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oauth_access_token(self, client_id, grant_type, **kwargs):
        """
        Exchange authorization code for access token.
        The final leg in the OAuth process which exchanges the specified access token for the access code needed to make API calls. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.oauth_access_token(client_id, grant_type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_id: The OAuth application client_id. (required)
        :param str grant_type: Type of grant (required)
        :param str code: Authorization code received back from the browser redirect
        :param str redirect_uri: The URI that you redirect the browser to to start the authorization process
        :param str refresh_token: The refresh token received during the original grant_type=authorization_code that can be used to return a new access token
        :return: OauthTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.oauth_access_token_with_http_info(client_id, grant_type, **kwargs)
        else:
            (data) = self.oauth_access_token_with_http_info(client_id, grant_type, **kwargs)
            return data

    def oauth_access_token_with_http_info(self, client_id, grant_type, **kwargs):
        """
        Exchange authorization code for access token.
        The final leg in the OAuth process which exchanges the specified access token for the access code needed to make API calls. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.oauth_access_token_with_http_info(client_id, grant_type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_id: The OAuth application client_id. (required)
        :param str grant_type: Type of grant (required)
        :param str code: Authorization code received back from the browser redirect
        :param str redirect_uri: The URI that you redirect the browser to to start the authorization process
        :param str refresh_token: The refresh token received during the original grant_type=authorization_code that can be used to return a new access token
        :return: OauthTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'grant_type', 'code', 'redirect_uri', 'refresh_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_access_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `oauth_access_token`")
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params) or (params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `oauth_access_token`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))
        if 'code' in params:
            form_params.append(('code', params['code']))
        if 'redirect_uri' in params:
            form_params.append(('redirect_uri', params['redirect_uri']))
        if 'refresh_token' in params:
            form_params.append(('refresh_token', params['refresh_token']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['ultraCartBrowserApiKey', 'ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/oauth/token', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OauthTokenResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def oauth_revoke(self, client_id, token, **kwargs):
        """
        Revoke this OAuth application.
        Revokes the OAuth application associated with the specified client_id and token. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.oauth_revoke(client_id, token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_id: The OAuth application client_id. (required)
        :param str token: The OAuth access token that is to be revoked.. (required)
        :return: OauthRevokeSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.oauth_revoke_with_http_info(client_id, token, **kwargs)
        else:
            (data) = self.oauth_revoke_with_http_info(client_id, token, **kwargs)
            return data

    def oauth_revoke_with_http_info(self, client_id, token, **kwargs):
        """
        Revoke this OAuth application.
        Revokes the OAuth application associated with the specified client_id and token. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.oauth_revoke_with_http_info(client_id, token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str client_id: The OAuth application client_id. (required)
        :param str token: The OAuth access token that is to be revoked.. (required)
        :return: OauthRevokeSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_revoke" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `oauth_revoke`")
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `oauth_revoke`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))
        if 'token' in params:
            form_params.append(('token', params['token']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['ultraCartBrowserApiKey', 'ultraCartOauth', 'ultraCartSimpleApiKey']

        return self.api_client.call_api('/oauth/revoke', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OauthRevokeSuccessResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
