const apiUrl = "http://10.0.0.141:5000/api/leds";

export function changeLed(body) {
  body = JSON.stringify(body);
  fetch(apiUrl, {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body,
  });
}
