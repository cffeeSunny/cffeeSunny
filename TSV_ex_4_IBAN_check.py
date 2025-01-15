
def verify_iban(iban: str) -> bool:
   iban_list=list(iban)
   first_half=iban_list[4:]
   second_half=iban_list[:4]
   new_iban_list=first_half +second_half
   acc=""
   nums="1234567890"
   nums=list(nums)
   dictionary={"A":"10", "B" : "11","C" : "12","D":"13", "E" :"14","F" :"15","G" :"16","H" :"17","I":"18", "J" :"19","K" :"20","L" :"21","M" :"22","N":"23", " O" :"24","P" :"25","Q" :"26","R" :"27","S" :"28","T" :"29","U":"30","V" :"31","W" :"32","X" :"33","Y" :"34","Z" :"35" }
   for element in new_iban_list:
       if not (element in nums):
           acc+= dictionary.get(element)
   return (int(acc) % 97 == 1)
   pass