# PatchedNotificationTemplateDetail

Serializer for detailed template view and editing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this notification template. | [optional] [readonly] 
**type** | **str** | Select the type of notification from the available options.  * &#x60;DEFAULT_TEMPLATE&#x60; - Default Template * &#x60;APP_REGISTRATION&#x60; - App Registration * &#x60;USER_NOTIF_USER_REGISTRATION&#x60; - User Notif User Registration * &#x60;USER_NOTIF_COURSE_ENROLLMENT&#x60; - User Notif Course Enrollment * &#x60;ADMIN_NOTIF_COURSE_ENROLLMENT&#x60; - Admin Notif Course Enrollment * &#x60;USER_NOTIF_USER_INACTIVITY&#x60; - User Notif User Inactivity * &#x60;USER_NOTIF_COURSE_COMPLETION&#x60; - User Notif Course Completion * &#x60;USER_NOTIF_CREDENTIALS&#x60; - User Notif Credentials * &#x60;CUSTOM_NOTIFICATION&#x60; - Custom Notification * &#x60;PLATFORM_INVITATION&#x60; - Platform Invitation * &#x60;PROGRAM_INVITATION&#x60; - Program Invitation * &#x60;COURSE_INVITATION&#x60; - Course Invitation * &#x60;USER_NOTIF_LEARNER_PROGRESS&#x60; - User Notif Learner Progress * &#x60;PROACTIVE_LEARNER_NOTIFICATION&#x60; - Proactive Learner Notification * &#x60;ROLE_CHANGE&#x60; - Role Change * &#x60;COURSE_LICENSE_ASSIGNMENT&#x60; - Course License Assignment * &#x60;COURSE_LICENSE_GROUP_ASSIGNMENT&#x60; - Course License Group Assignment * &#x60;PROGRAM_LICENSE_ASSIGNMENT&#x60; - Program License Assignment * &#x60;PROGRAM_LICENSE_GROUP_ASSIGNMENT&#x60; - Program License Group Assignment * &#x60;USER_LICENSE_ASSIGNMENT&#x60; - User License Assignment * &#x60;USER_LICENSE_GROUP_ASSIGNMENT&#x60; - User License Group Assignment | [optional] [readonly] 
**name** | **str** | A friendly name for the notification template. | [optional] 
**description** | **str** | Admin-friendly description of what this notification does, when it triggers, and what data it needs | [optional] 
**message_title** | **str** | The title for the notification message. | [optional] 
**message_body** | **str** | The full notification message body. | [optional] 
**short_message_body** | **str** | A short version of the notification message body. | [optional] 
**email_subject** | **str** | Email subject line (supports Django template syntax) | [optional] 
**email_from_address** | **str** | Sender email address (default: IBL &lt;noreply@ibl.ai&gt;) | [optional] 
**email_html_template** | **str** | Full HTML template for email body | [optional] 
**spas_detail** | [**List[Spa]**](Spa.md) |  | [optional] [readonly] 
**allowed_channels_detail** | [**List[ConsumerChannel]**](ConsumerChannel.md) |  | [optional] [readonly] 
**spa_ids** | **List[int]** |  | [optional] 
**channel_ids** | **List[int]** |  | [optional] 
**is_inherited** | **bool** |  | [optional] [readonly] 
**is_enabled** | **bool** |  | [optional] [readonly] 
**source_platform** | **str** |  | [optional] [readonly] 
**metadata** | **object** |  | [optional] 
**available_context** | **str** |  | [optional] [readonly] 
**proactive_prompt_message** | **str** | Default prompt message for AI mentor notifications | [optional] 
**periodic_config** | **str** |  | [optional] [readonly] 
**periodic_learner_scope** | [**PeriodicLearnerScopeEnum**](PeriodicLearnerScopeEnum.md) |  | [optional] 
**periodic_report_period_days** | **int** |  | [optional] 
**periodic_frequency** | [**PeriodicFrequencyEnum**](PeriodicFrequencyEnum.md) |  | [optional] 
**periodic_custom_interval_days** | **int** |  | [optional] 
**periodic_execution_time** | **str** |  | [optional] 
**periodic_timezone** | **str** |  | [optional] 
**periodic_mentors** | **List[Dict[str, object]]** | List of mentor configurations: [{\&quot;unique_id\&quot;: \&quot;uuid\&quot;, \&quot;prompt\&quot;: \&quot;...\&quot;, \&quot;name\&quot;: \&quot;...\&quot;}] | [optional] 
**created_at** | **datetime** | Timestamp when this template was created | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp when this template was last updated | [optional] [readonly] 

## Example

```python
from iblai.models.patched_notification_template_detail import PatchedNotificationTemplateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotificationTemplateDetail from a JSON string
patched_notification_template_detail_instance = PatchedNotificationTemplateDetail.from_json(json)
# print the JSON string representation of the object
print(PatchedNotificationTemplateDetail.to_json())

# convert the object into a dict
patched_notification_template_detail_dict = patched_notification_template_detail_instance.to_dict()
# create an instance of PatchedNotificationTemplateDetail from a dict
patched_notification_template_detail_from_dict = PatchedNotificationTemplateDetail.from_dict(patched_notification_template_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


