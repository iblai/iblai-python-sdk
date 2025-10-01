# ComparisonInfo

Comparison period information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_period_count** | **int** | Number of days in comparison period | [optional] 
**previous_period_value** | **float** | Cost value for comparison period | [optional] 
**comparison_start** | **str** | Start date of comparison period | [optional] 
**comparison_end** | **str** | End date of comparison period | [optional] 
**comparison_days** | **int** | Number of comparison days | [optional] 
**recent_period_value** | **float** | Cost value for current period | [optional] 

## Example

```python
from iblai.models.comparison_info import ComparisonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonInfo from a JSON string
comparison_info_instance = ComparisonInfo.from_json(json)
# print the JSON string representation of the object
print(ComparisonInfo.to_json())

# convert the object into a dict
comparison_info_dict = comparison_info_instance.to_dict()
# create an instance of ComparisonInfo from a dict
comparison_info_from_dict = ComparisonInfo.from_dict(comparison_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


