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


class MaintenanceWindow(object):
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
        'reason': 'str',
        'id': 'str',
        'customer_id': 'str',
        'relevant_customer_tags': 'list[str]',
        'title': 'str',
        'start_time_in_seconds': 'int',
        'end_time_in_seconds': 'int',
        'relevant_host_tags': 'list[str]',
        'relevant_host_names': 'list[str]',
        'creator_id': 'str',
        'updater_id': 'str',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'relevant_host_tags_anded': 'bool',
        'host_tag_group_host_names_group_anded': 'bool',
        'event_name': 'str',
        'running_state': 'str',
        'sort_attr': 'int'
    }

    attribute_map = {
        'reason': 'reason',
        'id': 'id',
        'customer_id': 'customerId',
        'relevant_customer_tags': 'relevantCustomerTags',
        'title': 'title',
        'start_time_in_seconds': 'startTimeInSeconds',
        'end_time_in_seconds': 'endTimeInSeconds',
        'relevant_host_tags': 'relevantHostTags',
        'relevant_host_names': 'relevantHostNames',
        'creator_id': 'creatorId',
        'updater_id': 'updaterId',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'relevant_host_tags_anded': 'relevantHostTagsAnded',
        'host_tag_group_host_names_group_anded': 'hostTagGroupHostNamesGroupAnded',
        'event_name': 'eventName',
        'running_state': 'runningState',
        'sort_attr': 'sortAttr'
    }

    def __init__(self, reason=None, id=None, customer_id=None, relevant_customer_tags=None, title=None, start_time_in_seconds=None, end_time_in_seconds=None, relevant_host_tags=None, relevant_host_names=None, creator_id=None, updater_id=None, created_epoch_millis=None, updated_epoch_millis=None, relevant_host_tags_anded=None, host_tag_group_host_names_group_anded=None, event_name=None, running_state=None, sort_attr=None):  # noqa: E501
        """MaintenanceWindow - a model defined in Swagger"""  # noqa: E501

        self._reason = None
        self._id = None
        self._customer_id = None
        self._relevant_customer_tags = None
        self._title = None
        self._start_time_in_seconds = None
        self._end_time_in_seconds = None
        self._relevant_host_tags = None
        self._relevant_host_names = None
        self._creator_id = None
        self._updater_id = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._relevant_host_tags_anded = None
        self._host_tag_group_host_names_group_anded = None
        self._event_name = None
        self._running_state = None
        self._sort_attr = None
        self.discriminator = None

        self.reason = reason
        if id is not None:
            self.id = id
        if customer_id is not None:
            self.customer_id = customer_id
        self.relevant_customer_tags = relevant_customer_tags
        self.title = title
        self.start_time_in_seconds = start_time_in_seconds
        self.end_time_in_seconds = end_time_in_seconds
        if relevant_host_tags is not None:
            self.relevant_host_tags = relevant_host_tags
        if relevant_host_names is not None:
            self.relevant_host_names = relevant_host_names
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if relevant_host_tags_anded is not None:
            self.relevant_host_tags_anded = relevant_host_tags_anded
        if host_tag_group_host_names_group_anded is not None:
            self.host_tag_group_host_names_group_anded = host_tag_group_host_names_group_anded
        if event_name is not None:
            self.event_name = event_name
        if running_state is not None:
            self.running_state = running_state
        if sort_attr is not None:
            self.sort_attr = sort_attr

    @property
    def reason(self):
        """Gets the reason of this MaintenanceWindow.  # noqa: E501

        The purpose of this maintenance window  # noqa: E501

        :return: The reason of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MaintenanceWindow.

        The purpose of this maintenance window  # noqa: E501

        :param reason: The reason of this MaintenanceWindow.  # noqa: E501
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def id(self):
        """Gets the id of this MaintenanceWindow.  # noqa: E501


        :return: The id of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MaintenanceWindow.


        :param id: The id of this MaintenanceWindow.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer_id(self):
        """Gets the customer_id of this MaintenanceWindow.  # noqa: E501


        :return: The customer_id of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this MaintenanceWindow.


        :param customer_id: The customer_id of this MaintenanceWindow.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def relevant_customer_tags(self):
        """Gets the relevant_customer_tags of this MaintenanceWindow.  # noqa: E501

        List of alert tags whose matching alerts will be put into maintenance because of this maintenance window  # noqa: E501

        :return: The relevant_customer_tags of this MaintenanceWindow.  # noqa: E501
        :rtype: list[str]
        """
        return self._relevant_customer_tags

    @relevant_customer_tags.setter
    def relevant_customer_tags(self, relevant_customer_tags):
        """Sets the relevant_customer_tags of this MaintenanceWindow.

        List of alert tags whose matching alerts will be put into maintenance because of this maintenance window  # noqa: E501

        :param relevant_customer_tags: The relevant_customer_tags of this MaintenanceWindow.  # noqa: E501
        :type: list[str]
        """
        if relevant_customer_tags is None:
            raise ValueError("Invalid value for `relevant_customer_tags`, must not be `None`")  # noqa: E501

        self._relevant_customer_tags = relevant_customer_tags

    @property
    def title(self):
        """Gets the title of this MaintenanceWindow.  # noqa: E501

        Title of this maintenance window  # noqa: E501

        :return: The title of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MaintenanceWindow.

        Title of this maintenance window  # noqa: E501

        :param title: The title of this MaintenanceWindow.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def start_time_in_seconds(self):
        """Gets the start_time_in_seconds of this MaintenanceWindow.  # noqa: E501

        The time in epoch seconds when this maintenance window will start  # noqa: E501

        :return: The start_time_in_seconds of this MaintenanceWindow.  # noqa: E501
        :rtype: int
        """
        return self._start_time_in_seconds

    @start_time_in_seconds.setter
    def start_time_in_seconds(self, start_time_in_seconds):
        """Sets the start_time_in_seconds of this MaintenanceWindow.

        The time in epoch seconds when this maintenance window will start  # noqa: E501

        :param start_time_in_seconds: The start_time_in_seconds of this MaintenanceWindow.  # noqa: E501
        :type: int
        """
        if start_time_in_seconds is None:
            raise ValueError("Invalid value for `start_time_in_seconds`, must not be `None`")  # noqa: E501

        self._start_time_in_seconds = start_time_in_seconds

    @property
    def end_time_in_seconds(self):
        """Gets the end_time_in_seconds of this MaintenanceWindow.  # noqa: E501

        The time in epoch seconds when this maintenance window will end  # noqa: E501

        :return: The end_time_in_seconds of this MaintenanceWindow.  # noqa: E501
        :rtype: int
        """
        return self._end_time_in_seconds

    @end_time_in_seconds.setter
    def end_time_in_seconds(self, end_time_in_seconds):
        """Sets the end_time_in_seconds of this MaintenanceWindow.

        The time in epoch seconds when this maintenance window will end  # noqa: E501

        :param end_time_in_seconds: The end_time_in_seconds of this MaintenanceWindow.  # noqa: E501
        :type: int
        """
        if end_time_in_seconds is None:
            raise ValueError("Invalid value for `end_time_in_seconds`, must not be `None`")  # noqa: E501

        self._end_time_in_seconds = end_time_in_seconds

    @property
    def relevant_host_tags(self):
        """Gets the relevant_host_tags of this MaintenanceWindow.  # noqa: E501

        List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window  # noqa: E501

        :return: The relevant_host_tags of this MaintenanceWindow.  # noqa: E501
        :rtype: list[str]
        """
        return self._relevant_host_tags

    @relevant_host_tags.setter
    def relevant_host_tags(self, relevant_host_tags):
        """Sets the relevant_host_tags of this MaintenanceWindow.

        List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window  # noqa: E501

        :param relevant_host_tags: The relevant_host_tags of this MaintenanceWindow.  # noqa: E501
        :type: list[str]
        """

        self._relevant_host_tags = relevant_host_tags

    @property
    def relevant_host_names(self):
        """Gets the relevant_host_names of this MaintenanceWindow.  # noqa: E501

        List of source/host names that will be put into maintenance because of this maintenance window  # noqa: E501

        :return: The relevant_host_names of this MaintenanceWindow.  # noqa: E501
        :rtype: list[str]
        """
        return self._relevant_host_names

    @relevant_host_names.setter
    def relevant_host_names(self, relevant_host_names):
        """Sets the relevant_host_names of this MaintenanceWindow.

        List of source/host names that will be put into maintenance because of this maintenance window  # noqa: E501

        :param relevant_host_names: The relevant_host_names of this MaintenanceWindow.  # noqa: E501
        :type: list[str]
        """

        self._relevant_host_names = relevant_host_names

    @property
    def creator_id(self):
        """Gets the creator_id of this MaintenanceWindow.  # noqa: E501


        :return: The creator_id of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this MaintenanceWindow.


        :param creator_id: The creator_id of this MaintenanceWindow.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def updater_id(self):
        """Gets the updater_id of this MaintenanceWindow.  # noqa: E501


        :return: The updater_id of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this MaintenanceWindow.


        :param updater_id: The updater_id of this MaintenanceWindow.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this MaintenanceWindow.  # noqa: E501


        :return: The created_epoch_millis of this MaintenanceWindow.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this MaintenanceWindow.


        :param created_epoch_millis: The created_epoch_millis of this MaintenanceWindow.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this MaintenanceWindow.  # noqa: E501


        :return: The updated_epoch_millis of this MaintenanceWindow.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this MaintenanceWindow.


        :param updated_epoch_millis: The updated_epoch_millis of this MaintenanceWindow.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def relevant_host_tags_anded(self):
        """Gets the relevant_host_tags_anded of this MaintenanceWindow.  # noqa: E501

        Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply.  If false, the tags are OR'ed, and a source/host must contain one of the tags. Default: false  # noqa: E501

        :return: The relevant_host_tags_anded of this MaintenanceWindow.  # noqa: E501
        :rtype: bool
        """
        return self._relevant_host_tags_anded

    @relevant_host_tags_anded.setter
    def relevant_host_tags_anded(self, relevant_host_tags_anded):
        """Sets the relevant_host_tags_anded of this MaintenanceWindow.

        Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply.  If false, the tags are OR'ed, and a source/host must contain one of the tags. Default: false  # noqa: E501

        :param relevant_host_tags_anded: The relevant_host_tags_anded of this MaintenanceWindow.  # noqa: E501
        :type: bool
        """

        self._relevant_host_tags_anded = relevant_host_tags_anded

    @property
    def host_tag_group_host_names_group_anded(self):
        """Gets the host_tag_group_host_names_group_anded of this MaintenanceWindow.  # noqa: E501

        If true, a source/host must be in 'relevantHostNames' and have tags matching the specification formed by 'relevantHostTags' and 'relevantHostTagsAnded' in order for this maintenance window to apply. If false, a source/host must either be in 'relevantHostNames' or match 'relevantHostTags' and 'relevantHostTagsAnded'. Default: false  # noqa: E501

        :return: The host_tag_group_host_names_group_anded of this MaintenanceWindow.  # noqa: E501
        :rtype: bool
        """
        return self._host_tag_group_host_names_group_anded

    @host_tag_group_host_names_group_anded.setter
    def host_tag_group_host_names_group_anded(self, host_tag_group_host_names_group_anded):
        """Sets the host_tag_group_host_names_group_anded of this MaintenanceWindow.

        If true, a source/host must be in 'relevantHostNames' and have tags matching the specification formed by 'relevantHostTags' and 'relevantHostTagsAnded' in order for this maintenance window to apply. If false, a source/host must either be in 'relevantHostNames' or match 'relevantHostTags' and 'relevantHostTagsAnded'. Default: false  # noqa: E501

        :param host_tag_group_host_names_group_anded: The host_tag_group_host_names_group_anded of this MaintenanceWindow.  # noqa: E501
        :type: bool
        """

        self._host_tag_group_host_names_group_anded = host_tag_group_host_names_group_anded

    @property
    def event_name(self):
        """Gets the event_name of this MaintenanceWindow.  # noqa: E501

        The name of an event associated with the creation/update of this maintenance window  # noqa: E501

        :return: The event_name of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this MaintenanceWindow.

        The name of an event associated with the creation/update of this maintenance window  # noqa: E501

        :param event_name: The event_name of this MaintenanceWindow.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def running_state(self):
        """Gets the running_state of this MaintenanceWindow.  # noqa: E501


        :return: The running_state of this MaintenanceWindow.  # noqa: E501
        :rtype: str
        """
        return self._running_state

    @running_state.setter
    def running_state(self, running_state):
        """Sets the running_state of this MaintenanceWindow.


        :param running_state: The running_state of this MaintenanceWindow.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONGOING", "PENDING", "ENDED"]  # noqa: E501
        if running_state not in allowed_values:
            raise ValueError(
                "Invalid value for `running_state` ({0}), must be one of {1}"  # noqa: E501
                .format(running_state, allowed_values)
            )

        self._running_state = running_state

    @property
    def sort_attr(self):
        """Gets the sort_attr of this MaintenanceWindow.  # noqa: E501

        Numeric value used in default sorting  # noqa: E501

        :return: The sort_attr of this MaintenanceWindow.  # noqa: E501
        :rtype: int
        """
        return self._sort_attr

    @sort_attr.setter
    def sort_attr(self, sort_attr):
        """Sets the sort_attr of this MaintenanceWindow.

        Numeric value used in default sorting  # noqa: E501

        :param sort_attr: The sort_attr of this MaintenanceWindow.  # noqa: E501
        :type: int
        """

        self._sort_attr = sort_attr

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
        if issubclass(MaintenanceWindow, dict):
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
        if not isinstance(other, MaintenanceWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
