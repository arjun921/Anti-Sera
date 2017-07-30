# turbo-winner
## Setup

`pip install django`

`pip install tensorflow`

`cd backend/webservice/`

`python manage.py migrate`

#### Run Server

`python manage.py runserver 0.0.0.0:8000`

#### Run App

Refer video: https://photos.app.goo.gl/7n25X5HLQqc1ZuqU2
or follow instructions
1. Enter IP Address of machine running Django on Mobile Chrome Browser, this is a Progressive Web-App. Mobile and server should be connected to same network.
2. Click on Menu, Add to HomeScreen.
3. Open `Anti-Sera` from Home-Screen
4. Click on file, choose camera.
5. Submit
6. App opens Google Maps with list of hospitals closest to vicinity if Venomous snake with confidence for a brief amount of time.
7. App just shows Snake not venomous, The End.

## About

This project is an Intersection of two themes, use of AI/Machine Learning in healthcare.

Roughly 46,000 people die of snakebites in India every year, according to the American Society of Tropical Medicine and Hygiene, accounting for nearly half of the 100,000 annual snakebite deaths the world over.

The objective of my hack is to bring down that number as much as I can. Even if it's just a fraction, it still counts.

##### There are mainly 4 commonly found venomous snakes that cause most of the fatalities in India,

##### these are called the Big Four:

\- Indian Cobra

\- Russel’s Viper

\- Saw Scaled Viper

\- Common Krait

##### What I wanted to build is as follows:

If you manage to take a picture of the snake, my app would tell you if the snake that bit you was a poisonous one or a non-poisonous one. If it is identified as a non-poisonous one, there’s nothing required to be done.

In case it is a poisonous one, there are multiple scenarios which could be dealt with.

The app tells, which snake it is, what sort of venom it has, what are the symptoms of the snake bite, etc. Once it is confirmed that the snake that bit is indeed a venomous and fatal one, either the app could connect to an Ambulance dispatch network which would send an ambulance from the closest hospital using geo-fencing.

Or else, the user can see directions to the closest hospital that can treat this sort of snake bite.

In India, tetravalent anti-sera is used for most common venomous snake bites, hence it’s not that important to strictly identify which species snake bit the person. But in the case of a snake like Taipan, Death Adder, Brown Snake; snake specific anti-venom has to be administered. Although species identification isn’t much important in the case of Indian Snakes, the app will help the user to find the medication required for the snake bite.

One more way of fool-proofing the system would be, if hospitals have a record of Anti-sera being available or not available, the patient can directly visit a hospital where Anti-serum is available. Every ticking minute after the snake bite counts, so if the patient goes to a place where antivenin is in stock, chronic damage is preventable.

If the user decides to navigate to the closest hospital available, the app would guide the patient or if someone else is accompanying him/her the basic steps of what to do and what not do after a snake bite. It will give them hope, and help them stay calm by playing a psychologically helping, soothing voice track that would guide the mind of the patient into a calm state as a scared victim, would have fast heart rate which would just help the venom spread through the system even faster causing more damage than it normally would.

##### What I have built, is mentioned below:

I have built the system that identifies if a snake is venomous or non-venomous.

Due to lack of volume of data collected, species classification was not possible in the short duration of time available. Given better data, species classification is definitely possible. Currently, the accuracy of the system for specifically 4 Species included in venomous snakes vs non-venomous snakes available in India given the poor quality and low volume of data is 89%. This can definitely be improved as and when new data sources are available for training the model. The model can only detect the Big four, venomous snakes so any other snakes being shown apart from the ones on the Venomous or Non-venomous list will be miss-classified. To fix this, we need more data. Current system detects if the snake is venomous or non-venomous and automatically opens maps application with a list of all hospitals available in the vicinity in ascending order of distance from the user. (This feature Requires google maps installed). Currently, I don’t know how to identify which hospitals can treat snake bites and which can’t. For this again, we need data.

##### Now comes the question, how do we collect this data that we need?

We give an incentive to snake catchers and herpetologists to contribute to the system. The data will be crowd sourced. Since only herpetologists or snake will be the one allowed to join the system, we can also give them a selection menu based on the locality. Now since we’re giving the option to contribute to the system to experts of the field, there is very little or no chance for a misclassification. Herpetologists or snake catchers will be our data providers and labelers as well.  The snake breed list will be populated based on the vicinity of where the picture was taken, and as soon as the user hits submit; the user’s location is also saved to create a heatmaps for identifying which snake could possibly occur given just a location, which would help narrow down the search in case the snake bite victim was not able to take a picture for the identification.

The snake catcher or herpetologist, takes a picture, uploads it and he gets free money for the task he has been doing forever.

##### Where will I pay them the incentive from?

Funding. Seed funds up to 80% will be given out as incentives as this system cannot flourish without the data labelers; hence herpetologists and snake catchers play an important role in this project. As for the data required for listing hospitals, if a centralized ledger can’t be maintained, then the end user can be asked to select the hospital from where he got treatment. Once a significant amount of users confirm that they got treated at the same hospital, more priority will be given to show that hospital on top even though if it is not close by as there is higher chance of getting help from there based on past experience.

##### Beyond the hackathon:

I will try my best to finish and add all the features mentioned above and publish it on the App Store and Play Store; as and when time permits.

The current system sends a picture to the server and gets a prediction of the snake. One main goal is to make this offline and make it run on device completely so that in remote places with spotty or no signal range, the app still can give a basic guideline as for First-Aid after a snake bite.
