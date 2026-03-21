# Contributing to FastAPI Template

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the Python and FastAPI community standards

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/aoa4eva/fastapi-template/issues)
2. If not, create a new issue using the bug report template
3. Include:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Relevant logs or error messages

### Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue using the feature request template
3. Explain:
   - The problem you're trying to solve
   - Your proposed solution
   - Alternative solutions you've considered
   - Whether you can help implement it

### Pull Requests

1. **Fork the repository**
   ```bash
   gh repo fork aoa4eva/fastapi-template --clone
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Install dependencies
   make install-pip

   # Run linter
   make lint

   # Run tests
   make test

   # Test setup script
   python setup_template.py --name test-project --non-interactive
   ```

5. **Commit with clear messages**
   ```bash
   git add .
   git commit -m "Add feature: description of what you added"
   ```

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   gh pr create --web
   ```

## Development Setup

### Prerequisites

- Python 3.13+
- Git
- GitHub CLI (optional but recommended)

### Setup

```bash
# Clone your fork
git clone git@github.com:aoa4eva/fastapi-template.git
cd fastapi-template

# Install dependencies
./install.sh
# or
make install-pip

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run linter
make lint

# Auto-format code
make format
```

## Style Guidelines

### Python Code

- Follow PEP 8 style guide
- Use type hints for all functions
- Maximum line length: 100 characters
- Use ruff for formatting and linting
- Write docstrings for all public functions/classes

Example:
```python
def setup_template(
    name: str,
    description: str = "A FastAPI application",
    author: str = "Your Name",
) -> bool:
    """
    Configure the template for a new project.

    Args:
        name: Project name (e.g., "my-api-project")
        description: Project description
        author: Author name

    Returns:
        True if setup succeeded, False otherwise

    Example:
        >>> setup_template(name="my-api", author="Jane Doe")
        True
    """
    # Implementation
```

### Documentation

- Update README.md for user-facing changes
- Update SETUP.md for setup process changes
- Add docstrings to new functions/classes
- Include examples in documentation
- Keep language clear and concise

### Commit Messages

Follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add PostgreSQL support to setup script
fix: correct import paths in generated files
docs: update installation instructions
```

## What to Contribute

### High Priority

- Bug fixes
- Documentation improvements
- Test coverage improvements
- Performance optimizations
- Security improvements

### Feature Ideas

- Additional database support (MongoDB, Redis patterns)
- Authentication templates (OAuth, JWT)
- More CI/CD examples (GitLab, CircleCI)
- Deployment guides (AWS, GCP, Azure)
- Additional frontend framework examples
- GraphQL support
- WebSocket examples
- Background task patterns (Celery, APScheduler)

### Areas Needing Help

Check issues labeled:
- `good first issue` - Good for newcomers
- `help wanted` - We need community help
- `documentation` - Documentation improvements needed

## Testing Guidelines

### Unit Tests

- Test all public functions
- Use pytest fixtures for common setups
- Mock external dependencies
- Aim for 80%+ code coverage

Example:
```python
def test_setup_template_creates_files(tmp_path):
    """Test that setup creates expected files."""
    setup = TemplateSetup(
        root_dir=tmp_path,
        project_name="test-api",
        interactive=False
    )

    success = setup.run()

    assert success
    assert (tmp_path / "src" / "test_api").exists()
    assert (tmp_path / "pyproject.toml").exists()
```

### Integration Tests

- Test the full setup workflow
- Test Docker builds
- Test with different Python versions
- Test on different operating systems (via CI)

## Documentation Guidelines

### README Updates

- Keep the README focused on getting started
- Move detailed docs to separate files
- Include code examples
- Add screenshots for visual features
- Update table of contents

### Code Documentation

- Add docstrings to all public APIs
- Include parameter descriptions
- Add usage examples
- Document exceptions raised
- Link to related documentation

## Review Process

1. **Automated Checks**: CI will run linting and tests
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any feedback or requested changes
4. **Approval**: Once approved, your PR will be merged
5. **Release**: Changes will be included in the next release

## Questions?

- Open a [Discussion](https://github.com/aoa4eva/fastapi-template/discussions)
- Join our community chat (if applicable)
- Check existing issues and PRs
- Read the documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing!** 🎉
