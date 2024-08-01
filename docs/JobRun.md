# JobRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**session** | **str** |  | 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**steps** | [**List[Step]**](Step.md) |  | 

## Example

```python
from iblai.models.job_run import JobRun

# TODO update the JSON string below
json = "{}"
# create an instance of JobRun from a JSON string
job_run_instance = JobRun.from_json(json)
# print the JSON string representation of the object
print(JobRun.to_json())

# convert the object into a dict
job_run_dict = job_run_instance.to_dict()
# create an instance of JobRun from a dict
job_run_from_dict = JobRun.from_dict(job_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


