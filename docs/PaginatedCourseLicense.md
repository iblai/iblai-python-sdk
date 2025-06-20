# PaginatedCourseLicense

Response serializer for paginated course license list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseLicenseDetail]**](CourseLicenseDetail.md) | List of course licenses | 

## Example

```python
from iblai.models.paginated_course_license import PaginatedCourseLicense

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseLicense from a JSON string
paginated_course_license_instance = PaginatedCourseLicense.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseLicense.to_json())

# convert the object into a dict
paginated_course_license_dict = paginated_course_license_instance.to_dict()
# create an instance of PaginatedCourseLicense from a dict
paginated_course_license_from_dict = PaginatedCourseLicense.from_dict(paginated_course_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


