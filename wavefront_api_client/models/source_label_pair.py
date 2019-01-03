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


class SourceLabelPair(object):
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
        'label': 'str',
        'severity': 'str',
        'host': 'str',
        'tags': 'dict(str, str)',
        'observed': 'int',
        'firing': 'int'
    }

    attribute_map = {
        'label': 'label',
        'severity': 'severity',
        'host': 'host',
        'tags': 'tags',
        'observed': 'observed',
        'firing': 'firing'
    }

    def __init__(self, label=None, severity=None, host=None, tags=None, observed=None, firing=None):  # noqa: E501
        """SourceLabelPair - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._severity = None
        self._host = None
        self._tags = None
        self._observed = None
        self._firing = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if severity is not None:
            self.severity = severity
        if host is not None:
            self.host = host
        if tags is not None:
            self.tags = tags
        if observed is not None:
            self.observed = observed
        if firing is not None:
            self.firing = firing

    @property
    def label(self):
        """Gets the label of this SourceLabelPair.  # noqa: E501


        :return: The label of this SourceLabelPair.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SourceLabelPair.


        :param label: The label of this SourceLabelPair.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def severity(self):
        """Gets the severity of this SourceLabelPair.  # noqa: E501


        :return: The severity of this SourceLabelPair.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this SourceLabelPair.


        :param severity: The severity of this SourceLabelPair.  # noqa: E501
        :type: str
        """
        allowed_values = ["INFO", "SMOKE", "WARN", "SEVERE"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def host(self):
        """Gets the host of this SourceLabelPair.  # noqa: E501

        Source (or host).  \"Source\" and \"host\" are synonyms in current versions of wavefront, but the host terminology is deprecated  # noqa: E501

        :return: The host of this SourceLabelPair.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SourceLabelPair.

        Source (or host).  \"Source\" and \"host\" are synonyms in current versions of wavefront, but the host terminology is deprecated  # noqa: E501

        :param host: The host of this SourceLabelPair.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def tags(self):
        """Gets the tags of this SourceLabelPair.  # noqa: E501


        :return: The tags of this SourceLabelPair.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SourceLabelPair.


        :param tags: The tags of this SourceLabelPair.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def observed(self):
        """Gets the observed of this SourceLabelPair.  # noqa: E501


        :return: The observed of this SourceLabelPair.  # noqa: E501
        :rtype: int
        """
        return self._observed

    @observed.setter
    def observed(self, observed):
        """Sets the observed of this SourceLabelPair.


        :param observed: The observed of this SourceLabelPair.  # noqa: E501
        :type: int
        """

        self._observed = observed

    @property
    def firing(self):
        """Gets the firing of this SourceLabelPair.  # noqa: E501


        :return: The firing of this SourceLabelPair.  # noqa: E501
        :rtype: int
        """
        return self._firing

    @firing.setter
    def firing(self, firing):
        """Sets the firing of this SourceLabelPair.


        :param firing: The firing of this SourceLabelPair.  # noqa: E501
        :type: int
        """

        self._firing = firing

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
        if issubclass(SourceLabelPair, dict):
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
        if not isinstance(other, SourceLabelPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
