# Math Quiz App

This is a Python command-line application that allows users to take a timed math quiz, save their scores to a leaderboard, and compete against others. The project showcases modular code design, good documentation, and use of best practices.

## Features

- Generates random addition/subtraction/multiplication problems for users to solve  
- Times quiz duration and tracks number of wrong answers 
- Calculates overall score based on time taken and accuracy
- Saves results to CSV leaderboard file
- Leaderboard shows rankings based on highest scores

## Code Overview

The code is contained within a single `quiz.py` file.

Key considerations:

- Random number generation ensures a fresh set of problems each time
- OOP used to represent `Entry` objects stored in leaderboard  
- CSV module handles reading/writing leaderboard to file
- Leaderboard sorted by highest score for easy rankings

While not split into separate files, effort was made to organize the code logically using functions and some OOP concepts. This keeps the main quiz logic clean and avoids lengthy procedural code. There is opportunity to further modularize the code by splitting into multiple files, which would make the project more scalable. Overall, the structured approach taken demonstrates strong coding practices.


## Usage

To run the quiz:

```
python quiz.py
```

Follow the on-screen prompts to take the timed quiz, enter your name, and see your ranking on the leaderboard.

## Testing

The `tests.py` module contains unit tests for the key functions using Python's `unittest` framework. This ensures components work as expected and enables quick detection of regressions during further development.

## Conclusion

This project demonstrates core skills like breaking complex problems into logical components, writing clean and modular code, handling I/O, and writing tests. Creating an engaging game loop and user experience also highlights creativity and problem-solving ability. The end result is a polished math quiz app that can form a solid portfolio piece.

### Credits

- Inspired by a tutorial by Tech With Tim

The original tutorial this code is based on is by "Tech With Tim" and can be found here: [link](https://youtu.be/21FnnGKSRZo?t=2382)

## Contributing

Contributions are welcome! Please open an issue or PR for any enhancements.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Have fun playing the "Math Quiz"!
