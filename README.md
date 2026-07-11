# NBA Stats CLI

A small Python CLI tool for fetching NBA player and team info using the [BallDontLie](https://www.balldontlie.io/) API. Built as a mini-project to practice working with `argparse` and REST APIs.

## Features

- Look up a player by first name (or first + last name)
- List all 30 NBA teams

## Prerequisites

- Python 3.8+
- A free API key from [balldontlie.io](https://www.balldontlie.io/) (sign up, then grab your key from your account dashboard)

## Installation

1. Clone the repo:
   ```bash
   git clone <https://github.com/giovannylindor/nba-api-practice.git>
   cd <nba-api-practice>
   ```

2. Install dependencies:
   ```bash
   pip install balldontlie python-dotenv
   ```

## Configuration

Create a `.env` file in the project root and add your API key:

```env
BALLDONTLIE_API=your_api_key_here
```

> The script loads this automatically via `dotenv`. Alternatively, you can hardcode the key directly in `script.py` in place of `os.getenv("BALLDONTLIE_API")`, but using a `.env` file is recommended so you don't accidentally commit your key.

## Usage

### Get a player by first name
```bash
python script.py -p LeBron
```

### Get a player by first and last name (recommended for common first names)
```bash
python script.py -p LeBron James
```

### List all NBA teams
```bash
python script.py --t
```

## Options

| Flag       | Description                                  |
|------------|-----------------------------------------------|
| `-p`       | Fetch player info. Accepts 1 or 2 args: `first_name` or `first_name last_name` |
| `--t`      | Fetch all 30 NBA teams                        |

## Example Output

**Player lookup:**
```
Name: LeBron James
Position: F
Height: 6-9
Weight: 250
College: 
Team: Los Angeles Lakers
```

**Team list:**
```
Atlanta Hawks
Boston Celtics
Brooklyn Nets
```
