# ModerationLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | [optional] 
**platform_key** | **str** |  | 
**mentor** | **int** |  | 
**prompt** | **str** |  | 
**reason** | **str** |  | 
**target_system** | [**TargetSystemEnum**](TargetSystemEnum.md) |  | [optional] 
**date_created** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.moderation_log import ModerationLog

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationLog from a JSON string
moderation_log_instance = ModerationLog.from_json(json)
# print the JSON string representation of the object
print(ModerationLog.to_json())

# convert the object into a dict
moderation_log_dict = moderation_log_instance.to_dict()
# create an instance of ModerationLog from a dict
moderation_log_from_dict = ModerationLog.from_dict(moderation_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


