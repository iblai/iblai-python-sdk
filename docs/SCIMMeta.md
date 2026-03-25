# SCIMMeta

SCIM meta object serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Resource type | [optional] 
**created** | **str** | Creation timestamp | [optional] 
**last_modified** | **str** | Last modification timestamp | [optional] 
**version** | **str** | Resource version | [optional] 
**location** | **str** | Resource location URL | [optional] 

## Example

```python
from iblai.models.scim_meta import SCIMMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMMeta from a JSON string
scim_meta_instance = SCIMMeta.from_json(json)
# print the JSON string representation of the object
print(SCIMMeta.to_json())

# convert the object into a dict
scim_meta_dict = scim_meta_instance.to_dict()
# create an instance of SCIMMeta from a dict
scim_meta_from_dict = SCIMMeta.from_dict(scim_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


