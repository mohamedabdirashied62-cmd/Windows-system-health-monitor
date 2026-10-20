
# Windows System Health Monitor

A lightweight, real-time command-line utility built in Python to monitor Windows system health—tracking CPU usage, RAM utilization, and disk space with built-in error handling for unready external drives.


# 📂 Project Structure

```text
windows-system-health-monitor/
│
├── .venv/              # Python virtual environment (ignored by Git)
├── .gitignore          # Specifies intentionally untracked files to ignore
├── main.py             # Main system health monitoring script
└── requirements.txt    # Project dependencies

🛠️ Step-by-Step Setup & Installation

Follow these exact steps to set up and run the project locally on Windows using PowerShell:
Step 1: Clone or Initialize the Repository
If you are starting fresh locally, navigate to your project folder and initialize Git:
git init

Step 2: Create a Virtual Environment
Create an isolated Python virtual environment inside your project directory:
python -m venv .venv

Step 3: Activate the Virtual Environment
Activate the virtual environment in PowerShell:
.venv\Scripts\Activate.ps1

(Note: If you encounter an execution policy error, run Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned first).
Step 4: Create the Requirements File
Create a requirements.txt file containing the project dependency (psutil):
Set-Content -Path "requirements.txt" -Value "psutil"

Step 5: Install Dependencies
Install the required packages using pip:
python -m pip install -r requirements.txt

💻 Usage
Run the system health monitor script directly from your terminal:
python main.py

What the Script Checks:
 * CPU Monitoring: Measures current CPU utilization and warns if usage is \ge 85\%.
 * Memory Monitoring: Tracks total physical RAM, available memory, and percentage usage, warning if usage is \ge 85\%.
 * Disk Monitoring: Scans all active partitions (like C:\), displaying total space, free space, and warnings if usage is \ge 90\%. Gracefully skips unready external drives or empty card readers (WinError 21).


# How to save and push this to GitHub right now:

Run these commands in your PowerShell terminal:

1. **Create and save the README file:**
   ```powershell
   Set-Content -Path "README.md" -Value "# Windows System Health Monitor`n`nA lightweight, real-time command-line utility built in Python to monitor Windows system health.`n`n## Installation & Usage`n1. Clone or open folder.`n2. Create venv: `python -m venv .venv` and activate it.`n3. Install dependencies: `python -m pip install -r requirements.txt`.`n4. Run script: `python main.py`."

(Or just paste the full README block above into your README.md file in VS Code and save it).
 * Commit and push to GitHub:
   git add README.md
git commit -m "Add detailed realistic README.md"
git branch -M main
git remote add origin https://github.com/mohamedabdirashied62-cmd/windows-system-health-monitor.git
git push -u origin main

   
