'''
    Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
    Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
    Write the Function:
        Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
        Use f-strings to incorporate these parameters into the song's lyrics.
        Ensure the function prints the customized song lyrics.
    Collect User Input:
        Write code to collect user input for each of the 8 variables.
        Use clear and descriptive prompts to guide the user.
    Call the Function:
        Call the custom_song function with the user inputs as named arguments.
        Ensure the order of arguments matches the parameters in your function definition.
        Hiya, Barbie!
Hi, Ken!
You wanna go for a ride?
Sure, Ken!
Jump in!
I'm a Barbie girl in a Barbie world
Life in plastic, it's fantastic
You can brush my hair, undress me everywhere
Imagination, life is your creation
Come on Barbie, let's go party

'''



#making a function with parameters
def barbie_world(greeting1,greeting2,name1,name2,travelingverb,adjective,emotion,action):
  print(f"{greeting1},{name1}")
  print(f"{greeting2},{name2}")
  print(f"you wanna go for a ", {travelingverb})
  print(f"Sure {name2}")
  print("Jump in!")
  print(f"Im a {adjective} girl, in a ")
  print(f"{emotion}, world!")
  print(f"you can{action} my hair, take me everywhere")

def main():
  greeting1 = input("enter a greeting")
  greeting2 = input("enter a second greeting")
  name1 = input("enter a name")
  name2 = input("enter a second name")
  travelingverb = input("enter a traveling verb")
  adjective = input("enter an adjective")
  emotion = input("enter an emotion ")
  action = input("enter an action ")

  barbie_world(
        greeting1=greeting1,
        greeting2=greeting2,
        name1=name1,
        name2=name2,
        travelingverb=travelingverb,
        adjective=adjective,
        emotion=emotion,
        action=action,
    )


    

main()