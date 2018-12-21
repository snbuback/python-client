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

from wavefront_api_client.models.metric_status import MetricStatus  # noqa: F401,E501


class IntegrationStatus(object):
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
        'content_status': 'str',
        'install_status': 'str',
        'metric_statuses': 'dict(str, MetricStatus)',
        'alert_statuses': 'dict(str, str)'
    }

    attribute_map = {
        'content_status': 'contentStatus',
        'install_status': 'installStatus',
        'metric_statuses': 'metricStatuses',
        'alert_statuses': 'alertStatuses'
    }

    def __init__(self, content_status=None, install_status=None, metric_statuses=None, alert_statuses=None):  # noqa: E501
        """IntegrationStatus - a model defined in Swagger"""  # noqa: E501

        self._content_status = None
        self._install_status = None
        self._metric_statuses = None
        self._alert_statuses = None
        self.discriminator = None

        self.content_status = content_status
        self.install_status = install_status
        self.metric_statuses = metric_statuses
        self.alert_statuses = alert_statuses

    @property
    def content_status(self):
        """Gets the content_status of this IntegrationStatus.  # noqa: E501

        Status of integration content, e.g. dashboards  # noqa: E501

        :return: The content_status of this IntegrationStatus.  # noqa: E501
        :rtype: str
        """
        return self._content_status

    @content_status.setter
    def content_status(self, content_status):
        """Sets the content_status of this IntegrationStatus.

        Status of integration content, e.g. dashboards  # noqa: E501

        :param content_status: The content_status of this IntegrationStatus.  # noqa: E501
        :type: str
        """
        if content_status is None:
            raise ValueError("Invalid value for `content_status`, must not be `None`")  # noqa: E501
        allowed_values = ["INVALID", "NOT_LOADED", "HIDDEN", "VISIBLE"]  # noqa: E501
        if content_status not in allowed_values:
            raise ValueError(
                "Invalid value for `content_status` ({0}), must be one of {1}"  # noqa: E501
                .format(content_status, allowed_values)
            )

        self._content_status = content_status

    @property
    def install_status(self):
        """Gets the install_status of this IntegrationStatus.  # noqa: E501

        Whether the customer or an automated process has installed the dashboards for this integration  # noqa: E501

        :return: The install_status of this IntegrationStatus.  # noqa: E501
        :rtype: str
        """
        return self._install_status

    @install_status.setter
    def install_status(self, install_status):
        """Sets the install_status of this IntegrationStatus.

        Whether the customer or an automated process has installed the dashboards for this integration  # noqa: E501

        :param install_status: The install_status of this IntegrationStatus.  # noqa: E501
        :type: str
        """
        if install_status is None:
            raise ValueError("Invalid value for `install_status`, must not be `None`")  # noqa: E501
        allowed_values = ["UNDECIDED", "UNINSTALLED", "INSTALLED"]  # noqa: E501
        if install_status not in allowed_values:
            raise ValueError(
                "Invalid value for `install_status` ({0}), must be one of {1}"  # noqa: E501
                .format(install_status, allowed_values)
            )

        self._install_status = install_status

    @property
    def metric_statuses(self):
        """Gets the metric_statuses of this IntegrationStatus.  # noqa: E501

        A Map from names of the required metrics to an object representing their reporting status.  The reporting status object has 3 boolean fields denoting whether the metric has been received during the corresponding time period: `ever`, `recentExceptNow`, and `now`.  `now` is on the order of a few hours, and `recentExceptNow` is on the order of the past few days, excluding the period considered to be `now`.  # noqa: E501

        :return: The metric_statuses of this IntegrationStatus.  # noqa: E501
        :rtype: dict(str, MetricStatus)
        """
        return self._metric_statuses

    @metric_statuses.setter
    def metric_statuses(self, metric_statuses):
        """Sets the metric_statuses of this IntegrationStatus.

        A Map from names of the required metrics to an object representing their reporting status.  The reporting status object has 3 boolean fields denoting whether the metric has been received during the corresponding time period: `ever`, `recentExceptNow`, and `now`.  `now` is on the order of a few hours, and `recentExceptNow` is on the order of the past few days, excluding the period considered to be `now`.  # noqa: E501

        :param metric_statuses: The metric_statuses of this IntegrationStatus.  # noqa: E501
        :type: dict(str, MetricStatus)
        """
        if metric_statuses is None:
            raise ValueError("Invalid value for `metric_statuses`, must not be `None`")  # noqa: E501

        self._metric_statuses = metric_statuses

    @property
    def alert_statuses(self):
        """Gets the alert_statuses of this IntegrationStatus.  # noqa: E501

        A Map from the ids of the alerts contained in this integration to their install status.  The install status can take on one of three values, `VISIBLE`, `HIDDEN`, and `NOT_LOADED`  # noqa: E501

        :return: The alert_statuses of this IntegrationStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._alert_statuses

    @alert_statuses.setter
    def alert_statuses(self, alert_statuses):
        """Sets the alert_statuses of this IntegrationStatus.

        A Map from the ids of the alerts contained in this integration to their install status.  The install status can take on one of three values, `VISIBLE`, `HIDDEN`, and `NOT_LOADED`  # noqa: E501

        :param alert_statuses: The alert_statuses of this IntegrationStatus.  # noqa: E501
        :type: dict(str, str)
        """
        if alert_statuses is None:
            raise ValueError("Invalid value for `alert_statuses`, must not be `None`")  # noqa: E501
        allowed_values = ["VISIBLE", "HIDDEN", "NOT_LOADED"]  # noqa: E501
        if not set(alert_statuses.keys()).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid keys in `alert_statuses` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alert_statuses.keys()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alert_statuses = alert_statuses

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
        if issubclass(IntegrationStatus, dict):
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
        if not isinstance(other, IntegrationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
