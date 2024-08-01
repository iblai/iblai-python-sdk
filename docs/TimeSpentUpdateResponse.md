# TimeSpentUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **object** |  | [optional] 

## Example

```python
from iblai.models.time_spent_update_response import TimeSpentUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentUpdateResponse from a JSON string
time_spent_update_response_instance = TimeSpentUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(TimeSpentUpdateResponse.to_json())

# convert the object into a dict
time_spent_update_response_dict = time_spent_update_response_instance.to_dict()
# create an instance of TimeSpentUpdateResponse from a dict
time_spent_update_response_from_dict = TimeSpentUpdateResponse.from_dict(time_spent_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


