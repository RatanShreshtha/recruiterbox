import axios from "axios";
import { apis, apiTimeout } from "./config";

class APIService {
  constructor(host, port) {
    this.instance = axios.create({
      baseURL: `${host}:${port}`,
      timeout: apiTimeout
    });
  }

  get(endpoint, options) {
    return this.instance.get(endpoint, options);
  }

  post(endpoint, data, options) {
    return this.instance.post(endpoint, data, options);
  }

  patch(endpoint, data, options) {
    return this.instance.patch(endpoint, data, options);
  }

  delete(endpoint, data, options) {
    return this.instance.delete(endpoint, data, options);
  }
}

const host = apis["baseURL"];
const port = apis["port"];

export const apiService = new APIService(host, port);
