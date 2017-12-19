# **_"My Way"_ of seeing music covers**

Please note that the main notebook is called "Project Notebook", we merged all of our separate work in it in a coherent way.

### Abstract

Everybody knows the definition of a cover song (and  can cite several of them) as a new performance of a previously recorded song, by someone other than the original artist or composer.
Something that is quite unknown is how the concept of cover version started. Actually, this phenomena started in the 1950s when record companies tried to reach out to more people by a way of reproducing original songs such that those were more appealing to a particular demography. If we go back to the racial segregation period in the United States, there were black radio stations and white radio stations. Covers versions were recorded by White artists and then diffused on white radio stations, without acknowledgement or financial compensation for the original (black) artists and it was clearly a "racist tool" as said the singer-songwriter Don McLean.

Fortunately, the mentality changed and cover versions are nowadays used as a revival of old songs, sometimes with a radically different style, in a different language or with lyrics added for the case of instrumental compositions.
Even if it's becomes a very profitable business for music industry, the goal of a cover version is still to spread a part of musical history to younger generations or to other cultures around the world.


Through a spatial and time analysis of cover songs history, our goal is to explore cultural or social underlying patterns and how it is diffused in a globalized world.

### Research questions 

- Are older songs more covered than recent ones ?
- Do artists tend to cover other artists from the same country or different ones ?
- How did those tendencies evolve over time ?
- As our world became more connected over time, do songs spread further than before ?
- Is there a certain genre(s) more covered than other genres ?
- Do artists tend to cover songs from other genres than their own or not ?
- Are covers generally more popular than their original ?

We integrated a "song story" where we follow the well-known and covered song "My Way" in time and space through its different cover versions.

### Dataset

- We mainly used the [SecondHandSongs](https://labrosa.ee.columbia.edu/millionsong/secondhand) dataset and website API to gather all the covers and their infos, such as the artists nationalities, songs languages and years, as the MSD is sparse and unreliable for those.
- We still used the [Million Songs](https://labrosa.ee.columbia.edu/millionsong/) dataset to fetch additional information such as tempo or "song hotness" to mesure popularity.
- [Last.fm](https://labrosa.ee.columbia.edu/millionsong/lastfm) to get the tags and determine the genre.
We used [musicgenreslist.com](http://www.musicgenreslist.com/) to establish an arborescence of genres and match the lastfm tags with them.


### A list of internal milestones

Until milestone 2 :

- Get acquainted with the data
- Data collection from diverse datasets and web scraping to complete this data
- Data cleaning
- Merge the data from the different sources

For milestone 3 :

- Analysis of the data in order to answer our research questions
- Selection of most interesting topics according to our first results
- Maybe a deeper analysis of those questions
- Create a data visualisation inspired by [this article](https://pudding.cool/2017/05/song-repetition/index.html).

### Members contribution

Anaïs: data cleaning and constitution of the main dataframe, coordinating and writing most of the Project Notebook, the whole song story part with the interactive map

Lou: establishing a genre hierarchy from external information and matching each song with a main genre from its lastfm tags, scraping the data to complete the location field, writing the Genre and Location notebooks, integrating our report and its visualisations into a webpage

Pierre-Antoine: fetching the necessary data from the cluster, computing the answers to the research questions, writing the Data Analysis notebook
