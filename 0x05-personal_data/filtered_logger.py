#!/usr/bin/env python3
"""
    Obfuscated and replace with regex
    Provide Log formatter
    Create logger
"""
import re
from typing import List
import logging

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.__fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
            Set the format of the record
            Args:
                record: Log record of a event
            Return:
                The function overloaded to make a new log with all items
        """
        message = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.__fields, self.REDACTION,
                            message, self.SEPARATOR)

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
