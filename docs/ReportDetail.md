# ReportDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportData**](ReportData.md) |  | 

## Example

```python
from iblai.models.report_detail import ReportDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDetail from a JSON string
report_detail_instance = ReportDetail.from_json(json)
# print the JSON string representation of the object
print(ReportDetail.to_json())

# convert the object into a dict
report_detail_dict = report_detail_instance.to_dict()
# create an instance of ReportDetail from a dict
report_detail_from_dict = ReportDetail.from_dict(report_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


