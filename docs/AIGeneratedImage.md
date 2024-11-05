# AIGeneratedImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | 
**image** | **str** |  | 
**platform** | **int** |  | 
**prompt** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**date_created** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.ai_generated_image import AIGeneratedImage

# TODO update the JSON string below
json = "{}"
# create an instance of AIGeneratedImage from a JSON string
ai_generated_image_instance = AIGeneratedImage.from_json(json)
# print the JSON string representation of the object
print(AIGeneratedImage.to_json())

# convert the object into a dict
ai_generated_image_dict = ai_generated_image_instance.to_dict()
# create an instance of AIGeneratedImage from a dict
ai_generated_image_from_dict = AIGeneratedImage.from_dict(ai_generated_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


