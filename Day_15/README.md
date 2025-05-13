# ☕ Coffee Machine Project

This is a console-based Coffee Machine program created as part of the **100 Days of Python** course. The program simulates a simple coffee vending machine that serves **espresso**, **latte**, and **cappuccino**. It includes features like checking resources, processing coins, giving change, and turning off the machine.

## 🧠 Features

### 1. Menu Prompt
- The user is continuously prompted with:
"What would you like? (espresso/latte/cappuccino):"
- The prompt shows again after each action is completed so that multiple customers can be served.

### 2. Turn Off the Machine
- Entering `"off"` will stop the program.
- This is intended as a **maintenance command** for shutting down the machine.

### 3. Generate a Report
- Entering `"report"` will display the current state of machine resources:
For example: Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5

### 4. Resource Check
- Before preparing a drink, the program checks if there are **enough ingredients**.
- If not enough, it prints a message like:
  Sorry there is not enough water.

### 5. Coin Processing
- If ingredients are sufficient, the user is prompted to insert coins:
- Quarters = $0.25
- Dimes = $0.10
- Nickels = $0.05
- Pennies = $0.01
- The program calculates the total inserted.

### 6. Transaction Validation
- If the inserted money is **less than** the drink's cost:
  "Sorry that's not enough money. Money refunded."

- If the amount is sufficient:
- The profit is added to the machine.
- If overpaid, it returns change:
  ```
  Here is $0.25 in change.
  ```

### 7. Make Coffee
- Once payment and resources are confirmed:
- Resources are **deducted**.
- The drink is served:
  ```
  Here is your latte. Enjoy!
  ```

## 🧰 Concepts & Skills Practiced
- Functions
- Dictionaries and nested data structures
- Conditionals
- Loops
- User input and output
- Variable scope and mutability

## 📁 Files Included
- `main.py` — contains the full coffee machine logic
- `README.md` — project description

## 🪞 Personal Reflection

This project has been a great opportunity to practice not just Python syntax but also essential **problem-solving** and **planning skills**. It challenged me to think through each step of the logic—breaking down a real-world process into code. I reinforced foundational concepts like `if/else` statements, `while` and `for` loops, and working with dictionaries. Although I was able to get the program working, I realized there are areas where my functions could be improved to be more **concise**



