Project Topic: CODE SEARCH
Group Code: 23


Team Details: a) Nishant Shinde (S20210010161)
              b) Omkar Khairnar (S20210010120)


Dataset:
    Size: 100500 documents 
    Columns: 3 Columns Each(docID, code_snippet, description)
    Sources: StackOverflow, Programmiz (Collected by web crawling)


Project Details: (Django Project is created for UI and HTML Template Handelling)
	1.Finding solutions (Javascript Issues) similar as stackoverflow - (Code Search) is Information Retrieval Project.
	2.It Search for solution Code and Description based on user query.
	3.User can give one input query at a time.
	4.On clicking 'Submit' - top 20 Relevant documents are retrieved.
	5.Feedback: For each document, two options (Relevant/ Non-Relevant) are provided. User can choose one of the option based on query results.
	6.At the Bottom of listed documents , 'Submit Feedback' button is provided.
	7.By clicking on 'Submit Feedback' button - a small window will pop-out showing P-R curve according to submitted feedback by the user.

How to Run Application - follow the below steps:
	1. Unzip P23-MiniProject-NISOM.zip 
	2. Open in terminal -> P23-MiniProject-NISOM
	3. Run following commands in the terminal one-by-one. (Parent directory should be 'P23-MiniProject-NISOM'): 
		a. cd ./code/ir_webapp
		b. python manage.py runserver
		c. Open the link in chrome http://127.0.0.1:8000/
	

      
