import { types } from "mobx-state-tree";
import MetricData from './MetricData';

const MetricModel = types
  .model({
    totalCount: types.integer,
    nextPageKey: types.maybeNull(types.string),
    resolution: types.string,
    data: types.array(MetricData)
  })
  .actions(self => ({
    addData(data) {
      const metricData = MetricData.create({
        syntheticLocation: data.syntheticLocation,
        timestamp: data.timestamp,
        value: data.value
      });
      self.data.push(metricData);
    }
  }));

export default MetricModel;
