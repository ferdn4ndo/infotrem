#!/usr/bin/env node

const apiUrl = process.env.API_URL || 'http://localhost:8080'
const specUrl = `${apiUrl.replace(/\/$/, '')}/docs/swagger.json`

const expected = {
  '/health': ['get'],
  '/login': ['post'],
  '/register': ['post'],
  '/me': ['get', 'patch'],
  '/me/password': ['patch'],
  '/media': ['get', 'post'],
  '/media/{media_id}': ['get', 'patch', 'put', 'delete'],
  '/media/{media_id}/comments': ['get', 'post'],
  '/media/{media_id}/likes': ['get', 'post'],
  '/media/{media_id}/favorites': ['get', 'post'],
  '/albums': ['get', 'post'],
  '/albums/{album_id}': ['get', 'patch', 'put', 'delete'],
  '/albums/{album_id}/comments': ['get', 'post'],
  '/comments': ['get', 'post'],
  '/search': ['get'],
  '/map': ['get'],
  '/companies': ['get', 'post'],
  '/manufacturers': ['get', 'post'],
  '/locations': ['get', 'post'],
  '/paths': ['get', 'post'],
  '/routes': ['get', 'post'],
  '/rolling-stock': ['get', 'post'],
  '/users': ['get', 'post'],
  '/mail': ['get', 'post'],
}

const response = await fetch(specUrl)
if (!response.ok) {
  throw new Error(`Failed to fetch ${specUrl}: ${response.status} ${response.statusText}`)
}

const document = await response.json()
const paths = document.paths || {}
const failures = []

for (const [path, methods] of Object.entries(expected)) {
  if (!paths[path]) {
    failures.push(`Missing path ${path}`)
    continue
  }

  for (const method of methods) {
    if (!paths[path][method]) {
      failures.push(`Missing ${method.toUpperCase()} ${path}`)
    }
  }
}

if (failures.length > 0) {
  console.error(failures.join('\n'))
  process.exit(1)
}

console.log(`OpenAPI contract smoke passed for ${specUrl}`)
