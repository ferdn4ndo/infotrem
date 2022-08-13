import { flow, types } from "mobx-state-tree";
import MetricModel from './MetricModel';
import { getMonitorMetrics } from '../../api/dynatrace';

const MonitorModel = types
  .model({
    id: types.string,
    name: types.string,
    type: types.enumeration('Type', ['BROWSER', 'HTTP']),
    enabled: types.boolean,
    metrics: types.maybeNull(MetricModel),
    loadingMetrics: types.maybeNull(types.boolean)
  })
  .actions(self => ({
    addMetricFromJsonResponse(jsonResponse) {
      self.metrics = MetricModel.create({
        totalCount: jsonResponse.totalCount,
        nextPageKey: jsonResponse.nextPageKey,
        resolution: jsonResponse.resolution,
        data: []
      });
      if (jsonResponse.result && jsonResponse.result[0].data) {
        jsonResponse.result[0].data.forEach(data => {
          self.metrics.addData({
            syntheticLocation: data.dimensions[1],
            timestamp: data.timestamps[0],
            value: data.values[0]
          });
        });
      }
    },
    fetchMetrics: flow(function* fetchMetrics() {
      self.loadingMetrics = true;
      yield getMonitorMetrics(self.id)
        .then((response) => {
          self.addMetricFromJsonResponse(response.data);
        });
      self.loadingMetrics = false;
    })
  }));

export default MonitorModel;
