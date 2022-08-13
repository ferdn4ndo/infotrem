import { flow, types } from 'mobx-state-tree';
import MonitorModel from './models/MonitorModel';
import { getAvailableMonitors } from '../api/dynatrace';

const MetricStore = types.model('GameStore', {
  monitors: types.map(MonitorModel),
  loadingMonitors: types.maybeNull(types.boolean)
})
.actions(self => ({
  addMonitor(monitor) {
    self.monitors.set(monitor.id, monitor)
  },
  fetchMonitors: flow(function* fetchMonitors() { // <- note the star, this a generator function!
    self.loadingMonitors = true;
    // ... yield can be used in async/await style
    yield getAvailableMonitors()
      .then(response => {
        console.log(response);
        response.data.monitors.sort((a, b) => (a.name > b.name ? 1 : -1));
        response.data.monitors.forEach((monitor) => {
          self.addMonitor({
            id: monitor.entityId,
            name: monitor.name,
            type: monitor.type,
            enabled: monitor.enabled,
            metrics: null,
            loadingMetrics: null
          })
        });
      });
    self.loadingMonitors = false;
  })
}));

export default MetricStore;
