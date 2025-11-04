
## 🐦 Live X — Real-time Feed App

This project demonstrates the integration of  **Uvicorn** ,  **Django** ,  **Celery** ,  **Redis** , **Django Channels** and **Docker** to build a **real-time, event-driven social feed system** — similar to a lightweight version of Twitter.

### 🚀 Key Features

* **Django + Uvicorn (ASGI):**

  High-performance asynchronous backend running with Uvicorn for real-time capabilities.
* **Django Channels (WebSockets):**

  Enables live updates — new posts and trending posts appear instantly without page reloads.
* **Celery + Redis:**

  Handles background tasks such as periodically broadcasting trending posts using Celery Beat and Redis as the message broker.
* **Caching (Redis):**

  Frequently accessed posts are cached for improved performance and reduced database load.
* **Responsive Frontend (Tailwind CSS):**

  A clean, minimal, and modern interface for live post feeds and trending updates.

### 💡 What This Project Shows

* How to broadcast **live feed updates** to all users via WebSockets.
* How to use **Celery Beat** for scheduled tasks (e.g., rotating trending posts).
* How to integrate **Redis caching** for optimal performance.
* How to run Django asynchronously using  **Uvicorn + Channels** .

| Command                                                                              | Description                                                                                                     |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `docker compose -f docker-compose.yml up -d`                                       | Builds (if needed) and starts all services in detached mode (background) using the `docker-compose.yml` file. |
| `docker compose -f docker-compose.yml ps`                                          | Lists all currently running containers defined in the compose file.                                             |
| `docker compose -f docker-compose.yml ps -a`                                       | Lists all containers (running + stopped) for the compose project.                                              |
| `docker compose -f docker-compose.yml exec django_project bash`                    | Opens an interactive shell (by default `/bin/sh` or `/bin/bash`) inside the `django_project` container.   |
| `docker compose -f docker-compose.yml stop`                                        | Stops all running containers without removing them (they can be restarted).                                     |
| `docker compose -f docker-compose.yml start`                                       | Restarts previously stopped containers without rebuilding or re-creating them.                                  |
| `docker compose -f docker-compose.yml down`                                        | Stops and removes all containers, networks, and temporary volumes created by the compose project.               |
| `docker exec -it redis_con redis-cli -u redis://rajesh:Hello123456@127.0.0.1:6379` | Opens an interactive shell inside the `redis_con` container.                                                  |

---

---

---

---
