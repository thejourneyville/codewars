"""
Story
A freak power outage at the zoo has caused all of the electric cage doors to malfunction and swing open...

All the animals are out and some of them are eating each other!

It's a Zoo Disaster!
Here is a list of zoo animals, and what they can eat

antelope eats grass
big-fish eats little-fish
bug eats leaves
bear eats big-fish
bear eats bug
bear eats chicken
bear eats cow
bear eats leaves
bear eats sheep
chicken eats bug
cow eats grass
fox eats chicken
fox eats sheep
giraffe eats leaves
lion eats antelope
lion eats cow
panda eats leaves
sheep eats grass
Kata Task
INPUT
A comma-separated string representing all the things at the zoo

TASK
Figure out who eats whom until no more eating is possible.

OUTPUT
A list of strings (refer to the example below) where:

The first element is the initial zoo (same as INPUT)
The last element is a comma-separated string of what the zoo looks like when all the eating has finished
All other elements (2nd to last-1) are of the form X eats Y describing what happened
Notes
Animals can only eat things beside them

Animals always eat to their LEFT before eating to their RIGHT

Always the LEFTMOST animal capable of eating will eat before any others

Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible

Example
Input

"fox,bug,chicken,grass,sheep"

Working

1	fox can't eat bug	
"fox,bug,chicken,grass,sheep"
2	bug can't eat anything	
"fox,bug,chicken,grass,sheep"
3	chicken eats bug	
"fox,chicken,grass,sheep"
4	fox eats chicken	
"fox,grass,sheep"
5	fox can't eat grass	
"fox,grass,sheep"
6	grass can't eat anything	
"fox,grass,sheep"
7	sheep eats grass	
"fox,sheep"
8	fox eats sheep	
"fox"
Output

["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"]
"""

def prep_data(data):
    animals = {}
    line = ""
    for i in data:
        if i == "\n":
            if line:
                pred_prey = line.split("eats")
                line = ""

                animals.setdefault(pred_prey[0], [])
                animals[pred_prey[0]].append(pred_prey[-1])
                continue

        elif i == " ":
            continue
        else:
            line += i
    return animals
        

rules = """
antelope eats grass
big-fish eats little-fish
bug eats leaves
bear eats big-fish
bear eats bug
bear eats chicken
bear eats cow
bear eats leaves
bear eats sheep
chicken eats bug
cow eats grass
fox eats chicken
fox eats sheep
giraffe eats leaves
lion eats antelope
lion eats cow
panda eats leaves
sheep eats grass
"""
predators = prep_data(rules)

def who_eats_who(zoo):
    
    lineup = zoo.split(",")
    eaten = True
    circle_of_life = [zoo]

    while eaten:

        for idx, animal in enumerate(lineup):
            eaten = False
            
            if animal in predators:
                
                if idx > 0 and lineup[idx - 1] in predators[animal]:
                    circle_of_life.append(f"{animal} eats {lineup[idx - 1]}")
                    lineup.pop(idx - 1)
                    eaten = True
                
                elif idx < len(lineup) - 1 and lineup[idx + 1] in predators[animal]:
                    circle_of_life.append(f"{animal} eats {lineup[idx + 1]}")
                    lineup.pop(idx + 1)
                    eaten = True

            if eaten:
                break
        else:
            eaten = False

    return circle_of_life + [",".join(lineup)]


data = "fox,bug,chicken,grass,sheep,poop"
print(who_eats_who(data))

"""
Expected output:
expected = ["fox,bug,chicken,grass,sheep", 
            "chicken eats bug", 
            "fox eats chicken", 
            "sheep eats grass", 
            "fox eats sheep", 
            "fox"]
"""
