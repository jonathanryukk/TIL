
Statement [#1](https://github.com/jonathanryukk/TIL/issues/1)
주문번호 ‘19971213’에 대하여 주문번호, 주문순번, 제품번호, 주문수량을 주문수량의
오름차순으로 조회하세요.
ORD_NO LINE_NO ITEM_ ORD_QTY

------

19971213 1 IT008 10
19971213 2 IT001 10
19971213 4 IT007 120
19971213 3 IT005 130
SELECT
Statement [#2](https://github.com/jonathanryukk/TIL/issues/2) 

1997년 12월에 공급처 ‘LG전자’로 주문한 모든 건에 대해 주문번호와 주문일
(YYYY-MM-DD 형식으로) 을 주문 일의 내림차순으로 조회하세요.
ORD_NO ORDER_DATE

------

19971216 1997-12-19
19971210 1997-12-09
19971204 1997-12-02
SELECT
Statement [#3](https://github.com/jonathanryukk/TIL/issues/3)
주문번호가 ‘19971203’인 주문에 대해 주문번호, 제품번호, 제품명, 제품별 주문수량
을 제품번호의 오름차순으로 조회하세요.
ORD_NO ITEM_ ITEM_NAME ORD_QTY

------

19971203 IT001 CONTROLLER 10
19971203 IT006 TRANSISTER 10
19971203 IT007 CONDENSOR 50
19971203 IT008 WIRE 10
SELECT
Statement [#4](https://github.com/jonathanryukk/TIL/issues/4) 납기가 지났으나 납품이 완료되지 않은 모든 주문에 대하여 주문번호와 공급처 이름,
전화번호를 공급처 이름의 오름차순으로 조회하세요.
ORD_NO SUP_NAME SUP_PHONE

------

19971216 LG전자 984-8376
19971213 대명전기 432-5344
19971215 우성전업사 165-6587
19971214 한진엔지니어링 345-6543
ORACLE Workshop [#3](https://github.com/jonathanryukk/TIL/issues/3)
3
SELECT
Statement #5
‘구매팀’, ‘외자팀’, ‘홍보부’ 내에서 각 부서별로 사번이 가장 빠른 사원의 부서명과
사원번호를 조회하세요.
EMP_DEP ???

------

구매팀 11111
외자팀 44444
홍보부 22222
SELECT
Statement #6
‘홍보부’의 ‘박찬호’ 직원이 1997년에 주문을 낸 공급처의 이름과 공급처의 주소를
공급처 이름의 오름차순으로 중복되지 않게 조회하세요.
SUP_NAME SUP_ADDR

------

일신상사 경기도 부천시 내동 SELECT Statement #7 공급처 ‘LG전자’ 로부터 1997년 12월에 납품받은 제품에 대한 총 지불 대금 즉, 각 제품 지불대금( 각 제품단가 * 제품 주문수량 ) 의 총합을 구하는 SQL문을 작성하세요. ???

589000
SELECT
Statement #8
납기를 잘 지키지 않는 불량 공급자를 파악하기 위해 공급자별로 납기 미 준수
횟수( 납품이 아직 안된 것은 제외) 가 2건 이상인 공급처를 공급처 번호와 납기 미준수
횟수로 조회하세요.
SUP_ ???

------

S005 2 SELECT Statement #9 1997년에 주문한 제품의 단가 중에 가장 높은 단가를 조회하세요. ?

210000



```sql


--1
SELECT *
FROM po_order_detail
WHERE ORD_NO = '19971213'
ORDER BY ORD_QTY ASC;

SELECT * FROM po_supplier;

--2
SELECT A.ORD_NO, TO_CHAR(a.ord_date,'YYYY-MM-DD')
FROM PO_ORDER_HEADER A, PO_SUPPLIER B
WHERE B.sup_name = 'LG전자'
AND A.SUP_NO = B.SUP_NO
AND TO_CHAR(ORD_DATE, 'YYYY-MM') = '1997-12'
ORDER BY a.ord_date DESC;

--3
SELECT A.ORD_NO, A.ITEM_NO, B.ITEM_NAME, A.ORD_QTY
FROM PO_ORDER_DETAIL A, PO_ITEM B
WHERE A.ORD_NO = '19971203'
AND A.ITEM_NO = B.ITEM_NO
ORDER BY A.ITEM_NO;

SELECT * FROM po_order_header;
SELECT * FROM PO_SUPPLIER;
--4
SELECT A.ORD_NO, B.SUP_NAME, B.SUP_PHONE
FROM PO_ORDER_HEADER A, PO_SUPPLIER B
WHERE A.DELV_DATE IS NULL AND A.SUP_NO = B.SUP_NO
ORDER BY B.SUP_NAME ;

--5
SELECT EMP_DEP, MIN(EMP_NO)
FROM PO_EMPLOYEER
WHERE EMP_DEP = '구매팀'
OR EMP_DEP = '외자팀'
OR EMP_DEP = '홍보부'
GROUP BY EMP_DEP
ORDER BY EMP_DEP;

--6
SELECT DISTINCT A.SUP_NAME, A.SUP_ADDR
FROM PO_SUPPLIER A, PO_ORDER_HEADER B, PO_EMPLOYEER C
WHERE A.SUP_NO = B.SUP_NO AND B.ORD_EMP = C.EMP_NO
AND C.EMP_NAME = '박찬호'
AND C.EMP_DEP = '홍보부'
AND TO_CHAR(ORD_DATE,'YYYY') = '1997'
ORDER BY A.SUP_NAME ASC;

--7
SELECT SUM(C.UNIT_PRICE*B.ORD_QTY)
FROM PO_ORDER_HEADER A, PO_ORDER_DETAIL B, PO_ITEM C, po_supplier D
WHERE A.ORD_NO = B.ORD_NO
AND B.ITEM_NO = C.ITEM_NO
AND D.SUP_NO = A.SUP_NO
AND D.SUP_NAME = 'LG전자'
AND TO_CHAR(A.DELV_DATE, 'YYYYMM') = '199712'
;

--8
SELECT SUP_NO, COUNT(*) FROM po_order_header
WHERE DUE_DATE < DELV_DATE
GROUP BY SUP_NO
HAVING COUNT(*) >=2;

--9
SELECT MAX(A.UNIT_PRICE)
FROM PO_ITEM A, PO_ORDER_HEADER B, PO_ORDER_DETAIL C
WHERE B.ORD_NO = C.ORD_NO
AND A.ITEM_NO = C.ITEM_NO
AND TO_CHAR(B.ORD_DATE, 'YYYY') = '1997';
```

