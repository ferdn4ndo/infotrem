import MetricStore from './metricStore';

export function createStore() {
  const store = MetricStore.create({
    monitors: {},
    loadingMonitors: true
  });

  return store;
}
