# The Disputed Federalist Papers

## Due Sunday, April 28

## Description

*The Federalist Papers* are a collection of essays written by Alexander Hamilton, James Madison, and John Jay, first published as newspaper articles in 1787 and 1788 and then later collected into book form. Originally written to encourage the people of New York to ratify the new U.S. Constitution, the *Papers* are considered to be classics of political science, providing essential insight into the Founding Fathers' views on government.

The text of the U.S. Constitution was approved by its Framers in Philadelphia in September 1787, but the document required the approval of 9 of the 13 states before it would take effect. Public attitudes toward the Constitution were initially uncertain, and the new plan was immediately attacked by "Anti-Federalist" essays appearing in newspapers, criticizing its expansion of federal power. Most of these opposing authors wrote under pseudonyms taken from classical history, such as "Cato" and "Brutus".

Over the fall of 1787 and spring of 1788, Hamilton, Madison and Jay wrote 77 short essays that appeared in New York papers, answering Anti-Federalist criticisms and outlining their views on government and the meaning of the new Constitution. These papers, plus eight more on similar topics, were collected and published as a book in 1788. All of the 85 essays were originally printed under the pseudonym "Publius", a reference to one of the founders of the Roman Republic. The true authors' names do not appear in the original papers.

Shortly before his 1804 death [in a duel with Aaron Burr](https://www.youtube.com/watch?v=0Gkqzxss8Ss), Hamilton wrote a list that claimed authorship of 63 of the 85 papers. In 1818, after finishing his service as the fourth President, Madison released his own authorship list, which overlapped partly with Hamilton's.

Hamilton is acknowledged as the undisputed sole author of 51 papers, with Madison as the sole author of 14. Jay is credited with five. Three of the articles are known to be collaborations between Madison and Hamilton, leaving the remaining 12 "disputed" papers that might have been written by Hamilton or Madison.

In this project, you'll re-create a study by Glenn Fung (see reference 1) that used machine learning to predict the authorship of the disputed *Federalist Papers*. You will be able to practice a complete machine learning project study, including extracting the feature vetors, developing a model, and writing up your results.

## Text Analysis

Different writers use language in different ways. Therefore, textual critics may resolve questions of authorship by examining how the words, style, and structure of a disputed passage compares to other known works by its potential authors.

In 1998, Robert Bosch and James Smith used **word counts** to distinguish between Madison and Hamilton's papers (see reference 2). They identified a set of 70 basic **function words** that are useful for textual analysis and counted their occurrences in each of *The Federalist Papers*. They then used these 70-element vectors to build a model that could classify Hamilton and Madison's known papers correctly. Fung's study used the same data with a machine learning technique called a **support-vector machine** (SVM), a variation of the linear classifier we studied earlier in the class.

### The Results

Bosch, Smith, and Fung attributed all of the 12 disputed papers to Madison. This agrees with the opinions of other scholars, although there are arguments that some of the essays attributed to Madison may have been collaborative efforts.

## The Data and Models

The file `federalist_paper_data.csv` contains the data for the project. This is the original data created by Bosch and Smith and also used by Fung, which I obtained from a previous project at UW-Madison.

The file has 118 lines, corresponding to 118 text excerpts. The first entry on each line is the class of the text excerpt:

- 1 for Hamilton's papers
- 2 for Madison's papers
- 3 for disputed papers

The remaining 70 values are the frequency of occurrence of the 70 function words in the text, scaled to units of estimated occurrences per 1000 words. The list of functions words is in `federalist_papers_wordlist.txt`.

Your goal is to train a model that successfully separates Hamilton's and Madison's papers, then apply it to the disputed papers and report the results. You may use any classification technique and any library. **You do not have to implement your models from scratch**.

## Submission

You will submit your paper in PDF format, descirbed in more detail below, and any code that you create to perform the analysis.

## The Paper

### Length

The paper will be **at most five pages**, including references. Use single-spacing, normal margins, and 12 point font.

### Sections

Your paper will have these sections:

1. Introduction: explains the basic idea of the paper and states its key contributions
2. Related Work: reviews and cites earlier relevant papers
3. Methods: describes the data and the steps of the analysis
4. Results: presents the results of the analysis, including relevant tables and graphs
5. Conclusion: restates the main contributions
6. References

This structure is typical for experimental papers, where the focus of the research is collecting and analyzing data to answer a question.

### Citations and References

You are required to find **two additional references**, beyond the Fund and Bosh and Smith papers referenced below. Your references must be **academic articles published in peer-reviwed journals or conference proceedings**. Do not reference general-interest media articles, opinion pieces, or web resources. I am requiring you to find only two articles because I want you to focus on finding, reading, and summarizing good, relevant articles.

When you read each article, write a **four or five sentence summary** of its main topic, methods, and results. These summaries will form the basis of your Related Work section.

Cite references in (Name, Year) style. I suggest using APA-style formatting, but I don't have a strong preference.

## Tips

*These are my suggestions on how to write each section. Many of them are strategies that have worked well for me in previous projects, but they aren't iron laws that all scientific papers are required to follow.*

Check out our [CS Honors Thesis Guide](https://github.com/dansmyers/HonorsThesisGuide) for more practical tips on writing a report.

### Introduction

The Introduction should start with a paragraph summarizing the general context and problem that motivates the study. Write this paragraph in such a way that your grandmother would understand why the paper is important.

The first sentence of the second paragraph will state the main topic of the paper. This is like the thesis sentence that motivates everything else that happens in the rest of the work. It's okay to phrase this as, "This paper will..." or "In this paper..."

The Intro should end with a **bulleted list of contributions**, summarizing what's going to happen in the rest of the paper:

> The rest of this paper makes the following contributions:
>
> - Section 2 summarizies previous work on the application of machine learning to the disputed *Federalist Papers*.
> - Section 3 describes the data set used for this study, including the generation of textual feature vectors from the *Papers*.
>
> and so forth for the other sections.

### Related Work

In the Related Work section, write one paragraph summarizing each of your references, then add a starting paragraph for the entire section that provides context. Discuss references in chronological order.

### Methods and Results

The Methods section should have two parts: a subsection describing the data for the study and a subsection describing the model(s) you have chosen for the classification.

The Results section is the most flexible. The key is to select and present useful information about the model and training process, beyond simply stating how many disputed papers landed in each category. There is no best answer, so **think carefully about what you want to say in this section**.

For both the Methods and Results sections, **include details**. **Lack of detail** is the most common weakness we see in student papers and theses. Don't simply state what you did in generic or high-level terms, give the specifics. If your paper becomes too long, *then* you can go back and edit some of the details to make it more compact.

### Conclusion

The conclusion can be short: one paragraph restating the key ideas of the paper is sufficient.

## References

Fung, G. (2003, October). The disputed Federalist Papers: SVM feature selection via concave minimization. In Proceedings of the 2003 Conference on Diversity in Computing (pp. 42-46). ACM.

Bosch, R. A., & Smith, J. A. (1998). Separating hyperplanes and the authorship of the disputed federalist papers. The American mathematical monthly, 105(7), 601-608.
