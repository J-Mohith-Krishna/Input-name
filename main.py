use std::io;

fn main() {
    // Prompt user for input
    println!("Enter your name:");

    // Read user input
    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read line");

    // Print personalized greeting
    println!("Hello, {}! Welcome to Rust programming.", name.trim());
}
