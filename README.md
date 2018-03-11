# Team-Bee

Hackmed 2018 

## Importing the database schema into MySQL

`mysql -u root -p < database_definition.sql`

If on Mac and don't have `mysql` in your path:

`/usr/local/mysql/bin/mysql -u root -p < database_definition.sql`

To remotely dump sql into ClearDB:

`/usr/local/mysql/bin/mysql --host=eu-cdbr-west-02.cleardb.net --user=b127d1018a3177 --password=XXXXXXX --reconnect heroku_4e232ea7b3dda54 < database_definition.sql`

