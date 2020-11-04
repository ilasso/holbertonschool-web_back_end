#!/usr/bin/env python3
"""filtered_logger:
module that contains function about personal data
"""
from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    Arguments:

    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
               all fields in the log line (message)
    """
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    function that takes no arguments and returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logging.propagate = False
    logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database
        (mysql.connector.connection.MySQLConnection object)
    """
    return mysql.connector.connect(
            host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
            user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
            password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))

def main():
    """
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * from users;")
    result = cursor.fetchall()
    for i in result:
        msg = f"name={i[0]};" + \
              f"email={i[1]};" + \
              f"phone={i[2]};" + \
              f"ssn={i[3]};"+ \
              f"password={i[4]};" + \
              f"ip={i[5]};" + \
              f"last_login={i[6]};" + \
              f"user_agent={i[7]};"
        record = logging.LogRecord("use_data", logging.INFO, None, None, msg, None, None)
        print(RedactingFormatter(PII_FIELDS).format(record))
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
