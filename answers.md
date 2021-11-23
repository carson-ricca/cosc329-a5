### Questions

1. Which text pairs are definitely plagiarized pairs? You can read the paragraphs in the original files to verify this.
   What type of plagiarism took place in these cases?
2. Which text pairs are similar enough that warrants a deeper investigation by a human? Explain your reasoning. How do
   the containment values for these text pairs compare to the text pairs in the previous question?
3. What happens to Cn(A,B) as n increases, for the same pair of texts? Why does this occur?
4. In this assignment, we did not do any stemming or lemmatization of the text. What would you expect the containment
   values to be like if we added stemming as a preprocessing step to the text? Do you expect them to increase, stay the
   same, or decrease? Explain your answer.
5. For paragraphs this short, what is a good value of n to use to detect plagiarism automatically? Does this hold for
   the borderline cases where plagiarism is not definite but only a possibility? Justify your choice based on the data
   in the table.
6. For the n you've chosen in the previous question, what is a good value of Cn(A,B) to use (for your data sample)?
   Justify your choice based on the data in the table. Again, consider both the situation of when the texts are
   definitely involved plagiarism veruses when the texts are likely to involve plagiarism.

### Answers

1. Question #1 Answer
    1. `b.txt` and `g.txt` are the exact same text copy and pasted. This is Verbatim plagiarism.
    2. I also believe from the data and reading the text files that `f.txt` plagiarizes `b.txt` and `g.txt`. This would
       be Inadequate Paraphrasing as the majority of the context behind the text is identical. It appears that
       in `f.txt` some words were changed, some sentences were reordered, and there were also some sentences that were
       directly copied.
2. Question #2 Answer
    1. All containment values in context of this answer were for uni-grams.
    2. `h.txt` and `y.txt` I found this tough to determine if there was plagiarism or if it was paraphrased correctly. I
       think this would be a good threshold for a human to investigate the two documents to see their similarities. The
       containment value for these two texts was `0.596` the containment values for the above answers were `1`
       and `0.684` respectively.
    3. `f.txt` and `p.txt` mainly for the same reasons as above, a look by a human would be required to determine if
       plagiarism occurred. Containment value is `0.52`.
    4. If we look at other values of `n` in the table, we can see that the containment value will be lower as n
       increases. I think looking at the values of containment for uni-grams and bi-grams give a fairly good indication
       if a human is required to check for plagiarism.
3. Question #3 Answer
    1. `C_n(A, B)` decreases as `n` increases for the same pair of texts. This makes sense as when `n` increase the
       length of words in the ngrams will also increase. The more words that are part of each item in a set the less
       likely it is that there will be an intersection with the other set.
4. Question #4 Answer
    1. If we added stemming to the preprocessing step of this project I believe that the containment values would
       increase. Since stemming reduces words to their word stem, there would be less distinct words among the
       paragraphs. In the case where students paraphrased poorly, stemming would increase the containment values, as
       their change in ordering or slight change in words would not make their paragraph as distinct after stemming has
       been completed.
5. Question #5 Answer
    1. For paragraphs that are this short, based on the data I would say that an `n` value of `2`, would be a good value
       to detect plagiarism automatically. This case does hold for the borderline cases where plagiarism may be a
       possibility. Based on the data in the table there is a containment value for `n = 2` that would be able to be
       used to automatically detect plagiarism, there is also a containment value that would indicate the possibility of
       plagiarism consistently.
6. Question #6 Answer
    1. For `n = 2` I believe a good containment value to automatically detect plagiarism would be `C_n(A, B) > 0.3`.
       Based on the data all texts that have a containment value greater than `0.3` meet the definition of plagiarism
       after reviewing the texts manually. For the case where the texts are likely to involve plagiarism, for `n = 2` a
       containment value that is `C_n(A, B) > 0.13` is indicative that it may be worth having a human read over the
       paragraphs for plagiarism. After reading over some texts in this range, there is certainly a chance that stuff
       was plagiarized, although it would not be possible to detect this automatically and consistently. 