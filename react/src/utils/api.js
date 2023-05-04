import axios from "axios";
export const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
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