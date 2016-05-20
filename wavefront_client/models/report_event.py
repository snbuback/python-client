# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ReportEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'annotations': 'dict(str, str)',
            'end_time': 'int',
            'hosts': 'list[str]',
            'is_ephemeral': 'bool',
            'is_user_event': 'bool',
            'name': 'str',
            'start_time': 'int',
            'summarized_events': 'int',
            'table': 'str',
            'tags': 'list[str]'
        }

        self.attribute_map = {
            'annotations': 'annotations',
            'end_time': 'endTime',
            'hosts': 'hosts',
            'is_ephemeral': 'isEphemeral',
            'is_user_event': 'isUserEvent',
            'name': 'name',
            'start_time': 'startTime',
            'summarized_events': 'summarizedEvents',
            'table': 'table',
            'tags': 'tags'
        }

        self._annotations = None
        self._end_time = None
        self._hosts = None
        self._is_ephemeral = False
        self._is_user_event = False
        self._name = None
        self._start_time = None
        self._summarized_events = None
        self._table = None
        self._tags = None

    @property
    def annotations(self):
        """
        Gets the annotations of this ReportEvent.
        Annotations for the event. Searchable during queries

        :return: The annotations of this ReportEvent.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this ReportEvent.
        Annotations for the event. Searchable during queries

        :param annotations: The annotations of this ReportEvent.
        :type: dict(str, str)
        """
        self._annotations = annotations

    @property
    def end_time(self):
        """
        Gets the end_time of this ReportEvent.
        End time in milliseconds for the event. If missing, the event is ongoing

        :return: The end_time of this ReportEvent.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this ReportEvent.
        End time in milliseconds for the event. If missing, the event is ongoing

        :param end_time: The end_time of this ReportEvent.
        :type: int
        """
        self._end_time = end_time

    @property
    def hosts(self):
        """
        Gets the hosts of this ReportEvent.
        Hosts associated for the event

        :return: The hosts of this ReportEvent.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this ReportEvent.
        Hosts associated for the event

        :param hosts: The hosts of this ReportEvent.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def is_ephemeral(self):
        """
        Gets the is_ephemeral of this ReportEvent.


        :return: The is_ephemeral of this ReportEvent.
        :rtype: bool
        """
        return self._is_ephemeral

    @is_ephemeral.setter
    def is_ephemeral(self, is_ephemeral):
        """
        Sets the is_ephemeral of this ReportEvent.


        :param is_ephemeral: The is_ephemeral of this ReportEvent.
        :type: bool
        """
        self._is_ephemeral = is_ephemeral

    @property
    def is_user_event(self):
        """
        Gets the is_user_event of this ReportEvent.


        :return: The is_user_event of this ReportEvent.
        :rtype: bool
        """
        return self._is_user_event

    @is_user_event.setter
    def is_user_event(self, is_user_event):
        """
        Sets the is_user_event of this ReportEvent.


        :param is_user_event: The is_user_event of this ReportEvent.
        :type: bool
        """
        self._is_user_event = is_user_event

    @property
    def name(self):
        """
        Gets the name of this ReportEvent.
        Name of the event

        :return: The name of this ReportEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportEvent.
        Name of the event

        :param name: The name of this ReportEvent.
        :type: str
        """
        self._name = name

    @property
    def start_time(self):
        """
        Gets the start_time of this ReportEvent.
        Start time in milliseconds for the event

        :return: The start_time of this ReportEvent.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this ReportEvent.
        Start time in milliseconds for the event

        :param start_time: The start_time of this ReportEvent.
        :type: int
        """
        self._start_time = start_time

    @property
    def summarized_events(self):
        """
        Gets the summarized_events of this ReportEvent.


        :return: The summarized_events of this ReportEvent.
        :rtype: int
        """
        return self._summarized_events

    @summarized_events.setter
    def summarized_events(self, summarized_events):
        """
        Sets the summarized_events of this ReportEvent.


        :param summarized_events: The summarized_events of this ReportEvent.
        :type: int
        """
        self._summarized_events = summarized_events

    @property
    def table(self):
        """
        Gets the table of this ReportEvent.
        The customer that owns the event

        :return: The table of this ReportEvent.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """
        Sets the table of this ReportEvent.
        The customer that owns the event

        :param table: The table of this ReportEvent.
        :type: str
        """
        self._table = table

    @property
    def tags(self):
        """
        Gets the tags of this ReportEvent.


        :return: The tags of this ReportEvent.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ReportEvent.


        :param tags: The tags of this ReportEvent.
        :type: list[str]
        """
        self._tags = tags

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
