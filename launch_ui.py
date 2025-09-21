"""
🚀 LeetCode Streak Tracker UI Launcher
Opens the web-based UI in your default browser
"""

import webbrowser
import os
import sys

def launch_ui():
    """Launch the streak tracker UI in the default browser"""
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ui_file = os.path.join(current_dir, "index.html")
    
    # Check if the UI file exists
    if not os.path.exists(ui_file):
        print("❌ Error: index.html not found!")
        print("Make sure you're running this from the correct directory.")
        return
    
    # Get the file URL
    file_url = f"file://{ui_file}"
    
    print("🚀 Launching LeetCode Streak Tracker UI...")
    print(f"📁 Opening: {ui_file}")
    
    try:
        # Open in default browser
        webbrowser.open(file_url)
        print("✅ UI launched successfully!")
        print("\n💡 Tips:")
        print("   - Bookmark this page for quick access")
        print("   - Keep this tab open for daily use")
        print("   - Your progress is saved automatically in your browser")
        print("\n🔥 Happy coding and keep that streak alive!")
        
    except Exception as e:
        print(f"❌ Error launching UI: {e}")
        print("\n🔧 Manual launch:")
        print(f"   Open your browser and navigate to: {file_url}")

if __name__ == "__main__":
    launch_ui()
