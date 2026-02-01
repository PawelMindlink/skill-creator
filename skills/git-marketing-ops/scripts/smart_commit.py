#!/usr/bin/env python3
import subprocess
import inquirer # pip install inquirer
import sys
import os

# Note: Ideally this script would use `inquirer` for a nice UI.
# However, to be dependency-free for standard environments, we'll use simple input() if inquirer isn't around.
# Or we can assume the agent environment has basic python.
# For robustness, we will implement a simple prompt fallback.

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def simple_prompt(question, options=None):
    print(f"\n{question}")
    if options:
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")
        selection = input("Select number or type value: ")
        try:
            idx = int(selection) - 1
            if 0 <= idx < len(options):
                return options[idx]
        except ValueError:
            pass
        return selection
    return input("> ")

def get_staged_files():
    res = run_command("git diff --cached --name-only")
    return res.stdout.strip().split('\n') if res.stdout.strip() else []

def smart_commit():
    print("--- 🎨 Marketing Smart Commit ---")
    
    # 1. Check Status
    staged = get_staged_files()
    if not staged:
        print("Nothing staged! Do you want to stage all changes?")
        if simple_prompt("Stage all? (y/n)").lower() == 'y':
            run_command("git add .")
            staged = get_staged_files()
            if not staged:
                print("Still nothing to commit. Exiting.")
                sys.exit(0)
        else:
            print("Please stage changes using 'git add' first.")
            sys.exit(1)
            
    print(f"Staged files: {len(staged)}")
    
    # 2. Select Type
    types = [
        "feat    (New functionality or major asset)",
        "content (Creative content: Copy, Images, Videos)",
        "design  (Visuals: CSS, Layout, Colors)",
        "analytics (Tracking: GTM, GA4, Pixels)",
        "config  (Settings: Audience, Targeting)",
        "fix     (Bug fix, typo correction)",
        "chore   (Maintenance, cleanup)"
    ]
    
    ctype_raw = simple_prompt("Select Change Type:", types)
    ctype = ctype_raw.split()[0] # extract 'feat' from 'feat (New...)'
    
    # 3. Select Scope
    scope = simple_prompt("Enter Scope (e.g. black-friday, hero-banner, meta):")
    if not scope:
        scope = "global"
        
    # 4. Description
    desc = simple_prompt("Short Description (imperative mood, e.g. 'update hero image'):")
    
    # 5. Construct Message
    message = f"{ctype}({scope}): {desc}"
    
    print(f"\nCommit Message: {message}")
    if simple_prompt("Commit now? (y/n)").lower() == 'y':
        res = run_command(f'git commit -m "{message}"')
        if res.returncode == 0:
            print("✅ Commit successful!")
            
            # 6. Push?
            if simple_prompt("Push to remote? (y/n)").lower() == 'y':
                print("Pushing...")
                push_res = run_command("git push")
                if push_res.returncode == 0:
                    print("🚀 Pushed successfully.")
                else:
                    print(f"❌ Push failed: {push_res.stderr}")
        else:
            print(f"❌ Commit failed: {res.stderr}")

if __name__ == "__main__":
    try:
        smart_commit()
    except KeyboardInterrupt:
        print("\nCancelled.")
