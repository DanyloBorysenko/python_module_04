import sys


def stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    sys.stdout.write("\n")

    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status: str = input("Input Stream active. Enter status report: ")
    sys.stdout.write("\n")

    # print(f"[STANDARD] Archive status from {id}: {status}")
    sys.stdout.write(f"[STANDARD] Archive status from "
                     f"{archivist_id}: {status}\n")

    # print("[ALERT] System diagnostic: Communication channels verified",
    #       file=sys.stderr)
    sys.stderr.write(("[ALERT] System diagnostic: "
                      "Communication channels verified\n"))

    # print("[STANDARD] Data transmission complete")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    sys.stdout.write("\n")
    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    stream_management()
