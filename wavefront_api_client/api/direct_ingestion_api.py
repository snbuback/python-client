# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wavefront_api_client.api_client import ApiClient


class DirectIngestionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def report(self, **kwargs):  # noqa: E501
        """Directly ingest data/data stream with specified format  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.report(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str f: Format of data to be ingested
        :param str body: Data to be ingested, in the specified format.  See https://docs.wavefront.com/direct_ingestion.html for more detail on how to format the data. Example in \"wavefront\" format:  <pre>test.metric 100 source=test.source</pre> which ingests a time series point with metric name \"test.metric\", source name \"test.source\", and value of 100 with timestamp of now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.report_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.report_with_http_info(**kwargs)  # noqa: E501
            return data

    def report_with_http_info(self, **kwargs):  # noqa: E501
        """Directly ingest data/data stream with specified format  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.report_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str f: Format of data to be ingested
        :param str body: Data to be ingested, in the specified format.  See https://docs.wavefront.com/direct_ingestion.html for more detail on how to format the data. Example in \"wavefront\" format:  <pre>test.metric 100 source=test.source</pre> which ingests a time series point with metric name \"test.metric\", source name \"test.source\", and value of 100 with timestamp of now.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['f', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method report" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'f' in params:
            query_params.append(('f', params['f']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream', 'application/x-www-form-urlencoded', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/report', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
