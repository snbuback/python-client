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


class BusinessActionGroupBasicDTO(object):
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
        'group_name': 'str',
        'display_name': 'str',
        'description': 'str',
        'required_default': 'bool'
    }

    attribute_map = {
        'group_name': 'groupName',
        'display_name': 'displayName',
        'description': 'description',
        'required_default': 'requiredDefault'
    }

    def __init__(self, group_name=None, display_name=None, description=None, required_default=None):  # noqa: E501
        """BusinessActionGroupBasicDTO - a model defined in Swagger"""  # noqa: E501

        self._group_name = None
        self._display_name = None
        self._description = None
        self._required_default = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if required_default is not None:
            self.required_default = required_default

    @property
    def group_name(self):
        """Gets the group_name of this BusinessActionGroupBasicDTO.  # noqa: E501


        :return: The group_name of this BusinessActionGroupBasicDTO.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this BusinessActionGroupBasicDTO.


        :param group_name: The group_name of this BusinessActionGroupBasicDTO.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def display_name(self):
        """Gets the display_name of this BusinessActionGroupBasicDTO.  # noqa: E501


        :return: The display_name of this BusinessActionGroupBasicDTO.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BusinessActionGroupBasicDTO.


        :param display_name: The display_name of this BusinessActionGroupBasicDTO.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this BusinessActionGroupBasicDTO.  # noqa: E501


        :return: The description of this BusinessActionGroupBasicDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BusinessActionGroupBasicDTO.


        :param description: The description of this BusinessActionGroupBasicDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required_default(self):
        """Gets the required_default of this BusinessActionGroupBasicDTO.  # noqa: E501


        :return: The required_default of this BusinessActionGroupBasicDTO.  # noqa: E501
        :rtype: bool
        """
        return self._required_default

    @required_default.setter
    def required_default(self, required_default):
        """Sets the required_default of this BusinessActionGroupBasicDTO.


        :param required_default: The required_default of this BusinessActionGroupBasicDTO.  # noqa: E501
        :type: bool
        """

        self._required_default = required_default

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
        if issubclass(BusinessActionGroupBasicDTO, dict):
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
        if not isinstance(other, BusinessActionGroupBasicDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
