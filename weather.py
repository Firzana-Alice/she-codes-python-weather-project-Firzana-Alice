import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celsius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    change_format = datetime.fromisoformat (iso_string)
    hrf = change_format.strftime("%A %d %B %Y")
    return hrf

def convert_f_to_c(temp_in_fahrenheit):
    # if type temp_in_fahrenheit == str:
    #     int (temp_in_fahrenheit)
    temp_in_celsius = (((float(temp_in_fahrenheit)-32)*5)/9)
    temp_rounded = round(temp_in_celsius,1)
    # else:
    #     temp_in_celsius = ((((temp_in_fahrenheit)-32)*5)/9)
    #     temp_rounded = round(temp_in_celsius,1)
    return temp_rounded 

"""Converts an temperature from farenheit to celsius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celsius, rounded to 1dp.
    """

def calculate_mean(weather_data):
    sum = 0
    for temp in weather_data:
        sum += float (temp)
    mean = sum/len(weather_data)
    return mean
    
"""mean = statistics.mean(float(weather_data/len(weather_data)))
#     return mean

#     total = 0
#     i = 0
#     if i < len(weather_data):

# for t in p:
#         total = total + p[i]
#         i += 1
#     return i

# mean = i / len(p)
# return mean """
  
"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    


def load_data_from_csv(csv_file):

    list = []
    with open (csv_file,encoding = "UTF-8") as csv_open:
        reader = csv.reader(csv_open)
        next(reader)
        for line in reader:
            if not (line):
                list.append([line[0],int(line[1]),int(line [2])])
    return list

"""Reads a csv file and stores the data in a list.

    #Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # MY 1ST APPROACH:
   # val_i = min_val_i = 0
   # if weather_data:
#        min_val = 
 #   float(min(weather_data))
   #     for i in range(len(weather_data)):
   #         if
   #     float(weather_data[i]==min_val):
    #    min_val_i=
    #    float(weather_data[i])
    #    val_i = i
    #return(float(min_val_i),(val_i)
    #else:
    #    return()

    #2nd Approach

def find_min(weather_data):

    if len(weather_data) == 0:
        return()

    min_index = 0
    minimum = float(weather_data[0])

    enumerated_wd = enumerate(weather_data)

    for data in enumerated_wd:
        index, temp = data
        temp = float(temp)

        if temp <= minimum:
            minimum = temp
            min_index = index 

    return (minimum, min_index)

def find_max(weather_data):

    if len(weather_data) > 0:

        max_value= float(max(weather_data))
        print(max_value)
        max_index = 0

    for item in range(len(weather_data)):
            value = float(weather_data[item])
            if max_value == value:
                max_index = item
                return max_value, max_index

    else: return ()   

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

#     5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

    Overview_day = len(weather_data)
    list_min = []
    list_max = []

    for item in weather_data:
        list_min.append(convert_f_to_c(item[1]))
        list_max.append(convert_f_to_c(item[2]))

    lowest_temp = find_min(list_min) 
    format_lowest_temp = format_temperature(lowest_temp[0])
    lowest_temp_day = convert_date(weather_data[lowest_temp[1]][0]) 

    highest_temp = find_max(list_max)
    format_highest_temp = format_temperature(highest_temp[0])
    highest_temp_day = convert_date(weather_data[highest_temp[1]][0]) 

    avg_low = calculate_mean(list_min)
    format_avg_low = format_temperature(round(avg_low,1))

    avg_high = calculate_mean(list_max)
    format_avg_high = format_temperature(round(avg_high,1))

    summary = (f"{Overview_day} Day Overview\n  The lowest temperature will be {format_lowest_temp}, and will occur on {lowest_temp_day}.\n  The highest temperature will be {format_highest_temp}, and will occur on {highest_temp_day}.\n  The average low this week is {format_avg_low}.\n  The average high this week is {format_avg_high}.\n"  )     

    return summary 

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    data_to_return = ""
    for daily_weather_list in weather_data:

        date_string = daily_weather_list[0]
        converted_date_string = convert_date(date_string)
        min_temp_f = daily_weather_list[1] 
        min_temp_c = convert_f_to_c(min_temp_f) 
        max_temp_f = daily_weather_list[2] 
        max_temp_c = convert_f_to_c(max_temp_f) 
        daily_summary = f"---- {converted_date_string} ----\n  Minimum Temperature: {min_temp_c}°C\n  Maximum Temperature: {max_temp_c}°C\n\n"
        data_to_return = data_to_return + daily_summary
    
    return data_to_return
