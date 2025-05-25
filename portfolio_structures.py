# portfolio_structures.py

# This script defines example reference portfolio structures for different
# pension fund life cycle stages (Growth, Maturity, Decline), based on allocations
# detailed in the 'pension_fund_lifecycle.md' document.
# It also provides utility functions to display, rebalance, retrieve, and visualize
# these portfolio allocations.

import matplotlib.pyplot as plt

# --- Portfolio Data Structures ---
# These dictionaries represent the target asset allocation for each life cycle stage.
# Allocations are expressed as decimals (e.g., 0.20 for 20%).

# Growth Stage: Focus on aggressive capital appreciation.
growth_portfolio = {
    "Equities": {
        "Domestic Large-Cap": 0.20,
        "Domestic Mid/Small-Cap": 0.10,
        "International Developed Markets": 0.20,
        "Emerging Markets Equities": 0.20,
    },
    "Fixed Income": {
        "Inflation-Linked Bonds": 0.05,
        "High-Yield Corporate Bonds": 0.05,
    },
    "Real Assets": {
        "Real Estate (REITs/Direct)": 0.05,
        "Infrastructure": 0.05,
    },
    "Alternatives": {
        "Private Equity (Buyout/VC)": 0.08,
    },
    "Cash & Equiv.": { # Renamed from "Cash & Equiv." for consistency
        "Money Market Funds/T-Bills": 0.02,
    }
}

# Maturity Stage: Balance between growth, capital preservation, and income generation.
maturity_portfolio = {
    "Equities": {
        "Domestic Large-Cap": 0.20,
        "International Developed Markets": 0.15,
        "Emerging Markets Equities": 0.10,
        "Low Volatility Equities": 0.05,
    },
    "Fixed Income": {
        "Government Bonds (Intermediate)": 0.10,
        "Investment-Grade Corporate Bonds": 0.10,
        "Inflation-Linked Bonds": 0.10,
    },
    "Real Assets": {
        "Real Estate (REITs/Direct)": 0.07,
        "Infrastructure": 0.05,
    },
    "Alternatives": {
        "Hedge Funds (e.g., Global Macro)": 0.03,
        "Private Debt": 0.02,
    },
    "Cash & Equiv.": { # Renamed from "Cash & Equiv." for consistency
        "Money Market Funds/T-Bills": 0.03,
    }
}

# Decline Stage: Focus on capital preservation, income generation, and liquidity.
decline_portfolio = {
    "Equities": {
        "Domestic Large-Cap (High Dividend)": 0.15,
        "Low Volatility International Equities": 0.10,
    },
    "Fixed Income": {
        "Government Bonds (Short-Interm.)": 0.20,
        "Investment-Grade Corporate Bonds": 0.25,
        "Inflation-Linked Bonds": 0.10,
    },
    "Real Assets": {
        "Real Estate (Income-focused REITs)": 0.03,
        "Infrastructure (Stable Utilities)": 0.02,
    },
    "Alternatives": {
        "(Generally unsuitable)": 0.00  # Explicitly 0% for clarity
    },
    "Cash & Equiv.": { # Renamed from "Cash & Equiv." for consistency
        "Treasury Bills": 0.10,
        "Money Market Funds": 0.05,
    }
}

# --- Utility Functions ---

