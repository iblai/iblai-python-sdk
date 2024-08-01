# ReportStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | Used to download the report | [optional] 
**report_name** | **str** | Report slug, this is passed when calling the create report endpoint | [optional] 
**state** | [**StateEnum**](StateEnum.md) | Report States  * &#x60;pending&#x60; - Pending * &#x60;running&#x60; - Running * &#x60;accumulating&#x60; - Accumulating * &#x60;processing&#x60; - Processing * &#x60;storing&#x60; - Storing * &#x60;completed&#x60; - Completed * &#x60;cancelled&#x60; - Cancelled * &#x60;error&#x60; - Error * &#x60;expired&#x60; - Expired | [optional] 
**started_on** | **str** | Report request timestamp (ISO 8601) | [optional] 
**owner** | **str** | Report Owner | [optional] 
**expires** | **str** | When report would expire and not available for download anymore | [optional] 
**url** | **str** | Download link for report when available | [optional] 

## Example

```python
from iblai.models.report_status import ReportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ReportStatus from a JSON string
report_status_instance = ReportStatus.from_json(json)
# print the JSON string representation of the object
print(ReportStatus.to_json())

# convert the object into a dict
report_status_dict = report_status_instance.to_dict()
# create an instance of ReportStatus from a dict
report_status_from_dict = ReportStatus.from_dict(report_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


