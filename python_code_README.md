# Pension Portfolio Lifecycle Python Utilities

## Description

This project provides a Python script (`portfolio_structures.py`) that defines and manages sample pension fund lifecycle portfolios (Growth, Maturity, and Decline). The script demonstrates several utilities for these portfolios, including:

*   Displaying detailed portfolio allocations.
*   Simulating rebalancing actions between a drifted portfolio and a target portfolio.
*   Retrieving target portfolios based on a given life cycle stage.
*   Generating and saving pie chart visualizations of major asset class allocations.

## Files

*   **`portfolio_structures.py`**:
    *   The main Python script containing the definitions of reference portfolio structures for Growth, Maturity, and Decline stages.
    *   Includes functions to display portfolio details, simulate rebalancing, retrieve portfolios by stage, and visualize allocations.
    *   The `if __name__ == '__main__':` block demonstrates the usage of all these functions.
*   **Generated Visualization Files**:
    *   `Growth_Stage_Portfolio_visualization.png`
    *   `Maturity_Stage_Portfolio_visualization.png`
    *   `Decline_Stage_Portfolio_visualization.png`
    *   `Drifted_Growth_Portfolio_Example_visualization.png`
    *   These PNG files are generated when `portfolio_structures.py` is executed. Each file contains a pie chart representing the major asset class allocations for the respective portfolio.

## Requirements/Dependencies

*   Python 3.x
*   `matplotlib` (for portfolio visualization)

## Installation of Dependencies

To install the necessary Python libraries, run the following command:

```bash
pip install matplotlib
```

## How to Run

To execute the script and see the demonstrations, run the following command in your terminal from the directory containing the file:

```bash
python portfolio_structures.py
```

## Expected Output

When you run the script, you should expect to see the following:

1.  **Console Output:**
    *   Detailed allocations for the Growth, Maturity, and Decline stage target portfolios.
    *   Allocations for a sample "Drifted Growth Portfolio."
    *   A step-by-step simulation of rebalancing actions required to bring the drifted portfolio back to its target allocation.
    *   Demonstration of retrieving a target portfolio (e.g., for the "Maturity" stage) and handling of invalid stage names.
    *   Messages indicating that pie chart visualization files have been saved (e.g., "Portfolio visualization saved to 'Growth_Stage_Portfolio_visualization.png'").
    *   A final verification of total allocations for each defined portfolio.

2.  **Image Files Created:**
    *   Several PNG image files (as listed under the "Files" section above) will be created in the same directory where the script is run. These images are pie charts visualizing the asset allocations.

This script is intended for educational and illustrative purposes to showcase how portfolio structures can be defined and manipulated programmatically.
