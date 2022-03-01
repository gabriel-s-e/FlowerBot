import random

def random_plant():
  return plant_list[random.randint(0, len(plant_list) - 1)]
plant_list = [
  "https://i.gyazo.com/95b1ccd84372ace21354961874b90b5e.png",
  "https://i.gyazo.com/d76af8e21f52b2cba4c809be04febf0d.png",
  "https://i.gyazo.com/11a97964253fcb7f535b78015e8e4f64.png"
]