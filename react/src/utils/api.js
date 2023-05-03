import axios from "axios";
export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  headers: {
    "Content-Type": "application/json",
  },
});

export const setAuthToken = (csrftoken) => {
  if (csrftoken) {
    api.defaults.headers.common["X-CSRFToken"] = "JWT " + csrftoken;
  } else {
    delete api.defaults.headers.common["X-CSRFToken"];
  }
};