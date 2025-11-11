# NotificationTemplateList

Serializer for listing notification templates with inheritance info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this notification template. | [readonly] 
**type** | **str** | Select the type of notification from the available options.  * &#x60;DEFAULT_TEMPLATE&#x60; - Default Template * &#x60;APP_REGISTRATION&#x60; - App Registration * &#x60;USER_NOTIF_USER_REGISTRATION&#x60; - User Notif User Registration * &#x60;USER_NOTIF_COURSE_ENROLLMENT&#x60; - User Notif Course Enrollment * &#x60;ADMIN_NOTIF_COURSE_ENROLLMENT&#x60; - Admin Notif Course Enrollment * &#x60;USER_NOTIF_USER_INACTIVITY&#x60; - User Notif User Inactivity * &#x60;USER_NOTIF_COURSE_COMPLETION&#x60; - User Notif Course Completion * &#x60;USER_NOTIF_CREDENTIALS&#x60; - User Notif Credentials * &#x60;CUSTOM_NOTIFICATION&#x60; - Custom Notification * &#x60;PLATFORM_INVITATION&#x60; - Platform Invitation * &#x60;PROGRAM_INVITATION&#x60; - Program Invitation * &#x60;COURSE_INVITATION&#x60; - Course Invitation * &#x60;USER_NOTIF_LEARNER_PROGRESS&#x60; - User Notif Learner Progress * &#x60;PROACTIVE_LEARNER_NOTIFICATION&#x60; - Proactive Learner Notification * &#x60;ROLE_CHANGE&#x60; - Role Change * &#x60;COURSE_LICENSE_ASSIGNMENT&#x60; - Course License Assignment * &#x60;COURSE_LICENSE_GROUP_ASSIGNMENT&#x60; - Course License Group Assignment * &#x60;PROGRAM_LICENSE_ASSIGNMENT&#x60; - Program License Assignment * &#x60;PROGRAM_LICENSE_GROUP_ASSIGNMENT&#x60; - Program License Group Assignment * &#x60;USER_LICENSE_ASSIGNMENT&#x60; - User License Assignment * &#x60;USER_LICENSE_GROUP_ASSIGNMENT&#x60; - User License Group Assignment | [optional] 
**name** | **str** | A friendly name for the notification template. | [optional] 
**description** | **str** | Admin-friendly description of what this notification does, when it triggers, and what data it needs | [optional] 
**is_inherited** | **bool** |  | [readonly] 
**source_platform** | **str** |  | [readonly] 
**is_enabled** | **bool** |  | [readonly] 
**can_customize** | **bool** |  | [readonly] 
**is_custom** | **bool** |  | [readonly] [default to False]
**message_title** | **str** | The title for the notification message. | [optional] 
**email_subject** | **str** | Email subject line (supports Django template syntax) | [optional] 
**spas** | **str** |  | [readonly] 
**allowed_channels** | **str** |  | [readonly] 
**available_context** | **str** |  | [readonly] 

## Example

```python
from iblai.models.notification_template_list import NotificationTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateList from a JSON string
notification_template_list_instance = NotificationTemplateList.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplateList.to_json())

# convert the object into a dict
notification_template_list_dict = notification_template_list_instance.to_dict()
# create an instance of NotificationTemplateList from a dict
notification_template_list_from_dict = NotificationTemplateList.from_dict(notification_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


