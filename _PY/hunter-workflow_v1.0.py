import time
import sys
import os

def send_notification(title, message):
    """Cross-platform notification"""
    print(f"\n🔔 {title.upper()}: {message}\n")
    # Mac/Linux/Windows simple beep
    sys.stdout.write('\a')
    sys.stdout.flush()

def hunter_cycle():
    print("--- 🐺 INITIATING HUNTER NEURO-PROTOCOL ---")

    # 1. EAT THE FROG
    frog = input("🐸 What is the ONE scary task you must do first? ")
    print(f"🔥 LOCK IN. Target: {frog}. You have 90 minutes.")

    # 90 Minute Sprint
    sprint_duration = 90 * 60
    time.sleep(sprint_duration)

    # Recovery Phase
    send_notification("SPRINT COMPLETE", "Step away from the screen.")
    print("🛑 RECOVERY MODE (20 Mins). Guidelines:")
    print("1. No Screens.\n2. Hydrate.\n3. Movement (Pushups/Walk).")

    # 20 Minute Recovery
    time.sleep(20 * 60)

    send_notification("RECOVERY COMPLETE", "Ready for Sprint 2?")
    input("Press Enter to start the next Hunt...")
    hunter_cycle() # Loop

if __name__ == "__main__":
    hunter_cycle()