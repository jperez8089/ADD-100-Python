import os 


def main():
#creating a folder 
  os.makedirs("diary",exist_ok=True)

  date = input("enter date: ")
  entry = input("enter your journal entry")

  #writing the file
  with open('diary/diary.txt',"a") as file:
    #allows the entry time and date
    file.write(f"{date}")
    file.write(f"{entry}")

    print("saved")

main()
    
