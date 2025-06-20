# PaginatedAIGeneratedImageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AIGeneratedImage]**](AIGeneratedImage.md) |  | 

## Example

```python
from iblai.models.paginated_ai_generated_image_list import PaginatedAIGeneratedImageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAIGeneratedImageList from a JSON string
paginated_ai_generated_image_list_instance = PaginatedAIGeneratedImageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAIGeneratedImageList.to_json())

# convert the object into a dict
paginated_ai_generated_image_list_dict = paginated_ai_generated_image_list_instance.to_dict()
# create an instance of PaginatedAIGeneratedImageList from a dict
paginated_ai_generated_image_list_from_dict = PaginatedAIGeneratedImageList.from_dict(paginated_ai_generated_image_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


