#!/usr/bin/env python3
import os
import argparse
import shutil
import subprocess
from pathlib import Path

def setup_git(target_dir):
    """Initialize git repo."""
    try:
        subprocess.run(["git", "init"], cwd=target_dir, check=True)
        print(f"Initialized git repository in {target_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing git: {e}")

def create_gitignore(target_dir):
    """Create a .gitignore file optimized for marketing/creative projects."""
    gitignore_content = """# System
.DS_Store
Thumbs.db
desktop.ini

# Python
__pycache__/
*.py[cod]
.venv/
env/

# Adobe / Creative
*.tmp
*.temp
~$*

# Large Media (Consider git-lfs for these if needed, but ignored by default to save space)
*.mp4
*.mov
# *.psd # Uncomment if you want to ignore source files
# *.ai  # Uncomment if you want to ignore source files

# Local Logs
*.log
"""
    with open(os.path.join(target_dir, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print("Created .gitignore")

def init_project(target_dir):
    target_path = Path(target_dir).resolve()
    target_path.mkdir(parents=True, exist_ok=True)
    
    # 1. Create Directory Structure
    folders = [
        "campaigns", 
        "assets/images", 
        "assets/videos", 
        "assets/copy", 
        "reports",
        "scripts"
    ]
    
    for folder in folders:
        (target_path / folder).mkdir(parents=True, exist_ok=True)
        # Create .gitkeep to ensure folder is tracked
        with open((target_path / folder / ".gitkeep"), "w") as f:
            f.write("")
            
    print(f"Created directory structure in {target_path}")

    # 2. Copy Template README
    script_dir = Path(__file__).resolve().parent
    template_path = script_dir.parent / "references" / "marketing-readme.md"
    
    if template_path.exists():
        readme_dest = target_path / "README.md"
        if not readme_dest.exists():
            shutil.copy(template_path, readme_dest)
            print("Created README.md from template")
        else:
            print("README.md already exists, skipping template copy.")
    else:
        print(f"Warning: Template not found at {template_path}")

    # 3. Setup Git
    if not (target_path / ".git").exists():
        setup_git(target_path)
    
    create_gitignore(target_path)
    
    print("\nProject initialized successfully!")
    print("NEXT STEPS:")
    print("1. Open README.md and fill in 'Business Goal', 'Objective', and 'Hypotheses'.")
    print("2. Commit the initial structure.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a Marketing Engineering project.")
    parser.add_argument("--target", default=".", help="Target directory for the project (default: current dir)")
    args = parser.parse_args()
    
    init_project(args.target)
