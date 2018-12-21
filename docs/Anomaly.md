# Anomaly

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | model for this anomaly | [optional] 
**id** | **str** | unique id that defines this anomaly | [optional] 
**row** | **int** | row number for this anomaly | 
**customer** | **str** | id of the customer to which this anomaly belongs | [optional] 
**deleted** | **bool** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**dashboard_id** | **str** | dashboard id for this anomaly | 
**chart_hash** | **str** | chart hash(as unique identifier) for this anomaly | 
**end_ms** | **int** | endMs for this anomaly | 
**param_hash** | **str** | param hash for this anomaly | 
**start_ms** | **int** | startMs for this anomaly | 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**query_hash** | **str** | query hash for this anomaly | 
**section** | **int** | section number for this anomaly | 
**col** | **int** | column number for this anomaly | 
**image_link** | **str** | image link for this anomaly | [optional] 
**original_stripes** | [**list[Stripe]**](Stripe.md) | list of originalStripe belongs to this anomaly | [optional] 
**_query_params** | **dict(str, str)** | map of query params belongs to this anomaly | 
**updated_ms** | **int** | updateMs for this anomaly | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


