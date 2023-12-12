#1. 
def product(a, b):
    return a * b

#2. 
def weekday_name(day_of_week):

    DAYS = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None

    return DAYS[day_of_week - 1]

#3.
def last_element(lst):
    if lst:
        return lst[-1]

#4. 
def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"

#5.
def reverse_string(phrase):
    return phrase[::-1]

#6. 
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

#7. 
def multiple_letter_count(phrase):
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter

#8. 
def list_manipulation(lst, command, location, value=None):

    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst

#9. 
def is_palindrome(phrase):

    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]

#10. 
def frequency(lst, search_term):

    return lst.count(search_term)

#11. 
def flip_case(phrase, to_swap):

    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out

#12. 
def multiply_even_numbers(nums):

    product = 1

    for num in nums:
        if num % 2 == 0:
            product = product * num

    return product

#13. 
def capitalize(phrase):

    return phrase.capitalize()

#14. 
def compact(lst):

    return [val for val in lst if val]

#15. 
def intersection(l1, l2):

    set2 = set(l2)

    return [val for val in l1 if val in set2]

#16. 
def partition(lst, fn):

    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)

    return [true_list, false_list]

#17.
def mode(nums):

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    max_value = max(counts.values())

    for (num, freq) in counts.items():
        if freq == max_value:
            return num

#18. 
def calculate(operation, a, b, make_int=False, message='The result is'):

    if operation == "add":
        res = a + b
    elif operation == "subtract":
        res = a - b
    elif operation == "multiply":
        res = a * b
    elif operation == "divide":
        res = a / b
    else:
        return

    if make_int:
        res = int(res)

    return f"{message} {res}"

#19. 
def friend_date(a, b):

    if set(a[2]) & set(b[2]):
        return True
    else:
        return False

#20.
def triple_and_filter(nums):

    return [num * 3 for num in nums if num % 4 == 0]

#21. 
def extract_full_names(people):

    return [f"{person['first']} {person['last']}" for person in people]

#22. 
def sum_floats(nums):

    return sum([num for num in nums if isinstance(num, float)])

#23. 
def list_check(lst):

    for item in lst:
        if not isinstance(item, list):
            return False

#24. 
def remove_every_other(lst):

    return lst[::2]

#25. 
def sum_pairs(nums, goal):

    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()

#26. 
VOWELS = set("aeiou")

def vowel_count(phrase):

    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter

#27.
def titleize(phrase):

    return phrase.title()

#28. 
def find_factors(num):

    n_list = [n for n in range (1, num // 2 + 1) if num % n == 0]

    n_list.append(num)

    return n_list

#29.
def includes(collection, sought, start=None):

    if isinstance(collection, dict):
        return sought in collection.values()

    if start is None or isinstance(collection, set):
        return sought in collection

    return sought in collection[start:]

#30. 
def repeat(phrase, num):

    if not isinstance(num, int) or num < 0:
        return None

    return phrase * num

#31. 
def truncate(phrase, n):

    if n < 3:
        return "Truncation must be at least 3 characters."

    if n > len(phrase) + 2:
        return phrase

    return phrase[:n - 3] + "..."

#32. 
def two_list_dictionary(keys, values):

    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

    return out

#33. 
def sum_range(nums, start=0, end=None):

    if end is None:
        end = len(nums)

    return sum(nums[start:end + 1])

#34. 
def freq_counter(coll):

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts


def same_frequency(num1, num2):


    return freq_counter(str(num1)) == freq_counter(str(num2))

#35. 
def two_oldest_ages(ages):

    uniq_ages = set(ages)
    oldest = sorted(uniq_ages)[-2:]
    return tuple(oldest)

#36. 
def find_the_duplicate(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

#37.
def sum_up_diagonals(matrix):

    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total

#38.
def min_max_keys(d):

    keys = d.keys()

    return (min(keys), max(keys))

#39.
def find_greater_numbers(nums):

    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

    return count


#Further Study:

#1. 

def is_odd_string(word):

    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1

#2. 
def valid_parentheses(parens):

    count = 0

    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0

#3. 
def three_odd_numbers(nums):

    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

    return False

#4. 
def reverse_vowels(s):

    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)
