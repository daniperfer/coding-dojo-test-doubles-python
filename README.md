# Coding dojo test doubles  
A solution for this kata, which was conducted at Gradiant by [Marcos Cela][Marcos Cela github] e Iván Gómez Rodríguez. 
  
# Objective  
  
Learn about some core concepts on testing using the so called helpers:  
  
- What kind of helpers can we use?  
- What does each kind of helper do?  
- How do I use them?  
  
# Source  
  
Most of the code, ideas and other were extracted from [Luis Rovirosa's GitHub][github/luisrovirosa/katas-java], as part  of the [Codium][Codium team main page] TDD course, conduced by [Luis Rovirosa][Luis Rovirosa LinkedIn] and [Jordi Anguela][Jordi Anguela LinkedIn].  
  
[github/luisrovirosa/katas-java]: https://github.com/luisrovirosa/katas-java/tree/master/print-date  
[Codium team main page]: http://www.codium.team  
[Luis Rovirosa LinkedIn]: https://www.linkedin.com/in/luisrovirosa  
[Jordi Anguela LinkedIn]: https://www.linkedin.com/in/jordianguela  
[Marcos Cela github]: https://github.com/Markoscl  
  
# Goal  
Be able to test ***`print_current_date`*** function without changing the method signature.  
  
  
## Rules of the kata  
  
* Under NO CIRCUNSTANCE touch the `__main__` function in `dojo.py`. It is a very  
  important production class that MUST NOT be modified.  
  
* You must test the `PrintDate` class to ensure that it does what it should do.  
  Since we want to mimic real-world coding standards, we will not tell you  
  what the class do, you should know!  
  
* You can change the `PrintDate` and `PrintDateTest` all you want with the following exceptions:  
  * Do NOT change the name!  
  * Do NOT change the signature of the method!  
  * DO NOT change the name of the method!  
  
* You can add libraries.  
  
## Steps  
  
* Test the code with doubles created by you (interface method)  
* Test the code with doubles from a library (usually MagicMock)  
  
## Code to test  
  
Method `print_current_date` from class `PrintDate`.  
  
  
## Learnings  

How to build a Mock and Stub manually.  
How to use a testing framework to generate the doubles.  
  
## Run  tests
  
```  
pytest -v src/dojo_test.py  
```
