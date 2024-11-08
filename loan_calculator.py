import pandas as pd

# Define loan categories and interest rates
data_corrected = {
    "Category": [
        "Loan Amount (Up to LKR 1,000,000)",
        "Loan Amount (LKR 1,000,001 - 2,000,000)",
        "Loan Amount (Above LKR 2,000,000)",
        "Term (Up to 1 Month)",
        "Term (6 Months)",
        "Term (1 Year)",
        "Collateral (Bare Land - Not Vacant)",
        "Collateral (Property with Residents)"
    ],
    "Interest Rate (%)": [
        "8% - 10%",
        "6% - 8%",
        "4% - 6%",
        "8% - 10%",
        "8% - 6%",
        "4% - 6%",
        "6% - 4%",
        "6% - 10%"
    ],
    "Notes": [
        "Higher interest rate due to smaller loan amount.",
        "Medium interest rate for mid-range loan amount.",
        "Lower interest rate for larger loans.",
        "Higher interest for short term, quick repayment.",
        "Medium rate for medium term loans.",
        "Lower rate for long term loans.",
        "Lower rate for land with development potential.",
        "Higher rate for properties with residents due to risk."
    ]
}

# Create a DataFrame for display purposes
df_corrected = pd.DataFrame(data_corrected)

def calculate_loan_deductions(loan_amount, processing_fee, interest_rate, stamp_duty=4, legal_fee=1, visit_fee=5000, extract_fee=5000, agreement_fee=5000, transport_fee=2500):
    """
    Calculate the net loan amount after all deductions.

    Parameters:
        loan_amount (float): The requested loan amount.
        processing_fee (float): The processing fee based on selected processing type.
        interest_rate (float): Monthly interest rate as a percentage.
        stamp_duty (float): Stamp duty rate as a percentage of the loan amount.
        legal_fee (float): Legal service fee rate as a percentage of the loan amount.
        visit_fee (float): Fixed fee for property visit verification.
        extract_fee (float): Fixed fee for property extract documentation.
        agreement_fee (float): Fixed fee for preparing the loan agreement.
        transport_fee (float): Transport fee, varies with distance (minimum LKR 2,500).

    Returns:
        dict: A summary of each deduction and the final net loan amount provided to the client.
    """

    # Calculate percentage-based deductions
    first_month_interest = (loan_amount * interest_rate) / 100
    stamp_duty_fee = (loan_amount * stamp_duty) / 100
    legal_service_fee = (loan_amount * legal_fee) / 100

    # Calculate total deductions
    total_deductions = (
        first_month_interest + stamp_duty_fee + legal_service_fee +
        processing_fee + visit_fee + extract_fee + agreement_fee + transport_fee
    )
    
    # Calculate net loan amount
    net_loan_amount = loan_amount - total_deductions
    
    # Prepare breakdown of deductions and net amount
    deduction_details = {
        "Loan Amount": loan_amount,
        "Processing Fee": processing_fee,
        "First Month Interest": first_month_interest,
        "STAMP Duty": stamp_duty_fee,
        "Legal Service Fee": legal_service_fee,
        "Property Visit Fee": visit_fee,
        "Extract Fee": extract_fee,
        "Agreement Fee": agreement_fee,
        "Transport Fee": transport_fee,
        "Total Deductions": total_deductions,
        "Net Loan Amount": net_loan_amount
    }
    
    return deduction_details

# Example usage:
loan_amount = 1000000  # Example loan amount
processing_fee = 10000  # Normal processing fee
interest_rate = 8  # Example interest rate based on loan category

# Calculate deductions and net loan amount
loan_summary = calculate_loan_deductions(loan_amount, processing_fee, interest_rate)

# Display the deduction summary
print("Deduction Breakdown and Net Loan Amount:")
for key, value in loan_summary.items():
    print(f"{key}: {value}")

# Optional: Show DataFrame for reference
print("\nLoan Categories and Interest Rates:")
print(df_corrected)
