import time

seconds = int(input("Duration (seconds): "))
while seconds > 0:
    print(f"\r{seconds // 60:02}:{seconds % 60:02}", end="", flush=True)
    time.sleep(1)
    seconds -= 1
print("\rTime's up!     ")