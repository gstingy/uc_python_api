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

from pprint import pformat
from six import iteritems
import re


class TempMultimediaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error=None, metadata=None, success=None, temp_multimedia=None):
        """
        TempMultimediaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error': 'Error',
            'metadata': 'ResponseMetadata',
            'success': 'bool',
            'temp_multimedia': 'TempMultimedia'
        }

        self.attribute_map = {
            'error': 'error',
            'metadata': 'metadata',
            'success': 'success',
            'temp_multimedia': 'temp_multimedia'
        }

        self._error = error
        self._metadata = metadata
        self._success = success
        self._temp_multimedia = temp_multimedia

    @property
    def error(self):
        """
        Gets the error of this TempMultimediaResponse.


        :return: The error of this TempMultimediaResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this TempMultimediaResponse.


        :param error: The error of this TempMultimediaResponse.
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """
        Gets the metadata of this TempMultimediaResponse.


        :return: The metadata of this TempMultimediaResponse.
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TempMultimediaResponse.


        :param metadata: The metadata of this TempMultimediaResponse.
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """
        Gets the success of this TempMultimediaResponse.


        :return: The success of this TempMultimediaResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this TempMultimediaResponse.


        :param success: The success of this TempMultimediaResponse.
        :type: bool
        """

        self._success = success

    @property
    def temp_multimedia(self):
        """
        Gets the temp_multimedia of this TempMultimediaResponse.


        :return: The temp_multimedia of this TempMultimediaResponse.
        :rtype: TempMultimedia
        """
        return self._temp_multimedia

    @temp_multimedia.setter
    def temp_multimedia(self, temp_multimedia):
        """
        Sets the temp_multimedia of this TempMultimediaResponse.


        :param temp_multimedia: The temp_multimedia of this TempMultimediaResponse.
        :type: TempMultimedia
        """

        self._temp_multimedia = temp_multimedia

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
