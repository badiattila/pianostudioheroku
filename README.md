# Piano Studio Kft. - Introduction of a Hungarian piano company  
This web page was made for Code Institute's Stream One Project: User-Centric Frontend Development and was updated for Code Institute's Interactive Frontend Development assesment.
Now it is once again reborn using Material Design by Google, python, flask, mongodb, a better contact form mail integration with a secure smtp server and should run under heroku if all goes right :) 

This web page is ment to introduce Piano Studio Kft, a Hungarian family owned and operated piano business.
It focuses on the owners (with a galery using instagram integration), services, pianos for sale (with an option to create new adds) and provides a contact form to make it easy for customers to ask their questions. 


## Demo
The latest heroku active demo can be found [here](https://piano-studio.herokuapp.com/)

The live outdated version of the webpage can be found [here](http://www.pianostudio.hu)
A live demo of the previous version using bootstrap can be found [here](https://badiattila.github.io/pianostudio/).


## UX
My goal in the design was to have an easy to use yet fresh appearence. 
The red color scheme was chosen to reflect a conservative but elegant image. 

For potential customers I want to give as much guidance on services and products as possible using pictures to illustrate.


## Technologies
1. HTML
2. CSS
3. Python
4. JavaScript
5. Flask
6. Material Design
7. Material.io
8. Instagram API


## Features
This site uses the native features of Material Design, Flask pymongo, Flask mail and integrates with Instagram API. 


### Features Left to Implement
The contact form can be better implemented, will need visual and functionality improvements. 
I might also include a dinamic section for piano renters to track their profile (piano rented and account status)
The Instagram API integration will need to be updated to use short term keys.

## Testing
The renter user story achieved the intended outcome of introducing the service and the gallery is providing customers with a showcase of available pianos to rent.
The buyer user story is satisfied by having the section Pianos to Sell.
The seller user story is satisfied by having the section Pianos to Buy.
The customer for services user story has the services section with piano tuning and restoration.
The contact form is sending out emails to attila.badi@gmail.com.
The Instagram API makes the gallery dinamic by showing all uploaded media.

If you try to submit the contact form with an invalid email address, there will be an error noting the invalid email address. 
Furthermore, the 'required' attribute is added to the First Name, Last Name and Email fields, so if those fields are not filled in, the form will not submit. If all field are valid, the form will send a mail to attila.badi@gmail.com. 

Social media links are tested and work as intended to both facebook and instagram.

This site was tested across multiple browsers (Chrome, Internet Explorer, FireFox) and on mobile devices (iPhone 6 and Huawei P10) to ensure compatibility and responsiveness. 

## Deployment
This site is hosted using Heroku, deployed directly from the master branch and backup in github. 

To run locally, you will need the SMTPPW defined as environment variable to the correct password to the smtp server and all components as defined in the requirement file.

## Credits

### Content
All content in this site were written by me. 

### Media
Background photos were taken from [Pexels](https://www.pexels.com/), a stock image library.
Pictures used (pianos owned and for sale sections and introduction) are taken by the owners and workers of Piano Studio Kft. 

### Acknowledgements
Code Institute's course material is heavily used as both inspiration and code examples.
Color schemes are inspired by an article found https://www.websitebuilderexpert.com/designing-websites/how-to-choose-color-for-your-website/
Instagram integration uses samlpe code from code institute and Instagrams own introductory how-to manuals.
File upload inspired by articles like https://pythonbasics.org/flask-upload-file/
StackOverflow is used to figure out solutions in all cases I got stuck with anything.
CSS Tutorial was at help whenever I needed a nicer interpretation https://www.w3schools.com/css/

**This is for educational use and possibly will be the successor of the currently hosted www.pianostudio.hu in the future.** 
