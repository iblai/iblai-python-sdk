# PreviewResponse

Response serializer for notification preview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**build_id** | **str** |  | 
**count** | **int** |  | 
**warning** | **str** |  | 
**recipients** | [**List[Recipient]**](Recipient.md) |  | 

## Example

```python
from iblai.models.preview_response import PreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewResponse from a JSON string
preview_response_instance = PreviewResponse.from_json(json)
# print the JSON string representation of the object
print(PreviewResponse.to_json())

# convert the object into a dict
preview_response_dict = preview_response_instance.to_dict()
# create an instance of PreviewResponse from a dict
preview_response_from_dict = PreviewResponse.from_dict(preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


