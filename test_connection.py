from db.session import get_db
from sqlalchemy import text
def test_connection():
    try:
        session = get_db()
        result = session.exec(text("SELECT 1")).one()
        print("✅ Database connection successful:", result)
    except Exception as e:
        print("❌ Database connection failed:", e)

if __name__ == "__main__":
    test_connection()