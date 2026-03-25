# ContentItem

Serializer for individual content items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Content identifier | 
**name** | **str** | Content name | 
**slug** | **str** | Content slug | 
**platform** | **str** | Platform key | 
**external** | **bool** | Whether content is external to the platform | 
**analytics** | [**ContentAnalytics**](ContentAnalytics.md) |  | 
**instructor** | **str** | Instructor name | [optional] 
**category** | **str** | Content category | [optional] 
**duration** | **str** | Content duration | [optional] 
**enabled** | **bool** | Whether content is enabled | [optional] 
**created** | **str** | Creation date | [optional] 
**updated** | **str** | Last update date | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from iblai.models.content_item import ContentItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContentItem from a JSON string
content_item_instance = ContentItem.from_json(json)
# print the JSON string representation of the object
print(ContentItem.to_json())

# convert the object into a dict
content_item_dict = content_item_instance.to_dict()
# create an instance of ContentItem from a dict
content_item_from_dict = ContentItem.from_dict(content_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


