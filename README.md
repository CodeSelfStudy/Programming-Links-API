# Programming Links API

A group project to display programming links on the site.

## TODO

* Implement Github authentication
* Allow users to comment on links
* Allow users to add links

## Examples

Example of posting a link:

    curl -d '[{"title": "Learn Python the Hard Way", "url": "http://learnpythonthehardway.org/book/", "description": "A book that teaches you how to program computuers with Python"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/links
