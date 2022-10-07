## User Story 

As a necrophobic person, I want to see no images of human remains in the image recommendations when you Google a topic or in the first 26 rows of images when you scroll down Google images, so I can predict where to stop looking. 

As a user, I do not need offline capabilities, but I wish that the result will show up within 10 seconds.

## In Scope

## Out of Scope 

## System Diagram 
![System Diagram](System%20Diagram.png)
A Python program will forward the query to Google Search, Google Search will return images queried. The system will then
call the AI and send the images from Google Search to be classified by the AI. The AI returns the labelled images to the system. The system will then send all images the AI classified as without human remains to the user.

## Plan 

### Take User Input Module 

“What do you want to search?” 

### Forward Query to Google Search Module 

TBD

### AI Module 

TBD