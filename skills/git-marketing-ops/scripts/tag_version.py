#!/usr/bin/env python3
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def get_latest_tag():
    res = run_command("git describe --tags --abbrev=0")
    if res.returncode != 0:
        return None
    return res.stdout.strip()

def tag_version():
    print("--- 🔖 Marketing Release Tagging ---")
    
    latest = get_latest_tag()
    print(f"Current Latest Tag: {latest if latest else 'None'}")
    
    print("\nChoose Version Bump:")
    print("1. Major (Launch / Rebrand)        -> v1.0.0")
    print("2. Minor (New Wave / Variant)      -> v1.1.0")
    print("3. Patch (Typo / Quick fix)        -> v1.0.1")
    
    choice = input("Select (1-3): ")
    
    # Simple logic for version bumping
    if not latest:
        major, minor, patch = 0, 0, 0
    else:
        # Strip 'v' if present
        v_str = latest.lstrip('v')
        try:
            parts = list(map(int, v_str.split('.')))
            if len(parts) < 3: parts += [0] * (3 - len(parts))
            major, minor, patch = parts
        except ValueError:
             print("Could not parse current tag. Starting from 0.0.0")
             major, minor, patch = 0, 0, 0

    if choice == '1':
        major += 1; minor = 0; patch = 0
    elif choice == '2':
        minor += 1; patch = 0
    elif choice == '3':
        patch += 1
    else:
        print("Invalid choice.")
        sys.exit(1)
        
    new_tag = f"v{major}.{minor}.{patch}"
    print(f"\nNew Tag: {new_tag}")
    
    notes = input("Release Notes (e.g. 'Campaign Q3 Launch'): ")
    msg = f"{new_tag}: {notes}"
    
    if input("Create Tag? (y/n): ").lower() == 'y':
        res = run_command(f'git tag -a {new_tag} -m "{msg}"')
        if res.returncode == 0:
            print("✅ Tag created.")
            if input("Push tags to remote? (y/n): ").lower() == 'y':
                run_command("git push --tags")
                print("🚀 Tags pushed.")
        else:
            print(f"❌ Failed to tag: {res.stderr}")

if __name__ == "__main__":
    tag_version()
