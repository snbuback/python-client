# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserToCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'email_address': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'groups': 'groups'
    }

    def __init__(self, email_address=None, groups=None):
        """
        UserToCreate - a model defined in Swagger
        """

        self._email_address = None
        self._groups = None
        self.discriminator = None

        self.email_address = email_address
        self.groups = groups

    @property
    def email_address(self):
        """
        Gets the email_address of this UserToCreate.
        The (unique) identifier of the user to create.  Must be a valid email address

        :return: The email_address of this UserToCreate.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this UserToCreate.
        The (unique) identifier of the user to create.  Must be a valid email address

        :param email_address: The email_address of this UserToCreate.
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")

        self._email_address = email_address

    @property
    def groups(self):
        """
        Gets the groups of this UserToCreate.
        List of permission groups to grant to this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission.  Possible values are browse, agent_management, alerts_management, dashboard_management, embedded_charts, events_management, external_links_management, host_tag_management, metrics_management, user_management

        :return: The groups of this UserToCreate.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this UserToCreate.
        List of permission groups to grant to this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission.  Possible values are browse, agent_management, alerts_management, dashboard_management, embedded_charts, events_management, external_links_management, host_tag_management, metrics_management, user_management

        :param groups: The groups of this UserToCreate.
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")

        self._groups = groups

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
        if not isinstance(other, UserToCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
