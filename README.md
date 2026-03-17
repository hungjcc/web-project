# Starter Web App

This project started as a plain HTML/CSS/JS app and is now upgraded to a Vite setup.

## Phase 2: Modern setup with Vite

Follow this in order.

### 1) Install Node.js (required for Vite)

Your machine currently does not have `node` and `npm` in PATH.

Install Node.js LTS from the official website:
https://nodejs.org

Then verify:

```bash
node --version
npm --version
```

### 2) Install project dependencies

From project root, run:

```bash
npm install
```

This installs `vite` from `package.json`.

### 3) Start development server

```bash
npm run dev
```

Vite will print a local URL, usually:
http://localhost:5173

### 4) Build for production

```bash
npm run build
```

Build output goes to `dist/`.

### 5) Preview production build locally

```bash
npm run preview
```

## New features added

The app now includes:

1. Theme toggle (light/dark) with saved preference via localStorage.
2. Live clock that updates every second.
3. Task list with add/remove and localStorage persistence.

You can test these features in both:

1. Development server (`npm run dev`)
2. Production preview (`npm run preview`)

## Helpful checks for production preview

If you are not sure which terminal is running production preview:

```bash
lsof -nP -iTCP:4173 -sTCP:LISTEN
```

Stop the preview server by PID (example):

```bash
kill 17230
```

Start preview again:

```bash
npm run preview
```

## Files added for Vite

1. `package.json` - npm scripts and Vite dependency.
2. `.gitignore` - ignores `node_modules` and build output.
3. `src/main.js` - app entry point used by Vite.
4. `src/style.css` - stylesheet imported by `src/main.js`.

## Files changed for Vite

1. `index.html` - now uses `<div id="app"></div>` and loads `/src/main.js` as a module.
2. `src/main.js` - now includes theme toggle, live clock, and task list logic.
3. `src/style.css` - now includes styling for cards, task UI, and dark theme.

## Note about old Phase 1 files

`app.js` and `styles.css` are from the original plain setup and are no longer used by Vite.
