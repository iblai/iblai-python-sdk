# DeleteXblock

Validate input for deleting an xblock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xblock_id** | **str** | The xblock locator to delete. | 

## Example

```python
from iblai.models.delete_xblock import DeleteXblock

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteXblock from a JSON string
delete_xblock_instance = DeleteXblock.from_json(json)
# print the JSON string representation of the object
print(DeleteXblock.to_json())

# convert the object into a dict
delete_xblock_dict = delete_xblock_instance.to_dict()
# create an instance of DeleteXblock from a dict
delete_xblock_from_dict = DeleteXblock.from_dict(delete_xblock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


