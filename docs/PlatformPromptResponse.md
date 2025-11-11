# PlatformPromptResponse

Response serializer for platform prompt retrieval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | 
**prompt_text** | **str** |  | 
**recommendation_type** | **str** |  | 
**spa_url** | **str** |  | [optional] 
**active** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** | Username of who created this prompt | [optional] 

## Example

```python
from iblai.models.platform_prompt_response import PlatformPromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformPromptResponse from a JSON string
platform_prompt_response_instance = PlatformPromptResponse.from_json(json)
# print the JSON string representation of the object
print(PlatformPromptResponse.to_json())

# convert the object into a dict
platform_prompt_response_dict = platform_prompt_response_instance.to_dict()
# create an instance of PlatformPromptResponse from a dict
platform_prompt_response_from_dict = PlatformPromptResponse.from_dict(platform_prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


