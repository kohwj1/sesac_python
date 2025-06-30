def palindrome(word):
    return word == word[::-1]

print(palindrome('우영우'))


def palindrome2(word):
    return word.lower() == word[::-1].lower()

print(palindrome2('Anna'))


def palindrome3(word):
    return word.replace(' ','').lower() == word[::-1].replace(' ','').lower()

print(palindrome3('My gym'))