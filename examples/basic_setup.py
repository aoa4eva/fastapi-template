#!/usr/bin/env python3
"""
Basic example of using the template setup library.

This script demonstrates how to use the template as a Python library
to programmatically create a new FastAPI project.
"""

from generaltemplate.setup import setup_template

# Option 1: Simple function call
print("Creating new project...")

success = setup_template(
    name="my-awesome-api",
    description="An awesome API for my project",
    author="Jane Doe",
    email="jane@example.com",
    github_user="janedoe"
)

if success:
    print("\n✓ Project created successfully!")
    print("\nNext steps:")
    print("  cd my-awesome-api")
    print("  ./install.sh")
    print("  ./run.sh")
else:
    print("\n✗ Project creation failed!")

# Option 2: Using the TemplateSetup class for more control
from pathlib import Path
from generaltemplate.setup import TemplateSetup

setup = TemplateSetup(
    root_dir=Path.cwd(),  # Use current directory
    project_name="another-api",
    description="Another API project",
    author="John Smith",
    email="john@example.com",
    github_user="johnsmith",
    interactive=False  # No prompts
)

# You can access properties before running
print(f"\nPackage name will be: {setup.package_name}")
print(f"New path will be: {setup.new_src_path}")

# Run the setup
# success = setup.run()
