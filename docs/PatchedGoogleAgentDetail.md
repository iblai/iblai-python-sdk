# PatchedGoogleAgentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**sub_agents** | **str** |  | [optional] [readonly] 
**platform** | **str** |  | [optional] [readonly] 
**unique_id** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instruction** | **str** |  | [optional] 
**output_key** | **str** |  | [optional] 
**inserted_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_by** | **int** | edX user ID | [optional] 

## Example

```python
from iblai.models.patched_google_agent_detail import PatchedGoogleAgentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGoogleAgentDetail from a JSON string
patched_google_agent_detail_instance = PatchedGoogleAgentDetail.from_json(json)
# print the JSON string representation of the object
print(PatchedGoogleAgentDetail.to_json())

# convert the object into a dict
patched_google_agent_detail_dict = patched_google_agent_detail_instance.to_dict()
# create an instance of PatchedGoogleAgentDetail from a dict
patched_google_agent_detail_from_dict = PatchedGoogleAgentDetail.from_dict(patched_google_agent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


