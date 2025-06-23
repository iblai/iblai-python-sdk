# WebResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**title** | **str** |  | 
**image_url** | **str** |  | [optional] 
**source** | **str** |  | [optional] [default to '']
**metadata** | **object** |  | [optional] 
**card** | [**WebResourceCard**](WebResourceCard.md) |  | [optional] 

## Example

```python
from iblai.models.web_resource import WebResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebResource from a JSON string
web_resource_instance = WebResource.from_json(json)
# print the JSON string representation of the object
print(WebResource.to_json())

# convert the object into a dict
web_resource_dict = web_resource_instance.to_dict()
# create an instance of WebResource from a dict
web_resource_from_dict = WebResource.from_dict(web_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


