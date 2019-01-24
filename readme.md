#Riot Games API Challenge 2018 Submission - custom.lol

This is the back end of the project.
It relies on the Python libraries [Pantheon](https://github.com/Canisback/pantheon) and [Static-data](https://github.com/Canisback/static-data). You will need to install them to make this project work.

You'll also need to set up an API key in the index.py file.



The main idea of the project is to create yet another LoL stats website (again...) but with a custom interface where the user can chose what data to display and where.
The system relies on the concept of schema, template and data.

The schema is a premade data structure representing all the data available and how to compute it if needed.
The template is based on the schema and saves what information should be displayed and where, and only appears client side.
The data is generated following the schema from the data from the RG API, and then sent to the client side.