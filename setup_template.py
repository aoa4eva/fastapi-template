#!/usr/bin/env python3
"""
Template Setup Script

This script configures the FastAPI template for a new project by:
- Collecting project information
- Renaming the package directory
- Updating all imports and references
- Customizing configuration files
- Cleaning up template files

Usage:
    python setup_template.py

Or non-interactively:
    python setup_template.py --name my-project --author "Your Name" --email your@email.com
"""

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import Optional


class TemplateSetup:
    """Handle template setup and configuration."""

    def __init__(
        self,
        project_name: Optional[str] = None,
        description: Optional[str] = None,
        author: Optional[str] = None,
        email: Optional[str] = None,
        github_user: Optional[str] = None,
        interactive: bool = True,
    ):
        self.root = Path(__file__).parent
        self.interactive = interactive
        self.old_name = "generaltemplate"

        # Collect project info
        if interactive:
            self.collect_info()
        else:
            self.project_name = project_name or "myproject"
            self.description = description or "A FastAPI project"
            self.author = author or "Your Name"
            self.email = email or "your.email@example.com"
            self.github_user = github_user or "aoa4eva"

        # Derive package name (valid Python identifier)
        self.package_name = self._to_valid_package_name(self.project_name)

        # Paths
        self.old_src_path = self.root / "src" / self.old_name
        self.new_src_path = self.root / "src" / self.package_name

    def collect_info(self):
        """Interactively collect project information."""
        print("=" * 60)
        print("FastAPI Template Setup")
        print("=" * 60)
        print()
        print("This script will configure the template for your new project.")
        print("Press Enter to use default values shown in [brackets].")
        print()

        self.project_name = self._prompt(
            "Project name",
            default="my-fastapi-project",
            help_text="Kebab-case recommended (e.g., my-api-project)",
        )

        self.package_name = self._prompt(
            "Package name",
            default=self._to_valid_package_name(self.project_name),
            help_text="Python package name (letters, numbers, underscores only)",
        )

        self.description = self._prompt(
            "Project description",
            default="A FastAPI application",
        )

        self.author = self._prompt(
            "Author name",
            default="Your Name",
        )

        self.email = self._prompt(
            "Author email",
            default="your.email@example.com",
        )

        self.github_user = self._prompt(
            "GitHub username",
            default="aoa4eva",
        )

        print()
        print("=" * 60)
        print("Configuration Summary:")
        print("=" * 60)
        print(f"Project Name:    {self.project_name}")
        print(f"Package Name:    {self.package_name}")
        print(f"Description:     {self.description}")
        print(f"Author:          {self.author} <{self.email}>")
        print(f"GitHub User:     {self.github_user}")
        print("=" * 60)
        print()

        confirm = input("Proceed with setup? [Y/n]: ").strip().lower()
        if confirm and confirm != "y":
            print("Setup cancelled.")
            sys.exit(0)

    def _prompt(
        self, field: str, default: str = "", help_text: str = ""
    ) -> str:
        """Prompt user for input with default value."""
        prompt = f"{field}"
        if help_text:
            prompt += f"\n  ({help_text})"
        prompt += f"\n  [{default}]: "

        value = input(prompt).strip()
        return value if value else default

    def _to_valid_package_name(self, name: str) -> str:
        """Convert project name to valid Python package name."""
        # Replace hyphens and spaces with underscores
        name = re.sub(r"[-\s]+", "_", name.lower())
        # Remove invalid characters
        name = re.sub(r"[^a-z0-9_]", "", name)
        # Ensure it doesn't start with a number
        if name and name[0].isdigit():
            name = f"_{name}"
        return name or "myproject"

    def run(self):
        """Execute the setup process."""
        print()
        print("Starting setup process...")
        print()

        try:
            self.rename_package_directory()
            self.update_python_imports()
            self.update_pyproject_toml()
            self.update_dockerfile()
            self.update_docker_compose()
            self.update_makefile()
            self.update_github_workflows()
            self.update_readme()
            self.update_env_example()
            self.cleanup_template_files()

            print()
            print("=" * 60)
            print("✓ Setup Complete!")
            print("=" * 60)
            print()
            print("Next steps:")
            print(f"  1. Review the updated files")
            print(f"  2. Initialize git: git init && git add . && git commit -m 'Initial commit'")
            print(f"  3. Install dependencies: ./install.sh or make install-pip")
            print(f"  4. Start development: ./run.sh or .venv/bin/uvicorn {self.package_name}.main:app --reload")
            print()
            print(f"Your API will be available at: http://localhost:8000")
            print(f"API Documentation: http://localhost:8000/docs")
            print()

        except Exception as e:
            print(f"Error during setup: {e}", file=sys.stderr)
            sys.exit(1)

    def rename_package_directory(self):
        """Rename the package directory from generaltemplate to new name."""
        print(f"[1/10] Renaming package directory: {self.old_name} → {self.package_name}")

        if not self.old_src_path.exists():
            print(f"  Warning: {self.old_src_path} not found, skipping rename")
            return

        if self.old_src_path == self.new_src_path:
            print(f"  Skipping: Already using package name '{self.package_name}'")
            return

        if self.new_src_path.exists():
            print(f"  Error: {self.new_src_path} already exists!")
            sys.exit(1)

        self.old_src_path.rename(self.new_src_path)
        print(f"  ✓ Renamed to: {self.new_src_path}")

    def update_python_imports(self):
        """Update all Python imports to use new package name."""
        print(f"[2/10] Updating Python imports: {self.old_name} → {self.package_name}")

        python_files = list(self.root.rglob("*.py"))
        updated_count = 0

        for file_path in python_files:
            if ".venv" in file_path.parts or "__pycache__" in file_path.parts:
                continue

            content = file_path.read_text()
            updated_content = content.replace(
                f"from {self.old_name}.",
                f"from {self.package_name}."
            ).replace(
                f"import {self.old_name}.",
                f"import {self.package_name}."
            ).replace(
                f'"{self.old_name}.',
                f'"{self.package_name}.'
            )

            if updated_content != content:
                file_path.write_text(updated_content)
                updated_count += 1

        print(f"  ✓ Updated {updated_count} Python files")

    def update_pyproject_toml(self):
        """Update pyproject.toml with new project information."""
        print(f"[3/10] Updating pyproject.toml")

        pyproject_path = self.root / "pyproject.toml"
        content = pyproject_path.read_text()

        # Update project metadata
        content = re.sub(
            r'name = ".*?"',
            f'name = "{self.project_name}"',
            content
        )
        content = re.sub(
            r'description = ".*?"',
            f'description = "{self.description}"',
            content
        )

        # Update author
        content = re.sub(
            r'{ name = ".*?", email = ".*?" }',
            f'{{ name = "{self.author}", email = "{self.email}" }}',
            content
        )

        # Update URLs
        repo_url = f"https://github.com/{self.github_user}/{self.project_name}"
        content = re.sub(
            r'Homepage = ".*?"',
            f'Homepage = "{repo_url}"',
            content
        )
        content = re.sub(
            r'Repository = ".*?"',
            f'Repository = "{repo_url}"',
            content
        )
        content = re.sub(
            r'Issues = ".*?"',
            f'Issues = "{repo_url}/issues"',
            content
        )

        # Update package references
        content = content.replace(
            f'["{self.old_name}"]',
            f'["{self.package_name}"]'
        ).replace(
            f'"{self.old_name}.',
            f'"{self.package_name}.'
        ).replace(
            f'"{self.old_name}"]',
            f'"{self.package_name}"]'
        )

        # Update script entry point
        content = re.sub(
            r'generaltemplate = ".*?"',
            f'{self.package_name} = "{self.package_name}.main:main"',
            content
        )

        # Update known-first-party
        content = re.sub(
            r'known-first-party = \[".*?"\]',
            f'known-first-party = ["{self.package_name}"]',
            content
        )

        pyproject_path.write_text(content)
        print(f"  ✓ Updated project metadata")

    def update_dockerfile(self):
        """Update Dockerfile with new package name."""
        print(f"[4/10] Updating Dockerfile")

        dockerfile_path = self.root / "Dockerfile"
        content = dockerfile_path.read_text()

        content = content.replace(
            f'uvicorn generaltemplate.main:app',
            f'uvicorn {self.package_name}.main:app'
        )

        dockerfile_path.write_text(content)
        print(f"  ✓ Updated Dockerfile")

    def update_docker_compose(self):
        """Update docker-compose.yml with new project name."""
        print(f"[5/10] Updating docker-compose.yml")

        compose_path = self.root / "docker-compose.yml"
        content = compose_path.read_text()

        # Update container names
        content = content.replace(
            "generaltemplate-api",
            f"{self.project_name}-api"
        ).replace(
            "generaltemplate-db",
            f"{self.project_name}-db"
        ).replace(
            "generaltemplate-redis",
            f"{self.project_name}-redis"
        ).replace(
            "generaltemplate-pass",
            f"{self.project_name}-pass"
        )

        # Update database name
        content = content.replace(
            "POSTGRES_DB: generaltemplate",
            f"POSTGRES_DB: {self.package_name}"
        )

        # Update uvicorn command
        content = content.replace(
            "uvicorn generaltemplate.main:app",
            f"uvicorn {self.package_name}.main:app"
        )

        compose_path.write_text(content)
        print(f"  ✓ Updated docker-compose.yml")

    def update_makefile(self):
        """Update Makefile with new package name."""
        print(f"[6/10] Updating Makefile")

        makefile_path = self.root / "Makefile"
        content = makefile_path.read_text()

        content = content.replace(
            f"docker build -t generaltemplate:latest",
            f"docker build -t {self.project_name}:latest"
        ).replace(
            f"docker run -p 8000:8000 --env-file .env generaltemplate:latest",
            f"docker run -p 8000:8000 --env-file .env {self.project_name}:latest"
        ).replace(
            f"uvicorn generaltemplate.main:app",
            f"uvicorn {self.package_name}.main:app"
        )

        makefile_path.write_text(content)
        print(f"  ✓ Updated Makefile")

    def update_github_workflows(self):
        """Update GitHub Actions workflows."""
        print(f"[7/10] Updating GitHub Actions workflows")

        workflow_path = self.root / ".github" / "workflows" / "ci.yml"
        if not workflow_path.exists():
            print(f"  Warning: {workflow_path} not found, skipping")
            return

        content = workflow_path.read_text()

        content = content.replace(
            "generaltemplate:latest",
            f"{self.project_name}:latest"
        ).replace(
            "generaltemplate:",
            f"{self.project_name}:"
        ).replace(
            "aoa4eva/generaltemplate",
            f"{self.github_user}/{self.project_name}"
        )

        workflow_path.write_text(content)
        print(f"  ✓ Updated CI workflow")

    def update_readme(self):
        """Update README.md with new project information."""
        print(f"[8/10] Updating README.md")

        readme_path = self.root / "README.md"
        content = readme_path.read_text()

        # Update title
        content = re.sub(
            r"# FastAPI Project Template",
            f"# {self.project_name}",
            content
        )

        # Update first description line
        content = re.sub(
            r"A production-ready FastAPI project template.*",
            self.description,
            content
        )

        # Update repository URLs
        content = content.replace(
            "aoa4eva/generaltemplate",
            f"{self.github_user}/{self.project_name}"
        ).replace(
            "generaltemplate/",
            f"{self.project_name}/"
        )

        # Update package references
        content = content.replace(
            "generaltemplate",
            self.package_name
        )

        # Update clone example
        content = re.sub(
            r"git clone .* my-new-project",
            f"# This is your project, already cloned!\ncd {self.project_name}",
            content
        )

        # Remove template-specific instructions
        content = re.sub(
            r"### Quick Start.*?## Development",
            f"### Quick Start\n\n```bash\n# Install dependencies\n./install.sh\n\n# Run the development server\n./run.sh\n```\n\nVisit [http://localhost:8000](http://localhost:8000) to see your API!\n\n## Development",
            content,
            flags=re.DOTALL
        )

        readme_path.write_text(content)
        print(f"  ✓ Updated README.md")

    def update_env_example(self):
        """Update .env.example with new project name."""
        print(f"[9/10] Updating .env.example")

        env_path = self.root / ".env.example"
        content = env_path.read_text()

        content = content.replace(
            "APP_NAME=generaltemplate",
            f"APP_NAME={self.package_name}"
        ).replace(
            "generaltemplate.db",
            f"{self.package_name}.db"
        ).replace(
            "/dbname",
            f"/{self.package_name}"
        )

        env_path.write_text(content)
        print(f"  ✓ Updated .env.example")

    def cleanup_template_files(self):
        """Remove template-specific files that aren't needed."""
        print(f"[10/10] Cleaning up template files")

        files_to_remove = [
            "setup_template.py",  # This script itself
            "PLAN.md",  # Template design document
        ]

        removed_count = 0
        for filename in files_to_remove:
            file_path = self.root / filename
            if file_path.exists():
                # Don't actually remove this script until we're done!
                if filename == "setup_template.py":
                    print(f"  Note: Remove {filename} manually after setup")
                else:
                    file_path.unlink()
                    removed_count += 1
                    print(f"  ✓ Removed {filename}")

        if removed_count > 0:
            print(f"  ✓ Cleaned up {removed_count} template files")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Configure FastAPI template for a new project"
    )
    parser.add_argument(
        "--name",
        help="Project name (e.g., my-api-project)",
    )
    parser.add_argument(
        "--description",
        help="Project description",
    )
    parser.add_argument(
        "--author",
        help="Author name",
    )
    parser.add_argument(
        "--email",
        help="Author email",
    )
    parser.add_argument(
        "--github-user",
        help="GitHub username",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Run without prompts (use with other flags)",
    )

    args = parser.parse_args()

    # Determine if we should be interactive
    interactive = not args.non_interactive

    if args.non_interactive and not args.name:
        print("Error: --name is required in non-interactive mode", file=sys.stderr)
        sys.exit(1)

    setup = TemplateSetup(
        project_name=args.name,
        description=args.description,
        author=args.author,
        email=args.email,
        github_user=args.github_user,
        interactive=interactive,
    )

    setup.run()


if __name__ == "__main__":
    main()
