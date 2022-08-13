import ApiClient from './ApiClient';

export function getAvailableMonitors() {
  const route = ApiClient.apiUrl + '/health?tag=SYN_Prod&enabled=true&type=HTTP';
  return ApiClient.client.get(route)
}

export function getMonitorMetrics(monitorId) {
  const route = ApiClient.apiUrl + `/health?metricSelector=builtin:synthetic.http.availability.location.total:avg:filter(eq("dt.entity.http_check","${monitorId}"))&resolution=1d`;
  return ApiClient.client.get(route)
}
