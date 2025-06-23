# NewPerLearnerListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**user_id** | **int** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**courses_enrolled** | **int** |  | 
**courses_completed** | **int** |  | 
**time_spent** | **str** |  | 
**pathways_assigned** | **int** |  | 
**pathways_completed** | **int** |  | 
**certificates_earned** | **int** |  | 
**assessments_passed** | **int** |  | 
**skills_earned** | **int** |  | 
**skills_points** | **int** |  | 
**last_login** | **str** |  | 
**location** | **str** |  | 

## Example

```python
from iblai.models.new_per_learner_list_data import NewPerLearnerListData

# TODO update the JSON string below
json = "{}"
# create an instance of NewPerLearnerListData from a JSON string
new_per_learner_list_data_instance = NewPerLearnerListData.from_json(json)
# print the JSON string representation of the object
print(NewPerLearnerListData.to_json())

# convert the object into a dict
new_per_learner_list_data_dict = new_per_learner_list_data_instance.to_dict()
# create an instance of NewPerLearnerListData from a dict
new_per_learner_list_data_from_dict = NewPerLearnerListData.from_dict(new_per_learner_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


