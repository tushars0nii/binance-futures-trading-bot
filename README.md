# Binance Futures Trading Bot

A command-line cryptocurrency trading bot built using Python and the Binance Futures Testnet API. The bot allows users to place market and limit orders, cancel orders, monitor positions, and check account balances through a simple menu-driven interface.

## Features

- Secure API authentication using environment variables
- Binance Futures Testnet integration
- Market Order execution
- Limit Order execution
- Order cancellation
- Wallet balance tracking
- Open position monitoring
- Input validation
- Error handling and logging
- Menu-driven Command Line Interface (CLI)

---

## Tech Stack

- Python 3
- Binance API
- python-binance
- python-dotenv
- Logging Module

---

## Project Structure

```text
trading_bot/
│
├── cli.py
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── logs/
│
└── .env
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate the environment:

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root directory.

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
SECRET_KEY=YOUR_BINANCE_TESTNET_SECRET_KEY
```

**Important:** Never upload your `.env` file to GitHub.

---

## Running the Bot

Start the trading bot:

```bash
python3 cli.py
```

---

## CLI Menu

```text
========================================
 BINANCE FUTURES TRADING BOT
========================================

1. Check Balance
2. Market Order
3. Limit Order
4. View Positions
5. Cancel Order
6. Exit
```

---

## Available Functions

### Check Balance

Displays available USDT balance in the Futures Testnet wallet.

### Market Order

Place a market buy or sell order.

Example:

```text
Symbol: BTCUSDT
Side: BUY
Quantity: 0.001
```

### Limit Order

Place a limit order at a specified price.

Example:

```text
Symbol: BTCUSDT
Side: BUY
Quantity: 0.001
Price: 50000
```

### View Positions

Displays currently active futures positions including:

- Symbol
- Quantity
- Entry Price

### Cancel Order

Cancel an existing limit order using:

- Symbol
- Order ID

---

## Logging

All order activity and errors are automatically recorded in:

```text
logs/bot.log
```

Example log entry:

```text
2025-07-01 16:30:45 - INFO - MARKET ORDER | BUY | BTCUSDT | Qty=0.001
```

---

## Security

- API keys are stored using environment variables.
- Sensitive information is excluded using `.gitignore`.
- Testnet environment is used to avoid real financial risk.

---

## Sample Output

```text
========================================
 BINANCE FUTURES TRADING BOT
========================================

1. Check Balance
2. Market Order
3. Limit Order
4. View Positions
5. Cancel Order
6. Exit

Select Option: 1

USDT Balance: 4999.95
```

---

## Future Improvements

- Stop Loss Orders
- Take Profit Orders
- Real-Time Price Tracking
- Profit & Loss Dashboard
- Telegram Notifications
- Streamlit Web Interface
- Automated Trading Strategies
- Trade History Analytics

---

## Author

**Tushar Soni**

B.Tech Electronics and Communication Engineering

Python Developer | Machine Learning Enthusiast | Future AI Engineer