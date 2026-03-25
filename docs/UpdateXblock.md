# UpdateXblock

Validate input for updating an xblock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xblock_id** | **str** | The xblock locator to update. | 
**display_name** | **str** | New display name. | [optional] 
**content** | **str** | New HTML content. Only applicable to component blocks (html, problem). | [optional] 

## Example

```python
from iblai.models.update_xblock import UpdateXblock

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateXblock from a JSON string
update_xblock_instance = UpdateXblock.from_json(json)
# print the JSON string representation of the object
print(UpdateXblock.to_json())

# convert the object into a dict
update_xblock_dict = update_xblock_instance.to_dict()
# create an instance of UpdateXblock from a dict
update_xblock_from_dict = UpdateXblock.from_dict(update_xblock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


