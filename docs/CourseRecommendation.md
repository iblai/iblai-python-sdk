# CourseRecommendation

Individual course recommendation with reasoning.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The ID of the recommended course | 
**course_title** | **str** | The title of the recommended course | 
**reason** | **str** | AI-generated explanation for why this course is recommended | 
**domain** | **str** | Course domain/subject area | [optional] 
**difficulty_level** | **str** | Course difficulty level | [optional] 
**estimated_hours** | **float** | Estimated hours to complete | [optional] 
**confidence_score** | **float** | AI confidence in this recommendation (0-1) | [optional] 
**platform_key** | **str** | Platform/tenant key this course belongs to (extracted from course_id or metadata) | [optional] 
**description** | **str** | Course description (priority: description &gt; short_description &gt; overview with HTML stripped) | [optional] 
**short_description** | **str** | Course short description from edx_data | [optional] 

## Example

```python
from iblai.models.course_recommendation import CourseRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of CourseRecommendation from a JSON string
course_recommendation_instance = CourseRecommendation.from_json(json)
# print the JSON string representation of the object
print(CourseRecommendation.to_json())

# convert the object into a dict
course_recommendation_dict = course_recommendation_instance.to_dict()
# create an instance of CourseRecommendation from a dict
course_recommendation_from_dict = CourseRecommendation.from_dict(course_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


