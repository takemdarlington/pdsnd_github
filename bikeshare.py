import time
import pandas as pd
import numpy as np

# Data files we will be working with
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to explore? chicago, new york city, or washington? ')
        city.lower()
        if (city in['chicago', 'new york city', 'washington']):
            break
        else:
            print('Ooops! Not a valid city, please enter either .chicago, new york city, or washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to explore for? january, february, march, april, may, june or all?: ')
        month.lower()
        if (month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
            break
        else: 
            print('Ooops! Please Enter a valid month, january, february, march, april, may, june or all.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of the week you would like to explore: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? ')
        day.lower()
        if (day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']):
            break
        else: print('Ooops!, that is not a valid day, please enter either monday, tuesday, wednesday, thursday, friday, saturday, sunday or all')

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
    
    # load data file into a dataframe according to the inputted city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day'] == day.title()]
#         days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#         day = days.index(day)
#         # filter by day of week to create the new dataframe
#         df = df.loc[df['day']== day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('The most common month for bike travel is: {}'.format(most_common_month))
    print('\n\n')

    # TO DO: display the most common day of week
    most_common_day = df['day'].value_counts().idxmax()
    print('The most common day for bike travel is: {}'.format(most_common_day))
    print('\n\n')

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour for bike travel is: {}'.format(most_common_hour))
    print('\n\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(most_common_start_station))
    print('\n\n')


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(most_common_end_station))
    print('\n\n')

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_comb'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_combination = df['frequent_comb'].mode().loc[0]
    print('The most frequent trip taken is from: {}'.format(most_frequent_combination))
    print('\n\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: {} seconds '.format(df['Trip Duration'].sum()))
    print('\n\n')


    # TO DO: display mean travel time
    print('Average Trip Duration: {} seconds'.format(df['Trip Duration'].mean()))
    print('\n\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Here are the counts user types: {}'.format(user_types))
    print('\n\n')
    
    # TO DO: Display counts of gender
    if ('Gender' in df):# Check is gender exist in the dataframe first
        user_gender_counts = df['Gender'].value_counts()
        print('Here are the user counts by gender: {}'.format(user_gender_counts))
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df):
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The earliest birth year is {:.0f}, the most recent birth year is {:.0f}, and the most common birth year is {:.0f}.'.format(earliest_birth_year, most_recent_birth_year, most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`
    
    """

    data = 0
#     print(df[0:5])

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[data : data+5])
            data += 5

        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
