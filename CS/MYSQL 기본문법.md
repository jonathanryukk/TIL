# MYSQL 기본문법



**1. SELECT**

 \- SELECT * FROM TableName;

 \- 데이터 불러오기

 

**2. DESC**

 \- DESC TableName;

 \- 테이블 구조 참조 

 

**3. WHERE**

 \- SELECT 열1, 열2 FROM TableName WHERE 조건식;

 

**4. 비교 연산자**

 \- =, <>, <, >, <=, >=, IS NULL 

 

**5. AND**

 \- 조건식1 AND 조건식2

 \- SELECT * FROM TableName WHERE a<>0 AND b<>0;

 \* OR 보다 AND의 우선 순위가 높음

 

**6. OR**

 \- 조건식1 OR 조건식2

 \- SELECT * FROM TableName WHERE no=1 OR no=2;

 \* OR 보다 AND의 우선 순위가 높음

 

**7. NOT**

 \- NOT 조건식

 \- SELECT * FROM TableName WHERE NOT(a<>0 OR b<>0);

 

**8. 패턴(LIKE)**

 \- 열 LIKE 패턴

 \- 메타문자 : %(임의의 문자열), _(임의의 문자 하나)

 \- WHERE text LIKE 'SQL%'

 \- % 검색 : WHERE text LIKE '%\%%'

 

**9. 정렬(ORDER BY)**

 \- SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명;

 \- ORDER BY는 WHERE 절 뒤에 위치

 \- SELECT * FROM TableName ORDER BY age;

 \- DESC를 쓰면 내림차순(큰수 -> 작은수), ASC는 오름차순(작은수 -> 큰수)으로 정렬

 \- SELECT 열명 FROM 테이블명 ORDER BY 열명 ASC;

 

**10. 복수 정렬**

 \- SELECT 열명 FROM 테이블명 WHERE 조건식 ORDER BY 열명1, 열명2

 \- SELECT * FROM TableName ORDER BY a ASC, b DESC;

 \- NULL은 MySQL에서 가장 작은 값으로 취급

 

**11. 제한하기(LIMIT)**

 \- SELECT 열명 FROM 테이블명 LIMIT 함수 (OFFSET 시작행)

 \- MySQL과 PostgreSQL문법

 \- ORDER BY 뒤에 위치

 \- SELECT * FROM TableName ORDER BY age DESC LIMIT 3;

 \- OFFSET을 사용하면 취득위치 표시 가능(기본값 0)

 \- SELECT * FROM TableName ORDER BY age DESC LIMIT 3 OFFSET 3; (4번째부터 출력)

 

**12. 수치연산
** - +, -, *, /, %, MOD

 \- SELECT 식1, 식2 ... FROM 테이블명

 \- SELECT *, price * quantity AS amount FROM TableName; 

 \- AS로 이름 지을경우 한글 사용시 쌍따옴표 사용

 \- 쌍따옴표는 데이터베이스 객체명에 사용하고, 따옴표는 문자열 상수에 사용

 \- SELECT *, price * quantity AS amount FROM TableName WHERE price * quantity >= 2000;

 \- NULL의 연산값은 NULL (NULL + 1 -> NULL)

 \- 함수 : ROUND(변수, 반올림수)

 

**13. 문자열 연산**

 \- +, ||, CONCAT, SUBSTRING, TRIM CHARACTER_LENGTH

 \- 'ABC' || '1234' -> 'ABC1234'

 \- +(문자열 결합), ||(문자열 결합), CONCAT(문자열 결합)

 \- SELECT CONCAT (quantity, unit) FROM TableName;

 \- SUBSTRING('20140125001', 5, 2) -> '01'

 \- TRIM('ABC   ') -> 'ABC'

 \- CHARACTER_LENGTH -> 문자열 길이 반환

 

**14. 날짜 연산**

 \- CURRENT_TIMESTAMP, CURRENT_DATE INTERVAL

 \- SELECT CURRENT_TIMESTAMP; -> 현재 시간 반환

 \- TO_DATE('2014/01/25', 'YYYY/MM/DD')

 \- 기간 더하기 : SELECT CURRENT_DATE + INTERVAL 1 DAY

 \- 날짜 빼기 : DATEDIFF('2014-02-28', '2014-01-01')

 

