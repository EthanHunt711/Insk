<h1>Information Retrieval (advanced course)</h1>

<h2>Assignment 1</h2>

<h3>Boolean Queries with Inverted Index</h3>
<p>This program is designed to take advantage of the flexibility and time-saving 
pre-processing stages where a dictionary containing each token is linked to a list 
of DocumentIDs (document names).</p>
<p>Since this is just a class assignment, a specialized class with methods for extracting text from a
a selected website (www.sparknotes.com) is being implemented which takes advantage of 
web-scraping methods for creating text files containing a summary of 35 randomly selected 
novels.</p>
<p>The output files are read by another class and after normalization and tokenization are used as input for a
dictionary building class. This dictionary, which as mentioned above, provides a posting list for each token is later
used in the main program for implementing boolean queries.</p>
<p>There are two methods for running this program:</p>
<ul>
<li>Using the web-scraping class</li>
<ol>
<li>run this line: python3 summary_web_scraping.py LIST_FILE</li>
<li>use the list_url.txt as LIST_FILE</li>
<li>the .txt files are created and saved in the same directory as the program</li>
<li>run the main program: python3 main_querry.py FOLDER_PATH</li>
<li>FOLDER_PATH must be the path to the file where the .txt files are saved</li>
<li>FOLDER_PATH must be given as shown here: python main_querry.py '....Projects/Insk/Assignment1/'
 </li>
<li>if the path does NOT end with a slash, the program cannot read the files</li>
</ol>
<p></p>
<li>Using the already extracted text files</li>
<ol>
<li>run the program using the .txt files provided in the folder named resources</li>
<li>run the main program: python3 main_querry.py FOLDER_PATH</li>
<li>FOLDER_PATH must be the path to the file where the .txt files are saved</li>
<li>FOLDER_PATH must be given as shown here: python main_querry.py '....Projects/Insk/Assignment1/Resources/'
 </li>
<li>if the path does NOT end with a slash, the program cannot read the files</li>
</ol>
</ul>

