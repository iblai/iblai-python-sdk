# NetRevenueOverTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FloatOverTime]**](FloatOverTime.md) |  | [optional] 
**total** | **float** | Grand total of all data | [optional] 

## Example

```python
from iblai.models.net_revenue_over_time import NetRevenueOverTime

# TODO update the JSON string below
json = "{}"
# create an instance of NetRevenueOverTime from a JSON string
net_revenue_over_time_instance = NetRevenueOverTime.from_json(json)
# print the JSON string representation of the object
print(NetRevenueOverTime.to_json())

# convert the object into a dict
net_revenue_over_time_dict = net_revenue_over_time_instance.to_dict()
# create an instance of NetRevenueOverTime from a dict
net_revenue_over_time_from_dict = NetRevenueOverTime.from_dict(net_revenue_over_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


