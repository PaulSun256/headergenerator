'''
+============================+
|         splitter()         |
+============================+
| Params:                    |
| - (str) string:            |
|   - String to smart-split  |
|     without cutting off    |
|     words.                 |
|                            |
| - (int) length:            |
|   - Maximum length of a    |
|     single line.           |
+============================+
'''
def spliter(string, length):

  output = ' ';
  cut = string[0:length].rfind(' ');
  output += string[0:cut] + '\n';
  newcut = cut + length;
  oldcut = cut;

  while newcut < len(string):
    cut = string[oldcut:newcut].rfind(' ');
    output += string[oldcut:oldcut+cut] + '\n';
    oldcut += cut;
    newcut = oldcut + length;

  output += string[oldcut:len(string)];
  oldcut += cut;
  newcut = oldcut + length;

  return output;

'''
+======================================+
|              formatA()               |
+======================================+
| Params:                              |
| - (str) title:                       |
|   - Title of the program to generate |
|     header for.                      |
|                                      |
| - (str) creator:                     |
|   - String to store the maker's name.|
|                                      |
| - (str) date:                        |
|   - The date this was made.          |
|                                      |
| - (str) teacher:                     |
|   - Course and teacher name.         |
|                                      |
| - (str) description:                 |
|   - Brief description of the program.|
|                                      |
| - (int) width:                       |
|   - How wide the header should be.   |
|     Cannot be modified yet.          |
|                                      |
| - (str) lang:                        |
|   - Language to make header for.     |
|     Headers are comments, and C/Java |
|     comments are different from      |
|     Python.                          |
+======================================+
'''
def formatA(title, creator, date, teacher, description, width, lang):
  finalResult = '';
  
  descriptionLine = description.split('\n');

  if (lang == "1"):
    finalResult += "'''\n";
  else:
    finalResult += '/*\n';
  finalResult += "+" + "=" * width + "+\n";
  finalResult += "|" + title.center(width) + "|\n";
  finalResult += "+" + "=" * width + "+\n";
  finalResult += "|" + (creator + ', ' + date).center(width) + "|\n";
  finalResult += "+" + "=" * width + "+\n";
  finalResult += "|" + teacher.center(width) + "|\n";
  finalResult += "+" + "=" * width + "+\n";
  for i in descriptionLine:
    finalResult += "|" + i.center(width) + "|\n";
  finalResult += "+" + "=" * width + "+\n";
  if (lang == "1"):
    finalResult += "'''\n";
  else:
    finalResult += '*/\n';
  print(finalResult);





run = 'y'
while (run == 'y'):
  title = input('name of program\n-->:');
  creator = input('person who made it\n-->:');
  date = input('date (ISO 8601)\n-->:');
  language = 3;
  while (language != "2" and language != "1"):
    language = input('what language is this program (1 = python, 2 = c/java)\n-->:');
  teacher = input('enter your course and teacher name\n-->:');
  description = spliter(input('tf does this do (dont put words over 40 letters, it will crash and burn)\n-->:'), 40);

  formatA(title, creator, date, teacher, description, 40, language);

  run = input("do you want to make another one? (y or n)\n-->:");
