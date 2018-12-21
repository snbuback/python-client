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

from wavefront_api_client.models.user_group import UserGroup  # noqa: F401,E501


class CustomerPreferences(object):
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
        'default_user_groups': 'list[UserGroup]',
        'id': 'str',
        'customer_id': 'str',
        'deleted': 'bool',
        'creator_id': 'str',
        'updater_id': 'str',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'invite_permissions': 'list[str]',
        'show_querybuilder_by_default': 'bool',
        'hide_ts_when_querybuilder_shown': 'bool',
        'blacklisted_emails': 'dict(str, int)',
        'hidden_metric_prefixes': 'dict(str, int)',
        'landing_dashboard_slug': 'str',
        'show_onboarding': 'bool',
        'grant_modify_access_to_everyone': 'bool'
    }

    attribute_map = {
        'default_user_groups': 'defaultUserGroups',
        'id': 'id',
        'customer_id': 'customerId',
        'deleted': 'deleted',
        'creator_id': 'creatorId',
        'updater_id': 'updaterId',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'invite_permissions': 'invitePermissions',
        'show_querybuilder_by_default': 'showQuerybuilderByDefault',
        'hide_ts_when_querybuilder_shown': 'hideTSWhenQuerybuilderShown',
        'blacklisted_emails': 'blacklistedEmails',
        'hidden_metric_prefixes': 'hiddenMetricPrefixes',
        'landing_dashboard_slug': 'landingDashboardSlug',
        'show_onboarding': 'showOnboarding',
        'grant_modify_access_to_everyone': 'grantModifyAccessToEveryone'
    }

    def __init__(self, default_user_groups=None, id=None, customer_id=None, deleted=None, creator_id=None, updater_id=None, created_epoch_millis=None, updated_epoch_millis=None, invite_permissions=None, show_querybuilder_by_default=None, hide_ts_when_querybuilder_shown=None, blacklisted_emails=None, hidden_metric_prefixes=None, landing_dashboard_slug=None, show_onboarding=None, grant_modify_access_to_everyone=None):  # noqa: E501
        """CustomerPreferences - a model defined in Swagger"""  # noqa: E501

        self._default_user_groups = None
        self._id = None
        self._customer_id = None
        self._deleted = None
        self._creator_id = None
        self._updater_id = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._invite_permissions = None
        self._show_querybuilder_by_default = None
        self._hide_ts_when_querybuilder_shown = None
        self._blacklisted_emails = None
        self._hidden_metric_prefixes = None
        self._landing_dashboard_slug = None
        self._show_onboarding = None
        self._grant_modify_access_to_everyone = None
        self.discriminator = None

        if default_user_groups is not None:
            self.default_user_groups = default_user_groups
        if id is not None:
            self.id = id
        self.customer_id = customer_id
        if deleted is not None:
            self.deleted = deleted
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if invite_permissions is not None:
            self.invite_permissions = invite_permissions
        self.show_querybuilder_by_default = show_querybuilder_by_default
        self.hide_ts_when_querybuilder_shown = hide_ts_when_querybuilder_shown
        if blacklisted_emails is not None:
            self.blacklisted_emails = blacklisted_emails
        if hidden_metric_prefixes is not None:
            self.hidden_metric_prefixes = hidden_metric_prefixes
        if landing_dashboard_slug is not None:
            self.landing_dashboard_slug = landing_dashboard_slug
        self.show_onboarding = show_onboarding
        self.grant_modify_access_to_everyone = grant_modify_access_to_everyone

    @property
    def default_user_groups(self):
        """Gets the default_user_groups of this CustomerPreferences.  # noqa: E501

        List of default user groups of the customer  # noqa: E501

        :return: The default_user_groups of this CustomerPreferences.  # noqa: E501
        :rtype: list[UserGroup]
        """
        return self._default_user_groups

    @default_user_groups.setter
    def default_user_groups(self, default_user_groups):
        """Sets the default_user_groups of this CustomerPreferences.

        List of default user groups of the customer  # noqa: E501

        :param default_user_groups: The default_user_groups of this CustomerPreferences.  # noqa: E501
        :type: list[UserGroup]
        """

        self._default_user_groups = default_user_groups

    @property
    def id(self):
        """Gets the id of this CustomerPreferences.  # noqa: E501


        :return: The id of this CustomerPreferences.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerPreferences.


        :param id: The id of this CustomerPreferences.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerPreferences.  # noqa: E501

        The id of the customer preferences are attached to  # noqa: E501

        :return: The customer_id of this CustomerPreferences.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerPreferences.

        The id of the customer preferences are attached to  # noqa: E501

        :param customer_id: The customer_id of this CustomerPreferences.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def deleted(self):
        """Gets the deleted of this CustomerPreferences.  # noqa: E501


        :return: The deleted of this CustomerPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CustomerPreferences.


        :param deleted: The deleted of this CustomerPreferences.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def creator_id(self):
        """Gets the creator_id of this CustomerPreferences.  # noqa: E501


        :return: The creator_id of this CustomerPreferences.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this CustomerPreferences.


        :param creator_id: The creator_id of this CustomerPreferences.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def updater_id(self):
        """Gets the updater_id of this CustomerPreferences.  # noqa: E501


        :return: The updater_id of this CustomerPreferences.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this CustomerPreferences.


        :param updater_id: The updater_id of this CustomerPreferences.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this CustomerPreferences.  # noqa: E501


        :return: The created_epoch_millis of this CustomerPreferences.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this CustomerPreferences.


        :param created_epoch_millis: The created_epoch_millis of this CustomerPreferences.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this CustomerPreferences.  # noqa: E501


        :return: The updated_epoch_millis of this CustomerPreferences.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this CustomerPreferences.


        :param updated_epoch_millis: The updated_epoch_millis of this CustomerPreferences.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def invite_permissions(self):
        """Gets the invite_permissions of this CustomerPreferences.  # noqa: E501

        List of permissions that are assigned to newly invited users  # noqa: E501

        :return: The invite_permissions of this CustomerPreferences.  # noqa: E501
        :rtype: list[str]
        """
        return self._invite_permissions

    @invite_permissions.setter
    def invite_permissions(self, invite_permissions):
        """Sets the invite_permissions of this CustomerPreferences.

        List of permissions that are assigned to newly invited users  # noqa: E501

        :param invite_permissions: The invite_permissions of this CustomerPreferences.  # noqa: E501
        :type: list[str]
        """

        self._invite_permissions = invite_permissions

    @property
    def show_querybuilder_by_default(self):
        """Gets the show_querybuilder_by_default of this CustomerPreferences.  # noqa: E501

        Whether the Querybuilder is shown by default  # noqa: E501

        :return: The show_querybuilder_by_default of this CustomerPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._show_querybuilder_by_default

    @show_querybuilder_by_default.setter
    def show_querybuilder_by_default(self, show_querybuilder_by_default):
        """Sets the show_querybuilder_by_default of this CustomerPreferences.

        Whether the Querybuilder is shown by default  # noqa: E501

        :param show_querybuilder_by_default: The show_querybuilder_by_default of this CustomerPreferences.  # noqa: E501
        :type: bool
        """
        if show_querybuilder_by_default is None:
            raise ValueError("Invalid value for `show_querybuilder_by_default`, must not be `None`")  # noqa: E501

        self._show_querybuilder_by_default = show_querybuilder_by_default

    @property
    def hide_ts_when_querybuilder_shown(self):
        """Gets the hide_ts_when_querybuilder_shown of this CustomerPreferences.  # noqa: E501

        Whether to hide TS source input when Querybuilder is shown  # noqa: E501

        :return: The hide_ts_when_querybuilder_shown of this CustomerPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._hide_ts_when_querybuilder_shown

    @hide_ts_when_querybuilder_shown.setter
    def hide_ts_when_querybuilder_shown(self, hide_ts_when_querybuilder_shown):
        """Sets the hide_ts_when_querybuilder_shown of this CustomerPreferences.

        Whether to hide TS source input when Querybuilder is shown  # noqa: E501

        :param hide_ts_when_querybuilder_shown: The hide_ts_when_querybuilder_shown of this CustomerPreferences.  # noqa: E501
        :type: bool
        """
        if hide_ts_when_querybuilder_shown is None:
            raise ValueError("Invalid value for `hide_ts_when_querybuilder_shown`, must not be `None`")  # noqa: E501

        self._hide_ts_when_querybuilder_shown = hide_ts_when_querybuilder_shown

    @property
    def blacklisted_emails(self):
        """Gets the blacklisted_emails of this CustomerPreferences.  # noqa: E501

        List of blacklisted emails of the customer  # noqa: E501

        :return: The blacklisted_emails of this CustomerPreferences.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._blacklisted_emails

    @blacklisted_emails.setter
    def blacklisted_emails(self, blacklisted_emails):
        """Sets the blacklisted_emails of this CustomerPreferences.

        List of blacklisted emails of the customer  # noqa: E501

        :param blacklisted_emails: The blacklisted_emails of this CustomerPreferences.  # noqa: E501
        :type: dict(str, int)
        """

        self._blacklisted_emails = blacklisted_emails

    @property
    def hidden_metric_prefixes(self):
        """Gets the hidden_metric_prefixes of this CustomerPreferences.  # noqa: E501

        Metric prefixes which should be hidden from user  # noqa: E501

        :return: The hidden_metric_prefixes of this CustomerPreferences.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._hidden_metric_prefixes

    @hidden_metric_prefixes.setter
    def hidden_metric_prefixes(self, hidden_metric_prefixes):
        """Sets the hidden_metric_prefixes of this CustomerPreferences.

        Metric prefixes which should be hidden from user  # noqa: E501

        :param hidden_metric_prefixes: The hidden_metric_prefixes of this CustomerPreferences.  # noqa: E501
        :type: dict(str, int)
        """

        self._hidden_metric_prefixes = hidden_metric_prefixes

    @property
    def landing_dashboard_slug(self):
        """Gets the landing_dashboard_slug of this CustomerPreferences.  # noqa: E501

        Dashboard where user will be redirected from landing page  # noqa: E501

        :return: The landing_dashboard_slug of this CustomerPreferences.  # noqa: E501
        :rtype: str
        """
        return self._landing_dashboard_slug

    @landing_dashboard_slug.setter
    def landing_dashboard_slug(self, landing_dashboard_slug):
        """Sets the landing_dashboard_slug of this CustomerPreferences.

        Dashboard where user will be redirected from landing page  # noqa: E501

        :param landing_dashboard_slug: The landing_dashboard_slug of this CustomerPreferences.  # noqa: E501
        :type: str
        """

        self._landing_dashboard_slug = landing_dashboard_slug

    @property
    def show_onboarding(self):
        """Gets the show_onboarding of this CustomerPreferences.  # noqa: E501

        Whether to show onboarding for any new user without an override  # noqa: E501

        :return: The show_onboarding of this CustomerPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._show_onboarding

    @show_onboarding.setter
    def show_onboarding(self, show_onboarding):
        """Sets the show_onboarding of this CustomerPreferences.

        Whether to show onboarding for any new user without an override  # noqa: E501

        :param show_onboarding: The show_onboarding of this CustomerPreferences.  # noqa: E501
        :type: bool
        """
        if show_onboarding is None:
            raise ValueError("Invalid value for `show_onboarding`, must not be `None`")  # noqa: E501

        self._show_onboarding = show_onboarding

    @property
    def grant_modify_access_to_everyone(self):
        """Gets the grant_modify_access_to_everyone of this CustomerPreferences.  # noqa: E501

        Whether modify access of new entites is granted to Everyone or to the Creator  # noqa: E501

        :return: The grant_modify_access_to_everyone of this CustomerPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._grant_modify_access_to_everyone

    @grant_modify_access_to_everyone.setter
    def grant_modify_access_to_everyone(self, grant_modify_access_to_everyone):
        """Sets the grant_modify_access_to_everyone of this CustomerPreferences.

        Whether modify access of new entites is granted to Everyone or to the Creator  # noqa: E501

        :param grant_modify_access_to_everyone: The grant_modify_access_to_everyone of this CustomerPreferences.  # noqa: E501
        :type: bool
        """
        if grant_modify_access_to_everyone is None:
            raise ValueError("Invalid value for `grant_modify_access_to_everyone`, must not be `None`")  # noqa: E501

        self._grant_modify_access_to_everyone = grant_modify_access_to_everyone

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
        if issubclass(CustomerPreferences, dict):
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
        if not isinstance(other, CustomerPreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
