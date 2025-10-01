# ContentAverages

Serializer for content summary averages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_rate** | **float** | Average completion rate percentage | [optional] 
**average_rating** | **float** | Average rating | [optional] 
**enrollments_per_course** | **float** | Average enrollments per course | [optional] 
**enrollments_per_program** | **float** | Average enrollments per program | [optional] 
**enrollments_per_pathway** | **float** | Average enrollments per pathway | [optional] 
**courses_per_skill** | **float** | Average courses per skill | [optional] 
**time_per_learner** | **float** | Average time spent per learner in seconds (courses only) | [optional] 

## Example

```python
from iblai.models.content_averages import ContentAverages

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAverages from a JSON string
content_averages_instance = ContentAverages.from_json(json)
# print the JSON string representation of the object
print(ContentAverages.to_json())

# convert the object into a dict
content_averages_dict = content_averages_instance.to_dict()
# create an instance of ContentAverages from a dict
content_averages_from_dict = ContentAverages.from_dict(content_averages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


