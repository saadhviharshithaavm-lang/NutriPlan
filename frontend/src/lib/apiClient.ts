import axios from 'axios'

/**
 * Single shared Axios instance for every API call in the app, so the base
 * URL and error shape are defined in exactly one place rather than scattered
 * across components (master prompt Section 8).
 *
 * In development, requests to `/api/...` are forwarded to the FastAPI server
 * by the Vite dev proxy (see vite.config.ts); no absolute URL is needed.
 */
export const apiClient = axios.create({
  baseURL: '/api/v1',
  timeout: 10_000,
})
