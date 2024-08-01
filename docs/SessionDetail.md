# SessionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**previous** | **str** |  | 
**next** | **str** |  | 
**results** | **List[str]** |  | 

## Example

```python
from iblai.models.session_detail import SessionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SessionDetail from a JSON string
session_detail_instance = SessionDetail.from_json(json)
# print the JSON string representation of the object
print(SessionDetail.to_json())

# convert the object into a dict
session_detail_dict = session_detail_instance.to_dict()
# create an instance of SessionDetail from a dict
session_detail_from_dict = SessionDetail.from_dict(session_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


