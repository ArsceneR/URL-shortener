import psycopg2

class PostgreDB:
    """Interact with PostgreSQL database."""

    def __init__(self, database_config):
        """
        Initialize the PostgreDB instance.

        Args:
            database_config (dict): Configuration parameters for connecting to the database.
        """
        self.database_config = database_config

    def add_data(self, data):
        """
        Add data to the database.

        Args:
            data (tuple): A tuple containing the data to be added.

        Raises:
            Exception: If an error occurs while adding the data.
        """
        try:
            conn = psycopg2.connect(**self.database_config)
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO URL (SHORTEN, ORIGINAL) VALUES (%s, %s)', data)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()

    def check_data_exist(self, shorten=None, original=None):
        """
        Check if data already exists in the database.

        Args:
            shorten (str): Short URL to check.
            original (str): Original URL to check.

        Returns:
            str or None: The corresponding URL (original or shorten) if found, otherwise None.

        Raises:
            Exception: If an error occurs while checking the data.
        """
        try:
            conn = psycopg2.connect(**self.database_config)
            cur = conn.cursor()
            if shorten:
                cur.execute('SELECT * FROM URL WHERE SHORTEN = %s',
                            (shorten,))
            else:
                cur.execute('SELECT * FROM URL WHERE ORIGINAL = %s',
                            (original,))
            result = cur.fetchone()
            if result and original:
                return result[1]
            elif result and shorten:
                return result[2]
            else:
                return None
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()

    def create_table(self):
        """
        Create the table in the database.

        Raises:
            Exception: If an error occurs while creating the table.
        """
        try:
            conn = psycopg2.connect(**self.database_config)
            cur = conn.cursor()
            cur.execute(
                '''
                CREATE TABLE IF NOT EXISTS URL (
                    ID SERIAL PRIMARY KEY,
                    SHORTEN TEXT NOT NULL,
                    ORIGINAL TEXT NOT NULL
                );
                '''
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
