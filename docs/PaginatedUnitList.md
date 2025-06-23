# PaginatedUnitList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Unit]**](Unit.md) |  | 

## Example

```python
from iblai.models.paginated_unit_list import PaginatedUnitList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUnitList from a JSON string
paginated_unit_list_instance = PaginatedUnitList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUnitList.to_json())

# convert the object into a dict
paginated_unit_list_dict = paginated_unit_list_instance.to_dict()
# create an instance of PaginatedUnitList from a dict
paginated_unit_list_from_dict = PaginatedUnitList.from_dict(paginated_unit_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


