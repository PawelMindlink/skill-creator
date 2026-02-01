#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def check_readme(target_path):
    readme_path = target_path / "README.md"
    if not readme_path.exists():
        return False, ["❌ Missing README.md"]
    
    with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    required_sections = [
        "Definition",
        "Structure",
        "Operation"
    ]
    
    missing = [sec for sec in required_sections if sec not in content]
    
    if missing:
        return True, [f"⚠️  README exists but missing sections: {', '.join(missing)}"]
    
    return True, ["✅ README follows 'Definition/Structure/Operation' standard."]

def check_structure(target_path):
    feedback = []
    
    # Check for loose files in root that should be organized
    root_files = [f for f in os.listdir(target_path) if os.path.isfile(target_path / f)]
    media_extensions = ['.png', '.jpg', '.mp4', '.mov', '.psd']
    loose_media = [f for f in root_files if any(f.lower().endswith(ext) for ext in media_extensions)]
    
    if loose_media:
        feedback.append(f"⚠️  Found loose media files in root ({len(loose_media)} files). Move them to 'assets/'.")
        
    # Check standard folders
    expected_folders = ["campaigns", "assets"]
    for folder in expected_folders:
        if not (target_path / folder).exists():
            feedback.append(f"ℹ️  Consider creating '{folder}/' to organize work.")
            
    return feedback

def audit_repo(target_dir):
    target_path = Path(target_dir).resolve()
    print(f"Auditing: {target_path}\n")
    
    has_readme, readme_notes = check_readme(target_path)
    structure_notes = check_structure(target_path)
    
    all_notes = readme_notes + structure_notes
    
    for note in all_notes:
        print(note)
        
    print("\n--- AGENT ACTION REQUIRED ---")
    if not has_readme:
        print("ACTION: Generate a README.md using the 'marketing-readme' template.")
        print("CONTEXT: Analyze the file list and git history to infer the 'Business Goal' and 'Structure'.")
    elif "Missing sections" in str(readme_notes):
        print("ACTION: Edit README.md to include the missing sections.")
        print("CONTEXT: Refactor existing content into 'Definition' (Goals), 'Structure' (Map), 'Operation' (How-to).")
    elif not all_notes:
        print("STATUS: Project looks healthy.")

if __name__ == "__main__":
    target = "."
    if len(sys.argv) > 1:
        target = sys.argv[1]
    audit_repo(target)
