# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:03:09 2018

@author: A.J
"""

import time
import pandas as pd
import numpy as np

# loading files
CITY_DATA = {'chicago':'chicago.csv',
            'new york city':'new_york_city.csv',
            'washington':'washington.csv'}

def city_input():


    print('Hello! I see you\'re interested in exploring bike share data.')
    print('\n')

    city = input('Would you like to see data for Washington, Chicago or New York?: ')


    while True:
            if city == 'chicago':
                print('The Windy City, deep dish time!')
                print('Let\'s check out Chicago\'s bike share characteristics.')
                print('Give it a sec...after all, patience is a virtue.')
                return 'chicago'

            if city.lower() == 'new york':
                print('The Big Apple!, That\'s a great choice.')
                print('Let\'s check out New York\'s bike share characteristics.')
                print('Give it a sec...after all, patience is a virtue.')
                return 'new york city'

            if city.lower() == 'new york city':
                print('The Big Apple!, That\'s a great choice.')
                print('Let\'s check out New York\'s bike share characteristics.')
                print('Give it a sec...after all, patience is a virtue.')
                return 'new york city'

            elif city.lower() == 'washington':
                print('The Capital...so much history, another great choice!')
                print('Let\'s check out Washington\'s bike share characteristics.')
                print('Give it a sec...after all, patience is a virtue.')
                return 'washington'

            else:
                print('I\'ve always wanted to visit, but I apologize, I don\'t have data for that city.')
                city= input('please choose between Washington, Chicago or New York City.')


    return city

def get_time():

    period = input('\n Would you like bike share characteristics broken down by month including day of the month, day of the week, or no filter at all? \n PLEASE ENTER MONTH, DAY, or NO:')


    while True:

        if period.lower() == 'month':
            while True:
                day_month = input('\n Do you want the bike share data broken down by day of the month as well?:').lower()
                if day_month == 'no':
                    print('\n Let\'s check out the monthly data,\n, give it a sec...')
                    return 'month'

                if day_month.lower() == 'yes':
                    print ('\n Let\'s check out the monthly data broken down by day of the month, within a month \n')
                    print('give it a sec...')
                    return 'day_of_month'

        if period.lower() == 'day':
            print('\n Bike share data is being broken down by day of the week \n')
            print('give it a sec...')
            return 'day_of_week'

        if period.lower() == 'no':
            print('\n Your selected bike share data has no filter applied')
            return "none"

        period = input('\n Would you like bike share characteristics broken down by month, day of the month, day of the week, or no filter at all? Please enter month, day, or no:\n')

def month_info(mth):
    if mth == 'month':
        month = input('\n Which month would you like to see data for: January, February, March, April, May, or June? \n')
        while month.lower() not in ['january',  'february',  'march',  'april',  'may', 'june']:
            month = input('\n I apologize, but I only have data for: January, February, March, April, May, and June? \n please pick any one of those months.')
        return month.lower()
    else:
        return 'none'

def month_day_info(df, day_mth):

    month_day = []

    if day_mth == "day_of_month":
        month = month_info("month")
        month_day.append(month)
        maximum_day_month = max_day_month(df, month)

        while (True):
            print('\n PLEASE NOTE SUNDAY = 1 AND SATURDAY = 7')
            ask = ' \n Which day of the month? \n Please type your response as an integer between 1 and 7:'
            ask  = ask + str(maximum_day_month)
            day_mth = input(ask)

            try:
                day_mth = int(day_mth)
                if 1 <= day_mth <= maximum_day_month:
                    month_day.append(day_mth)
                    return month_day
            except ValueError:
                print("Sorry,but that\'s not a numeric value")
    else:
        return 'none'

def day_info(d):

    if d == 'day_of_week':
        day = input('\n Which day do you want data broken down for?\n Please type- M, Tu, W, Th, F, Sa, Su: \n')
        while day.lower() not in ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']:
            day = input('\n I apologize, please select a choice from either,\n M, Tu, W, Th, F, Sa, Su:\n')
        return day.lower()

    else:
        return 'none'

def load_data(city):

    print('\n Working on getting the selected bike data \n')
    print('It shouldn\'t be too long \n')

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day
    return df

def time_filters(df, time, month, week_day, md):


    print('Working on getting your selected bike share characteristics. \n')
    print('It should\'t be too long \n')

    if time == 'month':
        months = ['january', 'february', 'march',  'april',  'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if time == 'day_of_week':
        days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]

    if time == "day_of_month":
        months = ['january',  'february',  'march',  'april',  'may', 'june']
        month = md[0]
        month = months.index(month) + 1
        df = df[df['month']==month]
        day = md[1]
        df = df[df['day_of_month'] == day]

    return df

def max_day_month(df, month):
   #will return the max day of the month '''

    months = {'january': 1, 'february': 2, 'march': 3, 'april':4, 'may': 5, 'june':6}
    df = df[df["month"] == months[month]]
    max_day = max(df["day_of_month"])
    return max_day

def month_frequency(df):
    # pop month

    print('\n Question #1a:')
    print('The most popular month for bike users.')
    m = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[m - 1].capitalize()
    return popular_month

def day_frequency(df):

    print('\n Question #1b:')
    print('The most popular day of the week for bike users is.')
    return df['day_of_week'].value_counts().reset_index()['index'][0]

def hour_frequency(df):

    print('\n Question #1c')
    print('The most popular user hour for riding is?')
    df['hour'] = df['Start Time'].dt.hour
    return df.hour.mode()[0]

def stations_frequency(df):

    print('\n Question # 2a')
    print('The most common start station is.')
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print (start_station)

    print('\n Question # 2b')
    print('The most common end station is')
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)

    return start_station, end_station

def common_trip(df):

    print('\n Question #2c')
    print('\n The most commonly traveled route combination by riders is')
    common = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)

    return common

def ride_duration(df):

    print('\n Question #3a & #3b')
    print('The total days of use for riders, and the average trip duration per user.')

    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']

    total_ride_time = np.sum(df['Travel Time'])
    total_days = str(total_ride_time).split()[0]

    print ('\n Riders amounted', total_days, ' days of total use. \n')

    mean_ride_time = np.mean(df['Travel Time'])
    mean_time = str(mean_ride_time).split()[0]

    print('Riders on average use bike services about', mean_time, 'days. \n')

    return total_ride_time, mean_time

def bike_users(df):

    print('\n Question #4a')
    print('\n The breakdown of user type per city is as follows: \n')
    return df['User Type'].value_counts()

def gender_data(df):

    try:
        print('\n Question #4b')
        print('\n  The gender demographics for riders in this city are: \n')
        return df['Gender'].value_counts()

    except:
        print('Please note that Washington does not have Gender specific info.')
        print('There is no gender data in the source.')

def birth_years(df):

    try:
        print('\n Question #4c')
        print('\n Birthday characteristics for users in this city are as follows: \n')
        earliest = np.min(df['Birth Year'])
        print ('\nThe earliest year of birth and therefore the oldest rider is', str(earliest), '\n')
        latest = np.max(df['Birth Year'])
        print ('The latest year of birth and therefore the youngest rider is', str(latest), '\n')
        most_common_bday= df['Birth Year'].mode()[0]
        print ('The most frequent year of birth year of riders is', str(most_common_bday), '\n')
        return earliest, latest, most_common_bday

    except:
        print('No available birth date data for this period.')

def process(f, df):
    '''Calculates the time it takes to commpute a statistic
    '''
    start_time = time.time()
    statToCompute = f(df)
    print(statToCompute)
    print("This stat took %s seconds." % (time.time() - start_time),'to retrieve')

def raw_data(df):

    row_index = 0

    see_data = input('\n Would you like to see five rows of the data used to compute the stats? Please write yes or no:\n')

    while True:
        if see_data.lower() == 'no':
            return
        if see_data.lower() == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5

        see_data = input('\n Would you like to see five more rows of the data used to compute the stats?\n  Please write yes or no: \n')

def main():


     #calling all the functions step by step
    city = city_input()
    df = load_data(city)
    period = get_time()
    month = month_info(period)
    day = day_info(period)
    month_day = month_day_info(df, period)

    df = time_filters(df, period, month, day, month_day)
    raw_data(df)


    stats_list = [month_frequency,
     day_frequency, hour_frequency,
     ride_duration, common_trip,
     stations_frequency, bike_users, birth_years, gender_data]

    for stat in stats_list:
        process(stat, df)


    restart = input("\n * Would you like to do it again and perform another analysis? Type \'yes\' or \'no\'.\n")
    if restart.lower() == 'yes' or restart.lower() == 'y':
        main()

    if restart.lower() == 'no':
        print('Adios Amigo, Goodbye Friend \n Thanks for stopping by.')

    exit()

main()
