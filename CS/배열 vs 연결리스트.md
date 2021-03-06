![img](https://blog.kakaocdn.net/dn/kSo0i/btriGjO8MrW/i26M9ZNy1LehH6WLyJVkXK/img.png)



## **🚀**

 

## **📌 배열(Array)**

#### **🔎 특징**

논리적 저장 순서와 물리적 저장 순서가 일치하는 자료구조. 따라서 인덱스(Index)로 해당 원소에 접근할 수 있으며 Random Access가 가능합니다. 하지만 삽입/삭제 시 해당 원소에 접근하여 작업을 완료한 후 빈 공간이 생기지 않도록 shift 해줘야 하므로 O(N)의 시간이 소요됩니다.

#### **✔️ 장점**

논리적 저장 순서 = 물리적 저장 순서

메모리상에서 원소들이 연속적으로 붙어있어 인덱스 값을 이용하여 랜덤 접근(Random Access)이 가능

#### **❌ 단점**

삽입/ 삭제가 번거로움

초기에 배열의 크기를 지정해야 하며, 고정적이고 변경할 수 없음

 

## **📌 동적 배열(Dynamic Array)**

#### **🔎 특징**

배열과는 조금 다르게 동적 배열의 크기를 유동적으로 할 수 있고 메모리상에서 원소들이 연속적으로 붙어있어 인덱스 값을 이용하여 랜덤 접근(Random Access)이 가능합니다.

#### **✔️ 장점**

배열의 크기가 유동적

메모리상에서 원소들이 연속적으로 붙어있어 인덱스 값을 이용하여 랜덤 접근(Random Access)이 가능

#### **❌ 단점**

삽입/ 삭제가 번거로움

 

## **📌 연결 리스트(Linked List)**

#### **🔎 특징**

어떠한 노드가 데이터와 다음 노드에 대한 주소 정보(포인터)를 가지고 노드들끼리 순차적으로 연결되어있는 방식의 자료구조입니다.

#### **✔️ 장점**

삽입, 삭제가 빠름

필요할 때 크기를 늘리거나 줄일 수 있어 메모리 관리가 효율적

연속된 메모리 공간이 필요 없음

#### **❌ 단점**

메모리 연속성을 가지지 않기 때문에 랜덤 접근(Random Access)이 불가능

검색 시 처음 노드부터 순차적으로 순회해야 합니다.

 

## **👀 시간 복잡도 비교**

| **작업** | **배열** | **동적 배열** | **연결 리스트** |
| -------- | -------- | ------------- | --------------- |
| **검색** | O(1)     | O(1)          | O(N)            |
| **삽입** | O(N)     | O(N)          | O(N)            |
| **삭제** | O(N)     | O(N)          | O(N)            |

(삽입, 삭제하려는 데이터의 위치가 맨 앞 혹은 맨 뒤 일 경우 시간 복잡도가 O(1)이 될 수도 있습니다.)

 

**데이터 접근(탐색, 조회)이 빈번할 경우 => Array**

**데이터 수정(삽입, 삭제)이 빈번할 경우 => Linked List**