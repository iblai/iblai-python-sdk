# WebResourcesQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 

## Example

```python
from iblai.models.web_resources_query import WebResourcesQuery

# TODO update the JSON string below
json = "{}"
# create an instance of WebResourcesQuery from a JSON string
web_resources_query_instance = WebResourcesQuery.from_json(json)
# print the JSON string representation of the object
print(WebResourcesQuery.to_json())

# convert the object into a dict
web_resources_query_dict = web_resources_query_instance.to_dict()
# create an instance of WebResourcesQuery from a dict
web_resources_query_from_dict = WebResourcesQuery.from_dict(web_resources_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


