def solution(array):
  answer = 0
  for i in array:
      arr = list(str(i))
      print(arr)
      answer += arr.count('7')
  return answer