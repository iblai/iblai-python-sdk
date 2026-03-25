# PaginatedClawInstanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ClawInstance]**](ClawInstance.md) |  | 

## Example

```python
from iblai.models.paginated_claw_instance_list import PaginatedClawInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClawInstanceList from a JSON string
paginated_claw_instance_list_instance = PaginatedClawInstanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedClawInstanceList.to_json())

# convert the object into a dict
paginated_claw_instance_list_dict = paginated_claw_instance_list_instance.to_dict()
# create an instance of PaginatedClawInstanceList from a dict
paginated_claw_instance_list_from_dict = PaginatedClawInstanceList.from_dict(paginated_claw_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


