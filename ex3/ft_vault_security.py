import sys


def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")

    try:
        with open("classified_data.txt", "r+") as file:
            print("Vault connection established with failsafe protocols")

            print("\nSECURE EXTRACTION:")
            print(file.read())

            print()

            print("SECURE PRESERVATION:")
            data: str = ("[CLASSIFIED] New security protocols archived")
            file.write(data)
            print(data)
        print("Vault automatically sealed upon completion\n")
    except OSError:
        sys.stderr.write(("Error occured during read-write operation "
                          "execution with file 'classified_data.txt'\n"))
    else:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security()
