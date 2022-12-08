#import list of words
from english_words import english_words_lower_set

#access the list of words like this:
words = english_words_lower_set

#list of alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']


#takes list of spelling bee letters and center letter
def answers(letters_list, center_letter):    

  #find not included letters
  unacceptable_letters = [l for l in alphabet if l not in letters_list]
  acceptable_words = []

  
  for word in words:
      if (center_letter in word) and (word not in acceptable_words) and len(word)>3 and any(l in unacceptable_letters for l in word) == False:
        acceptable_words.append(word)
                      
  return acceptable_words
      
      
      
# Test the functionTn

if __name__ == '__main__':
  lst = [*input("What are your letters?: ")]
  print(lst)
  let = input('And which one is in the center?: ')
  print('\n')
  print(f'{len(answers(lst,let))} answers -> {answers(lst,let)}')

  
