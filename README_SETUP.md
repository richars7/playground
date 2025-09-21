# 🔧 LeetCode Streak Tracker Setup Guide

Complete setup instructions for your LeetCode streak tracking system!

## 🚀 Quick Setup

### Option 1: Automated Setup (Recommended)

#### For Mac/Linux:
```bash
chmod +x setup_environment.sh
./setup_environment.sh
```

#### For Windows:
```cmd
setup_environment.bat
```

### Option 2: Manual Setup

#### Step 1: Create Virtual Environment
```bash
# Mac/Linux
python3 -m venv leetcode_env

# Windows
python -m venv leetcode_env
```

#### Step 2: Activate Virtual Environment
```bash
# Mac/Linux
source leetcode_env/bin/activate

# Windows
leetcode_env\Scripts\activate.bat
```

#### Step 3: Install Dependencies (Optional)
```bash
pip install -r requirements.txt
```

## 📦 What Gets Installed

### Core System (No Dependencies Required!)
The streak tracker works with **zero external dependencies** using only Python standard library:
- ✅ **json** - Data storage and retrieval
- ✅ **os** - File system operations
- ✅ **datetime** - Date and time handling
- ✅ **random** - Motivational message generation
- ✅ **webbrowser** - UI launcher functionality

### Optional Enhancements
The `requirements.txt` includes optional packages for enhanced functionality:

#### Date/Time Handling
- `python-dateutil` - Better date parsing and manipulation

#### Performance
- `ujson` - Faster JSON processing

#### Terminal Experience
- `colorama` - Cross-platform colored terminal output
- `tqdm` - Progress bars for long operations

#### Web Server (Advanced)
- `flask` - Web server for hosting the UI
- `flask-cors` - Cross-origin resource sharing

#### Data Visualization
- `matplotlib` - Create charts and graphs
- `plotly` - Interactive visualizations

#### Database Storage
- `sqlalchemy` - Database ORM for advanced data storage

#### Configuration
- `pyyaml` - YAML configuration files

#### Logging
- `loguru` - Enhanced logging capabilities

#### Testing
- `pytest` - Unit testing framework
- `pytest-cov` - Code coverage reporting

## 🎯 Usage After Setup

### Activate Environment
```bash
# Mac/Linux
source leetcode_env/bin/activate

# Windows
leetcode_env\Scripts\activate.bat
```

### Run the Streak Tracker
```bash
# Full dashboard
python leetcode_streak_tracker.py

# Quick problem solver
python quick_solve.py

# Daily check-in
python daily_reminder.py

# Launch web UI
python launch_ui.py
```

### Deactivate Environment
```bash
deactivate
```

## 🔧 Troubleshooting

### Python Not Found
```bash
# Check Python installation
python3 --version
# or
python --version

# Install Python if needed:
# macOS: brew install python3
# Ubuntu: sudo apt install python3 python3-pip python3-venv
# Windows: Download from https://python.org
```

### Virtual Environment Issues
```bash
# Try different Python command
python -m venv leetcode_env
# or
python3 -m venv leetcode_env

# Check if venv module is available
python -m venv --help
```

### Permission Issues
```bash
# Make scripts executable (Mac/Linux)
chmod +x setup_environment.sh
chmod +x launch_ui.sh

# Run with sudo if needed (not recommended)
sudo python3 -m venv leetcode_env
```

### Package Installation Issues
```bash
# Upgrade pip first
pip install --upgrade pip

# Install packages individually
pip install python-dateutil
pip install colorama
pip install tqdm
```

## 📁 Project Structure After Setup

```
test/
├── leetcode_env/              # Virtual environment
│   ├── bin/                   # Executables (Mac/Linux)
│   ├── Scripts/               # Executables (Windows)
│   └── lib/                   # Installed packages
├── 01_Arrays_Strings/         # Problem categories
├── 02_Linked_Lists/
├── ...                        # Other categories
├── leetcode_streak_tracker.py # Main tracker
├── quick_solve.py            # Quick solver
├── daily_reminder.py         # Daily check-in
├── launch_ui.py              # UI launcher
├── index.html                # Web UI
├── requirements.txt          # Dependencies
├── setup_environment.sh      # Setup script (Mac/Linux)
├── setup_environment.bat     # Setup script (Windows)
└── README_SETUP.md           # This file
```

## 🎉 You're All Set!

After setup, you can:

1. **Track your daily coding streak** 🔥
2. **Mark problems as solved** with instant feedback
3. **Unlock achievements** as you progress
4. **Use the beautiful web UI** for easy interaction
5. **Set weekly goals** and track progress
6. **View your problem history** and statistics

### Quick Start Commands:
```bash
# Activate environment
source leetcode_env/bin/activate  # Mac/Linux
# or
leetcode_env\Scripts\activate.bat  # Windows

# Launch the web UI
python launch_ui.py

# Or use the terminal interface
python leetcode_streak_tracker.py
```

**Happy coding and keep that streak alive! 🔥**
