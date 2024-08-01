# RecommendCourseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courses** | **List[object]** |  | 

## Example

```python
from iblai.models.recommend_course_response import RecommendCourseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendCourseResponse from a JSON string
recommend_course_response_instance = RecommendCourseResponse.from_json(json)
# print the JSON string representation of the object
print(RecommendCourseResponse.to_json())

# convert the object into a dict
recommend_course_response_dict = recommend_course_response_instance.to_dict()
# create an instance of RecommendCourseResponse from a dict
recommend_course_response_from_dict = RecommendCourseResponse.from_dict(recommend_course_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


