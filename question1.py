Timed True/False Math Check


Write a Python program that shows a math statement and asks whether it is true or false.

Requirements:

Randomly generate two integers between 1 and 20.
Randomly select addition, subtraction, or multiplication.
Show a math expression with a proposed answer.
The proposed answer should have a 50% chance of being right and about a 50% chance of being wrong.
The user types t for true, f for false, or done to quit.
The user has 3 seconds to answer.
Always tell the user how long they took to answer.
If they took more than 3 seconds, tell them they were too slow.
Give useful feedback after each answer.
At the end, show total attempted, correct answers, too-slow answers, and percentage correct.
Example Output:

Is this true or false?
8 + 5 = 13
Type t or f: t
Correct! You took 1.4 seconds.
 
Is this true or false?
6 * 4 = 30
Type t or f: t
Incorrect. You took 2.1 seconds.
6 * 4 is actually 24, so the statement was false.
 
Is this true or false?
9 + 2 = 11
Type t or f: t
Too slow! You took 4.2 seconds.
 
Type t, f, or done: done
 
Total attempted: 3
Correct: 1
Too slow: 1
Percentage correct: 33.3%
