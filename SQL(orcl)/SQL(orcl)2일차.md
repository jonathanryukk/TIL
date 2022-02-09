# sql 2일차





1. 모든 직원의 급여 총액, 급여 평균, 최고 급여, 최소 급여를 표시 하십시오.
2. 직위가 동일한 직원의 수를 표시 하십시오.
3. 직원들 중에서 관리자의 수를 표시 하십시오.
4. 총 직원 수를 구하고 2000, 2001, 2002, 2003년에 입사한 직원 수를 표시하십
   시오.
5. 지급된 보너스의 평균값을 구하십시오. (보너스가 없는 경우는 0으로 적용하
   세요)
6. 최고 급여가 10000원이 넘는 부서번호와 평균급여를 표시 하십시오.
7. 영업부 부서에서 근무하는 모든 직원의 이름, 직위, 부서번호, 부서이름을
   표시 하십시오.
8. 직원의 이름, 사번, 관리자 이름, 사번을 표시 하십시오.
9. 관리자가 지정되지 않은 직원도 포함하여 직원의 이름, 사번, 관리자 이름,
   관리자의 사번을 표시 하십시오.(관리자가 지정되지 않은 경우 관리자의 이름과
   사번은 ‘없음’으로 표시하세요)
10. 관리자 보다 먼저 입사한 모든 직원의 이름, 입사일, 관리자 이름,
    관리자 입사일을 표시 하십시오.
11. 보너스를 받는 직원의 이름, 부서 번호, 부서 이름을 표시 하십시오.



```sql


select * from member;

--1
select sum(sal) as "급여 총액", avg(sal) as "급여 평균", min(sal) as "최소 급여"
from member;

--2
select jikwi,count(*) from member
group by jikwi;

--3
select count(distinct mgr) as 관리자 from member;

--4
select
count(*) as "총 직원 수",
count(decode(to_char(hire,'yyyy'),'2000',1)) as "2000",
count(decode(to_char(hire,'yyyy'),'2001',1)) as "2001",
count(decode(to_char(hire,'yyyy'),'2002',1)) as "2002",
count(decode(to_char(hire,'yyyy'),'2003',1)) as "2003"
from member;

--5
select avg(nvl(bonus,0)) as 보너스 from member;

--6
select dept_id, avg(sal)
from member
group by dept_id
having max(sal) > 10000;

select * from member;
select * from dept;

--7
select a.name, a.jikwi, a.dept_id, b.dept_name
from member a, dept b
where a.dept_id = b.dept_id;

--8 셀프조인 (조직도)
select a.member_id, a.name, b.member_id as "관리자 사번", b.name as "관리자 이름" from member a, member b
where a.member_id = b.mgr;

--9
select a.member_id, a.name, b.member_id, b.name
from member a, member b
where a.member_id = b.mgr
and a.hire < b.hire;

--10
select a.member_id, a.name, b.member_id, b.name
from member a, member b
where a.member_id = b.mgr
and a.hire < b.hire;

--11
select a.member_id, a.name, b.dept_name
from member a, dept b
where a.dept_id = b.dept_id
and a.bonus is not null;

-- 이너조인
select * from member, dept
where member.dept_id = dept.dept_id;

select * from member inner join dept
on member.dept_id = dept.dept_id;
```







