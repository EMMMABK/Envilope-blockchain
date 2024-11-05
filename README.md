
# Crypto ENVILOPE Blockchain App

This is a cryptocurrency-based web application built using Flask, MySQL, and Python. It features user authentication, a blockchain ledger, and functionalities to register, login, transfer funds, and purchase assets.

The project combines blockchain principles with basic financial transaction functionality. Users can send money, buy assets, and view transaction history on a secure, decentralized ledger using blockchain technology.

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Code Analysis](#code-analysis)
5. [Usage](#usage)
6. [License](#license)

---

## Features
- **User Registration & Login**: Secured authentication system with encrypted passwords.
- **Blockchain Transactions**: Every transaction is recorded on a blockchain.
- **Buy and Send Money**: Ability to perform secure transactions and buy assets.
- **User Balance**: Track user balance by summing received and sent transactions on the blockchain.
- **Dashboard**: Displays blockchain transaction details for logged-in users.

---

## Project Structure

The project is organized as follows:

- **app.py**: Main Flask application, handles routing and transaction logic.
- **blockchain.py**: Defines the blockchain, block structure, and mining logic.
- **forms.py**: Contains forms for registration, login, and transaction functionalities.
- **sqlhelpers.py**: Contains helper classes for interacting with the MySQL database and blockchain synchronization.
- **templates/**: HTML files for rendering the front end (not shown here).

---

## Setup Instructions

Follow these steps to install and run the application:

1. **Clone the repository**:
    ```bash
    git clone <repo_url>
    cd <repo_directory>
    ```

2. **Install dependencies**:
    ```bash
    pip install flask flask_mysqldb passlib wtforms
    ```

3. **Configure the MySQL database**:
   - Ensure MySQL is installed and running on your machine.
   - Create a MySQL database named `crypto`.
   - In the MySQL configuration, create a user with access to this database.
   - Update the `app.config` values in `app.py` with your MySQL credentials.

4. **Run the application**:
   ```bash
   python app.py
   ```
   The app will run at `http://localhost:5000`.

---

## Code Analysis

### 1. **app.py**  
   This file is the main entry point of the application. It initializes the Flask app, configures the MySQL connection, and defines routes for various functionalities. Important functions:
   - `is_logged_in()`: Decorator function to secure routes that require login.
   - `log_in_user()`: Logs the user into the session after verifying credentials.
   - `transaction()`: Allows logged-in users to send money to other users.
   - `buy()`: Simulates buying currency from the "BANK" by adding funds to the user’s balance.

### 2. **blockchain.py**  
   This file defines the blockchain and block classes:
   - `updatehash()`: Creates a SHA-256 hash based on block data.
   - `Block` class: Represents a single block in the blockchain with properties like data, previous hash, nonce, etc.
   - `Blockchain` class: Manages a list of blocks. The `mine()` method finds a nonce value that meets the required difficulty (5 leading zeros).

### 3. **forms.py**  
   Contains form classes based on WTForms:
   - `RegisterForm`, `SendMoneyForm`, `BuyForm`: Define validation rules and form fields for user inputs.

### 4. **sqlhelpers.py**  
   This file contains helper classes for MySQL interactions:
   - `Table` class: Manages database tables, allowing insertion, deletion, and data retrieval.
   - `send_money()`: Validates and processes transactions, raising exceptions if the balance is insufficient or if the transaction is otherwise invalid.
   - `get_blockchain()` and `sync_blockchain()`: Manages blockchain data storage and retrieval from the MySQL database.

---

## Usage

### User Registration
- Navigate to the registration page and create a new account by filling out the form.
- After registration, the user is automatically logged in and redirected to the dashboard.

### Login & Dashboard
- Login using valid credentials. Successful login redirects to the dashboard, displaying a summary of the blockchain transactions.

### Sending and Receiving Money
- Navigate to the transaction page to send money. You must enter the recipient’s username and the amount to be sent.
- If the balance is sufficient, the transaction is recorded on the blockchain.

### Buying Assets
- Navigate to the buy page to add funds. Enter the amount you wish to buy from the "BANK."

### Checking Blockchain Integrity
- Blockchain integrity can be verified by checking the hashes of each block to ensure they align correctly.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
