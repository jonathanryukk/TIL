##### 1.급여가 14000에서 30000사이에 포함되지 않는 모든 직원의 이름과 급여를 표시 하십시오. 

##### 2. 직원의 사번, 이름, 급여및 급여를 20% 인상한 급여로 표시 하십시오. 

##### 3. 각 직원의 근무 달수를 표시 하십시오. 

##### 4. 각 직원의 근무 달수를 표시 하십시오. 결과는 소숫점 두째자리에서 반올림 합니다. 

##### 5. 각 직원의 이름 급여를 표시 하는 질의문을 작성 하십시오. 급여는 10자리 길이에 왼쪽에는 #표시가 채워지는 형식으로 표기 하십시오. 

##### 6. 각 직원의 사번, 이름, 입사일과 입사한 후에 10달이 경과된 날짜를 표시 하시오. (단 경과된 날짜의 결과는 ‘YYYY-MM-DD‘ 형식으로 표시 하십시오) 

##### 7. member 테이블에서 사원의 이름, 직위, 입사일 과 입사한 요일을 표시하되 월요일이 처음으로 하는 순서로 입사요일을 정렬 하십시오. 

##### 8. 모든 직원의 이름, 직위, 직위별 등급을 표시 하십시오. 각 직위별 등급은 아 래를 참조하십시오. 직위 직위별등급

사장 A
부장 B
과장 C
대리 D
사원 E

##### 9.각 직원들의 이름과 연봉을 계산 하십시오.

(sal*12 + bonus)

##### 10.2004년에 입사한 직원의 사번과 이름을 표시하십시오.

##### 11.관리자가 없는 직원의 이름과 직위를 표시하십시오.

##### 12.보너스를 받은 직원의 이름과 급여, 보너스를 기준으로 내림차순 정렬하여

##### 표시하십시오.





```sql
select * from member;

--1
select name, sal
from member
where sal < 14000 or sal > 30000;
--NOT BETWEEN 14000 AND 30000

--2
SELECT MEMBER_ID, NAME,SAL, (SAL*1.2) as newsal
FROM member;

--3
SELECT NAME, FLOOR(months_between(sysdate,hire)) as "근무 달수"
from member;

--4
SELECT NAME, ROUND(months_between(sysdate,hire),1) as "근무 달수"
from member;

--5
SELECT NAME, LPAD(SAL,10,'#') FROM MEMBER;

--6
SELECT MEMBER_ID,name, hire, add_months(to_date(member.hire),10) as "10개월 후"
from member,dual;

--7
SELECT NAME, JIKWI,HIRE, TO_CHAR(HIRE,'DAY')AS 요일 FROM MEMBER
ORDER BY to_char(hire-1,'d');

--8
SELECT NAME, JIKWI,
DECODE(
JIKWI,
'사장','A',
'부장','B',
'과장','C',
'대리','D',
'사원','E') AS 직위별등급
FROM MEMBER;

SELECT NAME, JIKWI,
CASE WHEN JIKWI='사장' THEN 'A'
WHEN JIKWI='부장' THEN 'B'
WHEN JIKWI='과장' THEN 'C'
WHEN JIKWI='대리' THEN 'D'
WHEN JIKWI='사원' THEN 'E' END AS 직위별등급
FROM MEMBER;

--9
select name, (sal*12+NVL(bonus,0)) as 연봉 from member;

--10
SELECT NAME, MEMBER_ID,HIRE FROM MEMBER
WHERE TO_CHAR(HIRE,'YY-MM-DD') LIKE '04%';

--11
SELECT NAME, JIKWI FROM MEMBER
WHERE MGR IS NULL;

--12
SELECT NAME, SAL, BONUS FROM MEMBER
ORDER BY NAME DESC, SAL DESC, BONUS DESC;
```

