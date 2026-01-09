"""
Shared value objects and lightweight types for edx-when.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from opaque_keys.edx.keys import CourseKey


@dataclass(frozen=True)
class CourseRef:
    """
    Immutable container for course identity.

    Args:
        course_key: Course identifier as CourseKey or its string representation.
        course_display_name: Human-readable course name to persist alongside content dates.
    """

    course_key: Union[CourseKey, str]
    course_display_name: str
