# Mad Libs Story Generator
# This program takes a story template with placeholder words inside <>.
# The user is prompted to enter custom words for each placeholder.
# The program replaces the placeholders and displays the final story.

with open("story.txt","r") as f:
    story=f.read()

words=set()
start_of_word=-1

for i,char in enumerate(story):
    if char=='<':
        start_of_word=i
    if char=='>' and start_of_word!=-1:
        word =story[start_of_word:i+1]
        words.add(word)
answer={}
for word in words:
    ans=input(f"Enter an {word} :")
    answer[word]=ans
for word in words:
    story=story.replace(word,answer[word])
print(story)





