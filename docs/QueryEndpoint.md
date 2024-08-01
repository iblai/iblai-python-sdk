# QueryEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 

## Example

```python
from iblai.models.query_endpoint import QueryEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of QueryEndpoint from a JSON string
query_endpoint_instance = QueryEndpoint.from_json(json)
# print the JSON string representation of the object
print(QueryEndpoint.to_json())

# convert the object into a dict
query_endpoint_dict = query_endpoint_instance.to_dict()
# create an instance of QueryEndpoint from a dict
query_endpoint_from_dict = QueryEndpoint.from_dict(query_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


