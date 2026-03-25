# ContentDetailsContentInfo

Serializer for the content information block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the content item | 
**name** | **str** |  | [optional] 
**type** | **str** | Content type (course, program, pathway, skill) | 
**slug** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**external** | **bool** | Whether the content is external to the platform | 
**metadata** | **Dict[str, object]** | Metadata associated with the content item | [optional] 

## Example

```python
from iblai.models.content_details_content_info import ContentDetailsContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsContentInfo from a JSON string
content_details_content_info_instance = ContentDetailsContentInfo.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsContentInfo.to_json())

# convert the object into a dict
content_details_content_info_dict = content_details_content_info_instance.to_dict()
# create an instance of ContentDetailsContentInfo from a dict
content_details_content_info_from_dict = ContentDetailsContentInfo.from_dict(content_details_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


