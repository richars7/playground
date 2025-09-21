"""
🚀 Start Daily Reminder Service
Simple launcher for the daily notification system
"""

import subprocess
import sys
import os

def install_schedule():
    """Install the schedule package if not available"""
    try:
        import schedule
        return True
    except ImportError:
        print("📦 Installing 'schedule' package for daily reminders...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "schedule"])
            print("✅ Schedule package installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install schedule package")
            print("Please install it manually: pip install schedule")
            return False

def start_reminder():
    """Start the daily reminder service"""
    print("🔔 LeetCode Daily Reminder Service")
    print("=" * 40)
    
    # Check if schedule package is available
    if not install_schedule():
        return
    
    # Start the reminder service
    try:
        from daily_notification import start_daily_reminder
        start_daily_reminder()
    except ImportError as e:
        print(f"❌ Error importing reminder service: {e}")
        print("Make sure daily_notification.py is in the same directory")

if __name__ == "__main__":
    start_reminder()
