"""
Python interface to Secure-IT Token SQLite3 database.

Database can be found in the following location on Android:
/data/data/uk.co.bmsnotts.mobilesecureit/files/LocalDB.db3
"""

import sqlite3
from collections import namedtuple
from typing import Any

User = namedtuple("User", ["id", "pin"])
UserToken = namedtuple("UserToken", ["id", "seed", "length", "index"])


def hex_encode(n: int) -> str:
    """Return hex-encoding of int n."""
    return hex(n)[2:].upper()


class DB:
    """Class to model data about a BMS token from Secure-IT database."""

    def __init__(self, database: str) -> None:
        """Initialise instance of BMS token."""
        self.database = database
        self.user = User(*self._exec_sql("SELECT * FROM User")[0])
        self.user_token = UserToken(*self._exec_sql("SELECT * FROM UserToken")[0])

    def _exec_sql(self, *args: Any) -> list[Any]:
        """Execute SQL in DB and return results."""
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        with conn:
            res = cur.execute(*args).fetchall()
        conn.close()
        return res

    @property
    def seed(self) -> str:
        """Get seed of token from DB."""
        return self.user_token.seed

    @property
    def length(self) -> str:
        """Get length of token from DB."""
        return self.user_token.length

    @property
    def index(self) -> str:
        """Get index of token from DB."""
        return self.user_token.index

    @property
    def pin(self) -> str:
        """Get user PIN from DB."""
        return self.user.pin


if __name__ == "__main__":
    database = "LocalDB.db3"
    bms_token = DB(database)
    print(f"Seed: {bms_token.seed}\nPIN: {bms_token.pin}")
    print(f"Length: {bms_token.length}\nIndex: {bms_token.index}")
