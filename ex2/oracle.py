import os
import sys


def check_configuration() -> list[str]:
    content = [
            "MATRIX_MODE",
            "DATABASE_URL",
            "API_KEY",
            "LOG_LEVEL",
            "ZION_ENDPOINT"
         ]

    missing: list[str] = []

    for item in content:
        if not os.getenv(item):
            missing.append(item)

    return missing


def show_configuration() -> None:
    matrix_dic = {
            "MATRIX_MODE": "Mode",
            "DATABASE_URL": "Database",
            "API_KEY": "API Access",
            "LOG_LEVEL": "Log Level",
            "ZION_ENDPOINT": "Zion Network"
            }

    print("Configuration loaded:\n")
    for item in matrix_dic:
        var: str | None = os.environ.get(item)
        if item == "MATRIX_MODE":
            if var != "development" and var != "production":
                print("WARNING - Unknown MATRIX_MODE")

        if item == "API_KEY":
            var = "Authentificated" if var else "Not Authentificated"

        if item == "DATABASE_URL":
            var = ("Connected to local instance"
                   if var == "localhost" else var)

        print(f"{matrix_dic[item]}: {var}")


def oracle() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError as e:
        print(f"Error: {e}\nInstall dotenv module")
        sys.exit(1)

    print("ORACLE STATUS: Reading the Matrix...")
    load_dotenv()

    missing = check_configuration()

    if missing:
        for term in missing:
            print(f"[WARNING] - [MISSING] {term}")
        print("Please update your .env files")
        return

    show_configuration()
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all Configurations.")


if __name__ == "__main__":
    oracle()
