# FastAPI Template Documentation

Complete documentation for the FastAPI project template.

## 📚 Table of Contents

### Getting Started
- [**Quick Start Guide**](QUICKSTART.md) - Get up and running in 5 minutes
- [**Setup Guide**](SETUP.md) - Complete template setup instructions
- [**Installation Options**](QUICKSTART.md#installation) - Different ways to install

### Advanced Usage
- [**Library Usage**](LIBRARY_USAGE.md) - Use the template as a Python library
- [**Setup Script API**](LIBRARY_USAGE.md#api-reference) - Programmatic usage documentation
- [**Batch Creation**](LIBRARY_USAGE.md#batch-project-creation) - Create multiple projects

### Architecture & Design
- [**Design Decisions**](PLAN.md) - Why we chose these tools and patterns
- [**Tool Choices**](PLAN.md#tool-choices) - uv, ruff, FastAPI, etc.
- [**Extension Patterns**](PLAN.md#extension-patterns) - How to extend the template

### GitHub & Deployment
- [**GitHub Setup**](GITHUB_SETUP.md) - Push your template to GitHub
- [**Repository Configuration**](GITHUB_SETUP.md#after-setup) - Topics, badges, settings
- [**CI/CD Pipeline**](../README.md#cicd) - GitHub Actions workflow

### Contributing
- [**Contributing Guide**](../CONTRIBUTING.md) - How to contribute
- [**Code of Conduct**](../CONTRIBUTING.md#code-of-conduct) - Community guidelines
- [**Development Setup**](../CONTRIBUTING.md#development-setup) - Set up for development

## 🎯 Quick Links

### Common Tasks

**First Time Setup:**
```bash
# Clone the template
git clone https://github.com/aoa4eva/fastapi-template.git my-project
cd my-project

# Run setup script
python setup_template.py

# Install dependencies
./install.sh

# Start development
./run.sh
```

**Using as Library:**
```python
from generaltemplate.setup import setup_template

setup_template(
    name="my-api",
    author="Your Name",
    email="your@email.com"
)
```

**Push to GitHub:**
```bash
./setup_repo.sh
```

### Documentation by Role

#### For Template Users
1. [Quick Start](QUICKSTART.md) - Start here!
2. [Setup Guide](SETUP.md) - Detailed setup instructions
3. [Main README](../README.md) - Project overview

#### For Developers
1. [Design Decisions](PLAN.md) - Understanding the architecture
2. [Contributing Guide](../CONTRIBUTING.md) - Making contributions
3. [Library Usage](LIBRARY_USAGE.md) - Programmatic usage

#### For DevOps/CI
1. [GitHub Setup](GITHUB_SETUP.md) - Repository automation
2. [Library Usage](LIBRARY_USAGE.md#cicd-integration) - CI/CD integration
3. [Deployment Patterns](../README.md#docker-deployment) - Deployment options

## 📖 Documentation Structure

```
docs/
├── README.md              # This file - documentation index
├── QUICKSTART.md          # 5-minute getting started guide
├── SETUP.md               # Complete setup instructions
├── LIBRARY_USAGE.md       # Using as a Python library
├── PLAN.md                # Architecture and design decisions
└── GITHUB_SETUP.md        # GitHub repository setup

Root directory:
├── README.md              # Project overview
├── CONTRIBUTING.md        # Contribution guidelines
└── LICENSE                # MIT License
```

## 🔍 Finding What You Need

### I want to...

**Create a new project from the template**
→ [Quick Start Guide](QUICKSTART.md)

**Understand why this template is designed this way**
→ [Design Decisions](PLAN.md)

**Use the template programmatically**
→ [Library Usage Guide](LIBRARY_USAGE.md)

**Push my template to GitHub**
→ [GitHub Setup Guide](GITHUB_SETUP.md)

**Contribute to the template**
→ [Contributing Guide](../CONTRIBUTING.md)

**Add a database / authentication / etc.**
→ [Extension Patterns](PLAN.md#extension-patterns)

**Deploy to production**
→ [Docker Deployment](../README.md#docker-deployment)

**Create multiple projects at once**
→ [Batch Creation](LIBRARY_USAGE.md#batch-project-creation)

## 💡 Tips

- Start with [QUICKSTART.md](QUICKSTART.md) if you're new
- Check [PLAN.md](PLAN.md) to understand design choices
- Use [LIBRARY_USAGE.md](LIBRARY_USAGE.md) for automation
- Read [CONTRIBUTING.md](../CONTRIBUTING.md) before submitting PRs

## 🆘 Getting Help

- **Issues**: [GitHub Issues](https://github.com/aoa4eva/fastapi-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/aoa4eva/fastapi-template/discussions)
- **Examples**: See the `examples/` directory in the repository

## 📝 Documentation Guidelines

When contributing documentation:

1. **Be Concise**: Get to the point quickly
2. **Use Examples**: Show, don't just tell
3. **Stay Current**: Update docs with code changes
4. **Link Related Content**: Help readers find more info
5. **Test Instructions**: Ensure commands actually work

## 🔄 Documentation Updates

This documentation is maintained alongside the code. If you find:
- ❌ Outdated information
- ❌ Broken links
- ❌ Missing explanations
- ❌ Unclear instructions

Please [open an issue](https://github.com/aoa4eva/fastapi-template/issues) or submit a PR!

---

**Last Updated**: 2024
**Maintained By**: [aoa4eva](https://github.com/aoa4eva)