def display_portfolio_allocation(portfolio, portfolio_name="Portfolio"):
    """
    Prints the detailed allocation of a given portfolio in a human-readable format.
    This includes sub-asset class allocations, total allocation for each major 
    asset class, and the overall total portfolio allocation.

    Args:
        portfolio (dict): A dictionary representing the portfolio structure.
                          Top-level keys are major asset classes (str).
                          Values are dictionaries of sub-asset classes (str) and 
                          their allocations (float, e.g., 0.1 for 10%).
        portfolio_name (str): The name of the portfolio for display purposes.
    """
    print(f"--- {portfolio_name} Allocation ---")
    overall_total_allocation = 0.0

    for asset_class, sub_assets in portfolio.items():
        print(f"\\n> {asset_class}:")
        asset_class_total = 0.0
        # Check if sub_assets is a dictionary and not empty
        if isinstance(sub_assets, dict) and sub_assets:
            for sub_asset_name, allocation in sub_assets.items():
                print(f"    - {sub_asset_name}: {allocation:.1%}") # Format as percentage
                asset_class_total += allocation
        elif isinstance(sub_assets, (int, float)) and sub_assets == 0.0 and asset_class == "Alternatives":
             # Special handling for "Alternatives": 0.00 in decline_portfolio
            print(f"    - (Generally unsuitable): 0.0%")
            asset_class_total = 0.0
        elif not sub_assets : # Handles empty dicts or if sub_assets is None
             print(f"  Total {asset_class}: 0.0%")
             continue


        print(f"  Total {asset_class}: {asset_class_total:.1%}")
        overall_total_allocation += asset_class_total
    
    print("\\n" + "="*40) # Increased separator length for visual distinction
    print(f"Overall Total Portfolio Allocation: {overall_total_allocation:.1%}")
    print("="*40 + "\\n")

def simulate_rebalancing(current_portfolio_allocations, target_portfolio_allocations, portfolio_name=""):
    """
    Simulates and prints the rebalancing actions (Buy/Sell/No change) required 
    to transition from a current portfolio allocation to a target allocation.
    It compares allocations for each sub-asset class and indicates the necessary
    adjustments.

    Args:
        current_portfolio_allocations (dict): The current (potentially drifted) 
                                              portfolio dictionary.
        target_portfolio_allocations (dict): The target portfolio dictionary.
        portfolio_name (str): An optional name for the rebalancing simulation scenario.
    """
    if portfolio_name:
        print(f"--- Simulating Rebalancing for: {portfolio_name} ---")
    else:
        print(f"--- Simulating Rebalancing from Current to Target ---")

    # Collect all unique major asset classes from both portfolios
    all_asset_classes = set(current_portfolio_allocations.keys()) | set(target_portfolio_allocations.keys())

    for asset_class in sorted(list(all_asset_classes)):
        print(f"\\n>> Processing Asset Class: {asset_class}")
        # Get sub-asset dictionaries; default to empty if asset class is missing
        current_sub_assets = current_portfolio_allocations.get(asset_class, {})
        target_sub_assets = target_portfolio_allocations.get(asset_class, {})

        # Collect all unique sub-asset names from both portfolios for this asset class
        all_sub_asset_names = set(current_sub_assets.keys()) | set(target_sub_assets.keys())

        if not all_sub_asset_names:
            print(f"  No sub-assets in either portfolio for {asset_class}.")
            continue

        for sub_asset_name in sorted(list(all_sub_asset_names)):
            # Get allocations; default to 0.0 if sub-asset is missing
            current_alloc = current_sub_assets.get(sub_asset_name, 0.0)
            target_alloc = target_sub_assets.get(sub_asset_name, 0.0)
            difference = target_alloc - current_alloc

            print(f"  Rebalancing for Sub-Asset Class '{sub_asset_name}':")
            print(f"    Current: {current_alloc:.1%}, Target: {target_alloc:.1%}")

            # Determine action based on the difference (tolerance for floating point)
            if abs(difference) < 1e-9: 
                print("    Action: No change")
            elif difference > 0:
                print(f"    Action: Buy {difference:.1%}")
            else: # difference < 0
                print(f"    Action: Sell {abs(difference):.1%}")
    print("\\n" + "="*50 + "\\n") # Increased separator length

