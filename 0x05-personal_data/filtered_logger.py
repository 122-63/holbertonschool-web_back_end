#!/usr/bin/env python3
"""
    Obfuscated and replace with regex
    Provide Log formatter
    Create logger
"""

from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Set the format of the record
        Return:
            The function overloaded to make a new log with all items
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get a point of connection toward the database
        Return:
            A connection toward the database
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"))


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        Filter and obfuscated the string
        Args:
            fields: a list of strings representing all fields to obfuscate
                    ["password", "date_of_birth"]
            redaction: a string representing by what the
                       field will be obfuscated
                       "XXXXX"
            message: a string representing the log line
                    ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"]
                    ["name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]
            separator: a string representing by which character is
                    separating all fields in the log line (message)
                    ";"
        Return:
            String with string ofuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message

def main():
    """Entry Point"""
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    column_names = [column[0] for column in cursor.description]
    log = get_logger()

    for record in cursor:
        message = ''.join(f'{column}={value}{RedactingFormatter.SEPARATOR} '
                          for column, value in zip(column_names, record))
        log.info(message)

    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
