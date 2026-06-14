# 🎓 Internship & Job Tracking Dashboard

> **Assignment #4 — Tools & Techniques for DS**  
> University of Central Punjab — Faculty of IT & CS  
> Department of Applied Computing & Technologies

A full-stack Streamlit web application for tracking internship and job opportunities, powered by PostgreSQL and deployed with Docker Compose.

---

## 🏗️ System Architecture

```
User Browser
    │
    ▼
Streamlit App Container  (http://localhost:8501)
    │
    ▼
PostgreSQL Container  ◄────►  pgAdmin Container
(port 5432)                   (http://localhost:5050)
    │
    ▼
Docker Volume (postgres_data) — Persistent Storage
    │
    ▼
GitHub Repository — Version Control & Collaboration
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Programming language |
| Streamlit | Web frontend |
| PostgreSQL | Relational database |
| pgAdmin 4 | Database GUI admin |
| Docker Desktop | Container runtime |
| Docker Compose | Multi-container orchestration |
| SQLAlchemy + psycopg2 | DB connection from Python |
| Plotly | Interactive charts |
| Pandas | Data manipulation |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure

```
streamlit-postgres-assignment/
│
├── app/
│   ├── main.py                        # Home page and auth
│   ├── db.py                          # Database connection
│   ├── queries.py                     # All SQL queries
│   ├── auth.py                        # Login / session state
│   ├── utils.py                       # Helper utilities
│   └── pages/
│       ├── 1_Add_Opportunity.py
│       ├── 2_View_Search.py
│       ├── 3_Update_Opportunity.py
│       ├── 4_Delete_Opportunity.py
│       ├── 5_Analytics_Dashboard.py
│       ├── 6_CSV_Upload_Export.py
│       ├── 7_Duplicate_Detection.py
│       ├── 8_Deadline_Alerts.py
│       └── 9_Database_Health_Check.py
│
├── database/
│   ├── init.sql                       # Table schema
│   └── seed_data.sql                  # 40+ sample records
│
├── screenshots/                       # App screenshots
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
└── report.pdf
```

---

## 🚀 Setup & Running

### Prerequisites
- Docker Desktop installed and running
- Git installed

### Step 1: Clone the repository

```bash
git clone https://github.com/<your-username>/streamlit-postgres-opportunity-dashboard.git
cd streamlit-postgres-opportunity-dashboard
```

### Step 2: Start all services

```bash
docker compose up -d
```

This starts:
- **PostgreSQL** at `localhost:5432`
- **pgAdmin** at `http://localhost:5050`
- **Streamlit App** at `http://localhost:8501`

### Step 3: Access the application

| Service | URL |
|---------|-----|
| Streamlit App | http://localhost:8501 |
| pgAdmin | http://localhost:5050 |

**Login credentials for the app:**
- Admin: `admin` / `admin123`
- Viewer: `viewer` / `viewer123`

---

## 🗄️ Database Configuration

The database is automatically initialized when the PostgreSQL container starts:
- `database/init.sql` — Creates the `opportunities` table
- `database/seed_data.sql` — Inserts 40+ sample records

### pgAdmin Connection

1. Open http://localhost:5050
2. Login: `admin@example.com` / `admin123`
3. Right-click **Servers** → **Register** → **Server**
4. **General tab:** Name = `OpportunityDB`
5. **Connection tab:**
   - Host: `postgres_db`
   - Port: `5432`
   - Database: `student_opportunities_db`
   - Username: `app_user`
   - Password: `app_password`

---

## 🐳 Docker Compose Explanation

The `docker-compose.yml` defines three services:

### `postgres_db`
- Runs the official PostgreSQL image
- Exposes port `5432`
- Uses a named volume `postgres_data` to persist data
- Runs SQL init scripts on first startup

### `pgadmin`
- Runs pgAdmin 4 for graphical database management
- Depends on `postgres_db`
- Accessible at port `5050`

### `streamlit_app`
- Built from the local `Dockerfile`
- Connects to `postgres_db` using Docker's internal DNS (service name as hostname)
- Depends on `postgres_db`

### Key Docker Compose Concepts Used

| Concept | Usage in this project |
|---------|----------------------|
| `services` | Defines postgres_db, pgadmin, streamlit_app |
| `image` | Specifies the Docker image (e.g., postgres:latest) |
| `build` | Builds Streamlit app from local Dockerfile |
| `container_name` | Names each container for easy reference |
| `ports` | Maps host ports to container ports |
| `environment` | Sets DB credentials and config |
| `volumes` | Persists PostgreSQL data; mounts SQL init scripts |
| `depends_on` | Ensures postgres starts before other services |
| `restart` | `unless-stopped` keeps containers running after reboot |
| `networks` | All services share `app_network` for internal communication |

---

## 🐳 Docker Commands Reference

```bash
# Start all services in background
docker compose up -d

# Check running services
docker compose ps

# View logs
docker compose logs postgres_db
docker compose logs pgadmin
docker compose logs streamlit_app

# Stop and remove containers (keep data)
docker compose down

# List Docker volumes
docker volume ls

# Inspect PostgreSQL volume
docker volume inspect streamlit-postgres-assignment_postgres_data

# Stop containers AND delete volumes (⚠️ data loss!)
docker compose down -v
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| PostgreSQL container not starting | Check `docker compose logs postgres_db` |
| Wrong username/password | Verify `.env` matches `docker-compose.yml` |
| pgAdmin can't connect | Use `postgres_db` (not `localhost`) as host |
| Port 5432 in use | Change host port: `"5433:5432"` in compose |
| Port 5050 in use | Change host port: `"5051:80"` in compose |
| Port 8501 in use | Change host port: `"8502:8501"` in compose |
| Streamlit can't connect to DB | Ensure both are on the same Docker network |
| Table doesn't exist | Delete volume and restart: `docker compose down -v && docker compose up -d` |
| Data lost after `docker compose down -v` | Use `docker compose down` without `-v` to keep data |
| Git push rejected | Run `git pull --rebase origin main` first |
| Merge conflict | Open conflicting file, resolve manually, then commit |

---

## 📊 Application Features

| Page | Description |
|------|-------------|
| Home | Project overview, team info, architecture |
| Add Opportunity | Form to insert new records with validation |
| View & Search | Search/filter with sidebar, export CSV |
| Update Opportunity | Edit any field of existing records |
| Delete Opportunity | Preview + confirm before deleting |
| Analytics Dashboard | 6 KPIs + 6 interactive Plotly charts |
| CSV Upload & Export | Bulk insert from CSV; filtered export |
| Duplicate Detection | Finds records with same company/title/city |
| Deadline Alerts | Shows records closing ≤7 days + expired |
| DB Health Check | PostgreSQL version, row count, schema |

---

## 👥 Contribution Table

| # | Name | Student ID | GitHub Username | Tasks Completed |
|---|------|-----------|-----------------|-----------------|
| 1 | Member 1 | BSIT-XXXX | @username1 | DB schema, queries.py, seed data |
| 2 | Member 2 | BSIT-XXXX | @username2 | Streamlit pages, UI design |
| 3 | Member 3 | BSIT-XXXX | @username3 | Docker Compose, Dockerfile, README |

---

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Docker Image](https://hub.docker.com/_/postgres)
- [pgAdmin Container Docs](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [GitHub Documentation](https://docs.github.com/)
