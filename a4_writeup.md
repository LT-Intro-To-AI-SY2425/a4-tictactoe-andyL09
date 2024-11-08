# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
>        For me the most difficult part of the tic tac toe game was working with the win conditions and the formatting and storage of the data for the board.  I had a slightly different approach to storing the data for the board.  I had originally had made three separate lists each with 3 values.  This approach would have worked pretty well too i think but i was having some trouble with the win conditions and it was easier to follow the given solution if my storage method for the board data was the same, though i do feel like my method was slightly more clear in what value took what space on the board.  
2. Explain how you would add a computer player to the game.
>        If you wanted to add a computer player to the game you would have to have the computer look at all values on the board.  It would then have to  check to see if there was any places on the board that had the value "*" then it would have to decide where to place its move using those.  If you just want to implement it really simply you could just have it choose randomly. It might be a Little more difficult to have it make intelligent moves.  
3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
>        To make a computer player you would probally need to make the computer first check to see what spots are open by looking at he board and checking what spots have "*". Then it would have to check the spaces around that spot to see if there was a possibility to either connect to one of its own blocks or block a opponents move.  It might just have to check the whole board when it is considering and diagonal moves come into play ontop of regular horzontal and vertical moves.  