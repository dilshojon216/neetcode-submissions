def concatenate(s1: str, s2: str) -> str:
      data=s1+s2;
      if len(data)<=10:
          return data
      else:
          return "Too long!"




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
