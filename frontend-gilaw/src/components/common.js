import axios from "axios";
import dateFormat from "dateformat";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X_CSRFToken";
axios.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken');

  const endPoint = "http://localhost:8000/";


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export const formatD = (date) =>{
  return dateFormat(date, "dd/mm/yyyy hh:mm:ss");
}

export const get = async (url, data = null) => {
  return await axios.get(endPoint + url, data ? { params: data } : null);
};

export const post = async (url, data) => {
  return await axios.post(endPoint + url, data, {
    headers: {
      "Content-Type": "multipart/form-data",
    }});
};

export const put = async (url, data) => {
  return await axios.put(endPoint + url, data);
};

export const patch = async (url, data) => {
  return await axios.patch(endPoint + url, data);
};
