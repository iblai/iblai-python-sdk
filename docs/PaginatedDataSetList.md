# PaginatedDataSetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DataSet]**](DataSet.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_data_set_list import PaginatedDataSetList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDataSetList from a JSON string
paginated_data_set_list_instance = PaginatedDataSetList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDataSetList.to_json())

# convert the object into a dict
paginated_data_set_list_dict = paginated_data_set_list_instance.to_dict()
# create an instance of PaginatedDataSetList from a dict
paginated_data_set_list_from_dict = PaginatedDataSetList.from_dict(paginated_data_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


