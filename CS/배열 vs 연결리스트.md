![img](https://blog.kakaocdn.net/dn/kSo0i/btriGjO8MrW/i26M9ZNy1LehH6WLyJVkXK/img.png)



## **π**

 

## **π λ°°μ΄(Array)**

#### **π νΉμ§**

λΌλ¦¬μ  μ μ₯ μμμ λ¬Όλ¦¬μ  μ μ₯ μμκ° μΌμΉνλ μλ£κ΅¬μ‘°. λ°λΌμ μΈλ±μ€(Index)λ‘ ν΄λΉ μμμ μ κ·Όν  μ μμΌλ©° Random Accessκ° κ°λ₯ν©λλ€. νμ§λ§ μ½μ/μ­μ  μ ν΄λΉ μμμ μ κ·Όνμ¬ μμμ μλ£ν ν λΉ κ³΅κ°μ΄ μκΈ°μ§ μλλ‘ shift ν΄μ€μΌ νλ―λ‘ O(N)μ μκ°μ΄ μμλ©λλ€.

#### **βοΈ μ₯μ **

λΌλ¦¬μ  μ μ₯ μμ = λ¬Όλ¦¬μ  μ μ₯ μμ

λ©λͺ¨λ¦¬μμμ μμλ€μ΄ μ°μμ μΌλ‘ λΆμ΄μμ΄ μΈλ±μ€ κ°μ μ΄μ©νμ¬ λλ€ μ κ·Ό(Random Access)μ΄ κ°λ₯

#### **β λ¨μ **

μ½μ/ μ­μ κ° λ²κ±°λ‘μ

μ΄κΈ°μ λ°°μ΄μ ν¬κΈ°λ₯Ό μ§μ ν΄μΌ νλ©°, κ³ μ μ μ΄κ³  λ³κ²½ν  μ μμ

 

## **π λμ  λ°°μ΄(Dynamic Array)**

#### **π νΉμ§**

λ°°μ΄κ³Όλ μ‘°κΈ λ€λ₯΄κ² λμ  λ°°μ΄μ ν¬κΈ°λ₯Ό μ λμ μΌλ‘ ν  μ μκ³  λ©λͺ¨λ¦¬μμμ μμλ€μ΄ μ°μμ μΌλ‘ λΆμ΄μμ΄ μΈλ±μ€ κ°μ μ΄μ©νμ¬ λλ€ μ κ·Ό(Random Access)μ΄ κ°λ₯ν©λλ€.

#### **βοΈ μ₯μ **

λ°°μ΄μ ν¬κΈ°κ° μ λμ 

λ©λͺ¨λ¦¬μμμ μμλ€μ΄ μ°μμ μΌλ‘ λΆμ΄μμ΄ μΈλ±μ€ κ°μ μ΄μ©νμ¬ λλ€ μ κ·Ό(Random Access)μ΄ κ°λ₯

#### **β λ¨μ **

μ½μ/ μ­μ κ° λ²κ±°λ‘μ

 

## **π μ°κ²° λ¦¬μ€νΈ(Linked List)**

#### **π νΉμ§**

μ΄λ ν λΈλκ° λ°μ΄ν°μ λ€μ λΈλμ λν μ£Όμ μ λ³΄(ν¬μΈν°)λ₯Ό κ°μ§κ³  λΈλλ€λΌλ¦¬ μμ°¨μ μΌλ‘ μ°κ²°λμ΄μλ λ°©μμ μλ£κ΅¬μ‘°μλλ€.

#### **βοΈ μ₯μ **

μ½μ, μ­μ κ° λΉ λ¦

νμν  λ ν¬κΈ°λ₯Ό λλ¦¬κ±°λ μ€μΌ μ μμ΄ λ©λͺ¨λ¦¬ κ΄λ¦¬κ° ν¨μ¨μ 

μ°μλ λ©λͺ¨λ¦¬ κ³΅κ°μ΄ νμ μμ

#### **β λ¨μ **

λ©λͺ¨λ¦¬ μ°μμ±μ κ°μ§μ§ μκΈ° λλ¬Έμ λλ€ μ κ·Ό(Random Access)μ΄ λΆκ°λ₯

κ²μ μ μ²μ λΈλλΆν° μμ°¨μ μΌλ‘ μνν΄μΌ ν©λλ€.

 

## **π μκ° λ³΅μ‘λ λΉκ΅**

| **μμ** | **λ°°μ΄** | **λμ  λ°°μ΄** | **μ°κ²° λ¦¬μ€νΈ** |
| -------- | -------- | ------------- | --------------- |
| **κ²μ** | O(1)     | O(1)          | O(N)            |
| **μ½μ** | O(N)     | O(N)          | O(N)            |
| **μ­μ ** | O(N)     | O(N)          | O(N)            |

(μ½μ, μ­μ νλ €λ λ°μ΄ν°μ μμΉκ° λ§¨ μ νΉμ λ§¨ λ€ μΌ κ²½μ° μκ° λ³΅μ‘λκ° O(1)μ΄ λ  μλ μμ΅λλ€.)

 

**λ°μ΄ν° μ κ·Ό(νμ, μ‘°ν)μ΄ λΉλ²ν  κ²½μ° => Array**

**λ°μ΄ν° μμ (μ½μ, μ­μ )μ΄ λΉλ²ν  κ²½μ° => Linked List**