# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_event_time** | **int** | Start time (in epoch millis) of the last event associated with this alert. | [optional] 
**severity** | **str** | Severity of the alert | 
**hidden** | **bool** |  | [optional] 
**name** | **str** |  | 
**id** | **str** |  | [optional] 
**target** | **str** | The email address or integration endpoint (such as PagerDuty or web hook) to notify when the alert status changes | [optional] 
**created** | **int** | When this alert was created, in epoch millis | [optional] 
**minutes** | **int** | The number of consecutive minutes that a series matching the condition query must evaluate to \&quot;true\&quot; (non-zero value) before the alert fires | 
**target_info** | [**list[TargetInfo]**](TargetInfo.md) | List of alert targets display information that includes name, id and type. | [optional] 
**sort_attr** | **int** | Attribute used for default alert sort that is derived from state and severity | [optional] 
**tags** | [**WFTags**](WFTags.md) |  | [optional] 
**status** | **list[str]** | Lists the current state of the alert. Can be one or more of: FIRING,SNOOZED, IN_MAINTENANCE, INVALID, NONE, CHECKING, TRASH, NO_DATA | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 
**updated** | **int** | When the alert was last updated, in epoch millis | [optional] 
**deleted** | **bool** |  | [optional] 
**targets** | **dict(str, str)** | Targets for severity. | [optional] 
**process_rate_minutes** | **int** | The interval between checks for this alert, in minutes.  Defaults to 1 minute | [optional] 
**last_processed_millis** | **int** | The time when this alert was last checked, in epoch millis | [optional] 
**update_user_id** | **str** | The user that last updated this alert | [optional] 
**in_maintenance_host_label_pairs** | [**list[SourceLabelPair]**](SourceLabelPair.md) | Lists the sources that will not be checked for this alert, due to matching a maintenance window | [optional] 
**failing_host_label_pairs** | [**list[SourceLabelPair]**](SourceLabelPair.md) | Failing host/metric pairs | [optional] 
**active_maintenance_windows** | **list[str]** | The names of the active maintenance windows that are affecting this alert | [optional] 
**condition** | **str** | A Wavefront query that is evaluated at regular intervals (default 1m).  The alert fires and notifications are triggered when a data series matching this query evaluates to a non-zero value for a set number of consecutive minutes | 
**alert_type** | **str** | Alert type. | [optional] 
**display_expression** | **str** | A second query whose results are displayed in the alert user interface instead of the condition query. This field is often used to display a version of the condition query with Boolean operators removed so that numerical values are plotted | [optional] 
**condition_qb_enabled** | **bool** | Whether the condition query was created using the Query Builder.  Default false | [optional] 
**display_expression_qb_enabled** | **bool** | Whether the display expression query was created using the Query Builder. Default false | [optional] 
**condition_qb_serialization** | **str** | The special serialization of the Query Builder that corresponds to the condition query.  Applicable only when conditionQBEnabled is true | [optional] 
**display_expression_qb_serialization** | **str** | The special serialization of the Query Builder that corresponds to the display expression query.  Applicable only when displayExpressionQBEnabled is true | [optional] 
**conditions** | **dict(str, str)** | Multi - alert conditions. | [optional] 
**include_obsolete_metrics** | **bool** | Whether to include obsolete metrics in alert query | [optional] 
**prefiring_host_label_pairs** | [**list[SourceLabelPair]**](SourceLabelPair.md) | Lists the series that are starting to fail, defined as failing for greater than 50% of the checks in the window determined by the \&quot;minutes\&quot; parameter | [optional] 
**no_data_event** | [**Event**](Event.md) | No data event related to the alert | [optional] 
**snoozed** | **int** | The until which time this alert is snoozed (not checked), in epoch millis.  A negative value implies the alert is snoozed indefinitely | [optional] 
**notificants** | **list[str]** | A derived field listing the webhook ids used by this alert | [optional] 
**additional_information** | **str** | User-supplied additional explanatory information for this alert.  Useful for linking runbooks, mitigations,, etc | [optional] 
**last_query_time** | **int** | Last query time of the alert, averaged on hourly basis | [optional] 
**alerts_last_day** | **int** |  | [optional] 
**alerts_last_week** | **int** |  | [optional] 
**alerts_last_month** | **int** |  | [optional] 
**in_trash** | **bool** |  | [optional] 
**query_failing** | **bool** | Whether there was an exception when the alert condition last ran | [optional] 
**create_user_id** | **str** |  | [optional] 
**last_failed_time** | **int** | The time of the last error encountered when running this alert&#39;s condition query, in epoch millis | [optional] 
**last_notification_millis** | **int** | When this alert last caused a notification, in epoch millis | [optional] 
**points_scanned_at_last_query** | **int** | A derived field recording the number of data points scanned when the system last computed this alert&#39;s condition | [optional] 
**num_points_in_failure_frame** | **int** | Number of points scanned in alert query time frame. | [optional] 
**metrics_used** | **list[str]** | Number of metrics checked by the alert condition | [optional] 
**hosts_used** | **list[str]** | Number of hosts checked by the alert condition | [optional] 
**system_owned** | **bool** | Whether this alert is system-owned and not writeable | [optional] 
**resolve_after_minutes** | **int** | The number of consecutive minutes that a firing series matching the condition query must evaluate to \&quot;false\&quot; (zero value) before the alert resolves.  When unset, this defaults to the same value as \&quot;minutes\&quot; | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**last_error_message** | **str** | The last error encountered when running this alert&#39;s condition query | [optional] 
**notification_resend_frequency_minutes** | **int** | How often to re-trigger a continually failing alert. If absent or &lt;&#x3D; 0, no retriggering occurs | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**severity_list** | **list[str]** | Alert severity list for multi-threshold type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


