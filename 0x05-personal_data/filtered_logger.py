#!/usr/bin/env python3
"""
    Obfuscated and replace with regex
    Provide Log formatter
    Create logger
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated message given its fields and its redaction.
    Args:
        fields: The fields of the message to be redacted.
        redaction: The redaction of each field's value.
        message: The message to be redacted.
        separator: The separator character between each field.
    Returns:
        The message redacted.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
