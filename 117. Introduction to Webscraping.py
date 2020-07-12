"""
Web scraping is a general term for techniques incolcing automating the gathering of
data from websites

In this section we will learn how to use python to conduct web scraping tasks,
such as downloading images or information off a website.

In order to web scrape with [python we need ot understand the basic concepts of
how a website works

When a browser loads a website, the user gets to see what is known as the front
end of website

HTML, CSS, Java script - Frontend

Main things we need to understand

1. Rules of web scraping
2. Limitaitons of web scraping
3. Basic HTML and CSS

1. Rules of webscraping

Always try to get permission before scraping

If you make too many scraping attempts or requests your IP address could get blocked

Some sites automatically block scraping software


2.Limitations  of webscraping

In general every website is unique, which means every web scraping script is unique

A slight change or update to a website may completely break your web scraping script

-----------------------
When viewing a website, the browser doesnt show you all the source code behind the website
instead it shows you the HTML and some CSS and JS that the webiste sends to your browser

HTML is used to create  the basic structure and content of a webpage.

CSS is used for the design and style of a webpage, where elements are placed and how it looks

Java script is used to define the interactive elements of webpage

For effective webscarping we only  need to have a basic understanding of HTML and CSS
elements programmaticallu and then extract information from the website.

Lets explore HTML and CSS in more detail
_____________

HTML - Hypertext markup language and present on every webiste on the internet

You can right click on a webiste and select "View Page source " to get an example

Lets see a small example of HTML code

<!DOCTYPE html>

<html>
    <head>
        <title> Title on Browser Tab</title>
    <head>
    <body>
        <h1>Website Header </h1>
        <p>Some Paragraph</p>
    <body>
<html>

CSS stands for Cascading style sheets
CSS gives style  to a website such as changign colors and fonts
CSS uses tags to define what html elements will be styled

HTML file + CSS
<!DOCTYPE html>

<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <title> Some Title</title>
    <head>
    <body>
        <p>id ='para2' Some Text</p>
    <body>
<html>

example of style.css file

#para2{
    color: red;
}

<!DOCTYPE html>

<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <title> Some Title</title>
    <head>
    <body>
        <p>class='cool' Some Text</p>
    <body>
<html>

.cool{
    color: red;
    font-familuy: verdana;
    }


"""




