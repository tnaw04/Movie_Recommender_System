import sqlite3
import os
import zipfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, 'data', 'processed')
DB_FILE = 'movies_database.db'
ZIP_FILE = 'movies_database.zip'
DB_PATH = os.path.join(DB_DIR, DB_FILE)
ZIP_PATH = os.path.join(DB_DIR, ZIP_FILE)

def get_connection():
    
    if not os.path.exists(DB_PATH) and os.path.exists(ZIP_PATH):
        try:
            with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
                zip_ref.extractall(DB_DIR)
        except: pass
    return sqlite3.connect(DB_PATH)



def init_config_table():
    """Tạo bảng cấu hình nếu chưa có"""
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_config 
                 (key TEXT PRIMARY KEY, value TEXT)''')
  
    c.execute("INSERT OR IGNORE INTO system_config (key, value) VALUES ('active_model', 'SVD')")
    conn.commit()
    conn.close()

def set_active_model(model_name):
    """Admin dùng hàm này để đổi model"""
    conn = get_connection()
    conn.execute("UPDATE system_config SET value = ? WHERE key = 'active_model'", (model_name,))
    conn.commit()
    conn.close()

def get_active_model():
    """User dùng hàm này để xem Admin đang bật model nào"""
    conn = get_connection()
    try:
        val = conn.execute("SELECT value FROM system_config WHERE key = 'active_model'").fetchone()
        return val[0] if val else 'SVD'
    except:
        return 'SVD'
    finally:
        conn.close()