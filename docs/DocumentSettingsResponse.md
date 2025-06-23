# DocumentSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retrain_interval_days** | **int** |  | [optional] 

## Example

```python
from iblai.models.document_settings_response import DocumentSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSettingsResponse from a JSON string
document_settings_response_instance = DocumentSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSettingsResponse.to_json())

# convert the object into a dict
document_settings_response_dict = document_settings_response_instance.to_dict()
# create an instance of DocumentSettingsResponse from a dict
document_settings_response_from_dict = DocumentSettingsResponse.from_dict(document_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


