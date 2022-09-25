# Basic-WebScraper-Matplotlib-and-ScikitLearn-Project
## **Idea**
It is a basic Data Science project I made to implement my basic knowledge of the different libraries on a single project. This project will servers as an introduction to Data Science workflow to anyone interested.

## **Introduction**
This project will plot a Linear Regression graph using Matplotlib and Scikit-learn. It will make Linear Regression on Hollywood movies production cost vs worldwide gross income using the huge data provided by [The Numbers](https://www.the-numbers.com/movie/budgets/all) website. We will use our simple Web Crawler to extract data from this website. We can use this Linear Regression graph to predict how much money we should allocate on a movie to get our desire revenue.
## **Prerequisite**
You can install require python libraries by running these following command if you do not have this installed in your machine.
```
pip3 install pandas
pip3 install matplotlib
pip3 install sklearn
pip3 install notebook
```
## **Workflow**
![Data Science Workflow](https://www.dataquest.io/wp-content/uploads/2019/05/what-is-data-science-workflow-1024x633.jpg)
### Step 1
The project start by running 'crawler.py' which will extract all the required data from [The Numbers](https://www.the-numbers.com/movie/budgets/all) webpages. We will store this unrefine extracted data to 'data.sqlite' database for further cleaning and managing.
```
python crawler.py
```
### Step 2
The next step is to run 'transform.py' which will only retrieve Production Budget and Wroldwide Gross data from 'data.sqlite' database. Then it will create 'data.csv' file using those data to make our Linear Regression graph easier.
```
python transform.py
```
### Step 3
Finally run 'regression.ipynb' from inside jupyter notebook to generate our Linear Regression. You can run jupyter notebook from your project root folder by running 'jupyter notebook' only if you have installed 'notebook' library using pip.
## **Results**
The final regression graph will look like this.
![Linear Regression](https://raw.githubusercontent.com/csjoy/Images/master/Screenshot%20(2).png)
## **Note**
If you want to build this Linear Regression graph from scratch, please delete 'data.sqlite' and 'data.csv' files from your project root directory. These will automatically generate if you run the python files.
