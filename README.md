# lottery-analysis

I always wanted to understand how randomness worked in computers... I tried to look into Lotto numbers to explore patterns and statistical analysis in what should be truly random data.

## What I Built

This project analyzes historical lottery data from South African Lotto and Powerball draws to understand frequency patterns, generate statistical predictions, and explore different draw generation strategies.

## Project Structure

```
lottery-analysis/
├── main.py                           # Main analysis and prediction engine
├── utils/
│   ├── get_winnings.py               # Load winning draws from data files
│   ├── add_winnings.py               # Add new winning draws to data files
│   └── analyse_winnings.py           # Statistical analysis functions
└── data/
    ├── lotto_winnings.txt            # Historical Lotto draw data
    └── powerball_winnings.txt        # Historical Powerball draw data
```

## Features Implemented

### Data Analysis

- **Frequency Analysis**: Count how often each number appears across all draws
- **Bonus Ball Analysis**: Separate analysis for bonus/powerball numbers
- **Sorting Algorithms**: Custom bubble sort implementation to rank numbers by frequency

### Prediction Strategies

- **Most Probable Draws**: Generate combinations using the most frequently drawn numbers
- **Statistical Scoring**: Score draw combinations based on historical frequency
- **Spread Out Draws**: Generate evenly distributed number combinations
- **Custom Draw Integration**: Include specific number combinations in generated sets

### Data Management

- Load historical draws from text files with date parsing
- Add new winning draws to the dataset
- Support for multiple lottery formats (Lotto, Lotto Plus 1, Lotto Plus 2, Powerball, Powerball Plus)

## What I Discovered

### Lotto Analysis (6 main numbers + 1 bonus from 1-52)

- Analyzes frequency of main numbers and bonus balls separately
- Generates 20 most probable combinations based on historical data
- Creates spread-out combinations for better number distribution

### Powerball Analysis (5 main numbers + 1 powerball from 1-50)

- Similar frequency analysis with different number ranges
- Separate bonus ball analysis for powerball numbers
- Statistical scoring system for ranking combinations

## Key Insights About Randomness

Through this analysis, I explored whether lottery draws are truly random by:

- Examining frequency distributions of numbers over time
- Looking for patterns in bonus ball selections
- Testing different prediction strategies against historical data
- Comparing deterministic vs. spread-out number selection methods

## Usage

Run the main analysis:

```bash
python main.py
```

The program will:

1. Load historical lottery data
2. Calculate frequency statistics for all numbers
3. Generate three types of predictions:
   - Most probable draws (frequency-based)
   - Statistically scored draws
   - Spread-out draws with custom numbers

## Data Format

Lottery data is stored in plain text files with the format:

```
day draw numbers
2025-07-04 powerball 15,16,22,30,32,07
```

## Future Exploration

- Time-series analysis to detect trends over periods
- Machine learning models for pattern recognition
- Visualization of frequency distributions
- Cross-lottery comparison analysis
- Monte Carlo simulations for probability testing
