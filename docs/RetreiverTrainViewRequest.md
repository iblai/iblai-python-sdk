# RetreiverTrainViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathway** | **str** | Pathway for document to be trained in | 
**url** | **str** | Url of the document to be trained | 

## Example

```python
from iblai.models.retreiver_train_view_request import RetreiverTrainViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetreiverTrainViewRequest from a JSON string
retreiver_train_view_request_instance = RetreiverTrainViewRequest.from_json(json)
# print the JSON string representation of the object
print(RetreiverTrainViewRequest.to_json())

# convert the object into a dict
retreiver_train_view_request_dict = retreiver_train_view_request_instance.to_dict()
# create an instance of RetreiverTrainViewRequest from a dict
retreiver_train_view_request_from_dict = RetreiverTrainViewRequest.from_dict(retreiver_train_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


