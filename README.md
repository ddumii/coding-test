day1 : 두 수를 사용한 사칙연산 함수 만들기(합/차/곱/몫)

학습 내용 :
 if  (-50000 <= num1 <= 50000) and (-50000 <= num1 <= 50000)
        return answer
        
느낀 점:
간단한 문법 정리가 안되어 있음을 느낌. 
부등호 순서, 들여쓰기 주의해야함.

day2 : 두 수의 나눗셈, 숫자 비교, 기약분수 최대 공약수 리스트로 출력
학습 내용:   if 0 < numer1 < 1000 and 0 < denom1 < 1000 and 0 < numer2 < 1000 and 0 < denom2 < 1000:
        new_numer = (numer1*denom2)+(numer2*denom1) 
        new_denom = (denom1*denom2)
        gcd = math.gcd(new_numer, new_denom)
        result = [ (new_numer//gcd), (new_denom//gcd)]
1. return은 함수 내부에 있어야 한다.(위치 주의!)
2. 기약분수 개념 학습 -> 이번에는 math.gcd를 사용했는데 내일은 for문을 사용해서 gcd 직접 구현해볼 예정이다.

느낀 점:
조건에 따라 코드가 달라짐. 조건을 잘 읽고 이해해서 작업해야 함.
