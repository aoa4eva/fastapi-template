"""
Template setup module - can be imported and used programmatically.

This module can be used in multiple ways:

1. As a standalone script:
   python setup_template.py

2. As a Python module:
   python -m generaltemplate.setup

3. As a library:
   from generaltemplate.setup import TemplateSetup
   setup = TemplateSetup(...)
   setup.run()

4. As a cookiecutter alternative:
   from generaltemplate.setup import setup_template
   setup_template(name="my-api", author="Jane Doe")
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


class TemplateSetup:
    """Handle template setup and configuration."""

    def __init__(
        self,
        root_dir: Optional[Path] = None,
        project_name: Optional[str] = None,
        description: Optional[str] = None,
        author: Optional[str] = None,
        email: Optional[str] = None,
        github_user: Optional[str] = None,
        interactive: bool = True,
    ):
        # Allow specifying root directory or auto-detect
        if root_dir:
            self.root = Path(root_dir)
        else:
            # Try to find the project root
            current = Path.cwd()
            if (current / "pyproject.toml").exists():
                self.root = current
            elif (current.parent / "pyproject.toml").exists():
                self.root = current.parent
            elif (current.parent.parent / "pyproject.toml").exists():
                self.root = current.parent.parent
            else:
                self.root = current

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

    def _prompt(self, field: str, default: str = "", help_text: str = "") -> str:
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

            return True

        except Exception as e:
            print(f"Error during setup: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            return False

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
            raise FileExistsError(f"{self.new_src_path} already exists")

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

            try:
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
            except Exception as e:
                print(f"  Warning: Could not update {file_path}: {e}")

        print(f"  ✓ Updated {updated_count} Python files")

    def update_pyproject_toml(self):
        """Update pyproject.toml with new project information."""
        print(f"[3/10] Updating pyproject.toml")

        pyproject_path = self.root / "pyproject.toml"
        content = pyproject_path.read_text()

        # Update project metadata
        content = re.sub(r'name = ".*?"', f'name = "{self.project_name}"', content)
        content = re.sub(r'description = ".*?"', f'description = "{self.description}"', content)

        # Update author
        content = re.sub(
            r'{ name = ".*?", email = ".*?" }',
            f'{{ name = "{self.author}", email = "{self.email}" }}',
            content
        )

        # Update URLs
        repo_url = f"https://github.com/{self.github_user}/{self.project_name}"
        content = re.sub(r'Homepage = ".*?"', f'Homepage = "{repo_url}"', content)
        content = re.sub(r'Repository = ".*?"', f'Repository = "{repo_url}"', content)
        content = re.sub(r'Issues = ".*?"', f'Issues = "{repo_url}/issues"', content)

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
        if not dockerfile_path.exists():
            print(f"  Warning: Dockerfile not found, skipping")
            return

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
        if not compose_path.exists():
            print(f"  Warning: docker-compose.yml not found, skipping")
            return

        content = compose_path.read_text()

        # Update container names and references
        content = content.replace("generaltemplate-", f"{self.project_name}-")
        content = content.replace(
            "POSTGRES_DB: generaltemplate",
            f"POSTGRES_DB: {self.package_name}"
        )
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
        if not makefile_path.exists():
            print(f"  Warning: Makefile not found, skipping")
            return

        content = makefile_path.read_text()
        content = content.replace("generaltemplate", self.package_name)
        content = content.replace(self.package_name, self.project_name, content.count("docker"))

        makefile_path.write_text(content)
        print(f"  ✓ Updated Makefile")

    def update_github_workflows(self):
        """Update GitHub Actions workflows."""
        print(f"[7/10] Updating GitHub Actions workflows")

        workflow_path = self.root / ".github" / "workflows" / "ci.yml"
        if not workflow_path.exists():
            print(f"  Warning: GitHub workflow not found, skipping")
            return

        content = workflow_path.read_text()
        content = content.replace("generaltemplate", self.project_name)
        content = content.replace(
            "aoa4eva",
            self.github_user
        )

        workflow_path.write_text(content)
        print(f"  ✓ Updated CI workflow")

    def update_readme(self):
        """Update README.md with new project information."""
        print(f"[8/10] Updating README.md")

        readme_path = self.root / "README.md"
        if not readme_path.exists():
            print(f"  Warning: README.md not found, skipping")
            return

        content = readme_path.read_text()

        # Update title and description
        content = re.sub(r"# FastAPI Project Template", f"# {self.project_name}", content)
        content = re.sub(
            r"A production-ready FastAPI project template.*",
            self.description,
            content
        )

        # Update URLs and references
        content = content.replace("aoa4eva/generaltemplate", f"{self.github_user}/{self.project_name}")
        content = content.replace("generaltemplate", self.package_name)

        readme_path.write_text(content)
        print(f"  ✓ Updated README.md")

    def update_env_example(self):
        """Update .env.example with new project name."""
        print(f"[9/10] Updating .env.example")

        env_path = self.root / ".env.example"
        if not env_path.exists():
            print(f"  Warning: .env.example not found, skipping")
            return

        content = env_path.read_text()
        content = content.replace("APP_NAME=generaltemplate", f"APP_NAME={self.package_name}")
        content = content.replace("generaltemplate", self.package_name)

        env_path.write_text(content)
        print(f"  ✓ Updated .env.example")

    def cleanup_template_files(self):
        """Remove template-specific files that aren't needed."""
        print(f"[10/10] Cleaning up template files")

        files_to_note = [
            "setup_template.py",
            "PLAN.md",
            "SETUP.md",
        ]

        print(f"  Note: Manually remove these files if desired:")
        for filename in files_to_note:
            file_path = self.root / filename
            if file_path.exists():
                print(f"    - {filename}")


def setup_template(
    name: str,
    description: str = "A FastAPI application",
    author: str = "Your Name",
    email: str = "your.email@example.com",
    github_user: str = "aoa4eva",
    root_dir: Optional[Path] = None,
) -> bool:
    """
    Convenience function for programmatic template setup.

    Args:
        name: Project name
        description: Project description
        author: Author name
        email: Author email
        github_user: GitHub username
        root_dir: Root directory of the template (auto-detected if None)

    Returns:
        bool: True if setup succeeded, False otherwise

    Example:
        >>> from generaltemplate.setup import setup_template
        >>> setup_template(
        ...     name="my-awesome-api",
        ...     description="An awesome API",
        ...     author="Jane Doe",
        ...     email="jane@example.com",
        ...     github_user="janedoe"
        ... )
    """
    setup = TemplateSetup(
        root_dir=root_dir,
        project_name=name,
        description=description,
        author=author,
        email=email,
        github_user=github_user,
        interactive=False,
    )

    return setup.run()


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(description="Configure FastAPI template for a new project")
    parser.add_argument("--name", help="Project name (e.g., my-api-project)")
    parser.add_argument("--description", help="Project description")
    parser.add_argument("--author", help="Author name")
    parser.add_argument("--email", help="Author email")
    parser.add_argument("--github-user", help="GitHub username")
    parser.add_argument("--non-interactive", action="store_true", help="Run without prompts")
    parser.add_argument("--root", help="Root directory of the template", type=Path)

    args = parser.parse_args()

    interactive = not args.non_interactive

    if args.non_interactive and not args.name:
        print("Error: --name is required in non-interactive mode", file=sys.stderr)
        sys.exit(1)

    setup = TemplateSetup(
        root_dir=args.root,
        project_name=args.name,
        description=args.description,
        author=args.author,
        email=args.email,
        github_user=args.github_user,
        interactive=interactive,
    )

    success = setup.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
