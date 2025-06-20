# NotificationTemplateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_title** | **str** | Title of the message | [optional] [default to '']
**message_body** | **str** |      This would be the body of the message. Some context are available to use in the system.      e.g      &#x60;&#x60;&#x60;     This is a sample message to {{username}}.      Available accessors are      - site_name     - site_url     - site_logo_url     - username     and &lt;anything passed into context dictionary&gt;     &#x60;&#x60;&#x60;       | 

## Example

```python
from iblai.models.notification_template_data import NotificationTemplateData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateData from a JSON string
notification_template_data_instance = NotificationTemplateData.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplateData.to_json())

# convert the object into a dict
notification_template_data_dict = notification_template_data_instance.to_dict()
# create an instance of NotificationTemplateData from a dict
notification_template_data_from_dict = NotificationTemplateData.from_dict(notification_template_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


