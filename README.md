# Messenger to QKSMS

This python script will allow you to convert the json file containing your sms with one of your facebook friends into a json file compatible with the [QKSMS](https://github.com/moezbhatti/qksms) application from which you will be able to import the messages.

## Common setup

- Clone Project :
```
git clone https://github.com/Co-7/MessengerToSms.git
cd messengertosms
```

- Install Dependencies and run Server
```
npm install
npm start
```
or 
```
yarn install
yarn start
```

- Server Running in http://localhost:3000/

## How to Use

Download your Facebook account information, if you don't know how to do it click [here](https://www.facebook.com/help/212802592074644).

Select only the messages to download and download the information in **_JSON_** format.

Now you must have a facebook archive where there is a message folder. Open the folder and open the inbox folder contained in it

In this folder you have the integrity of your messenger conversations. Find the conversation you want to import in QKSMS and open the folder.

The file we're interested in must be called _**message_1.json**_. Put it on the desk.

Now you can access the server previously launched. You have 3 fields to fill in.

```
Import Json file
``` 
```
Write Your Facebook name (Name and First Name displayed on your facebook profile. Capitalize correctly)
```
```
Telephone numbers of your contact as in QKSMS
```

**_I advise you to test with a number that you don't have at the beginning to check the correct operation and thus not to corrupt the messages with your contact._**

Click on Validate and a Json file was downloaded automatically.

You just have to import this Json file in QKSMS by making a restoration with this one
