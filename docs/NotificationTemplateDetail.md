# NotificationTemplateDetail

Serializer for detailed template view and editing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this notification template. | [readonly] 
**type** | **str** | Select the type of notification from the available options.  * &#x60;ADMIN_NOTIF_COURSE_ENROLLMENT&#x60; - Admin Notif Course Enrollment * &#x60;APP_REGISTRATION&#x60; - App Registration * &#x60;COURSE_INVITATION&#x60; - Course Invitation * &#x60;COURSE_LICENSE_ASSIGNMENT&#x60; - Course License Assignment * &#x60;COURSE_LICENSE_GROUP_ASSIGNMENT&#x60; - Course License Group Assignment * &#x60;CUSTOM_NOTIFICATION&#x60; - Custom Notification * &#x60;DEFAULT_TEMPLATE&#x60; - Default Template * &#x60;HUMAN_SUPPORT_NOTIFICATION&#x60; - Human Support Notification * &#x60;PLATFORM_INVITATION&#x60; - Platform Invitation * &#x60;POLICY_ASSIGNMENT&#x60; - Policy Assignment * &#x60;PROACTIVE_LEARNER_NOTIFICATION&#x60; - Proactive Learner Notification * &#x60;PROGRAM_INVITATION&#x60; - Program Invitation * &#x60;PROGRAM_LICENSE_ASSIGNMENT&#x60; - Program License Assignment * &#x60;PROGRAM_LICENSE_GROUP_ASSIGNMENT&#x60; - Program License Group Assignment * &#x60;REPORT_COMPLETED&#x60; - Report Completed * &#x60;ROLE_CHANGE&#x60; - Role Change * &#x60;USER_LICENSE_ASSIGNMENT&#x60; - User License Assignment * &#x60;USER_LICENSE_GROUP_ASSIGNMENT&#x60; - User License Group Assignment * &#x60;USER_NOTIF_COURSE_COMPLETION&#x60; - User Notif Course Completion * &#x60;USER_NOTIF_COURSE_ENROLLMENT&#x60; - User Notif Course Enrollment * &#x60;USER_NOTIF_CREDENTIALS&#x60; - User Notif Credentials * &#x60;USER_NOTIF_LEARNER_PROGRESS&#x60; - User Notif Learner Progress * &#x60;USER_NOTIF_USER_INACTIVITY&#x60; - User Notif User Inactivity * &#x60;USER_NOTIF_USER_REGISTRATION&#x60; - User Notif User Registration | [readonly] 
**name** | **str** | Template display name | [optional] 
**description** | **str** | Description of when this notification is sent | [optional] 
**message_title** | **str** | Title for push/in-app notifications | [optional] 
**message_body** | **str** | Body text (supports Django template syntax) | [optional] 
**short_message_body** | **str** | Short version for SMS or preview | [optional] 
**email_subject** | **str** | Email subject line (supports {{ variables }}) | [optional] 
**email_from_address** | **str** | Sender email address | [optional] 
**email_html_template** | **str** | HTML email body (supports Django template syntax) | [optional] 
**spas_detail** | [**List[Spa]**](Spa.md) |  | [readonly] 
**allowed_channels_detail** | [**List[ConsumerChannel]**](ConsumerChannel.md) |  | [readonly] 
**spa_ids** | **List[int]** | IDs of SPAs that can use this template | [optional] 
**channel_ids** | **List[int]** | IDs of delivery channels (email, push, etc.) | [optional] 
**is_inherited** | **bool** | True if using main platform template (no platform override) | [readonly] 
**is_enabled** | **bool** | True if notification is enabled for this platform | [readonly] 
**source_platform** | **str** | Platform key of the template source | [readonly] 
**can_customize** | **bool** | True if platform admin can edit template content | [readonly] 
**metadata** | **object** | JSON config (periodic_config, policy_config, etc.) | [optional] 
**available_context** | **str** | Context variables available for template rendering | [readonly] 
**proactive_prompt_message** | **str** | Default prompt message for AI mentor notifications | [optional] 
**periodic_config** | **str** | Periodic report configuration (PROACTIVE_LEARNER_NOTIFICATION only) | [readonly] 
**periodic_learner_scope** | [**PeriodicLearnerScopeEnum**](PeriodicLearnerScopeEnum.md) | Which learners to include: ACTIVE_LEARNERS or ALL_LEARNERS  * &#x60;ACTIVE_LEARNERS&#x60; - ACTIVE_LEARNERS * &#x60;ALL_LEARNERS&#x60; - ALL_LEARNERS | [optional] 
**periodic_report_period_days** | **int** | Number of days to include in the report period | [optional] 
**periodic_frequency** | [**PeriodicFrequencyEnum**](PeriodicFrequencyEnum.md) | How often to send: DAILY, WEEKLY, MONTHLY, or CUSTOM  * &#x60;DAILY&#x60; - DAILY * &#x60;WEEKLY&#x60; - WEEKLY * &#x60;MONTHLY&#x60; - MONTHLY * &#x60;CUSTOM&#x60; - CUSTOM | [optional] 
**periodic_custom_interval_days** | **int** | Custom interval in days (when frequency is CUSTOM) | [optional] 
**periodic_execution_time** | **str** | Time to run in HH:MM format (24-hour) | [optional] 
**periodic_timezone** | **str** | Timezone for execution time (e.g. America/New_York) | [optional] 
**periodic_mentors** | **List[Dict[str, object]]** | List of mentor configurations: [{\&quot;unique_id\&quot;: \&quot;uuid\&quot;, \&quot;prompt\&quot;: \&quot;...\&quot;, \&quot;name\&quot;: \&quot;...\&quot;}] | [optional] 
**policy_config** | **str** | Policy assignment notification config (POLICY_ASSIGNMENT only) | [readonly] 
**policy_enabled_policies** | **List[Dict[str, object]]** | Per-role config: [{\&quot;role_name\&quot;: \&quot;Analytics Viewer\&quot;, \&quot;enabled\&quot;: True, \&quot;subject\&quot;: \&quot;Custom subject for {{role_name}}\&quot;}, ...] | [optional] 
**policy_notify_on_assignment** | **bool** | Send notification when policy is assigned | [optional] 
**policy_notify_on_removal** | **bool** | Send notification when policy is removed | [optional] 
**human_support_config** | **str** | Human support notification config (HUMAN_SUPPORT_NOTIFICATION only) | [readonly] 
**human_support_recipient_mode** | [**HumanSupportRecipientModeEnum**](HumanSupportRecipientModeEnum.md) | Who receives human support ticket notifications  * &#x60;platform_admins_and_mentor_owner&#x60; - platform_admins_and_mentor_owner * &#x60;platform_admins_only&#x60; - platform_admins_only * &#x60;mentor_owner_only&#x60; - mentor_owner_only * &#x60;custom&#x60; - custom | [optional] 
**human_support_custom_recipients** | **List[Dict[str, object]]** | Custom targets: user: {type, id}; user_group: {type, id}; rbac_policy: {type, policy_name} | [optional] 
**created_at** | **datetime** | Timestamp when this template was created | [readonly] 
**updated_at** | **datetime** | Timestamp when this template was last updated | [readonly] 

## Example

```python
from iblai.models.notification_template_detail import NotificationTemplateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateDetail from a JSON string
notification_template_detail_instance = NotificationTemplateDetail.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplateDetail.to_json())

# convert the object into a dict
notification_template_detail_dict = notification_template_detail_instance.to_dict()
# create an instance of NotificationTemplateDetail from a dict
notification_template_detail_from_dict = NotificationTemplateDetail.from_dict(notification_template_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


