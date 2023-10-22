import mysql.connector

from datahound.connectors import ConnectorBase


class MySqlConnector(ConnectorBase):
    @staticmethod
    def get_connection(connection_string):
        return mysql.connector.connect(
            user=connection_string.user,
            password=connection_string.password,
            host=connection_string.host,
            port=connection_string.port,
            database=connection_string.database_name
        )
