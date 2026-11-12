from proxy import DatabaseProxy

def main():
    user_db = DatabaseProxy(False)
    admin_db = DatabaseProxy(True)
    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")

if __name__ == "__main__":
    main()