import csv
import json

# strings for palindrome test
palindrome_word = "deified"
palindrome_word_two = "deed"
non_palindrome_word = "summer"
palindrome_phrases_one = "Name now one man"
palindrome_phrases_two = "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"
non_palindrome_phrases = "Notable palindromic phrases in English"
palindrome_phrases_three = (
    "T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt "
    "upset on drab pot toilet.")

palindrome_string_list = [palindrome_word, palindrome_word_two, non_palindrome_word, palindrome_phrases_one,
                          palindrome_phrases_two, non_palindrome_phrases, palindrome_phrases_three]


# removes punctuations, spaces and concatenate in single string of lower letters
def punctuation_and_spaces_remover(string: str):
    return "".join(
        [
            c for c in string if c.isalnum()
        ]
    ).lower()


# checks if given number is int
def is_int(number):
    if isinstance(number, int):
        return True
    else:
        return False


def is_str(data):
    if isinstance(data, str):
        return True
    else:
        return False


# does not specify the expected argument type since uses list and str
def is_same_str(str_one, str_two):
    if str_one == str_two:
        return True
    else:
        return False


def read_from_csv(file: csv):
    with open(file, "r") as f:
        csv_file = csv.reader(f)
        csv_file.__next__()
        return [line for line in csv_file]


def read_from_json(file: json):
    with open(file, "r") as f:
        json_file = json.load(f)
        return json_file


def write_to_csv(filename, arr: list, fieldnames_list: list):
    with open(filename, "w") as f:
        csv_file = csv.DictWriter(f, fieldnames=fieldnames_list)
        csv_file.writeheader()
        csv_file.writerows(arr)
        return f"{filename} exported"


def sum_pairs_match(number: int, arr: list):
    pairs_list = []
    # adds each pair of numbers from the array whose sum is equal to the target number
    for i in arr:
        [
            pairs_list.append((i, j))
            for j in arr
            if i + j == number
        ]
    return pairs_list


def two_sum_unique_pairs(arr: list):
    unique_pairs = set()
    # sorting the pairs and using a set to filter unique only
    [
        unique_pairs.add(tuple(sorted(pair)))
        for pair in arr
    ]
    return unique_pairs


# checks if there is any element different from int in a given array
def is_int_arr(arr):
    for n in arr:
        if not is_int(n):
            return False
    else:
        return True


# reverse a string and join it
def reverse_str(string: str):
    return "".join([c for c in reversed(string)])
