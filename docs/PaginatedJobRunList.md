# PaginatedJobRunList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[JobRun]**](JobRun.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_job_run_list import PaginatedJobRunList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedJobRunList from a JSON string
paginated_job_run_list_instance = PaginatedJobRunList.from_json(json)
# print the JSON string representation of the object
print(PaginatedJobRunList.to_json())

# convert the object into a dict
paginated_job_run_list_dict = paginated_job_run_list_instance.to_dict()
# create an instance of PaginatedJobRunList from a dict
paginated_job_run_list_from_dict = PaginatedJobRunList.from_dict(paginated_job_run_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


