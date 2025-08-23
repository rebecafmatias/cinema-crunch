import csv

# Function: read_csv
# Input: Name of the CSV file
# Output: List of dictionaries with the data read


def read_csv(file_name: str) -> list:
    with open(file_name, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        return list(reader)


# Function: process_data
# Input: List of dictionaries
# Output: Processed dictionary as described


def process_data(list_name: list, column_chosen: str) -> dict:
    final_dict = {}
    for i in list_name:
        variable = i.get(column_chosen)
        if variable not in final_dict:
            final_dict[variable] = []
            final_dict[variable].append(i)
        else:
            final_dict[variable].append(i)

    return final_dict


# Function: calculate_sales_by_column
# Input: Processed dictionary
# Output: Dictionary with total sales by the column chosen


def calculate_sales_by_column(dict_name: dict, column_to_sum: str) -> dict:
    summarized_sales_dict = {}
    for i in dict_name:
        key_data = dict_name.get(i)
        for j in key_data:
            sale_value = float(j[column_to_sum])
            if i not in summarized_sales_dict:
                summarized_sales_dict[i] = sale_value
            else:
                summarized_sales_dict[i] += sale_value

    return summarized_sales_dict