**15. CASE**

 \- CASE WHEN 조건식1 THEN 식1

  [WHEN 조건식2 THEN 식2 ...]

  [ELSE 식3]

  END

 \- SELECT a, CASE WHEN a IS NULL THEN 0 ELSE a END "a(null=0)" FROM TableName;

 \- NULL 반환 :  SELECT a, COALESCE(a, 0) FROM TableName;

 \- 검색 case
  SELECT A AS "코드",

  CASE

   WHEN a = 1 THEN '남자'
   WHEN a = 2 THEN '여자'

   ELSE '미지정'

  END AS "성별" FROM TableName;

 \- 단순 case

  SELECT a AS "코드",

  CASE a

   WHEN 1 THEN '남자'

   WHEN 2 THEN '여자'

   ELSE '미지정'

  END AS "성별" FROM TableName;

 \- 단순 CASE 문으로는 NULL 값을 비교할 수 없음 -> 검색 CASE 문 사용 필수

 

**16. 행 개수 구하기(COUNT)**

 \- COUNT(집합)

 \- SELECT COUNT(*) FROM TableName;

 \- 중복제거 : SELECT DISTINCT name FROM TableName;

  \* 전체 : ALL

 

**17. 그 외의 집계함수**

 \- SUM : SELECT SUM(quantity) FROM TableName;

 \- AVG : SELECT AVG(quantity) FROM TableName;

 \- MIN : SELECT MIN(quantity) FROM TableName;

 \- MAX : SELECT MAX(quantity) FROM TableName;

 

**18. 그룹화(GROUP BY)**

 \- SELECT * FROM 테이블명 GROUP BY 열1, 열2;

 \- SELECT name FROM TableName GROUP BY. name; -> 중복된 값이 빠진 형태로 추출됨

 \- 집계함수와 같이 사용하지 않으면 큰 의미 없음

 \- SELECT name, COUNT(name), SUM(quantity) FROM TableName GROUP BY name;

 \- 내부처리 순서 : WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

 \- HAVING을 사용하면 결과에서 조건식을 지정할 수 있음

 \- SELECT name, COUNT(name) FROM TableName

  GROUP BY name HAVING COUNT(name) = 1;

 \- HAVING 사용시 alias 사용 불가

 \- 복수열의 그룹화

 \- SELECT name, quantity FROM TableName GROUP BY name, quantity;
 \- 결과값 정렬

 \- SELECT name, COUNT(name), SUM(quantity)

  FROM TableName GROUP BY name ORDER BY SUM(quantity) DESC;

 

**19. 서브쿼리**

 \- SELECT

  (SELECT COUNT(*) FROM TableName1) AS sq1,

  (SELECT COUNT(*) FROM TableName2) AS sq2;

 

**20. IN**

 \- 열명 IN(집합)

 \- SELECT * FROM TableName WHERE age IN (3, 5);

 \- SELECT * FROM TableName1 WHERE age IN

   (SELECT age2 FROM TableNAme2);

 

**21. 합집합(UNION)**

 \- SELECT * FROM TableName1

  UNION

  SELECT * FROM TableName2;

 \- ORDER BY는 마지막 SELECT 명령에만 지정

 \- SELECT a FROM TableName1

  UNION

  SELECT b FROM TableName2 ORDER BY b;

  \* alias 가능
 \- 기본은  DISTINCT임

 \- 교집합 : INTERSECT

 \- 차집합 : EXCEPT

 

**22. 테이블 결합**

 \- 교차결합(Cross Join)

 \- SELECT * FROM TableName1, TableName2;

 \- SELECT * FROM TableName1 CROSS JOIN TableName2;

 \- 내부결합

 \- SELECT * FROM 상품, 재고수

  WHERE 상품.상품코드 = 재고수.상품코드;

 \- 제한하기

 \- SELECT 상품.상품명, 재고수.재고수 FROM 상품, 재고수

  WHERE 상품.상품코드 = 재고수.상품코드

   AND 상품.상품분류 = '식료품';

 \- INNER JOIN을 이용하면 편하게 할 수 있음

 \- SELECT * FROM TableName1 INNER JOIN TableName2 ON 결합조건;

 \- SELECT S1.상품명, S2.상품명

  FROM 상품 S1 INNER JOIN 상품 S2

  ON S1.상품코드 = S2.상품코드;

 \- 외부결합은 한쪽 테이블에 데이터가 없을 경우 사용

 \- SELECT 상품3.상품명, 재고수.재고수

  FROM 상품3 LEFT JOIN 재고수

  ON 상품3.상품코드 = 재고수.상품코드

  WHERE 상품3.상품분류 = '식료품';