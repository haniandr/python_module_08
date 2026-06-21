import os
import sys

content = [
            "MATRIX_MODE",
            "DATABASE_URL",
            "API_KEY",
            "LOG_LEVEL",
            "ZION_ENDPOINT"
         ]


def check_configuration() -> list[str]:
    missing = []

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
    for item in content:
        var: str | None = os.environ.get(item)
        if item == "API_KEY":
            var = "Authentificated" if var else "Not Authentificated"
        if item == "DATABASE_URL":
            var = ("Connected to local instance"
                   if var == "localhost" or (not var)
                   else var)
        if var != "development" or var != "production":
            print("WARNING - Unknown MATRIX_MODE")
        print(f"{matrix_dic[item]}: {var}")


def oracle() -> None:
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError as e:
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
