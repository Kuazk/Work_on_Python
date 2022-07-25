import sys


def solution(N):
  
  num_str,result,mult = str(N),0,1
  hash = [0 for _ in range(10)]
  
  #record the number range from 0 to 9
  for num in range(len(num_str)):
    hash[int(num_str[num])] += 1
  for i in range(10):
    while hash[i] > 0:
      result += (i*mult)
      hash[i] -= 1
      mult *= 10
      
  return result

print(solution(12345))