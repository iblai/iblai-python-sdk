# ActivityInfo

Serializer for activity information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_activity** | **datetime** |  | 
**last_activity** | **datetime** |  | 

## Example

```python
from iblai.models.activity_info import ActivityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityInfo from a JSON string
activity_info_instance = ActivityInfo.from_json(json)
# print the JSON string representation of the object
print(ActivityInfo.to_json())

# convert the object into a dict
activity_info_dict = activity_info_instance.to_dict()
# create an instance of ActivityInfo from a dict
activity_info_from_dict = ActivityInfo.from_dict(activity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


