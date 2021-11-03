# "EDA and Business Intelligence to derive analytics from user subscription data" 
## Data Career Jumpstart Hackathon - Oct/Nov 2021
#### Team: Kedeisha Bryan, Yash Gokhale, Michelle T. , Stephanie

This project and the subsequent codes were developed as a submission to Data Career Jumpstart Hackathon 2021. The aim of the project was to conduct exploratory data analysis for user subscription data for a newsletter, "Column" and derive insights into the best time to send the newsletter to maximize subsciber rate and to analyze which topic is the most viewed, conducted using NLP (Natural Language Processing) bag of words model.

### What affects open %?
#### Exploratary Data Analysis Plots
![Visualization](https://github.com/yashgokhale/Miscellaneous/blob/master/DCJ%20Hackathon/images/Open%20Rate%20Hours.png) <br>
The date and time of sending the newsletter was visualized and it can be observed that maximum open rate (which is the metric to be used) is the highest when the newsletter is sent out between 6 to 8 am in the morning, which gives an idea of how the readers are most active. However, no clear model could be fit into this as the data is somewhat scattered and thus, it is important to look at other variables which could affect the open rate. This plot then prompted our team to look into other variables and see how the open rate can be maximized. In order to assess how the open rate is affected, several other variables were considered such as hour of the day, day of the week, number of links in the newsletter and number of words in the newsletter, which would influence the reader to keep on reading.

#### Intuition 
![Regression](https://github.com/yashgokhale/Miscellaneous/blob/master/DCJ%20Hackathon/images/Opens%20Regression.png) <br>
As confirmed by the above plot, it confirms the intuition that as the newsletter reaches a larger audience, the number of people opening the newsletter is high. This reaffirms that the newsletter is indeed having a positive impact and that, more subscribers are interested in reading the article. 

#### Clustering
Another parameter of consideration is the click rate (amount of subscribers actualy clicking the link) is compared against the number of links in the newsletter. Upon plotting the two, it can be observed that two distinct clusters are formed, implying that the relationship between the number of links is not linear with the click rate. Thus, greater the number of links does not necessarily mean higher click rate. There is an optimum number of links (in combination with hour of the day, which could be 6 to 8 am, which would maximize the click rate). <br>
![Clustering](https://github.com/yashgokhale/Miscellaneous/blob/master/DCJ%20Hackathon/images/Clusters.png)

### Natural Language Processing to get insights into topics
![News](https://github.com/yashgokhale/Miscellaneous/blob/master/DCJ%20Hackathon/images/Top%2010.png) <br>
The most clicked links of all the newsletters sent out till date is displayed. The top 10 links do not follow a regular pattern and thus, developing an NLP bag of words model is essential in understanding which topics are most insightful. <br>

A bag of words driven NLP (Natural Language Processing) model was developed, which was then used to develop link-up tables using Pandas in Python, which mimics the SQL query database and can be used to create datafiles and focus on the topics which were most impactful.
![Bag](https://github.com/yashgokhale/Miscellaneous/blob/master/DCJ%20Hackathon/images/NLP%20model.jpg)
