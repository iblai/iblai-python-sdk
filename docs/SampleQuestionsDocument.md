# SampleQuestionsDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [optional] 
**document** | **str** |  | 
**status** | [**SampleQuestionsDocumentStatusEnum**](SampleQuestionsDocumentStatusEnum.md) |  | [readonly] 
**difficulty** | **int** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**platform** | **int** |  | [readonly] 

## Example

```python
from iblai.models.sample_questions_document import SampleQuestionsDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SampleQuestionsDocument from a JSON string
sample_questions_document_instance = SampleQuestionsDocument.from_json(json)
# print the JSON string representation of the object
print(SampleQuestionsDocument.to_json())

# convert the object into a dict
sample_questions_document_dict = sample_questions_document_instance.to_dict()
# create an instance of SampleQuestionsDocument from a dict
sample_questions_document_from_dict = SampleQuestionsDocument.from_dict(sample_questions_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


