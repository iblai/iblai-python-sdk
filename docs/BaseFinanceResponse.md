# BaseFinanceResponse

Base response for all finance metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | The metric type that was requested | 
**filters** | [**FinanceFilters**](FinanceFilters.md) | Applied filters for this query | 
**value** | **float** | Primary metric value (cost in USD) | 
**percentage_change** | **float** | Percentage change vs comparison period (null if no comparison) | 
**overtime** | [**List[OvertimeData]**](OvertimeData.md) | Time series data for overtime visualization | 
**period_info** | [**PeriodInfo**](PeriodInfo.md) | Information about the analysis period | 
**comparison_info** | [**ComparisonInfo**](ComparisonInfo.md) | Information about comparison period (empty if no comparison) | 

## Example

```python
from iblai.models.base_finance_response import BaseFinanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseFinanceResponse from a JSON string
base_finance_response_instance = BaseFinanceResponse.from_json(json)
# print the JSON string representation of the object
print(BaseFinanceResponse.to_json())

# convert the object into a dict
base_finance_response_dict = base_finance_response_instance.to_dict()
# create an instance of BaseFinanceResponse from a dict
base_finance_response_from_dict = BaseFinanceResponse.from_dict(base_finance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


