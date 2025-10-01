# PaginatedDisclaimerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Disclaimer]**](Disclaimer.md) |  | 

## Example

```python
from iblai.models.paginated_disclaimer_list import PaginatedDisclaimerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDisclaimerList from a JSON string
paginated_disclaimer_list_instance = PaginatedDisclaimerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDisclaimerList.to_json())

# convert the object into a dict
paginated_disclaimer_list_dict = paginated_disclaimer_list_instance.to_dict()
# create an instance of PaginatedDisclaimerList from a dict
paginated_disclaimer_list_from_dict = PaginatedDisclaimerList.from_dict(paginated_disclaimer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


