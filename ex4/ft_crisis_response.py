import sys

class CrisisResponseSystem():
    def __init__(self):
        print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
        print()

    def check_file(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as file:
                print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
                print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed\n")
        except FileNotFoundError:
            sys.stderr.write(f"CRISIS ALERT: Attempting access to '{file_name}'...\n")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            sys.stderr.write(f"CRISIS ALERT: Attempting access to '{file_name}'...\n")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except OSError:
            sys.stderr.write(f"CRISIS ALERT: Attempting access to '{file_name}'...\n")
            print("RESPONSE: crisis response system failed")
            print("STATUS: Crisis handled\n")

if __name__ == "__main__":
    system: CrisisResponseSystem = CrisisResponseSystem()
    files: list[str] = ["lost_archive.txt", "classified_vault.txt", "standard_archive.txt"]
    for file_name in files:
        system.check_file(file_name)
    # system.check_file("corrupted_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")