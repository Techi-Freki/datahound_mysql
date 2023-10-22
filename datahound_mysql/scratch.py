from datahound import ConnectionString, DataProviderBase

connection_string = ConnectionString(
    'datahound_mysql',
    user='cms_user',
    password='cms_pass',
    database_name='cms_test',
    host='localhost',
    port='3306'
)


class MySqlProvider(DataProviderBase):
    def __init__(self):
        super().__init__(connection_string)


class DataProvider(object):
    mysql = MySqlProvider()


sql = 'select * from test_data'
records = DataProvider.mysql.fetchall(sql)

for record in records:
    print(record)
