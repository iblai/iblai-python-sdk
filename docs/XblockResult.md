# XblockResult

Standard response for xblock operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**detail** | **str** |  | 
**xblock_id** | **str** |  | [optional] 
**extra** | **object** |  | [optional] 

## Example

```python
from iblai.models.xblock_result import XblockResult

# TODO update the JSON string below
json = "{}"
# create an instance of XblockResult from a JSON string
xblock_result_instance = XblockResult.from_json(json)
# print the JSON string representation of the object
print(XblockResult.to_json())

# convert the object into a dict
xblock_result_dict = xblock_result_instance.to_dict()
# create an instance of XblockResult from a dict
xblock_result_from_dict = XblockResult.from_dict(xblock_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


