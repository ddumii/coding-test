#두 수의 나눗셈
def solution(num1, num2):
    if (0 <= num1 <=100) and (0 <= num2 <= 100):
        answer = (num1 / num2) * 1000
    return int(answer)

#숫자 비교하기
def solution(num1, num2):
    if (0 <= num1 <= 10000) and (0 <= num2 <= 10000):
        if num1 == num2:
            answer = 1
        else:
            answer = -1
    return answer


#분수의 덧셈
import math
def solution(numer1, denom1, numer2, denom2):
    if 0 < numer1 < 1000 and 0 < denom1 < 1000 and 0 < numer2 < 1000 and 0 < denom2 < 1000:
        new_numer = (numer1*denom2)+(numer2*denom1) 
        new_denom = (denom1*denom2)
        gcd = math.gcd(new_numer, new_denom)
        result = [ (new_numer//gcd), (new_denom//gcd)]
    return result

    