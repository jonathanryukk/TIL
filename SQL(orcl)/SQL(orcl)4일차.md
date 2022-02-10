1. 황기훈과 동일한 부서에 속한 사원의 이름과 입사일, 급여를 표시 하십시오.
2. 급여가 평균급여 보다 많은 사원의 사번, 이름을 표시 하십시오.
3. 최고의 평균 급여를 포함하는 부서 번호와 평균 급여를 표시 하십시오.
4. 배기수에게 보고 하는 모든 사원의 이름과 급여를 표시 하십시오.
5. 영업부 부서에 모든 사원의 사번, 이름, 부서번호, 직위를 표시 하십시오.
6. 부하직원이 있는 모든 사원을 표시 하십시오.
7. 부하직원이 없는 사원을 표시 하십시오.
8. 김주부 사원 보다 늦게 입사한 사원을 표시하십시오.
9. 보너스를 받는 사원과 부서 번호 및 급여가 일치 하는 사원의 이름,
   부서 번호 및 급여를 표시 하십시오
10. 모든 과장의 급여 보다 많이 받는 사원들을 표시 하십시오.
11. 자신의 부서 평균 급여 보다 많이 받는 사원들을 표시 하십시오.
12. 다음 데이터를 DEPT 테이블에 추가 하십시오. (60, ‘교육팀’ 600)
13. 김지희 사원을 찾아 급여를 6000으로 변경 하십시오.
14. 권민수 사원을 찾아 삭제 하십시오. 삭제한 후 내용을 확인한 후
    rollback 합니다.
    15.급여가 평균급여 보다 많은 사원의 사번, 이름를 표시 하십시오.



```sql


SELECT * FROM MEMBER;
SELECT * FROM DEPT;

--1
SELECT A.NAME, A.HIRE, A.SAL
FROM member A
WHERE A.DEPT_ID = (SELECT B.DEPT_ID
FROM MEMBER B
WHERE B.NAME = '황기훈');

--2
SELECT A.MEMBER_ID, A.NAME
FROM MEMBER A
WHERE A.SAL > (SELECT AVG(B.SAL)
FROM MEMBER B
)

--3
SELECT A.DEPT_ID, AVG(A.SAL)
FROM MEMBER A
WHERE B.SAL = MAX;

--4

SELECT A.NAME, A.SAL
FROM MEMBER A
WHERE A.MGR = (SELECT B.MEMBER_ID
FROM MEMBER B
WHERE B.NAME = '배기수');

--5
SELECT A.MEMBER_ID, A.NAME, A.DEPT_ID, A.JIKWI
FROM MEMBER A
WHERE A.DEPT_ID = (SELECT B.DEPT_ID
FROM DEPT B
WHERE B.DEPT_NAME = '영업부');

--6
SELECT A.NAME
FROM MEMBER A
WHERE A.MEMBER_ID = (SELECT B.MEMBER_ID
FROM MEMBER B
WHERE B.MGR IS NOT NULL);
```





