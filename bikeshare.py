import time
import datetime
import calendar
import pandas as pd
from collections import Counter
from itertools import groupby

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington).
    while True:
        city = input('Please choose a city: Chicago, New York City or Washington: ').title()
        if city in CITY_DATA.keys():
            break
        else:
            print('Wrong city name. Please try again.')

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please specify the month (january, february, ... , june OR all): ').title()
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        if month in months:
            break
        elif month == 'All':
            break
        else:
            print('Wrong month name. Please try again.')
            
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose a day of the week (monday, tuesday, ... , sunday OR all: ').title()
        dict_days = dict(enumerate((name for name in calendar.day_name if name), start=1))
        if day in dict_days.values():
            break
        elif day == 'All':
            break
        else:
            print('Wrong day name. Please try again.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert 'Start Time' column (string) to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of the week
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Day of week'] = df['Start Time'].dt.weekday_name
        
    # if a month was chosen, filter by month
    if month != 'All':
        df = df[df['Month'] == month]
    
    # if a day was chosen, filter by day
    if day != 'All':
        df = df[df['Day of week'] == day]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    
    # print it only if the user has selected data for all months (no month filter applied), otherwise this statistic has no sense
    if month == 'All':
        # group by frequency
        freq_gr_months = groupby(Counter(df['Month'].tolist()).most_common(), lambda x:x[1])
        # choose the first group with the highest frequncy
        freq_val_months = [val for val, count in next(freq_gr_months)[1]]
        # join elements into a string
        popular_month = ', '.join([str(elem) for elem in freq_val_months])
        # count number of items in the values list
        num_of_val_months = len(freq_val_months)
        if num_of_val_months == 1:
            print('Most common month: ' + popular_month)
        else:
            print('Most common months (equal frequency of occurrence): ' + popular_month)

    # Display the most common day of week
    
    # print it only if the user has selected data for all week days (no day filter applied), otherwise this statistic has no sense
    if day == 'All':
        # group by frequency
        freq_gr_days = groupby(Counter(df['Day of week'].tolist()).most_common(), lambda x:x[1])
        # choose the first group with the highest frequncy
        freq_val_days = [val for val, count in next(freq_gr_days)[1]]
        # join elements into a string
        popular_day = ', '.join([str(elem) for elem in freq_val_days])
        # count number of items in the values list
        num_of_val_days = len(freq_val_days)
        # display most common day of the week
        # if one value for frequency of occurence
        if num_of_val_days == 1:
            print('Most common day of week: ' + popular_day)
        # if more values for frequency of occurence
        else:
            print('Most common days of week (equal frequency of occurrence): ' + popular_day)

    # Display the most common start hour
    
    # extract hour from 'Start Time' column
    start_hour = df['Start Time'].dt.hour
    # group by frequency
    freq_gr_hours = groupby(Counter(start_hour.tolist()).most_common(), lambda x:x[1])
    # choose the first group with the highest frequncy
    freq_val_hours = [val for val, count in next(freq_gr_hours)[1]]
    #join elements into a string
    popular_start_hour = ', '.join([str(elem) for elem in freq_val_hours])
    #count number of items in the values list
    num_of_val_hours = len(freq_val_hours)
    # display most common hour of the day
    # if one value for frequency of occurence
    if num_of_val_hours == 1:
        print('Most common hour of day: ' + popular_start_hour)
    # if more values for frequency of occurence
    else:
        print('Most common hours of day (equal frequency of occurrence): ' + popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    
    # group by frequency
    freq_gr_start_stations = groupby(Counter(df['Start Station'].tolist()).most_common(), lambda x:x[1])
    # choose the first group with the highest frequncy
    freq_val_start_stations = [val for val, count in next(freq_gr_start_stations)[1]]
    # join elements into a string
    popular_start_station = ', '.join([str(elem) for elem in freq_val_start_stations])
    # count number of items in the values list
    num_of_val_start_stations = len(freq_val_start_stations)
    # display most common start station
    # if one value for frequency of occurence
    if num_of_val_start_stations == 1:
        print('Most common start station: ' + popular_start_station)
    # if more values for frequency of occurence
    else:
        print('Most common start stations (equal frequency of occurrence): ' + popular_start_station)

    # Display most commonly used end station
    
    # group by frequency
    freq_gr_end_stations = groupby(Counter(df['End Station'].tolist()).most_common(), lambda x:x[1])
    # choose the first group with the highest frequncy
    freq_val_end_stations = [val for val, count in next(freq_gr_end_stations)[1]]
    # join elements into a string
    popular_end_station = ', '.join([str(elem) for elem in freq_val_end_stations])
    # count number of items in the values list
    num_of_val_end_stations = len(freq_val_end_stations)
    # display most common end station
    # if one value for frequency of occurence
    if num_of_val_end_stations == 1:
        print('Most common end station: ' + popular_end_station)
    # if more values for frequency of occurence
    else:
        print('Most common end stations (equal frequency of occurrence): ' + popular_end_station)

    # Display most frequent combination of start station and end station trip
    
    start_end_comb = df['Start Station'] + ' - ' + df['End Station']
    # group by frequency
    freq_gr_start_end_stations = groupby(Counter(start_end_comb.tolist()).most_common(), lambda x:x[1])
    # choose the first group with the highest frequncy
    freq_val_start_end_stations = [val for val, count in next(freq_gr_start_end_stations)[1]]
    # join elements into a string
    popular_start_end_station = ', '.join([str(elem) for elem in freq_val_start_end_stations])
    # count number of items in the values list
    num_of_val_start_end_stations = len(freq_val_start_end_stations)
    # display most common end station
    # if one value for frequency of occurence
    if num_of_val_start_end_stations == 1:
        print('Most common combination of start and end stations: ' + popular_start_end_station)
    # if more values for frequency of occurence
    else:
        print('Most common combinations of start and end stations (equal frequency of occurrence): ' + popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_duration_sec = df['Trip Duration'].sum()
    total_travel_time = datetime.timedelta(days=0,seconds=int(total_duration_sec))
    print('Total travel time (seconds): ' + str(total_duration_sec))
    print('Total travel time (h:m:s): ' + str(total_travel_time))
    
    # Display average travel time
    avg_tot_duration_sec = df['Trip Duration'].mean()
    # transform seconds to hours:minutes:seconds
    avg_travel_time = datetime.timedelta(days=0,seconds=int(round(avg_tot_duration_sec))) # senconds rounded to the nearest integer
    print('Average travel time (seconds): ' + str(round(avg_tot_duration_sec, 2))) # rounded to two decimals in seconds
    print('Average travel time (h:m:s): ' + str(avg_travel_time)) # in hour:minutes:seconds format
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count = df['User Type'].value_counts().to_frame()
    print('Counts of each user type:\n\n',count)

    # Display counts of gender, if coulumn "Gender" exists, as some cities do not have this column.
    if 'Gender' in df:
        gender = df['Gender'].value_counts().to_frame()
        print('\nCounts of each gender:\n\n',gender)

    # Display earliest, most recent, and most common year of birth, 
    # if 'Birth Year' column exists, as some cities do not have this column.
    if 'Birth Year' in df:
        # earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest year of birth: ', int(earliest_birth_year))
        # most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        print('Most recent year of birth', int(most_recent_birth_year))
        # most common year of birth
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth: ', int(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data after month/day filtering applied"""
    
    # Count number of entries (rows) in df  
    row_count = len(df.index)
    
    # Prompt user to choose if wants too see raw data
    display_raw_data_answer = input('\nThere are {} rows of data to show after filtering.\nWould you like to see raw data? Enter yes or no.\n'.format(row_count)).lower()
    while display_raw_data_answer != "yes" and display_raw_data_answer != "no":
        display_raw_data_answer = input('\nPlease type a valid answer (yes or no).\n').lower()
        # If answer is no, it skips to the end of display_data
        
    # If answer is yes
    if display_raw_data_answer == 'yes':
        
        # First row in the group of 5 rows
        crt_idx = 0
        
        # Show the first 5 rows then prompt user to choose if wants to see the next 5 rows,
        # as longs as there are rows to show and as long as the answer is yes
        while True:
            # Last row in the group of five
            next_idx = crt_idx + 5
            # Displays 5 rows, crt_idx is inclusive, next_idx is exclusive
            print('\n', df.iloc[crt_idx:next_idx])
            # Increments the current index by taking the value of the next index
            crt_idx = next_idx
            # Calculates the number of rows remaining to be displayed
            remaining_rows = row_count - next_idx
            # Ask the right question, depending on the number of rows remaining to be displayed
            if remaining_rows > 5:
                display_next_rows_answer = input('\nWould you like to see the next 5 lines? Enter yes or no.\n'.format(remaining_rows)).lower()
            elif 1 < remaining_rows and remaining_rows < 5:
                display_next_rows_answer = input('\nWould you like to see the last {} lines? Enter yes or no.\n'.format(remaining_rows)).lower()
            elif remaining_rows == 1:
                display_next_rows_answer = input('\nWould you like to see the last line? Enter yes or no.\n').lower()            
            # Break the loop if user doesn't want to see more rows 
            if display_next_rows_answer == 'no':
                break
            # Break the loop if there are no more rows to be displayed
            if crt_idx >= row_count:
                break
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # if there is no data returned after filtering by month of the year and/or by day of the week
        if len(df.index) == 0:
            print('\nYour filtering conditions (city: {}, month: {}, day: {}) returned no data.'.format(city, month, day))
        # if only one row returned after filtering by month of the year and/or by day of the week
        elif len(df.index) == 1:
            print('\nYour filtering conditions (city: {}, month: {}, day: {}) returned only one entry:\n'.format(city, month, day))
            print(df)
            
        # if more than two rows after filtering by month of the year and/or by day of the week
        else:
            #calculate statistics
            time_stats(df, month, day)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()