def get_target_portfolio_for_stage(stage_name):
    """
    Retrieves the predefined target portfolio dictionary for a given life cycle stage name.

    Args:
        stage_name (str): The name of the life cycle stage. 
                          Expected values: "Growth", "Maturity", "Decline".
                          Case-sensitive.

    Returns:
        dict: The corresponding portfolio dictionary if stage_name is valid.
        None: If stage_name is not recognized.
    """
    if stage_name == "Growth":
        return growth_portfolio
    elif stage_name == "Maturity":
        return maturity_portfolio
    elif stage_name == "Decline":
        return decline_portfolio
    else:
        print(f"Error: Stage name '{stage_name}' not recognized. "
              "Valid names are 'Growth', 'Maturity', 'Decline'.")
        return None

def visualize_portfolio_allocation(portfolio, portfolio_name):
    """
    Generates and saves a pie chart visualizing the major asset class allocations 
    of a given portfolio. The chart is saved to a PNG file.

    Args:
        portfolio (dict): The portfolio dictionary to visualize.
        portfolio_name (str): The name for the chart title and output filename.
    """
    major_asset_classes = list(portfolio.keys())
    allocations = []
    # Calculate total allocation for each major asset class
    for asset_class in major_asset_classes:
        # Ensure sub_assets is a dictionary before summing its values
        sub_assets = portfolio.get(asset_class, {})
        if isinstance(sub_assets, dict):
            allocations.append(sum(sub_assets.values()))
        else: # Handles cases like "Alternatives": 0.00 directly
            allocations.append(0.0)


    # Filter out asset classes with zero or negligible allocation for a cleaner pie chart
    viz_labels = [label for i, label in enumerate(major_asset_classes) if allocations[i] > 1e-9]
    viz_sizes = [size for size in allocations if size > 1e-9]

    if not viz_sizes:
        print(f"No allocations greater than zero to visualize for {portfolio_name}.")
        return

    # Create and display the pie chart
    fig, ax = plt.subplots(figsize=(10, 7)) # Width, Height in inches
    ax.pie(viz_sizes, labels=viz_labels, autopct='%1.1f%%', startangle=90,
           wedgeprops={'edgecolor': 'white'}) # Add white edges for better separation
    ax.axis('equal')  # Ensures the pie chart is circular.
    plt.title(f"Major Asset Class Allocation for {portfolio_name}", pad=20) # Add padding to title
    
    # Sanitize portfolio_name to create a valid filename
    filename_safe_name = "".join(c if c.isalnum() else "_" for c in portfolio_name)
    save_filename = f"{filename_safe_name}_visualization.png"
    
    try:
        plt.savefig(save_filename) # Save the figure to a file
        print(f"Portfolio visualization saved to '{save_filename}'")
    except Exception as e:
        print(f"Error saving plot for {portfolio_name}: {e}")
    plt.close(fig) # Close the figure to free up memory


