#include <iostream>
#include "Redis.h"

using namespace std;

int main()
{
    Redis* redis = new Redis(); //redis 초기설정
    
    redis->RedisQuery("SET foo hello"); //또는 redis->RedisQuery("SET %s %s", "foo", "hello")
    const char* res = redis->RedisQuery("GET foo"); //또는 redis->RedisQuery("GET %s", "foo")
    cout << res << endl;
    return 0;
}
