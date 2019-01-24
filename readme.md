# Riot Games API Challenge 2018 Submission - custom.lol

By Canisback and Saig

There are plenty of website about data on LoL. They all present the data in different shapes, but no one can truly please every needs of every summoner. Given this assessment, one idea emerged : if we can't find a template that pleases every user, why not let every user create their own specific template?


About this repo : 

This is the back end of the project.
It relies on the Python libraries [Pantheon](https://github.com/Canisback/pantheon) and [Static-data](https://github.com/Canisback/static-data). You will need to install them to make this project work.

You'll also need to set up an API key in the index.py file.

Link to the client side : https://github.com/Canisback/RGAPI-challenge-2018-front


The main idea of the project is to create yet another LoL stats website (again...) but with a custom interface where the user can chose what data to display and where.
The system relies on the concept of schema, template and data.

The schema is a premade data structure representing all the data available and how to compute it if needed.
The template is based on the schema and saves what information should be displayed and where, and only appears client side.
The data is generated following the schema from the data from the RG API, and then sent to the client side.


A demo can be seen here : 

http://canisback.com:4200/summoner/euw1/ODS%20Saig

You can begin to create your template by clicking on the "New block" button and selecting a category of data to begin with. You can move and resize the block, pick specific data and configure options in the template viewer on the right.

It is also possible the use a premade template, click on the "lock" button top left to see the result : 

http://canisback.com:4200/summoner/euw1/ODS%20Saig/default

Well... it's more the begining of a premade template, but still.

Due to a lack of time, the result is not very good looking, suffers from critical bugs and is not really user friendly, but this is a project we will contiue to work on. The concept of letting the user choose the data he wants the way he wants is something that is missing a lot in today stats websites. No static template, even carefully designed, can't please every player as their needs are really different from a player to another.

The first step in our future work will be to finish the interface, get tid of bugs and offer the most user-friendly experience possible. Then we will add more data, on global statistics for champions, items and many thing else, create component specific to LoL (representation of the map...), take a look at esports data. 

This project is the realization of months, even years of ideas and knowledge on LoL and the API, and this Challenge has been a really good opportunity to finally create something.

We would like to thank the Riot API Team for their work and the community for its much appreciated support.
