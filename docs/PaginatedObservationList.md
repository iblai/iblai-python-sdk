# PaginatedObservationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Observation]**](Observation.md) |  | 

## Example

```python
from iblai.models.paginated_observation_list import PaginatedObservationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedObservationList from a JSON string
paginated_observation_list_instance = PaginatedObservationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedObservationList.to_json())

# convert the object into a dict
paginated_observation_list_dict = paginated_observation_list_instance.to_dict()
# create an instance of PaginatedObservationList from a dict
paginated_observation_list_from_dict = PaginatedObservationList.from_dict(paginated_observation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


