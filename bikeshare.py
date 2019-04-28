import time
import pandas as pd
import numpy as np

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
        city = input('Enter the name of city: ')
        city = city.lower()
        if city in CITY_DATA:
            break
        print('You entered an invalid city name')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the name of month: ')
        month = month.lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        print('You entered an invalid month name')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of week: ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        print('You entered an invalid weekday name')


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    month_name = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10: 'October', 11:'November', 12:'December'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: {}".format(month_name[df['month'].mode()[0]]))

    # TO DO: display the most common day of week
    print("Most common day of week: {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("Most common start hour: {}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most commonly used end station: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    start_end = df['Start Station'] + ' AND ' + df['End Station']
    print("Most frequent combination of start station and end station is {}".format(start_end.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Average travel time: {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User type breakdown: ')
    print(df['User Type'].value_counts().to_frame())
    print('\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('User gender breakdown: ')
        print(df['Gender'].value_counts().to_frame())
    else:
        print('Gender data not available for this city')
    print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('Most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('Birth year data not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw(df):
    last_row_index = df.shape[0]
    counter = 0
    while True:
        answer = input('Would you like to see five more lines of raw data?: ')
        if answer.lower() == 'yes':
            if counter >= len(df):
                print('You have seen everything now. Existing....')
                break
            print(df.iloc[counter:counter+5,:])
            counter += 5
        elif answer.lower() == 'no':
            print('OK, have it your way')
            break
        else:
            print('Invalid request. Say yes or no')
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
