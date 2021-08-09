# taxi-traffic
An algorithm to recognize, display, and predict highest areas of taxi demand in DC

### `taxi.ipynb`
clusters the 2019 data using the k-means algorithm for each month and prints out text files with the cluster dictionaries
### `taxi_predictions.ipynb`
takes the cluster dictionaries from taxi.ipynb and uses that data to predict the highest areas of taxi demand in future months
### `GMap.ipynb`
takes the data from taxi.ipynb and taxi_predictions.ipynb and plots them on the DC map
