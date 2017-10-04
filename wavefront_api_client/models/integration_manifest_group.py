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


class IntegrationManifestGroup(object):
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
        'title': 'str',
        'integrations': 'list[str]',
        'integration_objs': 'list[Integration]',
        'subtitle': 'str'
    }

    attribute_map = {
        'title': 'title',
        'integrations': 'integrations',
        'integration_objs': 'integrationObjs',
        'subtitle': 'subtitle'
    }

    def __init__(self, title=None, integrations=None, integration_objs=None, subtitle=None):
        """
        IntegrationManifestGroup - a model defined in Swagger
        """

        self._title = None
        self._integrations = None
        self._integration_objs = None
        self._subtitle = None
        self.discriminator = None

        self.title = title
        self.integrations = integrations
        if integration_objs is not None:
          self.integration_objs = integration_objs
        self.subtitle = subtitle

    @property
    def title(self):
        """
        Gets the title of this IntegrationManifestGroup.
        Title of this integration group

        :return: The title of this IntegrationManifestGroup.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this IntegrationManifestGroup.
        Title of this integration group

        :param title: The title of this IntegrationManifestGroup.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def integrations(self):
        """
        Gets the integrations of this IntegrationManifestGroup.
        A list of paths to JSON definitions for integrations in this group

        :return: The integrations of this IntegrationManifestGroup.
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """
        Sets the integrations of this IntegrationManifestGroup.
        A list of paths to JSON definitions for integrations in this group

        :param integrations: The integrations of this IntegrationManifestGroup.
        :type: list[str]
        """
        if integrations is None:
            raise ValueError("Invalid value for `integrations`, must not be `None`")

        self._integrations = integrations

    @property
    def integration_objs(self):
        """
        Gets the integration_objs of this IntegrationManifestGroup.
        Materialized JSONs for integrations belonging to this group, as referenced by `integrations`

        :return: The integration_objs of this IntegrationManifestGroup.
        :rtype: list[Integration]
        """
        return self._integration_objs

    @integration_objs.setter
    def integration_objs(self, integration_objs):
        """
        Sets the integration_objs of this IntegrationManifestGroup.
        Materialized JSONs for integrations belonging to this group, as referenced by `integrations`

        :param integration_objs: The integration_objs of this IntegrationManifestGroup.
        :type: list[Integration]
        """

        self._integration_objs = integration_objs

    @property
    def subtitle(self):
        """
        Gets the subtitle of this IntegrationManifestGroup.
        Subtitle of this integration group

        :return: The subtitle of this IntegrationManifestGroup.
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """
        Sets the subtitle of this IntegrationManifestGroup.
        Subtitle of this integration group

        :param subtitle: The subtitle of this IntegrationManifestGroup.
        :type: str
        """
        if subtitle is None:
            raise ValueError("Invalid value for `subtitle`, must not be `None`")

        self._subtitle = subtitle

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
        if not isinstance(other, IntegrationManifestGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
