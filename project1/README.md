<p><h1>CPSC 335 Project 1</h1>
<strong>Spring 2015</strong><br/>
<strong>Prof. Kevin Wortman, CSU Fullerton</strong></p>

<h2>Introduction</h2>
<p>In this project you will design, implement, and analyze straightforward greedy algorithms for two problems. For each problem, you will design an algorithm, describe your algorithm using clear pseudocode, analyze it mathematically, implement your algorithm in Python, measure its performance, compare your experimental results with the efficiency class of your algorithm, and draw conclusions.</p>

<h2>The hypothesis</h2>
<p>This experiment will test the following hypothesis:</p>

<p style="margin-left: 3em;"><em>For large values of n, the mathematically-derived efficiency class of an algorithm accurately predicts the observed running time of an implementation of that algorithm.</em></p>

<h2>The problems</h2>
<p>Both problems involve processing sets of (<em>x</em>,<em>y</em>) points in the Euclidean plane.</p>
<span>The <em>​bounding box</em> ​problem is:</span><br/>
<strong>input:​</strong> a list P of n two-dimensional points (<em>x</em>,<em>y</em>) <br/>
<strong>output:</strong>​
four coordinates (<em>x</em><sub><em>min</em></sub> , <em>y</em><sub><em>min</em></sub>, <em>x</em><sub><em>max</em></sub>, <em>y</em><sub><em>max</em></sub>) such that, for any (<em>x</em>,<em>y</em>) <em>∈ P</em>,<br/>
<center><p><em>x</em><sub><em>min</em></sub> ≤ <em>x</em> ≤ <em>x</em><sub><em>max</em></sub></p></center>
<p>and</p>
<center><p><em>y</em><sub><em>min</em></sub> ≤ <em>y</em> ≤ <em>y</em><sub><em>max</em></sub></p></center>

<p>There is a straightforward greedy algorithm that solves this problem in <em>O</em>(<em>n</em>) time.</p>

<span>The ​convex hull ​problem is</span><br/>
<strong>input:​</strong> a list <em>P</em> of n two-dimensional points (<em>x</em>,<em>y</em>)<br/>
<strong>output:</strong>​ a list of points <em>H</em> from <em>P</em> , such that <em>H</em> are the vertices of a convex polygon that contains all points in <em>P</em><br/>
<p>There is a straightforward greedy algorithm that solves this problem in <em>O</em>(<em>n<sup>3</sup></em>) time.</p>

<h2>What to do</h2>
<p>Repeat the following for each of the two problems:<p>
<ol>
<li>Design a greedy algorithm solving the problem.</li>
<li>Write clear pseudocode for your algorithm.</li>
<li>Analyze your pseudocode mathematically and prove its efficiency class. ​Hint: ​I expect the 3 efficiency classes to be <em>O(n)</em> and <em>O(n<sup>3</sup>)</em> respectively.</li>
<li>Implement your algorithm in Python 3, starting from the provided stub code.</li>
<li>Gather empirical timing data by running your implementation for various values of <em>n</em> . As discussed in class, you need enough data points to establish the shape of the best-fit curve (at least 5 data points, maybe more), and you should use <em>n</em> sizes that are large enough to produce large time values (ideally multiple seconds or even minutes) that minimize instrumental error.</li>
<li>Draw a scatter plot and fit line for your timing data. The instance size <em>n</em> should be on the horizontal axis and elapsed time should be on the vertical axis. Your plot should have a title, and labels and units on both axes.</li>
<li>Conclude whether or not your empirically-observed time efficiency data is consistent, or inconsistent, with your mathematically-derived big-<em>O</em> efficiency class</li>
</ol>