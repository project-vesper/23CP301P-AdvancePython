# LAB Assignment 1: Product Review from Text File

Consider a scenario where you are working as a data scientist for a
large e-commerce company. Your team is responsible for analyzing
customer feedback data, which is stored in multiple text files. Each
text file contains customer reviews for different product categories.
Your task is to write a Python script that performs the following
operations:

Read the contents of all the text files in a given directory.

For each review, extract the following information:

> •Customer ID (a 6-digit alphanumeric code)\
> •Product ID (a 10-digit alphanumeric code)\
> •Review date (in the format \"YYYY-MM-DD\")\
> •Review rating (an integer between 1 and 5)\
> •Review text (the actual feedback provided by the customer)

Calculate the average review rating for each product and store it in a
dictionary where the product ID is the key and the average rating is the
value.

Determine the top 3 products with the highest average review ratings.

Create a new text file named \"summary.txt\" and write the following
information into it:

> •The total number of reviews processed.
>
> •The total number of valid reviews (reviews with all required
> information extracted successfully).
>
> •The total number of invalid reviews (reviews with missing or
> incorrect information). •The product ID and average rating of the top
> 3 products with the highest average ratings.

Your Python script should be robust, handling any potential errors or
exceptions during the file handling process.

Additionally, you should implement efficient algorithms to handle large
volumes of data without consuming excessive memory or processing time.

Write the Python script to achieve the above objectives and provide
detailed comments explaining each step of your implementation.
