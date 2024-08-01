# PaginatedTrainingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Training]**](Training.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_training_list import PaginatedTrainingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTrainingList from a JSON string
paginated_training_list_instance = PaginatedTrainingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTrainingList.to_json())

# convert the object into a dict
paginated_training_list_dict = paginated_training_list_instance.to_dict()
# create an instance of PaginatedTrainingList from a dict
paginated_training_list_from_dict = PaginatedTrainingList.from_dict(paginated_training_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


