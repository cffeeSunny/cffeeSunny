def zodiac(birth_year: int) -> str:
    zodiac_dic={1:"Rooster",2:"Dog",3:"Pig",4:"Rat",5:"Ox",6:"Tiger",7:"Rabbit",8:"Dragon",9:"Snake",10:"Horse",11:"Goat",0: "Monkey"}
    zodiac_key = birth_year % 12
    return (zodiac_dic.get(zodiac_key))
    pass


