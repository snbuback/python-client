# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AzureBaseCredentials(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tenant': 'str',
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'tenant': 'tenant',
        'client_id': 'clientId',
        'client_secret': 'clientSecret'
    }

    def __init__(self, tenant=None, client_id=None, client_secret=None):  # noqa: E501
        """AzureBaseCredentials - a model defined in Swagger"""  # noqa: E501

        self._tenant = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None

        self.tenant = tenant
        self.client_id = client_id
        self.client_secret = client_secret

    @property
    def tenant(self):
        """Gets the tenant of this AzureBaseCredentials.  # noqa: E501

        Tenant Id for an Azure service account within your project.  # noqa: E501

        :return: The tenant of this AzureBaseCredentials.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this AzureBaseCredentials.

        Tenant Id for an Azure service account within your project.  # noqa: E501

        :param tenant: The tenant of this AzureBaseCredentials.  # noqa: E501
        :type: str
        """
        if tenant is None:
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def client_id(self):
        """Gets the client_id of this AzureBaseCredentials.  # noqa: E501

        Client Id for an Azure service account within your project.  # noqa: E501

        :return: The client_id of this AzureBaseCredentials.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AzureBaseCredentials.

        Client Id for an Azure service account within your project.  # noqa: E501

        :param client_id: The client_id of this AzureBaseCredentials.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this AzureBaseCredentials.  # noqa: E501

        Client Secret for an Azure service account within your project. Use 'saved_secret' to retain the client secret when updating.  # noqa: E501

        :return: The client_secret of this AzureBaseCredentials.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this AzureBaseCredentials.

        Client Secret for an Azure service account within your project. Use 'saved_secret' to retain the client secret when updating.  # noqa: E501

        :param client_secret: The client_secret of this AzureBaseCredentials.  # noqa: E501
        :type: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AzureBaseCredentials, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AzureBaseCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
