"""
API routers module.

This package contains all API route handlers organized by domain.
Each router should focus on a specific resource or feature.
"""

from generaltemplate.api import health, items

__all__ = ["health", "items"]
