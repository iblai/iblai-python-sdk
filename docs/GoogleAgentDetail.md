# GoogleAgentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**sub_agents** | **str** |  | [readonly] 
**platform** | **str** |  | [readonly] 
**unique_id** | **str** |  | [optional] 
**model** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**instruction** | **str** |  | 
**output_key** | **str** |  | [optional] 
**inserted_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**created_by** | **int** | edX user ID | [optional] 

## Example

```python
from iblai.models.google_agent_detail import GoogleAgentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAgentDetail from a JSON string
google_agent_detail_instance = GoogleAgentDetail.from_json(json)
# print the JSON string representation of the object
print(GoogleAgentDetail.to_json())

# convert the object into a dict
google_agent_detail_dict = google_agent_detail_instance.to_dict()
# create an instance of GoogleAgentDetail from a dict
google_agent_detail_from_dict = GoogleAgentDetail.from_dict(google_agent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


