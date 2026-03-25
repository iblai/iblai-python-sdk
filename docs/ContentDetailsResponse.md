# ContentDetailsResponse

Serializer for the content details API response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_info** | [**ContentDetailsContentInfo**](ContentDetailsContentInfo.md) |  | 
**summary** | [**ContentDetailsSummary**](ContentDetailsSummary.md) |  | 
**pagination** | [**ContentDetailsPagination**](ContentDetailsPagination.md) |  | 
**learners** | [**List[ContentDetailsLearner]**](ContentDetailsLearner.md) |  | 

## Example

```python
from iblai.models.content_details_response import ContentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsResponse from a JSON string
content_details_response_instance = ContentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsResponse.to_json())

# convert the object into a dict
content_details_response_dict = content_details_response_instance.to_dict()
# create an instance of ContentDetailsResponse from a dict
content_details_response_from_dict = ContentDetailsResponse.from_dict(content_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


