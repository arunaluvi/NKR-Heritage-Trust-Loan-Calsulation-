Data Definition: data_corrected creates a table of loan categories and interest rates, which can help users select appropriate rates based on loan criteria. This information could be displayed in the application interface or provided to users as a reference.
calculate_loan_deductions Function: This function calculates deductions and the net loan amount, breaking down each fee category:
Percentage-Based Deductions: Calculations include the first month’s interest, STAMP duty, and legal service fee, all based on the loan amount percentage.
Fixed Fees: These include property visit, extract, agreement, and transport fees.
Net Loan Amount: Subtracts all calculated fees from the original loan amount to arrive at the final disbursed amount.
Parameters:
loan_amount: The principal loan amount requested by the client.
processing_fee: Fee for normal or quick processing, determined by processing time.
interest_rate: Monthly interest rate applicable to the loan.
stamp_duty, legal_fee: Percentage fees based on loan amount.
visit_fee, extract_fee, agreement_fee, transport_fee: Fixed fees for specific services.
Example Usage: Illustrates how to calculate the deductions and net loan amount for a sample loan, allowing users to test with different values and adjust based on categories.
Display Output: loan_summary presents the final loan breakdown, showing how each deduction affects the total disbursed amount. This output can be modified to print or log each detail to ensure clarity for clients or internal records.
