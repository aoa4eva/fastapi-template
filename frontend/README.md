# Frontend Directory

This directory is a placeholder for a separate Node.js frontend (React, Vue, Svelte, etc.).

## Options for Frontend

### Option 1: Vanilla JavaScript (Current Setup)
- Use the `/static` and `/templates` directories
- No build step required
- FastAPI serves static files and Jinja2 templates
- Good for simple applications

### Option 2: Modern JavaScript Framework
Set up a framework in this directory:

#### React + Vite
```bash
cd frontend
npm create vite@latest . -- --template react-ts
npm install
npm run dev
```

#### Vue + Vite
```bash
cd frontend
npm create vite@latest . -- --template vue-ts
npm install
npm run dev
```

#### Next.js
```bash
cd frontend
npx create-next-app@latest .
npm run dev
```

### Option 3: Hybrid Approach
- Use Jinja2 templates for server-rendered pages
- Use `/static` for vanilla JS enhancements
- Add a separate SPA for complex features

## Connecting Frontend to API

### Development
- Frontend dev server: `http://localhost:3000` (typical for React/Vue)
- API backend: `http://localhost:8000`
- Configure proxy in frontend dev server to avoid CORS issues

Example Vite config (`vite.config.js`):
```javascript
export default {
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
}
```

### Production
Build the frontend and serve it through FastAPI:
```python
# In main.py
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="frontend")
```

Or deploy frontend separately (Vercel, Netlify, etc.) and use FastAPI as API only.
