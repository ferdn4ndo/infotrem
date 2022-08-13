import { types } from "mobx-state-tree";

const MetricData = types
  .model({
    syntheticLocation: types.string,
    timestamp: types.number,
    value: types.number
  });

export default MetricData;
