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

from wavefront_api_client.models.access_control_list_simple import AccessControlListSimple  # noqa: F401,E501
from wavefront_api_client.models.dashboard_parameter_value import DashboardParameterValue  # noqa: F401,E501
from wavefront_api_client.models.dashboard_section import DashboardSection  # noqa: F401,E501
from wavefront_api_client.models.wf_tags import WFTags  # noqa: F401,E501


class Dashboard(object):
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
        'can_user_modify': 'bool',
        'name': 'str',
        'id': 'str',
        'parameters': 'dict(str, str)',
        'description': 'str',
        'hidden': 'bool',
        'num_charts': 'int',
        'system_owned': 'bool',
        'favorite': 'bool',
        'num_favorites': 'int',
        'orphan': 'bool',
        'tags': 'WFTags',
        'customer': 'str',
        'creator_id': 'str',
        'updater_id': 'str',
        'url': 'str',
        'event_filter_type': 'str',
        'sections': 'list[DashboardSection]',
        'parameter_details': 'dict(str, DashboardParameterValue)',
        'display_description': 'bool',
        'display_section_table_of_contents': 'bool',
        'display_query_parameters': 'bool',
        'chart_title_scalar': 'int',
        'event_query': 'str',
        'default_time_window': 'str',
        'default_start_time': 'int',
        'default_end_time': 'int',
        'chart_title_color': 'str',
        'chart_title_bg_color': 'str',
        'views_last_day': 'int',
        'views_last_week': 'int',
        'views_last_month': 'int',
        'acl': 'AccessControlListSimple',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'deleted': 'bool'
    }

    attribute_map = {
        'can_user_modify': 'canUserModify',
        'name': 'name',
        'id': 'id',
        'parameters': 'parameters',
        'description': 'description',
        'hidden': 'hidden',
        'num_charts': 'numCharts',
        'system_owned': 'systemOwned',
        'favorite': 'favorite',
        'num_favorites': 'numFavorites',
        'orphan': 'orphan',
        'tags': 'tags',
        'customer': 'customer',
        'creator_id': 'creatorId',
        'updater_id': 'updaterId',
        'url': 'url',
        'event_filter_type': 'eventFilterType',
        'sections': 'sections',
        'parameter_details': 'parameterDetails',
        'display_description': 'displayDescription',
        'display_section_table_of_contents': 'displaySectionTableOfContents',
        'display_query_parameters': 'displayQueryParameters',
        'chart_title_scalar': 'chartTitleScalar',
        'event_query': 'eventQuery',
        'default_time_window': 'defaultTimeWindow',
        'default_start_time': 'defaultStartTime',
        'default_end_time': 'defaultEndTime',
        'chart_title_color': 'chartTitleColor',
        'chart_title_bg_color': 'chartTitleBgColor',
        'views_last_day': 'viewsLastDay',
        'views_last_week': 'viewsLastWeek',
        'views_last_month': 'viewsLastMonth',
        'acl': 'acl',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'deleted': 'deleted'
    }

    def __init__(self, can_user_modify=None, name=None, id=None, parameters=None, description=None, hidden=None, num_charts=None, system_owned=None, favorite=None, num_favorites=None, orphan=None, tags=None, customer=None, creator_id=None, updater_id=None, url=None, event_filter_type=None, sections=None, parameter_details=None, display_description=None, display_section_table_of_contents=None, display_query_parameters=None, chart_title_scalar=None, event_query=None, default_time_window=None, default_start_time=None, default_end_time=None, chart_title_color=None, chart_title_bg_color=None, views_last_day=None, views_last_week=None, views_last_month=None, acl=None, created_epoch_millis=None, updated_epoch_millis=None, deleted=None):  # noqa: E501
        """Dashboard - a model defined in Swagger"""  # noqa: E501

        self._can_user_modify = None
        self._name = None
        self._id = None
        self._parameters = None
        self._description = None
        self._hidden = None
        self._num_charts = None
        self._system_owned = None
        self._favorite = None
        self._num_favorites = None
        self._orphan = None
        self._tags = None
        self._customer = None
        self._creator_id = None
        self._updater_id = None
        self._url = None
        self._event_filter_type = None
        self._sections = None
        self._parameter_details = None
        self._display_description = None
        self._display_section_table_of_contents = None
        self._display_query_parameters = None
        self._chart_title_scalar = None
        self._event_query = None
        self._default_time_window = None
        self._default_start_time = None
        self._default_end_time = None
        self._chart_title_color = None
        self._chart_title_bg_color = None
        self._views_last_day = None
        self._views_last_week = None
        self._views_last_month = None
        self._acl = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._deleted = None
        self.discriminator = None

        if can_user_modify is not None:
            self.can_user_modify = can_user_modify
        self.name = name
        self.id = id
        if parameters is not None:
            self.parameters = parameters
        if description is not None:
            self.description = description
        if hidden is not None:
            self.hidden = hidden
        if num_charts is not None:
            self.num_charts = num_charts
        if system_owned is not None:
            self.system_owned = system_owned
        if favorite is not None:
            self.favorite = favorite
        if num_favorites is not None:
            self.num_favorites = num_favorites
        if orphan is not None:
            self.orphan = orphan
        if tags is not None:
            self.tags = tags
        if customer is not None:
            self.customer = customer
        if creator_id is not None:
            self.creator_id = creator_id
        if updater_id is not None:
            self.updater_id = updater_id
        self.url = url
        if event_filter_type is not None:
            self.event_filter_type = event_filter_type
        self.sections = sections
        if parameter_details is not None:
            self.parameter_details = parameter_details
        if display_description is not None:
            self.display_description = display_description
        if display_section_table_of_contents is not None:
            self.display_section_table_of_contents = display_section_table_of_contents
        if display_query_parameters is not None:
            self.display_query_parameters = display_query_parameters
        if chart_title_scalar is not None:
            self.chart_title_scalar = chart_title_scalar
        if event_query is not None:
            self.event_query = event_query
        if default_time_window is not None:
            self.default_time_window = default_time_window
        if default_start_time is not None:
            self.default_start_time = default_start_time
        if default_end_time is not None:
            self.default_end_time = default_end_time
        if chart_title_color is not None:
            self.chart_title_color = chart_title_color
        if chart_title_bg_color is not None:
            self.chart_title_bg_color = chart_title_bg_color
        if views_last_day is not None:
            self.views_last_day = views_last_day
        if views_last_week is not None:
            self.views_last_week = views_last_week
        if views_last_month is not None:
            self.views_last_month = views_last_month
        if acl is not None:
            self.acl = acl
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if deleted is not None:
            self.deleted = deleted

    @property
    def can_user_modify(self):
        """Gets the can_user_modify of this Dashboard.  # noqa: E501


        :return: The can_user_modify of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._can_user_modify

    @can_user_modify.setter
    def can_user_modify(self, can_user_modify):
        """Sets the can_user_modify of this Dashboard.


        :param can_user_modify: The can_user_modify of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._can_user_modify = can_user_modify

    @property
    def name(self):
        """Gets the name of this Dashboard.  # noqa: E501

        Name of the dashboard  # noqa: E501

        :return: The name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dashboard.

        Name of the dashboard  # noqa: E501

        :param name: The name of this Dashboard.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this Dashboard.  # noqa: E501

        Unique identifier, also URL slug, of the dashboard  # noqa: E501

        :return: The id of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dashboard.

        Unique identifier, also URL slug, of the dashboard  # noqa: E501

        :param id: The id of this Dashboard.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this Dashboard.  # noqa: E501

        Deprecated.  An obsolete representation of dashboard parameters  # noqa: E501

        :return: The parameters of this Dashboard.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Dashboard.

        Deprecated.  An obsolete representation of dashboard parameters  # noqa: E501

        :param parameters: The parameters of this Dashboard.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def description(self):
        """Gets the description of this Dashboard.  # noqa: E501

        Human-readable description of the dashboard  # noqa: E501

        :return: The description of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Dashboard.

        Human-readable description of the dashboard  # noqa: E501

        :param description: The description of this Dashboard.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """Gets the hidden of this Dashboard.  # noqa: E501


        :return: The hidden of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Dashboard.


        :param hidden: The hidden of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def num_charts(self):
        """Gets the num_charts of this Dashboard.  # noqa: E501


        :return: The num_charts of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._num_charts

    @num_charts.setter
    def num_charts(self, num_charts):
        """Sets the num_charts of this Dashboard.


        :param num_charts: The num_charts of this Dashboard.  # noqa: E501
        :type: int
        """

        self._num_charts = num_charts

    @property
    def system_owned(self):
        """Gets the system_owned of this Dashboard.  # noqa: E501

        Whether this dashboard is system-owned and not writeable  # noqa: E501

        :return: The system_owned of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this Dashboard.

        Whether this dashboard is system-owned and not writeable  # noqa: E501

        :param system_owned: The system_owned of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def favorite(self):
        """Gets the favorite of this Dashboard.  # noqa: E501


        :return: The favorite of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this Dashboard.


        :param favorite: The favorite of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def num_favorites(self):
        """Gets the num_favorites of this Dashboard.  # noqa: E501


        :return: The num_favorites of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._num_favorites

    @num_favorites.setter
    def num_favorites(self, num_favorites):
        """Sets the num_favorites of this Dashboard.


        :param num_favorites: The num_favorites of this Dashboard.  # noqa: E501
        :type: int
        """

        self._num_favorites = num_favorites

    @property
    def orphan(self):
        """Gets the orphan of this Dashboard.  # noqa: E501


        :return: The orphan of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._orphan

    @orphan.setter
    def orphan(self, orphan):
        """Sets the orphan of this Dashboard.


        :param orphan: The orphan of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._orphan = orphan

    @property
    def tags(self):
        """Gets the tags of this Dashboard.  # noqa: E501


        :return: The tags of this Dashboard.  # noqa: E501
        :rtype: WFTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Dashboard.


        :param tags: The tags of this Dashboard.  # noqa: E501
        :type: WFTags
        """

        self._tags = tags

    @property
    def customer(self):
        """Gets the customer of this Dashboard.  # noqa: E501

        id of the customer to which this dashboard belongs  # noqa: E501

        :return: The customer of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Dashboard.

        id of the customer to which this dashboard belongs  # noqa: E501

        :param customer: The customer of this Dashboard.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def creator_id(self):
        """Gets the creator_id of this Dashboard.  # noqa: E501


        :return: The creator_id of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Dashboard.


        :param creator_id: The creator_id of this Dashboard.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def updater_id(self):
        """Gets the updater_id of this Dashboard.  # noqa: E501


        :return: The updater_id of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this Dashboard.


        :param updater_id: The updater_id of this Dashboard.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

    @property
    def url(self):
        """Gets the url of this Dashboard.  # noqa: E501

        Unique identifier, also URL slug, of the dashboard  # noqa: E501

        :return: The url of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Dashboard.

        Unique identifier, also URL slug, of the dashboard  # noqa: E501

        :param url: The url of this Dashboard.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def event_filter_type(self):
        """Gets the event_filter_type of this Dashboard.  # noqa: E501

        How charts belonging to this dashboard should display events.  BYCHART is default if unspecified  # noqa: E501

        :return: The event_filter_type of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._event_filter_type

    @event_filter_type.setter
    def event_filter_type(self, event_filter_type):
        """Sets the event_filter_type of this Dashboard.

        How charts belonging to this dashboard should display events.  BYCHART is default if unspecified  # noqa: E501

        :param event_filter_type: The event_filter_type of this Dashboard.  # noqa: E501
        :type: str
        """
        allowed_values = ["BYCHART", "AUTOMATIC", "ALL", "NONE", "BYDASHBOARD", "BYCHARTANDDASHBOARD"]  # noqa: E501
        if event_filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_filter_type, allowed_values)
            )

        self._event_filter_type = event_filter_type

    @property
    def sections(self):
        """Gets the sections of this Dashboard.  # noqa: E501

        Dashboard chart sections  # noqa: E501

        :return: The sections of this Dashboard.  # noqa: E501
        :rtype: list[DashboardSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this Dashboard.

        Dashboard chart sections  # noqa: E501

        :param sections: The sections of this Dashboard.  # noqa: E501
        :type: list[DashboardSection]
        """
        if sections is None:
            raise ValueError("Invalid value for `sections`, must not be `None`")  # noqa: E501

        self._sections = sections

    @property
    def parameter_details(self):
        """Gets the parameter_details of this Dashboard.  # noqa: E501

        The current (as of Wavefront 4.0) JSON representation of dashboard parameters.  This is a map from a parameter name to its representation  # noqa: E501

        :return: The parameter_details of this Dashboard.  # noqa: E501
        :rtype: dict(str, DashboardParameterValue)
        """
        return self._parameter_details

    @parameter_details.setter
    def parameter_details(self, parameter_details):
        """Sets the parameter_details of this Dashboard.

        The current (as of Wavefront 4.0) JSON representation of dashboard parameters.  This is a map from a parameter name to its representation  # noqa: E501

        :param parameter_details: The parameter_details of this Dashboard.  # noqa: E501
        :type: dict(str, DashboardParameterValue)
        """

        self._parameter_details = parameter_details

    @property
    def display_description(self):
        """Gets the display_description of this Dashboard.  # noqa: E501

        Whether the dashboard description section is opened by default when the dashboard is shown  # noqa: E501

        :return: The display_description of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this Dashboard.

        Whether the dashboard description section is opened by default when the dashboard is shown  # noqa: E501

        :param display_description: The display_description of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._display_description = display_description

    @property
    def display_section_table_of_contents(self):
        """Gets the display_section_table_of_contents of this Dashboard.  # noqa: E501

        Whether the \"pills\" quick-linked the sections of the dashboard are displayed by default when the dashboard is shown  # noqa: E501

        :return: The display_section_table_of_contents of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._display_section_table_of_contents

    @display_section_table_of_contents.setter
    def display_section_table_of_contents(self, display_section_table_of_contents):
        """Sets the display_section_table_of_contents of this Dashboard.

        Whether the \"pills\" quick-linked the sections of the dashboard are displayed by default when the dashboard is shown  # noqa: E501

        :param display_section_table_of_contents: The display_section_table_of_contents of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._display_section_table_of_contents = display_section_table_of_contents

    @property
    def display_query_parameters(self):
        """Gets the display_query_parameters of this Dashboard.  # noqa: E501

        Whether the dashboard parameters section is opened by default when the dashboard is shown  # noqa: E501

        :return: The display_query_parameters of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._display_query_parameters

    @display_query_parameters.setter
    def display_query_parameters(self, display_query_parameters):
        """Sets the display_query_parameters of this Dashboard.

        Whether the dashboard parameters section is opened by default when the dashboard is shown  # noqa: E501

        :param display_query_parameters: The display_query_parameters of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._display_query_parameters = display_query_parameters

    @property
    def chart_title_scalar(self):
        """Gets the chart_title_scalar of this Dashboard.  # noqa: E501

        Scale (normally 100) of chart title text size  # noqa: E501

        :return: The chart_title_scalar of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._chart_title_scalar

    @chart_title_scalar.setter
    def chart_title_scalar(self, chart_title_scalar):
        """Sets the chart_title_scalar of this Dashboard.

        Scale (normally 100) of chart title text size  # noqa: E501

        :param chart_title_scalar: The chart_title_scalar of this Dashboard.  # noqa: E501
        :type: int
        """

        self._chart_title_scalar = chart_title_scalar

    @property
    def event_query(self):
        """Gets the event_query of this Dashboard.  # noqa: E501

        Event query to run on dashboard charts  # noqa: E501

        :return: The event_query of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._event_query

    @event_query.setter
    def event_query(self, event_query):
        """Sets the event_query of this Dashboard.

        Event query to run on dashboard charts  # noqa: E501

        :param event_query: The event_query of this Dashboard.  # noqa: E501
        :type: str
        """

        self._event_query = event_query

    @property
    def default_time_window(self):
        """Gets the default_time_window of this Dashboard.  # noqa: E501

        Default time window to query charts  # noqa: E501

        :return: The default_time_window of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._default_time_window

    @default_time_window.setter
    def default_time_window(self, default_time_window):
        """Sets the default_time_window of this Dashboard.

        Default time window to query charts  # noqa: E501

        :param default_time_window: The default_time_window of this Dashboard.  # noqa: E501
        :type: str
        """

        self._default_time_window = default_time_window

    @property
    def default_start_time(self):
        """Gets the default_start_time of this Dashboard.  # noqa: E501

        Default start time in milliseconds to query charts  # noqa: E501

        :return: The default_start_time of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._default_start_time

    @default_start_time.setter
    def default_start_time(self, default_start_time):
        """Sets the default_start_time of this Dashboard.

        Default start time in milliseconds to query charts  # noqa: E501

        :param default_start_time: The default_start_time of this Dashboard.  # noqa: E501
        :type: int
        """

        self._default_start_time = default_start_time

    @property
    def default_end_time(self):
        """Gets the default_end_time of this Dashboard.  # noqa: E501

        Default end time in milliseconds to query charts  # noqa: E501

        :return: The default_end_time of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._default_end_time

    @default_end_time.setter
    def default_end_time(self, default_end_time):
        """Sets the default_end_time of this Dashboard.

        Default end time in milliseconds to query charts  # noqa: E501

        :param default_end_time: The default_end_time of this Dashboard.  # noqa: E501
        :type: int
        """

        self._default_end_time = default_end_time

    @property
    def chart_title_color(self):
        """Gets the chart_title_color of this Dashboard.  # noqa: E501

        Text color of the chart title text are, in rgba(rvalue,gvalue,bvalue,avalue)  # noqa: E501

        :return: The chart_title_color of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._chart_title_color

    @chart_title_color.setter
    def chart_title_color(self, chart_title_color):
        """Sets the chart_title_color of this Dashboard.

        Text color of the chart title text are, in rgba(rvalue,gvalue,bvalue,avalue)  # noqa: E501

        :param chart_title_color: The chart_title_color of this Dashboard.  # noqa: E501
        :type: str
        """

        self._chart_title_color = chart_title_color

    @property
    def chart_title_bg_color(self):
        """Gets the chart_title_bg_color of this Dashboard.  # noqa: E501

        Background color of the chart title text area, in rgba(rvalue,gvalue,bvalue,avalue)  # noqa: E501

        :return: The chart_title_bg_color of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._chart_title_bg_color

    @chart_title_bg_color.setter
    def chart_title_bg_color(self, chart_title_bg_color):
        """Sets the chart_title_bg_color of this Dashboard.

        Background color of the chart title text area, in rgba(rvalue,gvalue,bvalue,avalue)  # noqa: E501

        :param chart_title_bg_color: The chart_title_bg_color of this Dashboard.  # noqa: E501
        :type: str
        """

        self._chart_title_bg_color = chart_title_bg_color

    @property
    def views_last_day(self):
        """Gets the views_last_day of this Dashboard.  # noqa: E501


        :return: The views_last_day of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._views_last_day

    @views_last_day.setter
    def views_last_day(self, views_last_day):
        """Sets the views_last_day of this Dashboard.


        :param views_last_day: The views_last_day of this Dashboard.  # noqa: E501
        :type: int
        """

        self._views_last_day = views_last_day

    @property
    def views_last_week(self):
        """Gets the views_last_week of this Dashboard.  # noqa: E501


        :return: The views_last_week of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._views_last_week

    @views_last_week.setter
    def views_last_week(self, views_last_week):
        """Sets the views_last_week of this Dashboard.


        :param views_last_week: The views_last_week of this Dashboard.  # noqa: E501
        :type: int
        """

        self._views_last_week = views_last_week

    @property
    def views_last_month(self):
        """Gets the views_last_month of this Dashboard.  # noqa: E501


        :return: The views_last_month of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._views_last_month

    @views_last_month.setter
    def views_last_month(self, views_last_month):
        """Sets the views_last_month of this Dashboard.


        :param views_last_month: The views_last_month of this Dashboard.  # noqa: E501
        :type: int
        """

        self._views_last_month = views_last_month

    @property
    def acl(self):
        """Gets the acl of this Dashboard.  # noqa: E501


        :return: The acl of this Dashboard.  # noqa: E501
        :rtype: AccessControlListSimple
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this Dashboard.


        :param acl: The acl of this Dashboard.  # noqa: E501
        :type: AccessControlListSimple
        """

        self._acl = acl

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this Dashboard.  # noqa: E501


        :return: The created_epoch_millis of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this Dashboard.


        :param created_epoch_millis: The created_epoch_millis of this Dashboard.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this Dashboard.  # noqa: E501


        :return: The updated_epoch_millis of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this Dashboard.


        :param updated_epoch_millis: The updated_epoch_millis of this Dashboard.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def deleted(self):
        """Gets the deleted of this Dashboard.  # noqa: E501


        :return: The deleted of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Dashboard.


        :param deleted: The deleted of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

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
        if issubclass(Dashboard, dict):
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
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
