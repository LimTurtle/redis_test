#include <iostream>
#include <mysql.h>

#pragma comment(lib, "libmySQL.lib")

using namespace std;

int main()
{
	cout << mysql_get_client_info() << endl;

	MYSQL Conn;
	MYSQL* ConnPtr = NULL;
	MYSQL_RES* Result;
	MYSQL_ROW Row;
	int Stat;

	mysql_init(&Conn);
	ConnPtr = mysql_real_connect(&Conn, "127.0.0.1", "root", "Z797944z!", "sakila", 3306, (char*)NULL, 0);

	if (ConnPtr == NULL)
	{
		cout << "Error : " << mysql_error(&Conn) << endl;
		return 1;
	}

	const char* Query = "SELECT * FROM actor";
	Stat = mysql_query(ConnPtr, Query);
	if (Stat != 0)
	{
		cout << "Error : " << mysql_error(&Conn) << endl;
		return 1;
	}

	Result = mysql_store_result(ConnPtr);
	while ((Row = mysql_fetch_row(Result)) != NULL)
	{
		cout << Row[0] << " / " << Row[1] << " / " << Row[2] << " / " << Row[3] << endl;
	}
	mysql_free_result(Result);

	mysql_close(ConnPtr);

	return 0;
}