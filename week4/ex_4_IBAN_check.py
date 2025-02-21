
def verify_iban(iban: str) -> bool:
   iban_list=list(iban)
   first_half=iban_list[4:]
   second_half=iban_list[:4]
   new_iban_list=first_half +second_half
   acc=0
   chars="abcdefghijklmnopqrstuvwxyz"
   chars.capitalize()
   characters=list(chars)
   nums=[str(i) for i in range (10,35)]
   dictinonary_letters=dict(zip(characters,nums))
   for element in new_iban_list:
       if isinstance(element,int):
           acc+=element
       else:
           acc+= dictinonary_letters[element]
   return acc % 97 == 1
pass

