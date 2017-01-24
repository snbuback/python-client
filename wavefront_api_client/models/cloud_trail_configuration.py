# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class CloudTrailConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudTrailConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'base_credentials': 'AWSBaseCredentials',
            'bucket_name': 'str',
            'prefix': 'str'
        }

        self.attribute_map = {
            'base_credentials': 'baseCredentials',
            'bucket_name': 'bucketName',
            'prefix': 'prefix'
        }

        self._base_credentials = None
        self._bucket_name = None
        self._prefix = None

    @property
    def base_credentials(self):
        """
        Gets the base_credentials of this CloudTrailConfiguration.


        :return: The base_credentials of this CloudTrailConfiguration.
        :rtype: AWSBaseCredentials
        """
        return self._base_credentials

    @base_credentials.setter
    def base_credentials(self, base_credentials):
        """
        Sets the base_credentials of this CloudTrailConfiguration.


        :param base_credentials: The base_credentials of this CloudTrailConfiguration.
        :type: AWSBaseCredentials
        """
        self._base_credentials = base_credentials

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this CloudTrailConfiguration.
        Name of the S3 bucket where CloudTrail logs are stored

        :return: The bucket_name of this CloudTrailConfiguration.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CloudTrailConfiguration.
        Name of the S3 bucket where CloudTrail logs are stored

        :param bucket_name: The bucket_name of this CloudTrailConfiguration.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def prefix(self):
        """
        Gets the prefix of this CloudTrailConfiguration.
        The common prefix, if any, appended to all CloudTrail log files

        :return: The prefix of this CloudTrailConfiguration.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CloudTrailConfiguration.
        The common prefix, if any, appended to all CloudTrail log files

        :param prefix: The prefix of this CloudTrailConfiguration.
        :type: str
        """
        self._prefix = prefix

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

