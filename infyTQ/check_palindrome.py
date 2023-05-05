#lex_auth_012693819159732224162

def check_palindrome(word):
    rev = word[::-1]
    if(rev==word):
      return 1;
    else:
      return 0;
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")