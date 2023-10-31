# DataFrameTor

This project create different test files for graph analysis.

Project structure

Directories:
* data: Data seeds
* emails: Generate emails dataset (column as file)
* kaggle_users: Generate users dataset (column as file)
* subset_tor_nodes: Generate nodes dataset (column as file)

Python Files:
* bitinfocharts_no_bad_rows.py: Delete bad rows (curated intermediate file for BTC)
* generate_list_gaus_btc.py: Operations library
* main.py: Generate output file with all fields (dataframe_example)
* main2.py: Only test. Remove in cleaned release
* test_bitinfocharts.py: Intermediate file (transform column from original format to xxx.yyy)
* test_btc2.py: Get balance from btc account (out_btc)
* create_list_to_dataset.py: Operations library
* test_btc.py: Get balance from btc account (tomate_out)      
* trash_functions.py: Only test. Remove in cleaned release

Result files:
* dataframe_example.xlsx: Complete set
* dataframe_example.csv  

* vamos.csv: BTC with all related fields
* vamos.xlsx

* tomate_out.csv: Get balance from BTC accounts
* tomate_out.xlsx     


 



