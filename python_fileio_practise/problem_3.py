import random 
def game():
  print("your playing a game :")
  score =  random.randint(1,100)
  with open("python_fileio_practise\\hiscore.text") as f:
   hiscore = f.read()
  if hiscore!="":
    hiscore =  int(hiscore)
  else:
    hiscore = 0
  print(f"your score is {score}")
  if(score>hiscore):
    print("congratulations! you have the highest score")
    with open("python_fileio_practise\\hiscore.text","w") as f:
        f.write(str(score))
  return score
game()