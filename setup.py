from setuptools import setup, find_packages


setup(
    name='datahound-mysql',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/Techi-Freki/datahound_mysql',
    license='MIT',
    author='Techi-Freki',
    author_email='techifreki@proton.me',
    description='A MySQL connector for datahound',
    install_requires=['datahound', 'mysql-connector-python'],
    extra_index_urls=['https://python.dbcombs.com/simple'],
    entry_points={
        'datahound.connectors': ['datahound_mysql=datahound_mysql.connectors:MySqlConnector']
    }
)
