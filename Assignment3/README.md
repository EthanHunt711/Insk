<h1>Information Retrieval (advanced course)</h1>

<h2>Assignment 3</h2>

<h3>Ranked Retrieval with Cosine Similarity</h3>
<p>This program is designed to take advantage of the flexibility and time-saving 
pre-processing stages where each document is turned into vectors so the vector space model could be used.</p>
<p>Since this is just a class assignment, a set of .txt files used in the first assignment is used 
as the source material. But any number of .txt files in a source folder could be used</p>
<p>The files are read and preprocessed and a matrix with vectors containing the tf-itf weights are 
constructed.</p>
<p>Run the program as follows:</p>
<ul>
<li>run the program using the .txt files provided in the folder named resources</li>
<li>run the main program: python3 cosine_top_k.py FOLDER_PATH</li>
<li>FOLDER_PATH must be the path to the file where the .txt files are saved</li>
<li>FOLDER_PATH must be written as shown here: python cosine_top_k.py '....Projects/Insk/Assignment1/Resources/'
 </li>
<li>if the path does NOT end with a slash, the program cannot read the files</li>

</ul>
<h3>Evaluating (plotted precision-recall curve)</h3>
<p></p>
<p>In order to evaluate two queries vs the gold_standard run the evaluation file as follows: </p>
<p>     python3 evaluation.py</p>

