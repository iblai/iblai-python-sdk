# ReportData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Report Name | [optional] 
**description** | **str** | Report Description | [optional] 
**report_name** | **str** | Report slug | [optional] 
**icon** | **str** |  | [optional] 
**extra_query_params** | **List[object]** | Extra parameters to be passed to the report create view, e.g learner_id | [optional] 
**result_columns** | **List[object]** | Columns to be available in the report | [optional] 
**status** | [**ReportStatus**](ReportStatus.md) | Report Status if any available | [optional] 

## Example

```python
from iblai.models.report_data import ReportData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportData from a JSON string
report_data_instance = ReportData.from_json(json)
# print the JSON string representation of the object
print(ReportData.to_json())

# convert the object into a dict
report_data_dict = report_data_instance.to_dict()
# create an instance of ReportData from a dict
report_data_from_dict = ReportData.from_dict(report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


