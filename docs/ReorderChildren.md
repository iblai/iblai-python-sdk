# ReorderChildren

Validate input for reordering children of an xblock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xblock_id** | **str** | The parent xblock whose children to reorder. | 
**children** | **List[str]** | Ordered list of child xblock IDs. All existing children must be included. | 

## Example

```python
from iblai.models.reorder_children import ReorderChildren

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderChildren from a JSON string
reorder_children_instance = ReorderChildren.from_json(json)
# print the JSON string representation of the object
print(ReorderChildren.to_json())

# convert the object into a dict
reorder_children_dict = reorder_children_instance.to_dict()
# create an instance of ReorderChildren from a dict
reorder_children_from_dict = ReorderChildren.from_dict(reorder_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


