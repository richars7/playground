"""
🔔 Daily LeetCode Reminder at 8 PM
Automatically checks your streak and reminds you to solve a problem
"""

import schedule
import time
import json
import os
from datetime import datetime, timedelta
from leetcode_streak_tracker import LeetCodeStreakTracker


def _vault_path():
    """Return an absolute path to the ML vault for quick sharing."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "ml_resources", "index.html")

def send_notification():
    """Send daily notification at 8 PM"""
    tracker = LeetCodeStreakTracker()
    
    today = datetime.now().date()
    last_activity = None
    
    if tracker.data["last_activity_date"]:
        last_activity = datetime.fromisoformat(tracker.data["last_activity_date"]).date()
    
    print(f"\n🔔 DAILY LEETCODE REMINDER - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    if last_activity == today:
        print("✅ You've already solved a problem today!")
        print(f"🔥 Current streak: {tracker.data['current_streak']} days")
        print(f"📊 Total problems: {tracker.data['total_problems_solved']}")
        print(f"\n💬 {tracker.get_motivational_message()}")
        print("\n🎯 Keep up the great work! You're on fire! 🔥")
    else:
        print("⚠️  You haven't solved a problem today yet!")
        print(f"🔥 Current streak: {tracker.data['current_streak']} days")
        
        if last_activity:
            days_since = (today - last_activity).days
            if days_since > 1:
                print(f"😱 {days_since} days since last problem!")
                print("🚨 Your streak is at risk!")
                print("💪 Don't give up! One problem can get you back on track!")
            else:
                print("⏰ Don't let your streak break!")
                print("🎯 Just one problem to keep the momentum going!")
        
        print(f"\n💡 {tracker.get_motivational_message()}")
        
        # Show weekly progress
        weekly_goal = tracker.data["weekly_goal"]
        current_week = tracker.data["current_week_problems"]
        progress = (current_week / weekly_goal) * 100 if weekly_goal > 0 else 0
        
        print(f"\n📈 Weekly Progress: {current_week}/{weekly_goal} ({progress:.1f}%)")
        
        if current_week < weekly_goal:
            remaining = weekly_goal - current_week
            print(f"🎯 {remaining} more problems needed this week!")
        
        print("\n🚀 Quick Actions:")
        print("1. Run 'python quick_solve.py' to mark a problem solved")
        print("2. Run 'python launch_ui.py' for the web interface")
        print("3. Run 'python leetcode_streak_tracker.py' for full dashboard")
    
    print("\n" + "=" * 60)

    vault_link = _vault_path()
    print("\n🧠 ML & System Design Vault")
    print(f"🔗 Open: {vault_link}")
    print("💡 Tap the playbooks for compact tips + problem sets before you dive in.")

def start_daily_reminder():
    """Start the daily reminder service"""
    print("🔔 Starting Daily LeetCode Reminder Service...")
    print("⏰ You'll get a reminder every day at 8:00 PM")
    print("🛑 Press Ctrl+C to stop the service")
    print("=" * 50)
    
    # Schedule the notification for 8 PM every day
    schedule.every().day.at("20:00").do(send_notification)
    
    # Send initial notification
    send_notification()
    
    # Keep the service running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n🛑 Daily reminder service stopped.")
        print("👋 Goodbye! Keep coding and maintain that streak! 🔥")

if __name__ == "__main__":
    start_daily_reminder()
