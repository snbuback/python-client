# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserModel(object):
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
        'identifier': 'str',
        'customer': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'customer': 'customer',
        'groups': 'groups'
    }

    def __init__(self, identifier=None, customer=None, groups=None):  # noqa: E501
        """UserModel - a model defined in Swagger"""  # noqa: E501

        self._identifier = None
        self._customer = None
        self._groups = None
        self.discriminator = None

        self.identifier = identifier
        self.customer = customer
        self.groups = groups

    @property
    def identifier(self):
        """Gets the identifier of this UserModel.  # noqa: E501

        The unique identifier of this user, which must be their valid email address  # noqa: E501

        :return: The identifier of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserModel.

        The unique identifier of this user, which must be their valid email address  # noqa: E501

        :param identifier: The identifier of this UserModel.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def customer(self):
        """Gets the customer of this UserModel.  # noqa: E501

        The id of the customer to which this user belongs  # noqa: E501

        :return: The customer of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UserModel.

        The id of the customer to which this user belongs  # noqa: E501

        :param customer: The customer of this UserModel.  # noqa: E501
        :type: str
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def groups(self):
        """Gets the groups of this UserModel.  # noqa: E501

        The permissions granted to this user  # noqa: E501

        :return: The groups of this UserModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserModel.

        The permissions granted to this user  # noqa: E501

        :param groups: The groups of this UserModel.  # noqa: E501
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
