# PlatformRevenueSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_volume** | **decimal.Decimal** |  | 
**sales_count** | **int** |  | 
**currency** | **str** |  | 

## Example

```python
from iblai.models.platform_revenue_summary import PlatformRevenueSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformRevenueSummary from a JSON string
platform_revenue_summary_instance = PlatformRevenueSummary.from_json(json)
# print the JSON string representation of the object
print(PlatformRevenueSummary.to_json())

# convert the object into a dict
platform_revenue_summary_dict = platform_revenue_summary_instance.to_dict()
# create an instance of PlatformRevenueSummary from a dict
platform_revenue_summary_from_dict = PlatformRevenueSummary.from_dict(platform_revenue_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


