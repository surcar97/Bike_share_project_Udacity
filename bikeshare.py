import pandas as pd
import numpy as np
import time


CITY_DATA = { 'CH': 'chicago.csv',
              'NY': 'new_york_city.csv',
              'DC': 'washington.csv' }
# input data section
def filtered_inputs():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('choose the city u need (chicago) as [CH] ,(new york city) as [NY] or (washington) as [DC]: ')
            
            city = city.upper()
                
            if city in ['CH','NY','DC']:
                break
            else :
                print("unvalid input it should be one of the choices above ")
        except:
            print('unvalid')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('what month do u need (all) or choose one of this list [january ,february ,..., june] : ')

            month = month.lower()
            if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print('unvalid input can u choose one of the choices above')
        except:
            print('unvalid')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input(' which day of week (all) or specific one (saturday , sunday ,..., friday) : ')

            day = day.lower()
            
            if day in ['all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
                break
            else:

                print('unvalid input can u choose a correct day from saturday till friday')

        except:
            print('unvalid')

    print('-'*40)
    return city , month , day
    


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

    # extract month , day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day of week'] = df['Start Time'].dt.weekday_name


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
        df = df[df['day of week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    print('the most common day of the week is : {} ' .format(df['day of week'].mode()[0]))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]

    print(' The most common month is : {} and the most common hour is : {} '.format(most_common_month,most_common_hour ))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]

    # make a combination between the two stations columns Start and End
    df['Full Trip']=' from '+ df['Start Station'] +' to '+ df['End Station']

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df['Full Trip'].mode()[0]

    print('Most common start station is : {} \n Most common end station is : {} \n Most common full trip is : {}'.format(most_common_used_start_station,most_common_used_end_station,most_common_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def readable_timedelta(days):
    #this function take one argument float as days and return it in weeks and what left in days but as ints
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time1 = df['Trip Duration'].sum()

    # to do: display total time in hours
    total_travel_time2 = total_travel_time1 / 86400

    # to do: display total time in weeks & days
    time_in_weeks_days = readable_timedelta(total_travel_time2)

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])

    print('total travel time is: {} in seconds but {} \n Mean is: {} '.format(total_travel_time1,time_in_weeks_days,mean_travel_time))
    print("\nThis operation took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    if city != 'DC':
        # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print('the gender stats \n',user_gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        earliest_year = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        print('For Birth year stats \n earliest {} , most recent {} , and most common year of birth {} '.format(earliest_year,most_recent,most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_rows(df, start_row, end_row):
    """this func print data from the df from start to end which diffrence 5 mean that i will get 5 diferent variables """   
    
    for i in range(start_row,end_row):
        print(df.iloc[i])     
        print('-'*40)

      

def main():
    while True:
        
        city, month, day = filtered_inputs()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        start = 0
        end = 5
        first_time = True
        while True:
            try:
                start_time = time.time()
                input_1 = ''
                
                if first_time:
                    input_1 = input('Do u want to see 5 rows of the data say [yes] or [no] if not :  ')
                    first_time = False
                else:
                    input_1 = input('if u want to continue seeing another 5 rows of the data say [yes] or [no] if not :  ')
                                               
                if input_1.lower() == 'yes':
                    print_rows(df,start,end)
                    start+=5
                    end+=5
                elif input_1.lower() == 'no' :
                    break
                
                else:
                    print('invalid input ')
                    
                print("\nThis took %s seconds." % (time.time() - start_time))
    
            except e:
               print(' somthing happend ', e)
            
        
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    