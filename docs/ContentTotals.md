# ContentTotals

Serializer for content summary totals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_learners** | **int** | Total number of learners | 
**total_enrollments** | **int** | Total number of enrollments | 
**total_time_spent** | **int** | Total time spent in seconds (courses only) | [optional] 
**courses** | **int** | Total number of courses | [optional] 
**active_courses** | **int** | Number of active courses | [optional] 
**platform_courses** | **int** | Number of platform-owned courses | [optional] 
**external_courses** | **int** | Number of external courses | [optional] 
**programs** | **int** | Total number of programs | [optional] 
**active_programs** | **int** | Number of active programs | [optional] 
**platform_programs** | **int** | Number of platform-owned programs | [optional] 
**external_programs** | **int** | Number of external programs | [optional] 
**pathways** | **int** | Total number of pathways | [optional] 
**active_pathways** | **int** | Number of active pathways | [optional] 
**platform_pathways** | **int** | Number of platform-owned pathways | [optional] 
**external_pathways** | **int** | Number of external pathways | [optional] 
**skills** | **int** | Total number of skills | [optional] 
**active_skills** | **int** | Number of active skills | [optional] 
**platform_skills** | **int** | Number of platform-owned skills | [optional] 
**external_skills** | **int** | Number of external skills | [optional] 
**associated_courses** | **int** | Number of courses associated with skills | [optional] 
**learners_with_skills** | **int** | Number of learners with skills | [optional] 

## Example

```python
from iblai.models.content_totals import ContentTotals

# TODO update the JSON string below
json = "{}"
# create an instance of ContentTotals from a JSON string
content_totals_instance = ContentTotals.from_json(json)
# print the JSON string representation of the object
print(ContentTotals.to_json())

# convert the object into a dict
content_totals_dict = content_totals_instance.to_dict()
# create an instance of ContentTotals from a dict
content_totals_from_dict = ContentTotals.from_dict(content_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


