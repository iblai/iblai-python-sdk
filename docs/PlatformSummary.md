# PlatformSummary

Serializer for platform summary data (cross-platform view).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollments** | **int** |  | 
**programs** | **int** |  | 
**pathways** | **int** |  | 
**resources** | **int** |  | 
**reported_skills** | **int** |  | 
**desired_skills** | **int** |  | 
**assigned_skills** | **int** |  | 
**total_skills** | **int** |  | 
**credentials** | **int** |  | 
**points** | **float** |  | 
**first_activity** | **datetime** |  | 
**last_activity** | **datetime** |  | 
**total_time_spent_seconds** | **int** | Total time spent | 
**top_content** | [**TopContent**](TopContent.md) | Course with most time spent | 

## Example

```python
from iblai.models.platform_summary import PlatformSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSummary from a JSON string
platform_summary_instance = PlatformSummary.from_json(json)
# print the JSON string representation of the object
print(PlatformSummary.to_json())

# convert the object into a dict
platform_summary_dict = platform_summary_instance.to_dict()
# create an instance of PlatformSummary from a dict
platform_summary_from_dict = PlatformSummary.from_dict(platform_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


