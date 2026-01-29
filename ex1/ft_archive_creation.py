def create_storage() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", "w") as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            data: str = ("[ENTRY 001] New quantum algorithm discovered\n"
                         "[ENTRY 002] Efficiency increased by 347%\n"
                         "[ENTRY 003] Archived by Data Archivist trainee\n")
            file.write(data)
            print(data)
    except OSError:
        print("ERROR: Failed to initialize storage unit.")
    else:
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    create_storage()
