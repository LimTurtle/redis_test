# Redis 명령어
- [여기](https://sungwookkang.com/1313)를 참조

# Python에서 Redis 사용법
- Terminal에서 ``` pip install redis ``` 명령어 실행
- 로컬 PC에서 Redis를 설치하고, Redis Server를 실행시킨 상태에서 진행해야 함

```python
import redis

r = redis.Redis(host="127.0.0.1", port="6379", password="~" charset="utf-8", decode_responses=True)
r.set(name="A", value="Lim")
print(r.get(name="A"))

>> Lim
```
* 키/값 입력 : ``` set key value ```
* 키/값 조회 : ``` get key ```
* 전체 키 확인 : ``` keys * ```
* 전체 키 삭제 : ``` flushall ```

# Python에서 MySQL 사용법
- Terminal에서 ``` pip install pymysql ``` 명령어 실행 (여기서는 ```pandas``` 통해 결과를 표로 확인할 것이므로,  ``` pip install pandas ``` 입력해 pandas 또한 함께 설치함)
```python
import pymysql
import pandas as pd

mysql_db = pymysql.connect(
    user="root",
    password="~",
    host="127.0.0.1",
    port=3306, #port는 문자열 사용하면 안 되는 것 주의
    db="sakial", #MySQL의 예제 데이터베이스 sakial을 사용
)

cursor = mysql_db.cursor()
cursor.execute("SQL Query문")
result = cursor.fetchall()
print(pd.DataFrame(result)) #pandas의 DataFrame 형식은 해당 결과를 2차원 배열, 즉 표로 출력함
```
# Redis와 MySQL 성능 비교
- python의 ```time``` 사용하여 처음 Run 시 redis가 비어있을 때 redis에 데이터를 넣고 mysql에서 데이터를 조회해오는 총 시간을 계산
- 마찬가지로, 두번 째 Run 시 redis에서 데이터를 조회해오는 총 시간을 계산하고, 2개의 시간을 비교
    * __1st Run Result (MySQL 조회)__
    ```
    1
    no cache
     0.00099992752075195 Sec
    MARY
    Sum of Total Time : 0.0009999275207519531
    
    ...
    
    499
    no cache
     0.00000000000000000 Sec
    MARC
    Sum of Total Time : 0.1820390224456787
    ```

    * __2nd Run Result (Redis 조회)__
    ```
    1
    cache
     0.00000000000000000 Sec
    MARY
    Sum of Total Time : 0.0
    
    ...
    
    499
    cache
     0.00000000000000000 Sec
    MARC
    Sum of Total Time : 0.06701517105102539
    ```
    **-> Redis가 MySQL보다 조회 시간이 약 3배 더 빠른 것을 확인**

# C++ MySQL 연동
- [초기 설정](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dd1587&logNo=221155813026)
- [참조](https://m.blog.naver.com/PostView.naver?blogId=dd1587&logNo=221157117516&targetKeyword=&targetRecommendationCode=1)

# C++ Redis 연동
- [초기 설정](https://sanghun219.tistory.com/193)
    - 이 때, 위 URL의 microsoft/hiredis 가 아닌 redis/hiredis 의 Release 다운
    - 포함 디렉토리 경로는 CMake로 생성된 경로가 아닌, Release 를 다운 했던 경로
- 사용법
```cpp
#include "Redis.h"

int main()
{
    Redis* redis = new Redis(); //redis 초기설정
    
    redis->RedisQuery("SET foo hello"); //또는 redis->RedisQuery("SET %s %s", "foo", "hello")
    const char* res = redis->RedisQuery("GET foo"); //또는 redis->RedisQuery("GET %s", "foo")
    cout << res << endl;
}

```
