# PaginatedClawModelProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ClawModelProvider]**](ClawModelProvider.md) |  | 

## Example

```python
from iblai.models.paginated_claw_model_provider_list import PaginatedClawModelProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClawModelProviderList from a JSON string
paginated_claw_model_provider_list_instance = PaginatedClawModelProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedClawModelProviderList.to_json())

# convert the object into a dict
paginated_claw_model_provider_list_dict = paginated_claw_model_provider_list_instance.to_dict()
# create an instance of PaginatedClawModelProviderList from a dict
paginated_claw_model_provider_list_from_dict = PaginatedClawModelProviderList.from_dict(paginated_claw_model_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


