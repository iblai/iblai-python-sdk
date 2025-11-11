# NotificationTemplateTest

Serializer for testing notification template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_email** | **str** | Email address to send test notification to. Defaults to requesting user&#39;s email. | [optional] 
**context** | **object** | Optional context variables for template rendering (e.g., {&#39;course_name&#39;: &#39;Test Course&#39;}) | [optional] 

## Example

```python
from iblai.models.notification_template_test import NotificationTemplateTest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateTest from a JSON string
notification_template_test_instance = NotificationTemplateTest.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplateTest.to_json())

# convert the object into a dict
notification_template_test_dict = notification_template_test_instance.to_dict()
# create an instance of NotificationTemplateTest from a dict
notification_template_test_from_dict = NotificationTemplateTest.from_dict(notification_template_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