if __name__ == '__main__':
    print("--- Pension Fund Portfolio Analysis Script ---")

    # Section 1: Displaying Allocations for Standard Portfolios
    print("\\n" + "="*20 + " Section 1: Standard Portfolio Allocations " + "="*20)
    display_portfolio_allocation(growth_portfolio, "Growth Stage Target Portfolio")
    display_portfolio_allocation(maturity_portfolio, "Maturity Stage Target Portfolio")
    display_portfolio_allocation(decline_portfolio, "Decline Stage Target Portfolio")

    # Section 2: Demonstrating Rebalancing Simulation
    print("\\n" + "="*20 + " Section 2: Rebalancing Simulation " + "="*20)
    # Define a hypothetical drifted portfolio for demonstration
    # This portfolio has drifted from the original 'growth_portfolio'
    drifted_growth_portfolio = {
        "Equities": { # Target 0.70
            "Domestic Large-Cap": 0.22,        # from 0.20
            "Domestic Mid/Small-Cap": 0.08,    # from 0.10
            "International Developed Markets": 0.21, # from 0.20
            "Emerging Markets Equities": 0.19,  # from 0.20
        }, 
        "Fixed Income": { # Target 0.10
            "Inflation-Linked Bonds": 0.06,    # from 0.05
            "High-Yield Corporate Bonds": 0.03, # from 0.05
            "New Emerging Market Debt": 0.01 # New sub-asset, not in target
        }, 
        "Real Assets": { # Target 0.10
            "Real Estate (REITs/Direct)": 0.06,# from 0.05
            "Infrastructure": 0.05,           # from 0.05 (no change)
        }, 
        "Alternatives": { # Target 0.08
            # "Private Equity (Buyout/VC)" is missing, was 0.08
        }, 
        "Cash & Equiv.": { # Target 0.02
            "Money Market Funds/T-Bills": 0.04, # from 0.02
        }
    } # Total sum: 0.22+0.08+0.21+0.19 + 0.06+0.03+0.01 + 0.06+0.05 + 0.04 = 0.70 + 0.10 + 0.11 + 0.00 + 0.04 = 0.95
      # The sum is not 1.0, which is realistic for a drifted portfolio before rebalancing cash.
      # For simulation purposes, the function handles non-1.0 sums correctly by focusing on individual allocations.

    print("\\nDisplaying allocations of the example 'Drifted Growth Portfolio':")
    display_portfolio_allocation(drifted_growth_portfolio, "Drifted Growth Portfolio (Example)")
    
    print("\\nSimulating rebalancing from 'Drifted Growth Portfolio' to 'Growth Stage Target Portfolio':")
    simulate_rebalancing(drifted_growth_portfolio, growth_portfolio, 
                         portfolio_name="Drifted Growth to Target Growth")
    
    # Section 3: Demonstrating Target Portfolio Retrieval
    print("\\n" + "="*20 + " Section 3: Target Portfolio Retrieval " + "="*20)
    valid_stage_name = "Maturity"
    print(f"\\nAttempting to retrieve portfolio for stage: '{valid_stage_name}'")
    retrieved_portfolio = get_target_portfolio_for_stage(valid_stage_name)
    if retrieved_portfolio:
        display_portfolio_allocation(retrieved_portfolio, f"Retrieved {valid_stage_name} Portfolio")

    invalid_stage_name = "Pre-Growth" # Example of an invalid stage name
    print(f"\\nAttempting to retrieve portfolio for stage: '{invalid_stage_name}'")
    retrieved_invalid = get_target_portfolio_for_stage(invalid_stage_name)
    if not retrieved_invalid:
        print(f"Portfolio retrieval for '{invalid_stage_name}' correctly returned None or an error was printed.")

    # Section 4: Demonstrating Portfolio Visualization (Saving to Files)
    print("\\n" + "="*20 + " Section 4: Portfolio Visualization " + "="*20)
    print("\\nGenerating and saving pie charts for major asset class allocations...")
    visualize_portfolio_allocation(growth_portfolio, "Growth Stage Portfolio")
    visualize_portfolio_allocation(maturity_portfolio, "Maturity Stage Portfolio")
    visualize_portfolio_allocation(decline_portfolio, "Decline Stage Portfolio")
    visualize_portfolio_allocation(drifted_growth_portfolio, "Drifted Growth Portfolio (Example)")


    # Section 5: Verification of Portfolio Totals (Optional Check)
    print("\\n" + "="*20 + " Section 5: Portfolio Totals Verification " + "="*20)
    for name, portfolio_dict in {
        "Growth Target": growth_portfolio,
        "Maturity Target": maturity_portfolio,
        "Decline Target": decline_portfolio,
        "Drifted Growth (Example)": drifted_growth_portfolio
    }.items():
        total_allocation = 0
        for asset_class_name, sub_asset_dict in portfolio_dict.items():
            if isinstance(sub_asset_dict, dict):
                 total_allocation += sum(sub_asset_dict.values())
            elif isinstance(sub_asset_dict, (int,float)): # e.g. Alternatives: 0.00
                 total_allocation += sub_asset_dict

        print(f"'{name}' overall total allocation: {total_allocation:.2%}")
    
    print("\\n--- End of Script ---")
