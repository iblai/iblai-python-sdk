# NotificationTemplateTestResponse

Serializer for test notification response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the test email was sent successfully | 
**message** | **str** | Description of the result | 
**recipient** | **str** | Email address the test was sent to | 

## Example

```python
from iblai.models.notification_template_test_response import NotificationTemplateTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateTestResponse from a JSON string
notification_template_test_response_instance = NotificationTemplateTestResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplateTestResponse.to_json())

# convert the object into a dict
notification_template_test_response_dict = notification_template_test_response_instance.to_dict()
# create an instance of NotificationTemplateTestResponse from a dict
notification_template_test_response_from_dict = NotificationTemplateTestResponse.from_dict(notification_template_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


