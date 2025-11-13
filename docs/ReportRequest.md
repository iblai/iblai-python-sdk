# ReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** | Report slug, this is passed when calling the create report endpoint | [optional] 
**start_date** | **date** | Start date for the report | [optional] 
**end_date** | **date** | End date for the report | [optional] 
**mentor** | **str** | Mentor ID for the report (Only for mentor reports) | [optional] 
**course_id** | **str** | Course ID for the report (Only for course reports) | [optional] 
**query** | **str** |  Advanced Query to run the report, supports SQL Like queries. This runs against the final result after all filters are applied.  e.g For date type filtering  date_joined &gt; &#39;2021-01-01&#39;   See https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query          | [optional] 

## Example

```python
from iblai.models.report_request import ReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportRequest from a JSON string
report_request_instance = ReportRequest.from_json(json)
# print the JSON string representation of the object
print(ReportRequest.to_json())

# convert the object into a dict
report_request_dict = report_request_instance.to_dict()
# create an instance of ReportRequest from a dict
report_request_from_dict = ReportRequest.from_dict(report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


