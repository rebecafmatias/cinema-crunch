import utils

# Calculate sales by category using the functions developed:

list_to_process = utils.read_csv("../data/box_office_sales.csv")
dict_processed = utils.process_data(list_to_process, "Category")
result = utils.calculate_sales_by_column(dict_processed, "Price")
