import "./style.css";

const app = document.getElementById("app");

app.innerHTML = `
  <main class="container">
    <header class="row">
      <h1>My First Vite App</h1>
      <button id="themeBtn" class="secondary" type="button">Toggle theme</button>
    </header>

    <p id="message">App loaded by Vite.</p>
    <p class="clock">Time: <span id="clockValue">--:--:--</span></p>

    <section class="card">
      <h2>Quick Action</h2>
      <button id="btn" type="button">Click me</button>
    </section>

    <section class="card">
      <h2>Task List</h2>
      <form id="taskForm" class="row" autocomplete="off">
        <input id="taskInput" type="text" placeholder="Add a task" required />
        <button type="submit">Add</button>
      </form>
      <ul id="taskList"></ul>
    </section>
  </main>
`;

const message = document.getElementById("message");
const button = document.getElementById("btn");
const themeBtn = document.getElementById("themeBtn");
const clockValue = document.getElementById("clockValue");
const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

const TASKS_KEY = "starter-vite-tasks";
const THEME_KEY = "starter-vite-theme";

button.addEventListener("click", () => {
  message.textContent = "Nice. Your Vite app is interactive.";
});

function renderClock() {
  const now = new Date();
  clockValue.textContent = now.toLocaleTimeString();
}

function loadTheme() {
  const savedTheme = localStorage.getItem(THEME_KEY);
  if (savedTheme === "dark") {
    document.body.classList.add("dark");
  }
}

themeBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  const isDark = document.body.classList.contains("dark");
  localStorage.setItem(THEME_KEY, isDark ? "dark" : "light");
});

function getTasks() {
  const stored = localStorage.getItem(TASKS_KEY);
  return stored ? JSON.parse(stored) : [];
}

function saveTasks(tasks) {
  localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
}

function renderTasks() {
  const tasks = getTasks();
  taskList.innerHTML = "";

  for (const task of tasks) {
    const item = document.createElement("li");
    item.className = "task-item";

    const text = document.createElement("span");
    text.textContent = task;

    const removeBtn = document.createElement("button");
    removeBtn.type = "button";
    removeBtn.className = "secondary";
    removeBtn.textContent = "Remove";
    removeBtn.addEventListener("click", () => {
      const nextTasks = getTasks().filter((t) => t !== task);
      saveTasks(nextTasks);
      renderTasks();
    });

    item.append(text, removeBtn);
    taskList.append(item);
  }
}

taskForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const value = taskInput.value.trim();
  if (!value) return;

  const tasks = getTasks();
  tasks.push(value);
  saveTasks(tasks);
  taskInput.value = "";
  renderTasks();
});

loadTheme();
renderClock();
setInterval(renderClock, 1000);
renderTasks();
