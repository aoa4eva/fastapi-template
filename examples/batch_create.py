#!/usr/bin/env python3
"""
Example: Create multiple projects from the template in batch.

This is useful when you need to scaffold multiple microservices
or related APIs from the same template.
"""

import shutil
from pathlib import Path
from generaltemplate.setup import TemplateSetup

# Define your projects
projects = [
    {
        "name": "user-service",
        "description": "User authentication and management service",
    },
    {
        "name": "product-service",
        "description": "Product catalog and inventory service",
    },
    {
        "name": "order-service",
        "description": "Order processing and fulfillment service",
    },
    {
        "name": "notification-service",
        "description": "Email and SMS notification service",
    },
]

# Configuration
template_source = Path(__file__).parent.parent  # generaltemplate directory
output_base = Path("/tmp/microservices")  # Where to create projects
output_base.mkdir(exist_ok=True)

# Common metadata for all projects
common_config = {
    "author": "Your Company DevOps",
    "email": "devops@company.com",
    "github_user": "your-company",
}

print(f"Creating {len(projects)} projects...")
print(f"Template: {template_source}")
print(f"Output:   {output_base}")
print()

# Create each project
created = []
failed = []

for project in projects:
    print(f"Creating {project['name']}...")

    # Create project directory
    project_dir = output_base / project["name"]

    try:
        # Copy template to new location
        if project_dir.exists():
            print(f"  Warning: {project_dir} exists, skipping copy")
        else:
            shutil.copytree(template_source, project_dir, ignore=shutil.ignore_patterns(
                '.venv', '__pycache__', '*.pyc', '.git', '.idea', 'examples'
            ))

        # Run setup
        setup = TemplateSetup(
            root_dir=project_dir,
            project_name=project["name"],
            description=project["description"],
            interactive=False,
            **common_config,
        )

        success = setup.run()

        if success:
            created.append(project["name"])
            print(f"  ✓ Created successfully\n")
        else:
            failed.append(project["name"])
            print(f"  ✗ Setup failed\n")

    except Exception as e:
        failed.append(project["name"])
        print(f"  ✗ Error: {e}\n")

# Summary
print("=" * 60)
print("Batch Creation Summary")
print("=" * 60)
print(f"Created:  {len(created)}/{len(projects)}")
if created:
    for name in created:
        print(f"  ✓ {name}")

if failed:
    print(f"\nFailed:   {len(failed)}/{len(projects)}")
    for name in failed:
        print(f"  ✗ {name}")

print()
print(f"Projects created in: {output_base}")
print()
print("Next steps for each project:")
print("  cd <project-name>")
print("  ./install.sh")
print("  ./run.sh")
