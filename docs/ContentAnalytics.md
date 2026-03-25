# ContentAnalytics

Serializer for individual content item analytics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollments** | **int** | Total enrollments for this item | 
**active_enrollments** | **int** | Active enrollments for this item | 
**completion_rate** | **float** | Completion rate percentage | 
**avg_rating** | **float** | Average rating | [optional] 
**rating_count** | **int** | Number of ratings | [optional] 
**associated_courses** | **int** | Associated courses (for skills) | [optional] 
**learners_count** | **int** | Number of learners (for skills) | [optional] 
**total_time_spent** | **int** | Total time spent on this content in seconds (courses only) | [optional] 
**avg_time_per_learner** | **float** | Average time spent per learner in seconds (courses only) | [optional] 

## Example

```python
from iblai.models.content_analytics import ContentAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalytics from a JSON string
content_analytics_instance = ContentAnalytics.from_json(json)
# print the JSON string representation of the object
print(ContentAnalytics.to_json())

# convert the object into a dict
content_analytics_dict = content_analytics_instance.to_dict()
# create an instance of ContentAnalytics from a dict
content_analytics_from_dict = ContentAnalytics.from_dict(content_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


