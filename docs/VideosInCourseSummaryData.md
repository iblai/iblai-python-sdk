# VideosInCourseSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Chapter name | 
**id** | **str** | Chapter Id | 
**subsections** | [**List[VideosWatchedSubSection]**](VideosWatchedSubSection.md) |  | [optional] 

## Example

```python
from iblai.models.videos_in_course_summary_data import VideosInCourseSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of VideosInCourseSummaryData from a JSON string
videos_in_course_summary_data_instance = VideosInCourseSummaryData.from_json(json)
# print the JSON string representation of the object
print(VideosInCourseSummaryData.to_json())

# convert the object into a dict
videos_in_course_summary_data_dict = videos_in_course_summary_data_instance.to_dict()
# create an instance of VideosInCourseSummaryData from a dict
videos_in_course_summary_data_from_dict = VideosInCourseSummaryData.from_dict(videos_in_course_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


