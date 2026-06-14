import os
from sqlalchemy import create_engine, text
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "student_opportunities_db")
DB_USER = os.getenv("DB_USER", "app_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "app_password")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


@st.cache_resource
def get_engine():
    """Create and cache the SQLAlchemy engine."""
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        return engine
    except Exception as e:
        st.error(f"Failed to create database engine: {e}")
        return None


def get_connection():
    """Get a database connection from the engine."""
    engine = get_engine()
    if engine:
        return engine.connect()
    return None


def test_connection():
    """Test database connectivity. Returns (success: bool, message: str)."""
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
        return True, version
    except Exception as e:
        return False, str(e)
