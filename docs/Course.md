# Course


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The edX course ID string for the course. | [readonly] 
**name** | **str** | The display name of the course. (Should match edX) | [readonly] 
**slug** | **str** | An additional unique slug field. (Optional) | [readonly] 
**org** | **str** |  | [optional] 

## Example

```python
from iblai.models.course import Course

# TODO update the JSON string below
json = "{}"
# create an instance of Course from a JSON string
course_instance = Course.from_json(json)
# print the JSON string representation of the object
print(Course.to_json())

# convert the object into a dict
course_dict = course_instance.to_dict()
# create an instance of Course from a dict
course_from_dict = Course.from_dict(course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


