class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return  ["FizzBuzz" if number % 3==0 and number % 5 ==0 else "Fizz" if number % 3 ==0 else "Buzz" if number % 5 ==0 else str(number) for number in range(1,n+1)]