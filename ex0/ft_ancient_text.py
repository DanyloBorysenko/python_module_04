def data_recovery() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        # file = open("ancient_fragment.txt", "r")
        with open("ancient_fragment.txt", "r") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
    except (FileNotFoundError):
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("\nData recovery complete. Storage unit disconnected.")
    # finally:
    #     file.close()


if __name__ == "__main__":
    data_recovery()
