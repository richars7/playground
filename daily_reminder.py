"""
📅 Daily LeetCode Reminder 📅
Get motivated to maintain your streak!
"""

import json
import os
from datetime import datetime, timedelta
from leetcode_streak_tracker import LeetCodeStreakTracker


def _vault_path():
    """Return an absolute path to the ML vault for quick sharing."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "ml_resources", "index.html")

def check_daily_status():
    """Check if user has solved a problem today"""
    tracker = LeetCodeStreakTracker()
    
    today = datetime.now().date()
    last_activity = None
    
    if tracker.data["last_activity_date"]:
        last_activity = datetime.fromisoformat(tracker.data["last_activity_date"]).date()
    
    print("\n" + "="*50)
    print("📅 DAILY LEETCODE CHECK-IN 📅")
    print("="*50)
    
    if last_activity == today:
        print("✅ You've already solved a problem today!")
        print(f"🔥 Current streak: {tracker.data['current_streak']} days")
        print(f"📊 Total problems: {tracker.data['total_problems_solved']}")
        print(f"\n💬 {tracker.get_motivational_message()}")
    else:
        print("⚠️  You haven't solved a problem today yet!")
        print(f"🔥 Current streak: {tracker.data['current_streak']} days")
        
        if last_activity:
            days_since = (today - last_activity).days
            if days_since > 1:
                print(f"😱 {days_since} days since last problem!")
                print("🚨 Your streak is at risk!")
            else:
                print("⏰ Don't let your streak break!")
        
        print(f"\n💡 {tracker.get_motivational_message()}")
        print("\n🎯 Quick actions:")
        print("1. Run 'python quick_solve.py' to mark a problem solved")
        print("2. Run 'python leetcode_streak_tracker.py' for full dashboard")
    
    # Show weekly progress
    weekly_goal = tracker.data["weekly_goal"]
    current_week = tracker.data["current_week_problems"]
    progress = (current_week / weekly_goal) * 100 if weekly_goal > 0 else 0
    
    print(f"\n📈 Weekly Progress: {current_week}/{weekly_goal} ({progress:.1f}%)")
    
    if current_week < weekly_goal:
        remaining = weekly_goal - current_week
        print(f"🎯 {remaining} more problems needed this week!")

    print("="*50)

    # Surface the new ML companion vault every time the reminder runs
    vault_link = _vault_path()
    print("\n🧠 ML & System Design Vault ready for a boost:")
    print(f"🔗 Open: {vault_link}")
    print("💡 Trio of tips, problems, and system design prompts to keep learning balanced.")

if __name__ == "__main__":
    check_daily_status()
