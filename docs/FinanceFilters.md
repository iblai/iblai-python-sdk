# FinanceFilters

Applied filters for the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**granularity** | **str** |  | 
**comparison_days** | **int** |  | [optional] 
**platform_key** | **str** |  | [optional] 
**mentor_unique_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**llm_model** | **str** |  | [optional] 
**all_time** | **bool** |  | [optional] 

## Example

```python
from iblai.models.finance_filters import FinanceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of FinanceFilters from a JSON string
finance_filters_instance = FinanceFilters.from_json(json)
# print the JSON string representation of the object
print(FinanceFilters.to_json())

# convert the object into a dict
finance_filters_dict = finance_filters_instance.to_dict()
# create an instance of FinanceFilters from a dict
finance_filters_from_dict = FinanceFilters.from_dict(finance_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


