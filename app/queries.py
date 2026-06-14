import pandas as pd
from sqlalchemy import text
from db import get_engine


# ---------- READ ----------

def get_all_opportunities():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql("SELECT * FROM opportunities ORDER BY created_at DESC", conn)


def search_opportunities(keyword="", category="", city="", work_mode="", status="", salary_min=None, salary_max=None, experience_level=""):
    engine = get_engine()
    query = "SELECT * FROM opportunities WHERE 1=1"
    params = {}
    if keyword:
        query += " AND (company_name ILIKE :kw OR job_title ILIKE :kw OR required_skills ILIKE :kw)"
        params["kw"] = f"%{keyword}%"
    if category:
        query += " AND category = :category"
        params["category"] = category
    if city:
        query += " AND city ILIKE :city"
        params["city"] = f"%{city}%"
    if work_mode:
        query += " AND work_mode = :work_mode"
        params["work_mode"] = work_mode
    if status:
        query += " AND status = :status"
        params["status"] = status
    if salary_min is not None:
        query += " AND salary_min >= :salary_min"
        params["salary_min"] = salary_min
    if salary_max is not None:
        query += " AND salary_max <= :salary_max"
        params["salary_max"] = salary_max
    if experience_level:
        query += " AND experience_level = :experience_level"
        params["experience_level"] = experience_level
    query += " ORDER BY created_at DESC"
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn, params=params)


def get_opportunity_by_id(opp_id):
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM opportunities WHERE opportunity_id = :id"), {"id": opp_id})
        row = result.fetchone()
        return dict(row._mapping) if row else None


# ---------- CREATE ----------

def insert_opportunity(data: dict):
    engine = get_engine()
    query = text("""
        INSERT INTO opportunities
        (company_name, job_title, category, city, country, work_mode, required_skills,
         salary_min, salary_max, currency, experience_level, application_deadline, status, source_link)
        VALUES
        (:company_name, :job_title, :category, :city, :country, :work_mode, :required_skills,
         :salary_min, :salary_max, :currency, :experience_level, :application_deadline, :status, :source_link)
    """)
    with engine.begin() as conn:
        conn.execute(query, data)


def bulk_insert_opportunities(df: pd.DataFrame):
    engine = get_engine()
    df.to_sql("opportunities", engine, if_exists="append", index=False)


# ---------- UPDATE ----------

def update_opportunity(opp_id, data: dict):
    engine = get_engine()
    query = text("""
        UPDATE opportunities SET
            company_name = :company_name,
            job_title = :job_title,
            category = :category,
            city = :city,
            country = :country,
            work_mode = :work_mode,
            required_skills = :required_skills,
            salary_min = :salary_min,
            salary_max = :salary_max,
            currency = :currency,
            experience_level = :experience_level,
            application_deadline = :application_deadline,
            status = :status,
            source_link = :source_link
        WHERE opportunity_id = :id
    """)
    data["id"] = opp_id
    with engine.begin() as conn:
        conn.execute(query, data)


# ---------- DELETE ----------

def delete_opportunity(opp_id):
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM opportunities WHERE opportunity_id = :id"), {"id": opp_id})


# ---------- ANALYTICS ----------

def get_kpis():
    engine = get_engine()
    with engine.connect() as conn:
        total = conn.execute(text("SELECT COUNT(*) FROM opportunities")).scalar()
        open_count = conn.execute(text("SELECT COUNT(*) FROM opportunities WHERE status='Open'")).scalar()
        companies = conn.execute(text("SELECT COUNT(DISTINCT company_name) FROM opportunities")).scalar()
        avg_salary = conn.execute(text("SELECT ROUND(AVG((salary_min+salary_max)/2),0) FROM opportunities WHERE currency='PKR'")).scalar()
        deadline_soon = conn.execute(text(
            "SELECT COUNT(*) FROM opportunities WHERE application_deadline BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days' AND status='Open'"
        )).scalar()
        expired = conn.execute(text("SELECT COUNT(*) FROM opportunities WHERE status='Expired'")).scalar()
    return {
        "total": total, "open": open_count, "companies": companies,
        "avg_salary": avg_salary, "deadline_soon": deadline_soon, "expired": expired
    }


def get_category_distribution():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql("SELECT category, COUNT(*) as count FROM opportunities GROUP BY category ORDER BY count DESC", conn)


def get_work_mode_distribution():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql("SELECT work_mode, COUNT(*) as count FROM opportunities GROUP BY work_mode", conn)


def get_status_distribution():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql("SELECT status, COUNT(*) as count FROM opportunities GROUP BY status", conn)


def get_salary_by_category():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(
            "SELECT category, ROUND(AVG(salary_min),0) as avg_min, ROUND(AVG(salary_max),0) as avg_max FROM opportunities WHERE currency='PKR' GROUP BY category",
            conn
        )


def get_top_cities():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql("SELECT city, COUNT(*) as count FROM opportunities GROUP BY city ORDER BY count DESC LIMIT 10", conn)


def get_experience_distribution():
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql("SELECT experience_level, COUNT(*) as count FROM opportunities GROUP BY experience_level", conn)


# ---------- DUPLICATES ----------

def get_duplicates():
    engine = get_engine()
    query = """
        SELECT a.* FROM opportunities a
        JOIN (
            SELECT company_name, job_title, city, COUNT(*) as cnt
            FROM opportunities
            GROUP BY company_name, job_title, city
            HAVING COUNT(*) > 1
        ) b ON a.company_name = b.company_name AND a.job_title = b.job_title AND a.city = b.city
        ORDER BY a.company_name, a.job_title
    """
    with engine.connect() as conn:
        return pd.read_sql(query, conn)


# ---------- DEADLINE ALERTS ----------

def get_deadline_alerts():
    engine = get_engine()
    with engine.connect() as conn:
        soon = pd.read_sql(
            "SELECT * FROM opportunities WHERE application_deadline BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days' AND status='Open' ORDER BY application_deadline",
            conn
        )
        expired = pd.read_sql(
            "SELECT * FROM opportunities WHERE (application_deadline < CURRENT_DATE OR status='Expired') ORDER BY application_deadline DESC",
            conn
        )
    return soon, expired


# ---------- DB HEALTH ----------

def get_db_health():
    engine = get_engine()
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version()")).scalar()
        row_count = conn.execute(text("SELECT COUNT(*) FROM opportunities")).scalar()
        latest = conn.execute(text("SELECT * FROM opportunities ORDER BY created_at DESC LIMIT 1")).fetchone()
        columns = conn.execute(text(
            "SELECT column_name, data_type FROM information_schema.columns WHERE table_name='opportunities' ORDER BY ordinal_position"
        )).fetchall()
    return {
        "version": version,
        "row_count": row_count,
        "latest": dict(latest._mapping) if latest else None,
        "columns": [{"column": c[0], "type": c[1]} for c in columns]
    }
