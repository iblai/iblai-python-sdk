# FinanceDetailsResponse

Serializer for /financial/details responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**limit** | **int** |  | 
**total_pages** | **int** |  | 
**total_records** | **int** |  | 
**rows** | **List[Dict[str, object]]** |  | 
**total_cost** | **float** |  | [optional] 
**metrics** | [**List[MetricInfo]**](MetricInfo.md) |  | [optional] 

## Example

```python
from iblai.models.finance_details_response import FinanceDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinanceDetailsResponse from a JSON string
finance_details_response_instance = FinanceDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(FinanceDetailsResponse.to_json())

# convert the object into a dict
finance_details_response_dict = finance_details_response_instance.to_dict()
# create an instance of FinanceDetailsResponse from a dict
finance_details_response_from_dict = FinanceDetailsResponse.from_dict(finance_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


