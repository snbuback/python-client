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

from wavefront_api_client.models.user_group_properties_dto import UserGroupPropertiesDTO  # noqa: F401,E501


class UserGroup(object):
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
        'id': 'str',
        'name': 'str',
        'permissions': 'list[str]',
        'customer': 'str',
        'users': 'list[str]',
        'user_count': 'int',
        'properties': 'UserGroupPropertiesDTO'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'permissions': 'permissions',
        'customer': 'customer',
        'users': 'users',
        'user_count': 'userCount',
        'properties': 'properties'
    }

    def __init__(self, id=None, name=None, permissions=None, customer=None, users=None, user_count=None, properties=None):  # noqa: E501
        """UserGroup - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._permissions = None
        self._customer = None
        self._users = None
        self._user_count = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.permissions = permissions
        if customer is not None:
            self.customer = customer
        if users is not None:
            self.users = users
        if user_count is not None:
            self.user_count = user_count
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this UserGroup.  # noqa: E501

        Unique ID for the user group  # noqa: E501

        :return: The id of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGroup.

        Unique ID for the user group  # noqa: E501

        :param id: The id of this UserGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserGroup.  # noqa: E501

        Name of the user group  # noqa: E501

        :return: The name of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroup.

        Name of the user group  # noqa: E501

        :param name: The name of this UserGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this UserGroup.  # noqa: E501

        Permission assigned to the user group  # noqa: E501

        :return: The permissions of this UserGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserGroup.

        Permission assigned to the user group  # noqa: E501

        :param permissions: The permissions of this UserGroup.  # noqa: E501
        :type: list[str]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def customer(self):
        """Gets the customer of this UserGroup.  # noqa: E501

        ID of the customer to which the user group belongs  # noqa: E501

        :return: The customer of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UserGroup.

        ID of the customer to which the user group belongs  # noqa: E501

        :param customer: The customer of this UserGroup.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def users(self):
        """Gets the users of this UserGroup.  # noqa: E501

        List of Users that are members of the user group. Maybe incomplete.  # noqa: E501

        :return: The users of this UserGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UserGroup.

        List of Users that are members of the user group. Maybe incomplete.  # noqa: E501

        :param users: The users of this UserGroup.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def user_count(self):
        """Gets the user_count of this UserGroup.  # noqa: E501

        Total number of users that are members of the user group  # noqa: E501

        :return: The user_count of this UserGroup.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this UserGroup.

        Total number of users that are members of the user group  # noqa: E501

        :param user_count: The user_count of this UserGroup.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def properties(self):
        """Gets the properties of this UserGroup.  # noqa: E501

        The properties of the user group(name editable, users editable, etc.)  # noqa: E501

        :return: The properties of this UserGroup.  # noqa: E501
        :rtype: UserGroupPropertiesDTO
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UserGroup.

        The properties of the user group(name editable, users editable, etc.)  # noqa: E501

        :param properties: The properties of this UserGroup.  # noqa: E501
        :type: UserGroupPropertiesDTO
        """

        self._properties = properties

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
        if issubclass(UserGroup, dict):
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
        if not isinstance(other, UserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
