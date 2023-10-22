# Datahound MySQL

A MySQL connector for [datahound](https://github.com/Techi-Freki/datahound).

## Usage

### Extending provider base

    from datahound import DataProviderBase, ConnectionString


    # add your connection string data to the ConnectionString object
    mysql_connection = ConnectionString('datahound_mysql',
                                        user='test_user',
                                        password='test_pass',
                                        host='localhost',
                                        port=3306,
                                        database_name='test_db'
                                        )

    sqlite_connection = ConnectionString(database_path='/path/to/db.sqlite') # datahound defaults to sqlite3 when a connector_name is not passed in

    # extend the DataProviderBase class
    class MySqlProvider(DataProviderBase):
        def __init__(self):
            super().__init__(mysql_connection)


    class SqLite3Provider(DataProviderBase):
        def __init__(self):
            super().__init__(sqlite_connection)


    class DataProvider(object):
        mysql = MySqlProvider()
        sqlite = SqLite3Provider()


    # you are now ready to use the DataProvider class to access your databases
    # See the datahound README for additional information

## Changelog

1.0.0

* Initial Release.
