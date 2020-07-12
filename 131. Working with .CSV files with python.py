"""
CSV stands for comman separated variables and is  a very common output for spread sheet programs

Example

Name, HOurs, Rate

David 20 15

Claire 40 20

*) NOte that while its possible to export excel files and Google spread sheets to .csv files ,
it only exports the information.

*)Things like formulas, images and macros can not be within a .csv file.

*)SImply put a .csv file onlu contains the raw data from the spreadsheet

*)we will work with the built in csv module for python,which will allow is to grab columns,
rows and values from .csv file as well as write to a .csv file.

*)Keep in mind, this is a very populsat space for outside libraries, which you may want to
explore
___________________________________________
Other libraries to consider

Pandas
1. Full data analysis library can work with almost any tabular data type

2. Runs visualization and analysis
3. One of my personal favourites , we teach it in various data science courses


Openpyxl

1. Designed specifically for excel files
2.Reatins a lot of excel specific functionality
3.supports excel formulas
4.python -excel.org tracks various other excel based python libraries


Google Sheets python API
1.Directs python interface for working with Google Spreadsheets.

2.Allows you to directly make changes to the spreadsheets hosted online.

3.More complex syntax , but available in many programming languages.

The common factor between all of these spreadsheet programs is that they can always
export to .csv

Lets explore python built in capabilites with csv module

"""


