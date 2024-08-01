# CheckDocumentTrainingStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the training | 
**message** | **str** | Message of the training | 

## Example

```python
from iblai.models.check_document_training_status import CheckDocumentTrainingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDocumentTrainingStatus from a JSON string
check_document_training_status_instance = CheckDocumentTrainingStatus.from_json(json)
# print the JSON string representation of the object
print(CheckDocumentTrainingStatus.to_json())

# convert the object into a dict
check_document_training_status_dict = check_document_training_status_instance.to_dict()
# create an instance of CheckDocumentTrainingStatus from a dict
check_document_training_status_from_dict = CheckDocumentTrainingStatus.from_dict(check_document_training_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


