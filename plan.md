## Problem description

As a commuter, it is the most convenient to find places next by the light rail so I can quickly drop off and quickly do something rather than taking a bus in and out which can cost an extra 20 minutes. However, through Google Maps, you can only look at one station at once, while the light rail provides multiple stations. As a result, using preexisting solutions are difficult, You will have to research location to location manually. Hence, my tool aims to automate that process so you can search for results for all light rail stations near you as an alternative search engine. This is for people who depend on public transit. Public transit is great at Seattle, but requires more specialized tools for planning.

## APIs

Our main API will be the Google Maps. It is free for the first 10,000 events per month. In particular, we can use its [places API](https://developers.google.com/maps/documentation/places/web-service) to locate places based on location based on user input. For each resulting place, we can use place details to get general information about the place for ranking. We can also use the [Routes API](https://developers.google.com/maps/documentation/routes?hl=en) to note what places that take too much time to walk.

Building on Google Maps API, we can also get more information about a place through Yelp. Through [Business Match](https://docs.developer.yelp.com/reference/v3_business_match), we can find the business ID which we can use to find even more [details](https://docs.developer.yelp.com/reference/v3_business_info) for a business like if it's closed and its rating. I intend to connect places found in Google Maps to Yelp so we can build a better perspective of the location.

By collecting as much information as possible, we can make a rough algorithm to determine the place for the best needs of the user.
 
## Output

For functionality, first, we ask the user what light rail stations they are willing to come out of. I was thinking making a visual diagram which is similar to the official sound transit map. This is so that people who are less familiar to the light rail are not lost and for people who are familiar to clearly understand which stations they should pick. Then we ask for categories and additional advance details. Google provides a lot of vague information like "good for children", "dine in", and "allow for dogs", so there is a lot potential things we can collect. I was thinking a simple step by step process, first asking what category, and then diverge choices from there. Then we ask Google Maps API, what are places that matches those search terms in the area of every selected light rail stations? After we get that list, we could also ask Yelp, what are your thoughts on that location? At the end, we could make a heuristic algorithm to organize, rank, and display results and display them. I plan to use a table, giving basic details of each location, ratings, address, which light rail station, etc. This is similar to HW 4 pages with the Wikipedia articles. This way, it's easier to compare between different options and utilize them in the end. 

## Plan

### Week 1

1. Creating accounts for Google API

2. Write basic python fetcher of Google Maps AI

3. Collect both locations and location details

4. Create basic algorithm to rank locations

### Week 2

1. Create basic UI in HTML to make the request to flask

2. Output the results in HTML in basics

### Week 3

1. Cotinuing working on output the results in HTML 

2. Do UI map for light rail stations

3. Do CSS to make the website look prettier

### Week 4/If Time permits

1. Add Yelp API for results


