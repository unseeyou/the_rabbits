story = "The rabbits came many grandparents ago. || At first, we didn’t know what to think. || They looked a bit like us. There weren’t many of them. || Some were friendly, but our old people warned us, || “be careful they won’t understand the right ways. They only know their own country.” || They came by water. || They didn’t live in the trees like we did. They made their own houses. || We couldn’t understand the way they talked. || They brought new food and they brought other animals. || We liked some of the food and we liked some of the animals, || but some of the food made us sick, and some of the animals scared us. || The rabbits spread across the country. || No mountain could stop them. || No desert, no river. || Still more of them came. || Sometimes we had fights, || but there were too many rabbits. || We lost the fights. || They ate our grass, they chopped down our trees, || and scared away our friends, and stole our children. || Rabbits, rabbits, rabbits. || Millions and millions of rabbits, everywhere we look there are rabbits. || The land is bare and brown, and the wind blows empty across the plain. || Where is the rich dark earth, brown and moist? || Where is the smell of rain dripping from gum trees? || Where are the great billabongs, alive with long-legged birds who will save us from the rabbits?"

rabbit = """   /gg\           /gg\ 
  /g.gg\         /gg.g\ 
 |gg..gg\       /gg..gg| 
 |gg...g|       |g...gg| 
 |gg...g|       |g...gg| 
  \gg..g/       \g..gg/ 
   |gg.gvgggggggvg.gg| 
  /ggggggggggggggggggg\ 
 /gggg(((ggggggg)))gggg\ 
|ggggg....ggggg....ggggg| 
|ggggg....ggggg....ggggg| 
|ggcccgggg\___/ggggcccgg| 
|ggcccccgggg|ggggcccccgg| 
  \gcccggg\---/gggcccg/ 
     \ggggggggggggg/"""

write = story.split('|| ')

print(' ')
print("== The Rabbits - by John Marsden ==") # title

for line in write:
    print(line)

print(' ')
print(rabbit)
