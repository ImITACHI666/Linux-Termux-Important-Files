import os
import subprocess
from datetime import datetime
import platform

SAVED_DATA_DIR = "Saved_Data"
LOG_FILE = "logs.txt"

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def create_directory():
    if not os.path.exists(SAVED_DATA_DIR):
        os.makedirs(SAVED_DATA_DIR)

def write_log(action: str):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {action}\n")

def google_saver():
    try:
        create_directory()
        print("\n[ Google Account Saver ]")
        email = input("Введите Gmail: ").strip()
        password = input("Введите пароль: ").strip()
        
        gmail_file = os.path.join(SAVED_DATA_DIR, "gmail.txt")
        num = 1
        
        if os.path.exists(gmail_file):
            with open(gmail_file, "r") as f:
                lines = [line for line in f if line.strip()]
                num = len(lines) + 1
        
        with open(gmail_file, "a") as f:
            f.write(f"[{num}] ) {email}  -  {password}\n")
        
        write_log(f"Added Google: {email[:3]}***@...")
        print("\n[ Данные сохранены! ]")
    
    except Exception as e:
        print(f"Ошибка: {e}")

def seed_saver():
    try:
        create_directory()
        print("\n[ Seed Phrase Saver ]")
        seed = input("Введите сид-фразу: ").strip()
        
        seed_file = os.path.join(SAVED_DATA_DIR, "seed.txt")
        num = 1
        
        if os.path.exists(seed_file):
            with open(seed_file, "r") as f:
                lines = [line for line in f if line.strip()]
                num = len(lines) + 1
        
        with open(seed_file, "a") as f:
            f.write(f"[{num}] ) {seed}\n")
        
        write_log(f"Added Seed: {seed[:6]}...")  # Усеченная версия в логи
        print("\n[ Сид-фраза сохранена! ]")
    
    except Exception as e:
        print(f"Ошибка: {e}")

def proot_config():
    try:
        write_log("Opened proot-distro config")
        subprocess.call(["nano", "debian.sh"])
        write_log("Closed proot-distro config")
    except Exception as e:
        print(f"Ошибка: {e}")

def clear_logs():
    try:
        open(LOG_FILE, "w").close()
        print("\n[ Логи очищены ]")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    clear_screen()
    while True:
        print("\n" + "="*30)
        print("1. Google Saver")
        print("2. Crypto Seed Saver")
        print("3. Proot-distro config")
        print("4. Clear Logs")
        print("5. Выход")
        
        choice = input("Выберите опцию: ").strip()
        
        if choice == "1":
            google_saver()
        elif choice == "2":
            seed_saver()
        elif choice == "3":
            proot_config()
        elif choice == "4":
            clear_logs()
        elif choice == "5":
            write_log("Program terminated")
            print("\n[ Выход ]")
            break
        else:
            print("\n[ Неверный выбор ]")
        
        input("\nНажмите Enter чтобы продолжить...")
        clear_screen()

if __name__ == "__main__":
    create_directory()
    main()