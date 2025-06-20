# TriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** |  | 
**slug** | **str** |  | 
**parameters** | **object** |  | 

## Example

```python
from iblai.models.trigger_request import TriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerRequest from a JSON string
trigger_request_instance = TriggerRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerRequest.to_json())

# convert the object into a dict
trigger_request_dict = trigger_request_instance.to_dict()
# create an instance of TriggerRequest from a dict
trigger_request_from_dict = TriggerRequest.from_dict(trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


