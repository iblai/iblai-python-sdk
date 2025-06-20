# NewPerLearnerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NewPerLearnerListData]**](NewPerLearnerListData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.new_per_learner_list import NewPerLearnerList

# TODO update the JSON string below
json = "{}"
# create an instance of NewPerLearnerList from a JSON string
new_per_learner_list_instance = NewPerLearnerList.from_json(json)
# print the JSON string representation of the object
print(NewPerLearnerList.to_json())

# convert the object into a dict
new_per_learner_list_dict = new_per_learner_list_instance.to_dict()
# create an instance of NewPerLearnerList from a dict
new_per_learner_list_from_dict = NewPerLearnerList.from_dict(new_per_learner_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


