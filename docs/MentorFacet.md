# MentorFacet

Serializer for mentor facets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of mentors in this facet | 
**terms** | **Dict[str, object]** | Terms and their counts in this facet | 
**other** | **int** | Count of mentors not in any term | 

## Example

```python
from iblai.models.mentor_facet import MentorFacet

# TODO update the JSON string below
json = "{}"
# create an instance of MentorFacet from a JSON string
mentor_facet_instance = MentorFacet.from_json(json)
# print the JSON string representation of the object
print(MentorFacet.to_json())

# convert the object into a dict
mentor_facet_dict = mentor_facet_instance.to_dict()
# create an instance of MentorFacet from a dict
mentor_facet_from_dict = MentorFacet.from_dict(mentor_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


