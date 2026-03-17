const message = document.getElementById("message");
const button = document.getElementById("btn");

message.textContent = "App loaded successfully.";

button.addEventListener("click", () => {
  message.textContent = "Nice. You clicked the button.";
});
