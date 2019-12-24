import time
import pandas as pd
import numpy as np

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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    while True:
      city = input("\n¿what city do you want to see? new york city, chicago or Washington?: \n".title())
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Error. Try again please.")
        continue
      else:
        break
    

    while True:
      month = input("\n¿What month do you want to view? January, February, March, April, May, June or indicate 'all' for everything.\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Error. Try again please.")
        continue
      else:
        break
    

    while True:
      day = input("\nWhat day do you want to see?: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or indicate 'all' for everything.\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Error. Try again please.")
        continue
      else:
        break

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
    # convert the Start Time column to datetime
    # extract month and day of week from Start Time to create new columns
    
    df = pd.read_csv(CITY_DATA[city])    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        
       # use the index of the months list to get the corresponding int
       # filter by month to create the new dataframe
       # filter by day of week if applicable 
    
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1       
        df = df[df['month'] == month]

        
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour

    popular_month = df['month'].mode()[0]
    print('Most Common Month is: ', popular_month)
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day is: ', popular_day)
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour is: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station is: ', Start_Station)
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station is: ', End_Station)
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip is: ', Start_Station, " and ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # TO DO: display mean travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time is: ', Total_Travel_Time/86400, " Days.")
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time is: ', Mean_Travel_Time/60, " Minutes.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

    user_types = df['User Type'].value_counts()    
    print('User Types:\n', user_types)

    

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data for this month.") 

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year is: ', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
