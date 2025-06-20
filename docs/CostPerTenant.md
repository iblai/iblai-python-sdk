# CostPerTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | 
**total_cost** | **float** |  | 
**model_costs** | [**List[ModelCost]**](ModelCost.md) |  | 

## Example

```python
from iblai.models.cost_per_tenant import CostPerTenant

# TODO update the JSON string below
json = "{}"
# create an instance of CostPerTenant from a JSON string
cost_per_tenant_instance = CostPerTenant.from_json(json)
# print the JSON string representation of the object
print(CostPerTenant.to_json())

# convert the object into a dict
cost_per_tenant_dict = cost_per_tenant_instance.to_dict()
# create an instance of CostPerTenant from a dict
cost_per_tenant_from_dict = CostPerTenant.from_dict(cost_per_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


