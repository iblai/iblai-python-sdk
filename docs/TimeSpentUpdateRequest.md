# TimeSpentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Time when the event occurred, ensure it is UTC (ISO 8601 format) | 
**course_id** | **str** | Course ID to track time spent | [optional] 
**mentor_uuid** | **str** | Mentor UUID to track time spent | [optional] 
**block_id** | **str** | Block ID to track time spent | [optional] 
**count** | **int** | Time spent in seconds | 
**url** | **str** | Source URL | 
**metadata** | **object** | Additional metadata | [optional] 
**session_uuid** | **str** | Session UUID to track time spent | [optional] 

## Example

```python
from iblai.models.time_spent_update_request import TimeSpentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentUpdateRequest from a JSON string
time_spent_update_request_instance = TimeSpentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TimeSpentUpdateRequest.to_json())

# convert the object into a dict
time_spent_update_request_dict = time_spent_update_request_instance.to_dict()
# create an instance of TimeSpentUpdateRequest from a dict
time_spent_update_request_from_dict = TimeSpentUpdateRequest.from_dict(time_spent_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


