import os
import shutil
import pymysql
from pathlib import Path

# Set the base directory of your Django project
BASE_DIR = Path(__file__).resolve().parent

# MySQL database credentials (from your settings.py)
DB_NAME = 'reactif'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = 3306

# Path to your Django apps - update this to use the base directory instead of a non-existent "reactif" directory
APPS_DIR = BASE_DIR

def delete_migrations():
    """Delete all migration files except __init__.py"""
    total_deleted = 0
    
    # Find all Django apps - Add a filter to only include actual app directories
    potential_apps = [
        d for d in os.listdir(APPS_DIR) 
        if os.path.isdir(os.path.join(APPS_DIR, d)) and d not in ['__pycache__', '.git', 'reactif', 'templates']
    ]
    
    # Filter to only include directories that are likely Django apps
    apps = []
    for app in potential_apps:
        # Check if it has models.py, views.py, or a migrations folder - typical Django app patterns
        app_dir = os.path.join(APPS_DIR, app)
        if (os.path.isfile(os.path.join(app_dir, 'models.py')) or 
            os.path.isfile(os.path.join(app_dir, 'views.py')) or
            os.path.exists(os.path.join(app_dir, 'migrations'))):
            apps.append(app)
    
    print("Found Django apps:", apps)
    
    for app in apps:
        migrations_dir = os.path.join(APPS_DIR, app, 'migrations')
        
        if os.path.exists(migrations_dir):
            print(f"Processing migrations for {app}...")
            
            # Get all files in the migrations directory
            for filename in os.listdir(migrations_dir):
                file_path = os.path.join(migrations_dir, filename)
                
                # Delete all migration files except __init__.py
                if os.path.isfile(file_path) and filename != '__init__.py':
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    total_deleted += 1
                    
                # Delete __pycache__ directory if it exists
                pycache_dir = os.path.join(migrations_dir, '__pycache__')
                if os.path.exists(pycache_dir):
                    shutil.rmtree(pycache_dir)
                    print(f"Deleted: {pycache_dir}")
        else:
            print(f"No migrations directory found for {app}")
    
    return total_deleted

def delete_all_pycache():
    """Recursively find and delete all __pycache__ folders in the project"""
    total_deleted = 0
    
    # Start from the base directory and walk through all subdirectories
    for root, dirs, files in os.walk(BASE_DIR):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"Deleted: {pycache_path}")
                total_deleted += 1
            except Exception as e:
                print(f"Error deleting {pycache_path}: {e}")
    
    return total_deleted

def reset_database():
    """Reset the MySQL database by dropping and recreating it"""
    try:
        # Connect to MySQL server (without specifying the database)
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        with conn.cursor() as cursor:
            # Drop database if it exists
            cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
            print(f"Dropped database: {DB_NAME}")
            
            # Create database
            cursor.execute(f"CREATE DATABASE {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"Created database: {DB_NAME}")
            
        conn.close()
        return True
    except Exception as e:
        print(f"Error resetting database: {e}")
        return False

if __name__ == "__main__":
    # Ask for confirmation
    confirm = input("This will delete all migration files, __pycache__ folders, and reset the database. Continue? (y/n): ")
    
    if confirm.lower() == 'y':
        # Delete migration files
        deleted_count = delete_migrations()
        print(f"Deleted {deleted_count} migration files")
        
        # Delete all __pycache__ folders
        pycache_deleted = delete_all_pycache()
        print(f"Deleted {pycache_deleted} __pycache__ folders")
        
        # Reset database
        if reset_database():
            print("\nDatabase has been reset successfully.")
            print("\nNext steps:")
            print("1. Run 'python manage.py makemigrations' to create new migration files")
            print("2. Run 'python manage.py migrate' to apply migrations")
        else:
            print("\nFailed to reset database. Check your database credentials.")
    else:
        print("Operation cancelled.") 