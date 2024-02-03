# Input-name
## Description-
This program imports the io module from the standard library, prompts the user for their name, reads the input, and then prints a personalized greeting using the entered name.
## Explanation-
   -Importing the Standard Library's I/O Module (io):
The use std::io; statement brings in the Input/Output module from the Rust standard library.

   -Defining the main Function:
The fn main() function is the entry point of the program.

   -Prompting User for Input:
println!("Enter your name:"); displays a message instructing the user to input their name.

   -Reading User Input:
let mut name = String::new(); declares a mutable variable name to store the user's input.
io::stdin().read_line(&mut name).expect("Failed to read line"); reads the user's input from the standard input (keyboard) and stores it in the name variable. The expect method is used for error handling in case reading the input fails.

   -Printing Personalized Greeting:
println!("Hello, {}! Welcome to Rust programming.", name.trim()); prints a personalized greeting using the entered name. The trim method is used to remove any trailing newline characters from the user's input.
