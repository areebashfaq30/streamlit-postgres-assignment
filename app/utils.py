import pandas as pd
import io

CATEGORIES = ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"]
WORK_MODES = ["Remote", "Onsite", "Hybrid"]
STATUSES = ["Open", "Closed", "Expired", "Shortlisted"]
EXPERIENCE_LEVELS = ["Entry-Level", "Mid-Level", "Senior"]
CURRENCIES = ["PKR", "USD", "EUR", "GBP"]

REQUIRED_CSV_COLUMNS = [
    "company_name", "job_title", "category", "city", "country",
    "work_mode", "required_skills", "salary_min", "salary_max",
    "currency", "experience_level", "application_deadline", "status", "source_link"
]


def validate_csv(df: pd.DataFrame):
    """Return (is_valid, errors, cleaned_df)."""
    errors = []
    missing = [c for c in REQUIRED_CSV_COLUMNS if c not in df.columns]
    if missing:
        return False, [f"Missing columns: {missing}"], None

    df = df[REQUIRED_CSV_COLUMNS].copy()
    df.dropna(subset=["company_name", "job_title", "category", "required_skills"], inplace=True)

    invalid_category = ~df["category"].isin(CATEGORIES)
    if invalid_category.any():
        errors.append(f"{invalid_category.sum()} row(s) have invalid category. Valid: {CATEGORIES}")
        df = df[~invalid_category]

    invalid_mode = ~df["work_mode"].isin(WORK_MODES)
    if invalid_mode.any():
        errors.append(f"{invalid_mode.sum()} row(s) have invalid work_mode. Valid: {WORK_MODES}")
        df = df[~invalid_mode]

    invalid_status = ~df["status"].isin(STATUSES)
    if invalid_status.any():
        errors.append(f"{invalid_status.sum()} row(s) have invalid status. Valid: {STATUSES}")
        df = df[~invalid_status]

    return True, errors, df


def dataframe_to_csv_bytes(df: pd.DataFrame) -> bytes:
    """Convert DataFrame to downloadable CSV bytes."""
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue().encode("utf-8")
