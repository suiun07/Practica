'1'
def concat_arrays(nums):
    n = len(nums)
    ans = nums + nums
    return ans

nums = [1, 2, 1]
result = concat_arrays(nums)
print(result)

'2'

def permutation(nums):
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        ans[i] = nums[nums[i]]
    return ans

nums = [2, 0, 1, 3]
result = permutation(nums)
print(result)

'3'

def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.8 + 32
    return [round(kelvin, 5), round(fahrenheit, 5)]

celsius = 25.75
result = convert_temperature(celsius)
print(result)
